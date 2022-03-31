import time
import typing
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from ucloud.core.transport import http
from ucloud.core.transport.http import Request, Response, SSLOption
from ucloud.core.utils.middleware import Middleware
from ucloud.core import exc


class RequestsTransport(http.Transport):
    """transport is the implementation of http client, use for send a request and return a http response

    :type max_retries: int
    :param max_retries: max retries is the max number of transport request when occur http error
    :type backoff_factor: float
    :param backoff_factor: backoff factor will calculate the backoff delay during retrying,
        the backoff delay = {backoff factor} * (2 ^ ({number of total retries} - 1))
    :type status_forcelist: tuple
    :param status_forcelist: the status code list that could be retried
    """

    def __init__(
        self,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
        status_forcelist: typing.Tuple[int] = (500, 502, 504),
    ):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.status_forcelist = status_forcelist

        self._adapter = self._load_adapter(max_retries)
        self._middleware = Middleware()

    def send(self, req: Request, **options: typing.Any) -> http.Response:
        """send request and return the response

        :param req: the full http request descriptor
        :return: the response of http request
        """
        for handler in self.middleware.request_handlers:
            req = handler(req)

        try:
            resp = self._send(req, **options)
        except Exception as e:
            for handler in self.middleware.exception_handlers:
                handler(e)
            raise e

        for handler in self.middleware.response_handlers:
            resp = handler(resp)

        return resp

    @property
    def middleware(self) -> Middleware:
        """the middleware object, see :mod:

        :return: the transport middleware
        """
        return self._middleware

    def _send(self, req: Request, **options: typing.Any) -> requests.Response:
        with requests.Session() as session:
            adapter = self._load_adapter(options.get("max_retries"))
            session.mount("http://", adapter=adapter)
            session.mount("https://", adapter=adapter)

            ssl_option = options.get("ssl_option")
            kwargs = self._build_ssl_option(ssl_option) if ssl_option else {}

            req.request_time = time.time()
            session_resp = session.request(
                method=req.method.upper(),
                url=req.url,
                json=req.json,
                data=req.data,
                params=req.params,
                headers=req.headers,
                timeout=options.get("timeout"),
                **kwargs
            )
            resp = self.convert_response(session_resp)
            resp.request = req
            resp.response_time = time.time()

            if resp.status_code >= 400:
                raise exc.HTTPStatusException(
                    resp.status_code, resp.request_uuid
                )
            return resp

    @staticmethod
    def _build_ssl_option(ssl_option):
        kwargs = {"verify": ssl_option.ssl_verify and ssl_option.ssl_cacert}
        if not ssl_option.ssl_cert:
            return kwargs

        if ssl_option.ssl_key:
            kwargs["cert"] = (ssl_option.ssl_cert, ssl_option.ssl_key)
        else:
            kwargs["cert"] = ssl_option.ssl_cert
        return kwargs

    def _load_adapter(
        self, max_retries: typing.Optional[int] = None
    ) -> HTTPAdapter:
        if max_retries is None and self._adapter is not None:
            return self._adapter

        max_retries = max_retries or 0
        adapter = HTTPAdapter()
        adapter.max_retries = Retry(
            total=max_retries,
            read=max_retries,
            connect=max_retries,
            backoff_factor=self.backoff_factor,
            status_forcelist=self.status_forcelist,
        )
        return adapter

    @staticmethod
    def convert_response(r: requests.Response) -> Response:
        return Response(
            url=r.url,
            method=r.request.method,
            status_code=r.status_code,
            reason=r.reason,
            headers=r.headers,
            content=r.content,
            encoding=r.encoding or r.apparent_encoding,
        )
