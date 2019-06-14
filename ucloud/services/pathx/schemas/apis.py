from ucloud.core.typesystem import schema, fields
from ucloud.services.pathx.schemas import models


""" PathX API Schema
"""


"""
API: DescribeGlobalSSHArea

获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性
"""


class DescribeGlobalSSHAreaRequestSchema(schema.RequestSchema):
    """ DescribeGlobalSSHArea - 获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性
    """

    fields = {
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeGlobalSSHAreaResponseSchema(schema.ResponseSchema):
    """ DescribeGlobalSSHArea - 获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性
    """

    fields = {
        "AreaSet": fields.List(
            models.GlobalSSHAreaSchema(), required=False, load_from="AreaSet"
        ),
        "Message": fields.Str(required=False, load_from="Message"),
    }


"""
API: DescribeGlobalSSHInstance

获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）
"""


class DescribeGlobalSSHInstanceRequestSchema(schema.RequestSchema):
    """ DescribeGlobalSSHInstance - 获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）
    """

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "InstanceId": fields.Str(required=False, dump_to="InstanceId"),
    }


class DescribeGlobalSSHInstanceResponseSchema(schema.ResponseSchema):
    """ DescribeGlobalSSHInstance - 获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）
    """

    fields = {
        "InstanceSet": fields.List(
            models.GlobalSSHInfoSchema(), required=False, load_from="InstanceSet"
        )
    }


"""
API: ModifyGlobalSSHPort

修改GlobalSSH端口
"""


class ModifyGlobalSSHPortRequestSchema(schema.RequestSchema):
    """ ModifyGlobalSSHPort - 修改GlobalSSH端口
    """

    fields = {
        "InstanceId": fields.Str(required=True, dump_to="InstanceId"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class ModifyGlobalSSHPortResponseSchema(schema.ResponseSchema):
    """ ModifyGlobalSSHPort - 修改GlobalSSH端口
    """

    fields = {"Message": fields.Str(required=False, load_from="Message")}


"""
API: ModifyGlobalSSHRemark

修改GlobalSSH备注
"""


class ModifyGlobalSSHRemarkRequestSchema(schema.RequestSchema):
    """ ModifyGlobalSSHRemark - 修改GlobalSSH备注
    """

    fields = {
        "InstanceId": fields.Str(required=True, dump_to="InstanceId"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class ModifyGlobalSSHRemarkResponseSchema(schema.ResponseSchema):
    """ ModifyGlobalSSHRemark - 修改GlobalSSH备注
    """

    fields = {"Message": fields.Str(required=False, load_from="Message")}


"""
API: CreateGlobalSSHInstance

创建GlobalSSH实例
"""


class CreateGlobalSSHInstanceRequestSchema(schema.RequestSchema):
    """ CreateGlobalSSHInstance - 创建GlobalSSH实例
    """

    fields = {
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Area": fields.Str(required=True, dump_to="Area"),
        "TargetIP": fields.Str(required=True, dump_to="TargetIP"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "AreaCode": fields.Str(required=True, dump_to="AreaCode"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
    }


class CreateGlobalSSHInstanceResponseSchema(schema.ResponseSchema):
    """ CreateGlobalSSHInstance - 创建GlobalSSH实例
    """

    fields = {
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "AcceleratingDomain": fields.Str(
            required=False, load_from="AcceleratingDomain"
        ),
        "Message": fields.Str(required=False, load_from="Message"),
    }


"""
API: DeleteGlobalSSHInstance

删除GlobalSSH实例
"""


class DeleteGlobalSSHInstanceRequestSchema(schema.RequestSchema):
    """ DeleteGlobalSSHInstance - 删除GlobalSSH实例
    """

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "InstanceId": fields.Str(required=True, dump_to="InstanceId"),
    }


class DeleteGlobalSSHInstanceResponseSchema(schema.ResponseSchema):
    """ DeleteGlobalSSHInstance - 删除GlobalSSH实例
    """

    fields = {"Message": fields.Str(required=False, load_from="Message")}
