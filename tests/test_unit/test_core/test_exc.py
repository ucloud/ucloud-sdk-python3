import pytest
from ucloud.core import exc


def test_ret_code_error():
    assert not exc.UCloudException().retryable

    code_error = exc.RetCodeException("Foo", 1, "")
    assert str(code_error)
    assert not code_error.retryable
    assert code_error.json() == {"Action": "Foo", "Message": "", "RetCode": 1}

    validate_error = exc.ValidationException(ValueError("invalid type"))
    assert not validate_error.retryable
    assert str(validate_error)
