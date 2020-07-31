import json
import uuid

import pytest
import logging
import collections
import requests_mock

from ucloud.client import Client
from ucloud.core import exc
from ucloud.core.transport import RequestsTransport, http
from ucloud.testing.mock import MockedTransport

from tests.test_unit.test_core import consts

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
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


def test_client_invoke(client):
    expected = {"RetCode": 0, "Action": "Foo"}
    with requests_mock.Mocker() as m:
        m.post(
            consts.TEST_URL,
            text=json.dumps(expected),
            headers={http.REQUEST_UUID_HEADER_KEY: str(uuid.uuid4())},
        )
        assert client.invoke("Foo") == expected


def test_client_invoke_code_error(client):
    expected = {"RetCode": 171, "Action": "Foo", "Message": "签名错误"}

    with requests_mock.Mocker() as m:
        m.post(
            consts.TEST_URL,
            text=json.dumps(expected),
            headers={http.REQUEST_UUID_HEADER_KEY: str(uuid.uuid4())},
        )

        with pytest.raises(exc.RetCodeException):
            try:
                client.invoke("Foo")
            except exc.RetCodeException as e:
                assert e.retryable is False
                assert e.json() == {
                    "RetCode": 171,
                    "Action": "Foo",
                    "Message": "签名错误",
                }
                raise e


def test_client_invoke_with_retryable_error(client):
    # RetCodeError is retryable when code is greater than 2000
    with requests_mock.Mocker() as m:
        m.post(
            consts.TEST_URL,
            text=json.dumps({"RetCode": 10000, "Action": "Foo"}),
        )
        with pytest.raises(exc.RetCodeException):
            client.invoke("Foo")


def test_client_invoke_with_unexpected_error(client):
    def raise_error(_):
        raise ValueError("temporary error")

    transport = RequestsTransport()
    transport.middleware.request(raise_error)
    client.transport = transport

    with pytest.raises(ValueError):
        client.invoke("Foo")


def test_client_try_import(client):
    for name in dir(client):
        if name.startswith("_") or name in [
            "invoke",
            "logged_request_handler",
            "logged_response_handler",
            "logged_exception_handler",
        ]:
            continue

        client_factory = getattr(client, name)
        if isinstance(client_factory, collections.Callable):
            print(client_factory())
