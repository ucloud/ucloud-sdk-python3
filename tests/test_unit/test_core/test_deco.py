from ucloud.core.utils.deco import deprecated


@deprecated(instead_of="bar")
def foo():
    pass


def test_deprecated_deco(caplog):
    foo()
    assert "deprecated" in caplog.text
