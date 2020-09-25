import base64
import typing
import collections

from ucloud.core.typesystem import abstract
from ucloud.core.exc import ValidationException
from ucloud.core.utils.compat import str


class List(abstract.Field):
    """array param is the custom field to parse custom param such as:

    - IP.N
    - UDisk.N.Size
    - NetInterface.N.EIP.Bandwidth
    """

    def __init__(
        self,
        item: typing.Union[abstract.Field, abstract.Schema],
        default=list,
        **kwargs
    ):
        super(List, self).__init__(default=default, **kwargs)
        self.item = item

    def dumps(self, value, name=None, **kwargs):
        if not isinstance(value, collections.Iterable):
            raise ValidationException(
                "invalid field {}, expect list, got {}".format(
                    name, type(value)
                )
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
                "invalid field {}, expect list, got {}".format(
                    name, type(value)
                )
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
        return self._convert(value, name)

    def loads(self, value, name=None, **kwargs):
        return self._convert(value, name)

    def _convert(self, value, name=None):
        if self.strict and not isinstance(value, str):
            self.fail(name, "str", type(value))

        return str(value)


class Base64(Str):
    def dumps(self, value, name=None, **kwargs):
        s = super(Base64, self).dumps(value, name)
        return base64.b64encode(s.encode()).decode()

    def loads(self, value, name=None, **kwargs):
        s = super(Base64, self).loads(value, name)
        return base64.b64decode(s.encode()).decode()


class Int(abstract.Field):
    def dumps(self, value, name=None, **kwargs):
        return self._convert(value, name)

    def loads(self, value, name=None, **kwargs):
        return self._convert(value, name)

    def _convert(self, value, name=None):
        if self.strict and not isinstance(value, int):
            self.fail(name, "int", type(value))

        try:
            return int(value)
        except ValueError:
            self.fail(name, "int", type(value))


class Float(abstract.Field):
    def dumps(self, value, name=None, **kwargs):
        return self._convert(value, name)

    def loads(self, value, name=None, **kwargs):
        return self._convert(value, name)

    def _convert(self, value, name=None):
        if self.strict and not isinstance(value, float):
            self.fail(name, "float", type(value))

        try:
            return float(value)
        except ValueError:
            self.fail(name, "float", type(value))


class Bool(abstract.Field):
    def dumps(self, value, name=None, **kwargs):
        return self._convert(value, name)

    def loads(self, value, name=None, **kwargs):
        return self._convert(value, name)

    def _convert(self, value, name=None):
        if self.strict and not isinstance(value, bool):
            self.fail(name, "bool", type(value))

        if value == "true" or value is True:
            return True

        if value == "false" or value is False:
            return False

        self.fail(name, "bool", type(value))
