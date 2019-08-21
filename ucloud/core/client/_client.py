import typing
import logging
import sys

from ucloud import version
from ucloud.core.client._cfg import Config
from ucloud.core.transport import Transport, RequestsTransport, Request
from ucloud.core.typesystem import encoder
from ucloud.core.utils import log
from ucloud.core.utils.middleware import Middleware
from ucloud.core import auth, exc

default_transport = RequestsTransport()


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
        self.transport = transport or default_transport
        self.logger = logger or log.default_logger
        if middleware is None:
            middleware = Middleware()
            middleware.response(self.logged_response_handler)
            middleware.request(self.logged_request_handler)
        self._middleware = middleware

    def invoke(self, action: str, args: dict = None, **options) -> dict:
        """ invoke will invoke the action with arguments data and options

        :param str action: the api action, like `CreateUHostInstance`
        :param dict args: arguments of api(action), see doc: `UCloud API Documentation <https://docs.ucloud.cn/api>`__
        :return:
        """
        retries = 0
        max_retries = options.get("max_retries") or self.config.max_retries

        while retries <= max_retries:
            try:
                return self._send(action, args or {}, **options)
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
            except Exception as e:
                raise e

    @property
    def middleware(self) -> Middleware:
        return self._middleware

    def logged_request_handler(self, req):
        self.logger.info("[request] {} {}".format(req.get("Action", ""), req))
        return req

    def logged_response_handler(self, resp):
        self.logger.info(
            "[response] {} {}".format(resp.get("Action", ""), resp)
        )
        return resp

    @staticmethod
    def _parse_dict_config(
        config: dict
    ) -> typing.Tuple[Config, auth.Credential]:
        return Config.from_dict(config), auth.Credential.from_dict(config)

    def _send(self, action: str, args: dict, **options) -> dict:
        args["Action"] = action
        for handler in self.middleware.request_handlers:
            args = handler(args)
        req = self._build_http_request(args)

        max_retries = options.get("max_retries") or self.config.max_retries
        timeout = options.get("timeout") or self.config.timeout
        resp = self.transport.send(
            req, timeout=timeout, max_retries=max_retries
        ).json()

        for handler in self.middleware.response_handlers:
            resp = handler(resp)

        if int(resp.get("RetCode", -1)) != 0:
            raise exc.RetCodeException(
                action=req.data.get("Action"),
                code=int(resp.get("RetCode")),
                message=resp.get("Message"),
            )

        return resp

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
            },
        )

    def _build_user_agent(self) -> str:
        python_version = "{v[0]}.{v[1]}.{v[2]}".format(v=sys.version_info)
        user_agent = "Python/{python_version} Python-SDK/{sdk_version}".format(
            python_version=python_version, sdk_version=version.version
        ) + (self.config.user_agent or "")
        return user_agent

    def __repr__(self):
        return '<{}("{}")>'.format(self.__class__.__name__, self.config.region)
