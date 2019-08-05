import logging

import pytest

from ucloud.core import exc
from ucloud.core.typesystem import fields, schema

logger = logging.getLogger(__name__)


def test_request_basic():
    class Schema(schema.RequestSchema):
        fields = {
            "Foo": fields.Int(required=True),
            "Bar": fields.Int(required=False)
        }

    assert Schema().dumps({'Foo': "42"}) == {'Foo': 42}
    assert Schema().dumps({'Foo': "42"}) == {'Foo': 42}

    with pytest.raises(exc.ValidationException):
        Schema().dumps({})

    with pytest.raises(exc.ValidationException):
        Schema().dumps({'Foo': "bar"})


def test_request_array():
    class Schema(schema.RequestSchema):
        fields = {"IP": fields.List(fields.Str())}

    # basic
    d = Schema().dumps({"IP": ["127.0.0.1"]})
    assert d == {"IP.0": "127.0.0.1"}

    # default by zero value
    d = Schema().dumps({})
    assert d == {}


def test_request_array_with_default():
    class Schema(schema.RequestSchema):
        fields = {"IP": fields.List(fields.Str(), default=["127.0.0.1"])}

    # basic
    d = Schema().dumps({"IP": ["192.168.0.1"]})
    assert d == {"IP.0": "192.168.0.1"}

    # default by default value
    d = Schema().dumps({})
    assert d == {"IP.0": "127.0.0.1"}


def test_request_object_model():
    class Schema(schema.RequestSchema):
        fields = {"IP": fields.List(fields.Str())}

    class NestedObjectSchema(schema.RequestSchema):
        fields = {"Interface": Schema()}

    # success
    d = NestedObjectSchema().dumps({"Interface": {"IP": ["127.0.0.1"]}})
    assert d == {"Interface.IP.0": "127.0.0.1"}

    # dumps
    with pytest.raises(exc.ValidationException):
        NestedObjectSchema().dumps({"Interface": 1})


def test_request_array_model_with_default():
    class Schema(schema.RequestSchema):
        fields = {"IP": fields.List(fields.Str())}

    class NestedArraySchema(schema.RequestSchema):
        fields = {
            "Interface": fields.List(
                Schema(default=lambda: "127.0.0.1"),
                default=lambda: [{"IP": ["192.168.1.1"]}],
            )
        }

    # the top-level default value will overwrite nested default value
    d = NestedArraySchema().dumps({})
    assert d == {"Interface.0.IP.0": "192.168.1.1"}

    # nested value
    d = {
        "Interface": [
            {"IP": ["127.0.0.1", "192.168.0.1"]},
            {"IP": ["172.16.0.1"]},
        ]
    }
    d = NestedArraySchema().dumps(d)
    assert d == {
        "Interface.0.IP.0": "127.0.0.1",
        "Interface.0.IP.1": "192.168.0.1",
        "Interface.1.IP.0": "172.16.0.1",
    }


def test_response_basic():
    class Schema(schema.ResponseSchema):
        fields = {
            "Foo": fields.Int(required=True),
            "Bar": fields.Int(required=False),
            "Default": fields.Int(default=42),
            "Call": fields.List(fields.Int(), default=list)
        }

    assert Schema().dumps({'Foo': "42"}) == {
        'Foo': 42, 'Default': 42, 'Call': []
    }
    assert Schema().loads({'Foo': "42"}) == {
        'Foo': 42, 'Default': 42, 'Call': []
    }

    with pytest.raises(exc.ValidationException):
        Schema().dumps({})

    with pytest.raises(exc.ValidationException):
        Schema().dumps({'Foo': "bar"})

    with pytest.raises(exc.ValidationException):
        Schema().dumps({})

    with pytest.raises(exc.ValidationException):
        Schema().dumps({'Foo': "bar"})


def test_response_array():
    class Schema(schema.ResponseSchema):
        fields = {"IP": fields.List(fields.Str())}

    d = Schema().loads({})
    assert d == {"IP": []}

    d = Schema().loads({"IP": ["127.0.0.1"]})
    assert d == {"IP": ["127.0.0.1"]}

    with pytest.raises(exc.ValidationException):
        Schema().loads({"IP": 1})


def test_response_array_with_default():
    class Schema(schema.ResponseSchema):
        fields = {"IP": fields.List(fields.Str(), default=["127.0.0.1"])}

    # basic
    d = Schema().dumps({"IP": ["192.168.0.1"]})
    assert d == {"IP": ["192.168.0.1"]}

    # default by default value
    d = Schema().dumps({})
    assert d == {"IP": ["127.0.0.1"]}


def test_response_object_model():
    class Schema(schema.ResponseSchema):
        fields = {"IP": fields.List(fields.Str())}

    class NestedObjectSchema(schema.ResponseSchema):
        fields = {"EIP": Schema()}

    # basic
    d = NestedObjectSchema().loads({"EIP": {"IP": ["127.0.0.1"]}})
    assert d == {"EIP": {"IP": ["127.0.0.1"]}}

    # default by zero value
    d = NestedObjectSchema().loads({})
    assert d == {"EIP": {"IP": []}}


def test_response_object_model_case_insensitive():
    class Schema(schema.ResponseSchema):
        fields = {"IP": fields.List(fields.Str())}

    class NestedObjectSchema(schema.ResponseSchema):
        fields = {"EIP": Schema()}

    d = NestedObjectSchema().loads({"eip": {"Ip": ["127.0.0.1"]}})
    assert d == {"EIP": {"IP": ["127.0.0.1"]}}


def test_response_array_model_with_default():
    class Schema(schema.ResponseSchema):
        fields = {"IP": fields.List(fields.Str())}

    class NestedArraySchema(schema.ResponseSchema):
        fields = {
            "Interface": fields.List(
                Schema(default=lambda: {"IP": ["127.0.0.1"]}),
                default=lambda: [{"IP": ["192.168.1.1"]}],
            )
        }

    # the top-level default value will overwrite nested default value
    d = NestedArraySchema().dumps({})
    assert d == {"Interface": [{"IP": ["192.168.1.1"]}]}

    # nested value
    d = {
        "Interface": [
            {"IP": ["127.0.0.1", "192.168.0.1"]},
            {"IP": ["172.16.0.1"]},
        ]
    }
    d = NestedArraySchema().dumps(d)
    assert d == {
        "Interface": [
            {"IP": ["127.0.0.1", "192.168.0.1"]},
            {"IP": ["172.16.0.1"]},
        ]
    }
