from ucloud.core.typesystem import schema, fields


class GlobalSSHAreaSchema(schema.ResponseSchema):
    """ GlobalSSHArea - GlobalSSH覆盖地区,包括关联的UCloud机房信息
    """

    fields = {
        "Area": fields.Str(required=True, load_from="Area"),
        "AreaCode": fields.Str(required=True, load_from="AreaCode"),
        "RegionSet": fields.List(fields.Str()),
    }


class GlobalSSHInfoSchema(schema.ResponseSchema):
    """ GlobalSSHInfo - GlobalSSH实例信息
    """

    fields = {
        "Port": fields.Int(required=True, load_from="Port"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "AcceleratingDomain": fields.Str(required=True, load_from="AcceleratingDomain"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "Area": fields.Str(required=True, load_from="Area"),
        "TargetIP": fields.Str(required=True, load_from="TargetIP"),
    }
