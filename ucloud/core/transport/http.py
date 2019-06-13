import json as json_mod


class Request:
    url: str
    method: str
    params: dict = None
    data: dict = None
    json: dict = None
    headers: dict = None

    def __init__(
        self, url: str, method: str, params: dict, data: dict, json: dict, headers: dict
    ):
        self.url = url
        self.method = method
        self.params = params
        self.data = data
        self.json = json
        self.headers = headers


class Response:
    url: str
    method: str
    request: Request
    status_code: int
    reason: str
    headers: dict = dict
    content: str = str

    def __init__(
        self,
        url: str,
        method: str,
        request: Request,
        status_code: int,
        reason: str,
        headers: dict,
        content: str,
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
