""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class ServiceIDSchema(schema.ResponseSchema):
    """ServiceID - 服务ID"""

    fields = {
        "Id": fields.Str(required=True, load_from="Id"),
    }
