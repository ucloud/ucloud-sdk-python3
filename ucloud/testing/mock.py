import json
import typing

from ucloud.core.transport import Transport, Request, Response


class MockedTransport(Transport):
    def __init__(self):
        super(MockedTransport, self).__init__()
        self.transport_handlers = []
        self.client_handler = []

    def send(self, req: Request, **options: typing.Any) -> Response:
        resp = Response(req.url, req.method)
        for handler in self.transport_handlers:
            resp = handler(req)

        for handler in self.client_handler:
            payload = handler(req.payload())
            resp.content = json.dumps(payload).encode("utf-8")

        return resp

    def mock(self, handler: typing.Callable[[Request], Response]):
        self.transport_handlers.append(handler)

    def mock_data(self, handler: typing.Callable[[dict], dict]):
        self.client_handler.append(handler)
