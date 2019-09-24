""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.uphost.schemas import models


""" UPHost API Schema
"""


"""
API: CreatePHost

指定数据中心，根据资源使用量创建指定数量的UPHost物理云主机实例。
"""


class CreatePHostRequestSchema(schema.RequestSchema):
    """ CreatePHost - 指定数据中心，根据资源使用量创建指定数量的UPHost物理云主机实例。
    """

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Cluster": fields.Str(required=False, dump_to="Cluster"),
        "Count": fields.Int(required=False, dump_to="Count"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Str(required=False, dump_to="Quantity"),
        "Raid": fields.Str(required=False, dump_to="Raid"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "SecurityGroupId": fields.Str(required=False, dump_to="SecurityGroupId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreatePHostResponseSchema(schema.ResponseSchema):
    """ CreatePHost - 指定数据中心，根据资源使用量创建指定数量的UPHost物理云主机实例。
    """

    fields = {"PHostId": fields.List(fields.Str(), required=False, load_from="PHostId")}


"""
API: DescribePHost

获取物理机详细信息
"""


class DescribePHostRequestSchema(schema.RequestSchema):
    """ DescribePHost - 获取物理机详细信息
    """

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "PHostId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribePHostResponseSchema(schema.ResponseSchema):
    """ DescribePHost - 获取物理机详细信息
    """

    fields = {
        "PHostSet": fields.List(
            models.PHostSetSchema(), required=False, load_from="PHostSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribePHostImage

获取物理云主机镜像列表
"""


class DescribePHostImageRequestSchema(schema.RequestSchema):
    """ DescribePHostImage - 获取物理云主机镜像列表
    """

    fields = {
        "ImageId": fields.List(fields.Str()),
        "ImageType": fields.Str(required=False, dump_to="ImageType"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribePHostImageResponseSchema(schema.ResponseSchema):
    """ DescribePHostImage - 获取物理云主机镜像列表
    """

    fields = {
        "ImageSet": fields.List(
            models.PHostImageSetSchema(), required=False, load_from="ImageSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribePHostTags

获取物理机tag列表（业务组）
"""


class DescribePHostTagsRequestSchema(schema.RequestSchema):
    """ DescribePHostTags - 获取物理机tag列表（业务组）
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribePHostTagsResponseSchema(schema.ResponseSchema):
    """ DescribePHostTags - 获取物理机tag列表（业务组）
    """

    fields = {
        "TagSet": fields.List(
            models.PHostTagSetSchema(), required=False, load_from="TagSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetPHostPrice

获取物理机价格列表
"""


class GetPHostPriceRequestSchema(schema.RequestSchema):
    """ GetPHostPrice - 获取物理机价格列表
    """

    fields = {
        "ChargeType": fields.Str(required=True, dump_to="ChargeType"),
        "Cluster": fields.Str(required=False, dump_to="Cluster"),
        "Count": fields.Int(required=True, dump_to="Count"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=True, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetPHostPriceResponseSchema(schema.ResponseSchema):
    """ GetPHostPrice - 获取物理机价格列表
    """

    fields = {
        "PriceSet": fields.List(
            models.PHostPriceSetSchema(), required=False, load_from="PriceSet"
        )
    }


"""
API: ModifyPHostInfo

更改物理机信息
"""


class ModifyPHostInfoRequestSchema(schema.RequestSchema):
    """ ModifyPHostInfo - 更改物理机信息
    """

    fields = {
        "Name": fields.Str(required=False, dump_to="Name"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ModifyPHostInfoResponseSchema(schema.ResponseSchema):
    """ ModifyPHostInfo - 更改物理机信息
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}


"""
API: PoweroffPHost

断电物理云主机
"""


class PoweroffPHostRequestSchema(schema.RequestSchema):
    """ PoweroffPHost - 断电物理云主机
    """

    fields = {
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class PoweroffPHostResponseSchema(schema.ResponseSchema):
    """ PoweroffPHost - 断电物理云主机
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}


"""
API: RebootPHost

重启物理机
"""


class RebootPHostRequestSchema(schema.RequestSchema):
    """ RebootPHost - 重启物理机
    """

    fields = {
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class RebootPHostResponseSchema(schema.ResponseSchema):
    """ RebootPHost - 重启物理机
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}


"""
API: ReinstallPHost

重装物理机操作系统
"""


class ReinstallPHostRequestSchema(schema.RequestSchema):
    """ ReinstallPHost - 重装物理机操作系统
    """

    fields = {
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Raid": fields.Str(required=False, dump_to="Raid"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "ReserveDisk": fields.Str(required=False, dump_to="ReserveDisk"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ReinstallPHostResponseSchema(schema.ResponseSchema):
    """ ReinstallPHost - 重装物理机操作系统
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}


"""
API: StartPHost

启动物理机
"""


class StartPHostRequestSchema(schema.RequestSchema):
    """ StartPHost - 启动物理机
    """

    fields = {
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class StartPHostResponseSchema(schema.ResponseSchema):
    """ StartPHost - 启动物理机
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}


"""
API: TerminatePHost

删除物理云主机
"""


class TerminatePHostRequestSchema(schema.RequestSchema):
    """ TerminatePHost - 删除物理云主机
    """

    fields = {
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ReleaseEIP": fields.Bool(required=False, dump_to="ReleaseEIP"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class TerminatePHostResponseSchema(schema.ResponseSchema):
    """ TerminatePHost - 删除物理云主机
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}
