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
        "Quantity": fields.Str(required=False, dump_to="Quantity"),
        "Count": fields.Int(required=False, dump_to="Count"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Cluster": fields.Str(required=False, dump_to="Cluster"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "Raid": fields.Str(required=False, dump_to="Raid"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "SecurityGroupId": fields.Str(required=False, dump_to="SecurityGroupId"),
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
        "PHostId": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
    }


class DescribePHostResponseSchema(schema.ResponseSchema):
    """ DescribePHost - 获取物理机详细信息
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "PHostSet": fields.List(
            models.PHostSetSchema(), required=False, load_from="PHostSet"
        ),
    }


"""
API: DescribePHostImage

获取物理云主机镜像列表
"""


class DescribePHostImageRequestSchema(schema.RequestSchema):
    """ DescribePHostImage - 获取物理云主机镜像列表
    """

    fields = {
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageType": fields.Str(required=False, dump_to="ImageType"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "ImageId": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribePHostImageResponseSchema(schema.ResponseSchema):
    """ DescribePHostImage - 获取物理云主机镜像列表
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "ImageSet": fields.List(
            models.PHostImageSetSchema(), required=False, load_from="ImageSet"
        ),
    }


"""
API: DescribePHostTags

获取物理机tag列表（业务组）
"""


class DescribePHostTagsRequestSchema(schema.RequestSchema):
    """ DescribePHostTags - 获取物理机tag列表（业务组）
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribePHostTagsResponseSchema(schema.ResponseSchema):
    """ DescribePHostTags - 获取物理机tag列表（业务组）
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "TagSet": fields.List(
            models.PHostTagSetSchema(), required=False, load_from="TagSet"
        ),
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
        "Quantity": fields.Int(required=True, dump_to="Quantity"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Cluster": fields.Str(required=False, dump_to="Cluster"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Count": fields.Int(required=True, dump_to="Count"),
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
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
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
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
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
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "ReserveDisk": fields.Str(required=False, dump_to="ReserveDisk"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Raid": fields.Str(required=False, dump_to="Raid"),
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "ReleaseEIP": fields.Bool(required=False, dump_to="ReleaseEIP"),
    }


class TerminatePHostResponseSchema(schema.ResponseSchema):
    """ TerminatePHost - 删除物理云主机
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}
