import logging
import json as json_mod

logger = logging.getLogger(__name__)


class Request:
    def __init__(
        self,
        url: str,
        method: str = "GET",
        params: dict = None,
        data: dict = None,
        json: dict = None,
        headers: dict = None,
        **kwargs
    ):
        self.url = url
        self.method = method
        self.params = params
        self.data = data
        self.json = json
        self.headers = headers


class Response:
    def __init__(
        self,
        url: str,
        method: str,
        request: Request = None,
        status_code: int = None,
        reason: str = None,
        headers: dict = None,
        content: str = None,
        **kwargs
    ):
        self.url = url
        self.method = method
        self.request = request
        self.status_code = status_code
        self.reason = reason
        self.headers = headers
        self.content = content

    def json(self) -> dict:
        return json_mod.loads(self.content)


class Transport:
    """ the abstract class of transport implementation """

    def send(self, req: Request, **options: dict) -> Response:
        raise NotImplementedError
