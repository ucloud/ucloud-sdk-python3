import pytest

from ucloud.core.typesystem import encoder


@pytest.mark.parametrize(
    "input_vector,expected",
    [
        ({"foo": "bar"}, {"foo": "bar"}),
        ({"foo": 42}, {"foo": "42"}),
        ({"foo": 42.42}, {"foo": "42.42"}),
        ({"foo": 42.0}, {"foo": "42"}),
        ({"foo": True}, {"foo": "true"}),
        ({"foo": False}, {"foo": "false"}),
        ({"IP": ["127.0.0.1"]}, {"IP.0": "127.0.0.1"}),
        ({"TemplateParams": ["中文"]}, {"TemplateParams.0": "中文"}),
        ({"IP": ["foo", "bar"]}, {"IP.0": "foo", "IP.1": "bar"}),
        ({"IP": [{"foo": "bar"}]}, {"IP.0.foo": "bar"}),
    ],
)
def test_params_encode(input_vector, expected):
    result = encoder.encode(input_vector)
    assert result == expected
