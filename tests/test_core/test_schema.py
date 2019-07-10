import logging

from ucloud.core.typesystem import fields, schema

logger = logging.getLogger(__name__)


def test_array():
    class TestSchema(schema.RequestSchema):
        fields = {"IP": fields.List(fields.Str())}

    ret = TestSchema().dumps({"IP": ["127.0.0.1"]})
    assert ret.get("IP.0") == "127.0.0.1"
    assert ret.get("IP") is None
    assert ret.get("IP.1") is None


def test_array_model():
    class TestSchema(schema.RequestSchema):
        fields = {"IP": fields.List(fields.Str(), default=["127.0.0.1"])}

    class TestArrayModel(schema.RequestSchema):
        fields = {"Interface": TestSchema()}

    class TestArrayModelArray(schema.RequestSchema):
        fields = {"Interface": fields.List(TestSchema(), default=list)}

    d = {"Interface": {"IP": ["127.0.0.1", "192.168.0.1"]}}
    ret = TestArrayModel().dumps(d)
    assert ret.get("Interface.IP.0") == "127.0.0.1"
    assert ret.get("Interface.IP.1") == "192.168.0.1"

    d = {
        "Interface": [
            {"IP": ["127.0.0.1", "192.168.0.1"]},
            {"IP": ["172.16.0.1"]},
        ]
    }
    ret = TestArrayModelArray().dumps(d)
    assert ret.get("Interface.0.IP.0") == "127.0.0.1"
    assert ret.get("Interface.0.IP.1") == "192.168.0.1"
    assert ret.get("Interface.1.IP.0") == "172.16.0.1"

    d = {}
    ret = TestArrayModelArray().dumps(d)
    assert ret.get("Interface") is None

    d = {"Interface": [{"IP": None}]}
    ret = TestArrayModelArray().dumps(d)
    assert ret.get("Interface.0.IP.0") == "127.0.0.1"

    d = {"Interface": [{}]}
    ret = TestArrayModelArray().dumps(d)
    assert ret.get("Interface.0.IP.0") == "127.0.0.1"
