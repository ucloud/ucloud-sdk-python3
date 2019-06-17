import typing
import logging
import sys

from ucloud import version
from ucloud.core.client._cfg import Config
from ucloud.core.transport import (
    Transport,
    RequestsTransport,
    Request,
    Response
)
from ucloud.core.utils.middleware import Middleware
from ucloud.core import auth, exc

logger = logging.getLogger(__name__)

default_transport = RequestsTransport()


class Client:
    def __init__(
        self,
        config: dict,
        transport: typing.Optional[Transport] = None,
        middleware: typing.Optional[Middleware] = None
    ):
        cfg, cred = self._parse_dict_config(config)
        self.config = cfg
        self.credential = cred
        self.transport = transport or default_transport
        self._middleware = middleware or Middleware()
        self.middleware.response(Client.logged_response_handler)

    def invoke(self, action: str, args: dict = None, **options: dict) -> dict:
        """ invoke will invoke the action with arguments data and options

        :param str action: the api action, like `CreateUHostInstance`
        :param dict args: arguments of api(action), see doc: `UCloud API Documentation <https://docs.ucloud.cn/api>`__
        :return:
        """
        retries = 0
        req = self._build_request(action, args)
        max_retries = options.get("max_retries") or self.config.max_retries

        while retries <= max_retries:
            try:
                return self._send(req, **options)
            except exc.UCloudException as e:
                if e.retryable and retries != max_retries:
                    logging.info(
                        "Retrying {action}: {args}".format(action=action,
                                                           args=args))
                    retries += 1
                    continue
                raise e
            except Exception as e:
                raise e

        raise exc.RetryTimeoutException("max retries is reached")

    @property
    def middleware(self) -> Middleware:
        return self._middleware

    @staticmethod
    def logged_response_handler(resp: Response) -> Response:
        """ logging response data

        :param resp:
        :return:
        """
        logger.info(resp)
        return resp

    def __enter__(self):
        yield self

    @staticmethod
    def _parse_dict_config(config: dict) -> typing.Tuple[Config,
                                                         auth.Credential]:
        return Config.from_dict(config), auth.Credential.from_dict(config)

    def _send(self, req: Request, **options: dict) -> dict:
        for handler in self.middleware.request_handlers:
            req = handler(req)

        timeout = options.get("timeout") or self.config.timeout
        resp = self.transport.send(req, timeout=timeout).json()

        for handler in self.middleware.response_handlers:
            resp = handler(resp)

        if int(resp.get("RetCode", -1)) != 0:
            raise exc.RetCodeException(
                action=req.json.get("Action"),
                code=int(resp.get("RetCode")),
                message=resp.get("Message"),
            )

        return resp

    def _build_request(self, action: str, data: dict = None) -> Request:
        payload = {"Region": self.config.region,
                   "ProjectId": self.config.project_id}
        payload.update(
            {k: v for k, v in (data or {}).items() if v is not None}
        )  # overwrite region and project id
        payload["Action"] = action  # overwrite action
        payload["Signature"] = self.credential.verify_ac(payload)

        return Request(
            url=self.config.base_url,
            method="post",
            json=payload,
            headers={
                "User-Agent": self._build_user_agent(),
                "Content-Type": "application/json",
            },
        )

    def _build_user_agent(self) -> str:
        python_version = "{v[0]}.{v[1]}.{v[2]}".format(v=sys.version_info)
        user_agent = "Python/{python_version} Python-SDK/{sdk_version}".format(
            python_version=python_version, sdk_version=version.version
        ) + (self.config.user_agent or "")
        return user_agent
