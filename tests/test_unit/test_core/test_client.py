import os
import pytest
import logging

from ucloud.client import Client
from ucloud.core import exc
from ucloud.testing.mock import MockedTransport

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def client():
    return Client(
        {
            "region": "cn-bj2",
            "public_key": "foo",
            "private_key": "foo",
            "timeout": 10,
            "max_retries": 3,
            "ssl_verify": False,
        }
    )


@pytest.fixture(scope="function", autouse=True)
def transport():
    return MockedTransport()


class TestClient:
    def test_client_invoke(self, client, transport):
        transport.mock_data(lambda _: {"RetCode": 0, "Action": "Foo"})
        client.transport = transport

        assert client.invoke("Foo") == {"RetCode": 0, "Action": "Foo"}

    def test_client_invoke_code_error(self, client, transport):
        transport.mock_data(lambda _: {"RetCode": 171, "Action": "Foo"})
        client.transport = transport

        with pytest.raises(exc.RetCodeException):
            try:
                client.invoke("Foo")
            except exc.RetCodeException as e:
                assert str(e)
                expected = {"RetCode": 171, "Action": "Foo", "Message": ""}
                assert e.json() == expected
                raise e

    def test_client_invoke_with_retryable_error(self, client, transport):
        # RetCodeError is retryable when code is greater than 2000
        transport.mock_data(lambda _: {"RetCode": 10000, "Action": "Foo"})
        client.transport = transport

        with pytest.raises(exc.RetCodeException):
            client.invoke("Foo")

    def test_client_invoke_with_unexpected_error(self, client, transport):
        def raise_error(_):
            raise ValueError("temporary error")

        transport.mock_data(raise_error)
        client.transport = transport

        with pytest.raises(ValueError):
            client.invoke("Foo")

    def test_client_try_import(self, client):
        assert client.pathx()
        assert client.stepflow()
        assert client.uaccount()
        assert client.udb()
        assert client.udpn()
        assert client.udisk()
        assert client.uhost()
        assert client.ulb()
        assert client.umem()
        assert client.unet()
        assert client.uphost()
        assert client.vpc()
