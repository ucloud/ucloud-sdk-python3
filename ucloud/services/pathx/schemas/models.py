from ucloud.core.typesystem import schema, fields


class GlobalSSHInfoSchema(schema.ResponseSchema):
    """ GlobalSSHInfo - GlobalSSH实例信息
    """

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "AcceleratingDomain": fields.Str(required=True, load_from="AcceleratingDomain"),
        "Area": fields.Str(required=True, load_from="Area"),
        "Port": fields.Int(required=True, load_from="Port"),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "TargetIP": fields.Str(required=True, load_from="TargetIP"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
    }


class GlobalSSHAreaSchema(schema.ResponseSchema):
    """ GlobalSSHArea - GlobalSSH覆盖地区,包括关联的UCloud机房信息
    """

    fields = {
        "Area": fields.Str(required=True, load_from="Area"),
        "AreaCode": fields.Str(required=True, load_from="AreaCode"),
        "RegionSet": fields.List(fields.Str()),
    }
