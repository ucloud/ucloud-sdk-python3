""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class GroupBaseInfoSchema(schema.ResponseSchema):
    """GroupBaseInfo - Group基础信息"""

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "GroupName": fields.Str(required=True, load_from="GroupName"),
        "Id": fields.Str(required=True, load_from="Id"),
        "Remark": fields.Str(required=True, load_from="Remark"),
    }
