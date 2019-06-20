import base64
import typing
import collections

from ucloud.core.utils import compact
from ucloud.core.typesystem import abstract
from ucloud.core.exc import ValidationException


class List(abstract.Field):
    """ array param is the custom field to parse custom param such as:

    - IP.N
    - UDisk.N.Size
    - NetInterface.N.EIP.Bandwidth
    """

    def __init__(
        self,
        item: typing.Union[abstract.Field, abstract.Schema],
        required: bool = False,
        **kwargs
    ):
        super(List, self).__init__(required=required, **kwargs)
        self.item = item

    def dumps(self, value, name=None, **kwargs):
        if not isinstance(value, collections.Iterable):
            raise ValidationException(
                "invalid field {}, expect list, got {}".format(name, type(value))
            )

        errors = []
        values = []
        for each in value:
            try:
                v = self.item.dumps(each)
            except ValidationException as e:
                errors.extend(e.errors)
            else:
                values.append(v)

        if len(errors) > 0:
            raise ValidationException(errors)

        return values

    def loads(self, value, name=None, **kwargs):
        if not isinstance(value, collections.Iterable):
            raise ValidationException(
                "invalid field {}, expect list, got {}".format(name, type(value))
            )

        errors = []
        values = []
        for each in value:
            try:
                v = self.item.loads(each)
            except ValidationException as e:
                errors.extend(e.errors)
            else:
                values.append(v)

        if len(errors) > 0:
            raise ValidationException(errors)

        return values


class Str(abstract.Field):
    def dumps(self, value, name=None, **kwargs):
        if not isinstance(value, compact.string_types):
            raise ValidationException(
                "invalid field {}, expect str, got {}".format(name, type(value))
            )
        return value

    def loads(self, value, name=None, **kwargs):
        if not isinstance(value, compact.string_types):
            raise ValidationException(
                "invalid field {}, expect str, got {}".format(name, type(value))
            )
        return value


class Base64(Str):
    def dumps(self, value, name=None, **kwargs):
        s = super(Base64, self).dumps(value, name)
        return base64.b64encode(s.encode()).decode()

    def loads(self, value, name=None, **kwargs):
        s = super(Base64, self).loads(value, name)
        return base64.b64decode(s.encode()).decode()


class Int(abstract.Field):
    def dumps(self, value, name=None, **kwargs):
        if not isinstance(value, int):
            raise ValidationException(
                "invalid field {}, expect int, got {}".format(name, type(value))
            )
        return int(value)

    def loads(self, value, name=None, **kwargs):
        if not isinstance(value, int):
            raise ValidationException(
                "invalid field {}, expect int, got {}".format(name, type(value))
            )
        return int(value)


class Float(abstract.Field):
    def dumps(self, value, name=None, **kwargs):
        if not isinstance(value, float):
            raise ValidationException(
                "invalid field {}, expect float, got {}".format(name, type(value))
            )
        return float(value)

    def loads(self, value, name=None, **kwargs):
        if not isinstance(value, float):
            raise ValidationException(
                "invalid field {}, expect float, got {}".format(name, type(value))
            )
        return float(value)


class Bool(abstract.Field):
    def dumps(self, value, name=None, **kwargs):
        if not isinstance(value, bool):
            raise ValidationException(
                "invalid field {}, expect bool, got {}".format(name, type(value))
            )
        return bool(value)

    def loads(self, value, name=None, **kwargs):
        if not isinstance(value, bool):
            raise ValidationException(
                "invalid field {}, expect bool, got {}".format(name, type(value))
            )
        return bool(value)
