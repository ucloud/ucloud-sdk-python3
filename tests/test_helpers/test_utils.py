from ucloud.helpers import utils


def test_b64encode():
    encoded = utils.b64encode("foobar42")
    assert encoded == 'Zm9vYmFyNDI='


def test_b64decode():
    decoded = utils.b64decode("Zm9vYmFyNDI=")
    assert decoded == 'foobar42'
