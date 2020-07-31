import json
import uuid

import pytest
import logging
import requests_mock
from collections import Counter

from tests.test_unit.test_core.consts import TEST_URL
from ucloud.core import exc
from ucloud.core.transport import (
    RequestsTransport,
    Request,
    Response,
    utils,
    http,
)

logger = logging.getLogger(__name__)


@pytest.fixture(name="transport", scope="function", autouse=True)
def transport_factory():
    return RequestsTransport()


@pytest.mark.parametrize(
    argnames=("status_code", "content", "expect", "expect_exc", "retryable"),
    argvalues=(
        (
            200,
            '{"Action": "Mock", "RetCode": 0}',
            {"Action": "Mock", "RetCode": 0},
            None,
            False,
        ),
        (500, "{}", None, exc.HTTPStatusException, False),
        (429, "{}", None, exc.HTTPStatusException, True),
        (500, "x", None, exc.HTTPStatusException, False),
        (200, "x", None, exc.InvalidResponseException, False),
    ),
)
def test_transport(
    transport, status_code, content, expect, expect_exc, retryable
):
    with requests_mock.Mocker() as m:
        m.post(TEST_URL, text=content, status_code=status_code)

        got_exc = None
        try:
            resp = transport.send(Request(url=TEST_URL, method="post", json={}))
            assert resp.json() == expect
        except Exception as e:
            got_exc = e

        if expect_exc:
            assert str(got_exc)
            assert got_exc.retryable == retryable
            assert isinstance(got_exc, expect_exc)


def test_transport_handler(transport):
    req_key, resp_key, exc_key = "req", "resp", "exc"
    counter = Counter({req_key: 0, resp_key: 0, exc_key: 0})

    def request_handler(r):
        counter[req_key] += 1
        return r

    def response_handler(r):
        counter[resp_key] += 1
        return r

    def exception_handler(r):
        counter[exc_key] += 1
        return r

    transport.middleware.request(handler=request_handler)
    transport.middleware.response(handler=response_handler)
    transport.middleware.exception(handler=exception_handler)

    expect = {"foo": "bar"}
    req = Request(url=TEST_URL, method="post", json=expect)

    with requests_mock.Mocker() as m:
        request_uuid = str(uuid.uuid4())
        m.post(
            TEST_URL,
            text=json.dumps(expect),
            status_code=200,
            headers={http.REQUEST_UUID_HEADER_KEY: request_uuid},
        )
        resp = transport.send(req)
        assert resp.text
        assert resp.json() == expect
        assert resp.request_uuid == request_uuid

    with pytest.raises(Exception):
        transport.send(Request(url="/"))

    assert counter[req_key] == 2
    assert counter[resp_key] == 1
    assert counter[exc_key] == 1


def test_guess_json_utf():
    encodings = [
        "utf-32",
        "utf-8-sig",
        "utf-16",
        "utf-8",
        "utf-16-be",
        "utf-16-le",
        "utf-32-be",
        "utf-32-le",
    ]
    for e in encodings:
        s = json.dumps("表意字符").encode(e)
        assert utils.guess_json_utf(s) == e


def test_request_methods():
    req = Request(
        TEST_URL, data={"foo": 42}, json={"bar": 42}, params={"q": "search"}
    )
    assert req.payload() == {"foo": 42, "bar": 42, "q": "search"}


def test_response_methods():
    r = Response(TEST_URL, "post")
    assert not r.text
    assert r.json() is None

    r = Response(TEST_URL, "post", content=b"\xd6", encoding="utf-8")
    with pytest.raises(exc.InvalidResponseException):
        assert r.json() is None
