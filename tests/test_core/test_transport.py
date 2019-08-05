import pytest
import logging

from ucloud.core.transport import RequestsTransport, Request, Response, utils

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
def transport():
    return RequestsTransport()


class TestTransport:
    def test_transport_send(self, transport):
        req = Request(
            url="http://httpbin.org/anything",
            method="post",
            json={"foo": "bar"},
        )
        resp = transport.send(req)
        assert resp.text
        assert resp.json()["json"] == {"foo": "bar"}

    def test_transport_handler(self, transport):
        global_env = {}

        def request_handler(r):
            global_env["req"] = r
            return r

        def response_handler(r):
            global_env["resp"] = r
            return r

        transport.middleware.request(handler=request_handler)
        transport.middleware.response(handler=response_handler)

        req = Request(
            url="http://httpbin.org/anything",
            method="post",
            json={"foo": "bar"},
        )
        resp = transport.send(req)
        assert resp.text
        assert resp.json()["json"] == {"foo": "bar"}

        assert "req" in global_env
        assert "resp" in global_env


class TestResponse:
    def test_guess_json_utf(self):
        import json
        encodings = [
            "utf-32", "utf-8-sig", "utf-16", "utf-8", "utf-16-be",
            "utf-16-le", "utf-32-be", "utf-32-le"
        ]
        for e in encodings:
            s = json.dumps('表意字符').encode(e)
            assert utils.guess_json_utf(s) == e

    def test_response_empty_content(self):
        r = Response('http://foo.bar', 'post')
        assert not r.text
        assert r.json() is None
