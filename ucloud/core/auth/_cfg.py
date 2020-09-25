import hashlib
from collections import OrderedDict
from ucloud.core.typesystem import schema, fields, encoder


class CredentialSchema(schema.Schema):
    fields = {
        "public_key": fields.Str(required=True),
        "private_key": fields.Str(required=True),
    }


def verify_ac(private_key: str, params: dict) -> str:
    """calculate signature by private_key/public_key

    the keys can be found on `APIKey documentation <https://console.ucloud.cn/uapi/apikey>`__

    >>> verify_ac("my_private_key", {"foo": "bar"})
    '634edc1bb957c0d65e5ab5494cf3b7784fbc87af'

    >>> verify_ac("my_private_key", {"foo": "bar"})
    '634edc1bb957c0d65e5ab5494cf3b7784fbc87af'

    :param private_key: private key
    :param params:
    :return:
    """
    params = OrderedDict(sorted(params.items(), key=lambda item: item[0]))

    simplified = ""
    for key, value in params.items():
        simplified += str(key) + encoder.encode_value(value)
    simplified += private_key

    hash_new = hashlib.sha1()
    hash_new.update(simplified.encode("utf-8"))
    hash_value = hash_new.hexdigest()
    return hash_value


class Credential:
    """credential is the object to store credential information

    the keys can be found on `APIKey documentation <https://console.ucloud.cn/uapi/apikey>`__

    it can calculate signature for OpenAPI:

    >>> cred = Credential('my_public_key', 'my_private_key')
    >>> cred.verify_ac({"foo": "bar"})
    'd4411ab30953fb0bbcb1e7313081f05e4e91a394'

    :param public_key:
    :param private_key:
    """

    PUBLIC_KEY_NAME = "PublicKey"

    def __init__(self, public_key: str, private_key: str, **kwargs):
        self.public_key = public_key
        self.private_key = private_key

    def verify_ac(self, args: dict) -> str:
        args[Credential.PUBLIC_KEY_NAME] = self.public_key
        return verify_ac(self.private_key, args)

    @classmethod
    def from_dict(cls, d: dict):
        parsed = CredentialSchema().dumps(d)
        return cls(**parsed)

    def to_dict(self) -> dict:
        return {"public_key": self.public_key, "private_key": self.private_key}
