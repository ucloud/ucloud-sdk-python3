import typing
import abc


class Field(abc.ABC):
    def __init__(
        self,
        required: bool = False,
        default: typing.Any = None,
        dump_to: str = None,
        load_from: str = None,
        **kwargs
    ):
        self.required = required
        self.default = default
        self.dump_to = dump_to
        self.load_from = load_from
        self.options = kwargs

    def dumps(self, value, **kwargs):
        raise NotImplementedError

    def loads(self, value, **kwargs):
        raise NotImplementedError


class Schema(abc.ABC):
    fields = {}

    def __init__(
        self,
        required: bool = False,
        default: typing.Any = None,
        dump_to: str = None,
        load_from: str = None,
        **kwargs
    ):
        self.required = required
        self.default = default
        self.dump_to = dump_to
        self.load_from = load_from
        self.options = kwargs

    def dumps(self, d: dict) -> dict:
        raise NotImplementedError

    def loads(self, d: dict) -> dict:
        raise NotImplementedError
