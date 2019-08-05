import pytest
import logging

from ucloud.core.transport import (
    RequestsTransport,
    Request,
    Response
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
def transport():
    return RequestsTransport()


class TestTransport:
    def test_transport_send(self, transport):
        req = Request(
            url='http://httpbin.org/anything',
            method='post',
            json={'foo': 'bar'},
        )
        resp = transport.send(req)
        assert resp.json()['json'] == {'foo': 'bar'}

    def test_transport_handler(self, transport):
        global_env = {}

        def request_handler(r):
            global_env['req'] = r
            return r

        def response_handler(r):
            global_env['resp'] = r
            return r

        transport.middleware.request(handler=request_handler)
        transport.middleware.response(handler=response_handler)

        req = Request(
            url='http://httpbin.org/anything',
            method='post',
            json={'foo': 'bar'},
        )
        resp = transport.send(req)
        assert resp.json()['json'] == {'foo': 'bar'}

        assert 'req' in global_env
        assert 'resp' in global_env
