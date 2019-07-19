import logging
from ucloud.core.typesystem import abstract, fields
from ucloud.core.exc import ValidationException
from ucloud.core.utils import compact

logger = logging.getLogger(__name__)


class Schema(abstract.Schema):
    fields = {}

    def dumps(self, d: dict, name=None, **kwargs) -> dict:
        result = {}
        errors = []

        for k, field in self.fields.items():
            v = d.get(k)

            # resolve value is empty
            if v is None:
                if field.required:
                    errors.append(
                        ValidationException("the field {k} is required".format(k=k))
                    )
                    continue

                if field.default is None:
                    continue

                if isinstance(field.default, compact.Callable):
                    v = field.default()
                else:
                    v = field.default

            try:
                serialized = field.dumps(v, name=k)
            except ValidationException as e:
                errors.extend(e.errors)
                continue

            result[field.dump_to or k] = serialized

        if len(errors) > 0:
            raise ValidationException(errors)

        return result

    def loads(self, d: dict, name=None, **kwargs) -> dict:
        result = {}
        errors = []

        if not self.case_sensitive:
            d = {k.lower(): v for k, v in d.items()}

        for k, field in self.fields.items():
            load_key = (field.load_from or k)
            v = d.get(load_key if self.case_sensitive else load_key.lower())
            if v is None:
                if field.default is None:
                    continue

                if isinstance(field.default, compact.Callable):
                    v = field.default()
                else:
                    v = field.default

            try:
                serialized = field.loads(v, name=k)
            except ValidationException as e:
                errors.extend(e.errors)
                continue

            result[k] = serialized

        if len(errors) > 0:
            raise ValidationException(errors)

        return result


class RequestSchema(Schema):
    fields = {}

    def dumps(self, d: dict, name=None, **kwargs) -> dict:
        if not isinstance(d, dict):
            raise ValidationException(
                "invalid field {}, expect dict, got {}".format(name, type(d))
            )

        result = {}
        errors = []

        for k, field in self.fields.items():
            v = d.get(k)

            # resolve value is empty
            if v is None:
                if field.required:
                    errors.append(
                        ValidationException("the field {k} is required".format(k=k))
                    )
                    continue

                if field.default is None:
                    continue

                if isinstance(field.default, compact.Callable):
                    v = field.default()
                else:
                    v = field.default

            try:
                serialized = field.dumps(v, name=k)
            except ValidationException as e:
                errors.extend(e.errors)
                continue

            k = field.dump_to or k

            if isinstance(field, fields.List):
                for i, item in enumerate(serialized):
                    if not isinstance(field.item, RequestSchema):
                        result["{k}.{i}".format(k=k, i=i)] = item
                        continue

                    for item_k, item_v in item.items():
                        result[
                            "{k}.{i}.{item_k}".format(k=k, i=i, item_k=item_k)
                        ] = item_v
            elif isinstance(field, RequestSchema):
                for dk, dv in serialized.items():
                    result["{k}.{dk}".format(k=k, dk=dk)] = dv
            else:
                result[k] = serialized

        if len(errors) > 0:
            raise ValidationException(errors)

        return result


class ResponseSchema(Schema):
    pass
