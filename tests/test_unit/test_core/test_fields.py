import logging

import pytest

from ucloud.core import exc
from ucloud.core.typesystem import fields

logger = logging.getLogger(__name__)


def test_field_str():
    s = fields.Str()
    assert s.dumps(s.loads("foo")) == "foo"

    with pytest.raises(exc.ValidationException):
        fields.Str(strict=True).loads(42)


def test_field_int():
    i = fields.Int()
    assert i.dumps(i.loads("42")) == 42

    with pytest.raises(exc.ValidationException):
        fields.Int().dumps("foo")

    with pytest.raises(exc.ValidationException):
        fields.Int(strict=True).loads("42")


def test_field_float():
    f = fields.Float()
    assert f.dumps(f.loads("42.0")) == 42.0

    with pytest.raises(exc.ValidationException):
        fields.Float().dumps("foo")

    with pytest.raises(exc.ValidationException):
        fields.Float(strict=True).loads("42.0")


def test_field_bool():
    b = fields.Bool()
    assert b.dumps(b.loads("true"))
    assert not b.dumps(b.loads("false"))

    with pytest.raises(exc.ValidationException):
        fields.Bool().dumps("foo")

    with pytest.raises(exc.ValidationException):
        fields.Bool(strict=True).loads("true")


def test_field_list():
    l = fields.List(fields.Int())
    assert l.dumps(l.loads(["42"])) == [42]

    with pytest.raises(exc.ValidationException):
        fields.List(fields.Int(), strict=True).dumps(42)

    with pytest.raises(exc.ValidationException):
        fields.List(fields.Int()).dumps(["foo"])

    with pytest.raises(exc.ValidationException):
        fields.List(fields.Int(strict=True)).loads(["42"])


def test_field_base64():
    b64 = fields.Base64()
    assert b64.loads("Zm9v") == "foo"
    assert b64.dumps("foo") == "Zm9v"
