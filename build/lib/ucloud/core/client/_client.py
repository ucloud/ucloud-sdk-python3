import typing
import logging
import sys
import time

from ucloud import version
from ucloud.core.client._cfg import Config
from ucloud.core.transport import (
    Transport,
    RequestsTransport,
    Request,
    SSLOption,
    http,
)
from ucloud.core.typesystem import encoder
from ucloud.core.utils import log
from ucloud.core.utils.middleware import Middleware
from ucloud.core import auth, exc


class Client:
    def __init__(
        self,
        config: dict,
        transport: typing.Optional[Transport] = None,
        middleware: typing.Optional[Middleware] = None,
        logger: typing.Optional[logging.Logger] = None,
    ):
        cfg, cred = self._parse_dict_config(config)
        self.config = cfg
        self.credential = cred
        self.transport = transport or RequestsTransport()
        self.logger = logger or log.default_logger
        if middleware is None:
            middleware = Middleware()
            middleware.response(self.logged_response_handler)
            middleware.request(self.logged_request_handler)
            middleware.exception(self.logged_exception_handler)
        self._middleware = middleware

    def invoke(self, action: str, args: dict = None, **options) -> dict:
        """invoke will invoke the action with arguments data and options

        :param str action: the api action, like `CreateUHostInstance`
        :param dict args: arguments of api(action), see doc: `UCloud API Documentation <https://docs.ucloud.cn/api>`__
        :return:
        """
        retries = 0
        max_retries = options.get("max_retries") or self.config.max_retries
        timeout = options.get("timeout") or self.config.timeout

        while retries <= max_retries:
            try:
                return self._send(
                    action, args or {}, max_retries=max_retries, timeout=timeout
                )
            except exc.UCloudException as e:
                if e.retryable and retries != max_retries:
                    logging.info(
                        "Retrying {action}: {args}".format(
                            action=action, args=args
                        )
                    )
                    retries += 1
                    continue
                raise e

    @property
    def middleware(self) -> Middleware:
        return self._middleware

    def logged_request_handler(self, req):
        action = req.get("Action", "")
        self.logger.info("[request] {} {}".format(action, req))
        return req

    def logged_response_handler(self, resp, http_resp: http.Response = None):
        action = resp.get("Action", "")
        request_uuid = http_resp and http_resp.request_uuid
        self.logger.info(
            "[response] [{}] {} {}".format(request_uuid or "*", action, resp)
        )
        return resp

    def logged_exception_handler(self, e: Exception):
        if isinstance(e, exc.RetCodeException):
            self.logger.warning(e)
        else:
            self.logger.exception(e)
        return e

    @staticmethod
    def _parse_dict_config(
        config: dict,
    ) -> typing.Tuple[Config, auth.Credential]:
        return Config.from_dict(config), auth.Credential.from_dict(config)

    def _send(self, action: str, args: dict, max_retries, timeout) -> dict:
        args["Action"] = action

        # inject request middleware
        for handler in self.middleware.request_handlers:
            args = handler(args)

        # send http request
        try:
            req = self._build_http_request(args)

            resp = self.transport.send(
                req,
                ssl_option=SSLOption(
                    self.config.ssl_verify,
                    self.config.ssl_cacert,
                    self.config.ssl_cert,
                    self.config.ssl_key,
                ),
                timeout=timeout,
                max_retries=max_retries,
            )
            data = resp.json()
        except Exception as e:
            for handler in self.middleware.exception_handlers:
                handler(e)
            raise e

        # inject response middleware
        for handler in self.middleware.response_handlers:
            data = handler(data, resp)

        # return when successful
        if int(data.get("RetCode", -1)) == 0:
            return data

        # inject exception middleware
        ret_code_exc = exc.RetCodeException(
            action=req.data.get("Action", ""),
            code=int(data.get("RetCode", 0)),
            message=data.get("Message", ""),
            request_uuid=resp.request_uuid,
        )
        for handler in self.middleware.exception_handlers:
            handler(ret_code_exc)
        raise ret_code_exc

    def _build_http_request(self, args: dict) -> Request:
        config = {
            "Region": self.config.region,
            "ProjectId": self.config.project_id,
        }
        payload = {k: v for k, v in config.items() if v is not None}
        payload.update({k: v for k, v in args.items() if v is not None})
        payload = encoder.encode(payload)
        payload["Signature"] = self.credential.verify_ac(payload)

        return Request(
            url=self.config.base_url,
            method="post",
            data=payload,
            headers={
                "User-Agent": self._build_user_agent(),
                "Content-Type": "application/x-www-form-urlencoded",
                "U-Timestamp-Ms": str(int(round(time.time() * 1000))),
            },
        )

    def _build_user_agent(self) -> str:
        python_version = "{v[0]}.{v[1]}.{v[2]}".format(v=sys.version_info)
        user_agent = "Python/{python_version} Python-SDK/{sdk_version}".format(
            python_version=python_version, sdk_version=version.version
        ) + (self.config.user_agent or "")
        return user_agent

    def __repr__(self):
        return '<{}(region="{}")>'.format(
            self.__class__.__name__, self.config.region
        )
