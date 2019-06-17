from ucloud.core.typesystem import schema, fields
from ucloud.services.uphost.schemas import models


""" UPHost API Schema
"""


"""
API: DescribePHostImage

获取物理云主机镜像列表
"""


class DescribePHostImageRequestSchema(schema.RequestSchema):
    """ DescribePHostImage - 获取物理云主机镜像列表
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageType": fields.Str(required=False, dump_to="ImageType"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "ImageId": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
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
API: ModifyPHostInfo

更改物理机信息
"""


class ModifyPHostInfoRequestSchema(schema.RequestSchema):
    """ ModifyPHostInfo - 更改物理机信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class ModifyPHostInfoResponseSchema(schema.ResponseSchema):
    """ ModifyPHostInfo - 更改物理机信息
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
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "Region": fields.Str(required=True, dump_to="Region"),
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
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "ReserveDisk": fields.Str(required=False, dump_to="ReserveDisk"),
        "Raid": fields.Str(required=False, dump_to="Raid"),
        "Region": fields.Str(required=True, dump_to="Region"),
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
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
        "ReleaseEIP": fields.Bool(required=False, dump_to="ReleaseEIP"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class TerminatePHostResponseSchema(schema.ResponseSchema):
    """ TerminatePHost - 删除物理云主机
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}


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
        "Raid": fields.Str(required=False, dump_to="Raid"),
        "Cluster": fields.Str(required=False, dump_to="Cluster"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "SecurityGroupId": fields.Str(required=False, dump_to="SecurityGroupId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Region": fields.Str(required=True, dump_to="Region"),
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
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "PHostId": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
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
API: DescribePHostTags

获取物理机tag列表（业务组）
"""


class DescribePHostTagsRequestSchema(schema.RequestSchema):
    """ DescribePHostTags - 获取物理机tag列表（业务组）
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
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
        "Count": fields.Int(required=True, dump_to="Count"),
        "ChargeType": fields.Str(required=True, dump_to="ChargeType"),
        "Quantity": fields.Int(required=True, dump_to="Quantity"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Cluster": fields.Str(required=False, dump_to="Cluster"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
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
API: PoweroffPHost

断电物理云主机
"""


class PoweroffPHostRequestSchema(schema.RequestSchema):
    """ PoweroffPHost - 断电物理云主机
    """

    fields = {
        "PHostId": fields.Str(required=True, dump_to="PHostId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class PoweroffPHostResponseSchema(schema.ResponseSchema):
    """ PoweroffPHost - 断电物理云主机
    """

    fields = {"PHostId": fields.Str(required=False, load_from="PHostId")}
