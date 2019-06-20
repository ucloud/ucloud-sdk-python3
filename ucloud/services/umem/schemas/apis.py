from ucloud.core.typesystem import schema, fields
from ucloud.services.umem.schemas import models


""" UMem API Schema
"""


"""
API: DescribeUMemcachePrice

获取umemcache组价格信息
"""


class DescribeUMemcachePriceRequestSchema(schema.RequestSchema):
    """ DescribeUMemcachePrice - 获取umemcache组价格信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class DescribeUMemcachePriceResponseSchema(schema.ResponseSchema):
    """ DescribeUMemcachePrice - 获取umemcache组价格信息
    """

    fields = {
        "DataSet": fields.List(
            models.UMemcachePriceSetSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: DescribeUMemcacheUpgradePrice

获取umemcache升级价格信息
"""


class DescribeUMemcacheUpgradePriceRequestSchema(schema.RequestSchema):
    """ DescribeUMemcacheUpgradePrice - 获取umemcache升级价格信息
    """

    fields = {
        "Size": fields.Int(required=True, dump_to="Size"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUMemcacheUpgradePriceResponseSchema(schema.ResponseSchema):
    """ DescribeUMemcacheUpgradePrice - 获取umemcache升级价格信息
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: DescribeURedisPrice

取uredis价格信息
"""


class DescribeURedisPriceRequestSchema(schema.RequestSchema):
    """ DescribeURedisPrice - 取uredis价格信息
    """

    fields = {
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeURedisPriceResponseSchema(schema.ResponseSchema):
    """ DescribeURedisPrice - 取uredis价格信息
    """

    fields = {
        "DataSet": fields.List(
            models.URedisPriceSetSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: ModifyURedisGroupName

修改主备redis名称
"""


class ModifyURedisGroupNameRequestSchema(schema.RequestSchema):
    """ ModifyURedisGroupName - 修改主备redis名称
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Name": fields.Str(required=True, dump_to="Name"),
    }


class ModifyURedisGroupNameResponseSchema(schema.ResponseSchema):
    """ ModifyURedisGroupName - 修改主备redis名称
    """

    fields = {}


"""
API: CreateURedisGroup

创建主备redis
"""


class CreateURedisGroupRequestSchema(schema.RequestSchema):
    """ CreateURedisGroup - 创建主备redis
    """

    fields = {
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Password": fields.Base64(required=False, dump_to="Password"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Size": fields.Int(required=False, dump_to="Size"),
        "AutoBackup": fields.Str(required=False, dump_to="AutoBackup"),
        "ConfigId": fields.Str(required=False, dump_to="ConfigId"),
        "Version": fields.Str(required=False, dump_to="Version"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "HighAvailability": fields.Str(required=True, dump_to="HighAvailability"),
        "MasterGroupId": fields.Str(required=False, dump_to="MasterGroupId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "BackupId": fields.Str(required=False, dump_to="BackupId"),
        "BackupTime": fields.Int(required=False, dump_to="BackupTime"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
    }


class CreateURedisGroupResponseSchema(schema.ResponseSchema):
    """ CreateURedisGroup - 创建主备redis
    """

    fields = {"GroupId": fields.Str(required=False, load_from="GroupId")}


"""
API: DescribeUMemPrice

获取UMem实例价格信息
"""


class DescribeUMemPriceRequestSchema(schema.RequestSchema):
    """ DescribeUMemPrice - 获取UMem实例价格信息
    """

    fields = {
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
    }


class DescribeUMemPriceResponseSchema(schema.ResponseSchema):
    """ DescribeUMemPrice - 获取UMem实例价格信息
    """

    fields = {
        "DataSet": fields.List(
            models.UMemPriceSetSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: DescribeUMemUpgradePrice

获取UMem升级价格信息
"""


class DescribeUMemUpgradePriceRequestSchema(schema.RequestSchema):
    """ DescribeUMemUpgradePrice - 获取UMem升级价格信息
    """

    fields = {
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUMemUpgradePriceResponseSchema(schema.ResponseSchema):
    """ DescribeUMemUpgradePrice - 获取UMem升级价格信息
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: DescribeUMemcacheGroup

显示Memcache
"""


class DescribeUMemcacheGroupRequestSchema(schema.RequestSchema):
    """ DescribeUMemcacheGroup - 显示Memcache
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """ DescribeUMemcacheGroup - 显示Memcache
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.UMemcacheGroupSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeURedisGroup

查询主备Redis
"""


class DescribeURedisGroupRequestSchema(schema.RequestSchema):
    """ DescribeURedisGroup - 查询主备Redis
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
    }


class DescribeURedisGroupResponseSchema(schema.ResponseSchema):
    """ DescribeURedisGroup - 查询主备Redis
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.URedisGroupSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeURedisUpgradePrice

获取uredis升级价格信息
"""


class DescribeURedisUpgradePriceRequestSchema(schema.RequestSchema):
    """ DescribeURedisUpgradePrice - 获取uredis升级价格信息
    """

    fields = {
        "Size": fields.Int(required=True, dump_to="Size"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeURedisUpgradePriceResponseSchema(schema.ResponseSchema):
    """ DescribeURedisUpgradePrice - 获取uredis升级价格信息
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: ModifyUMemSpaceName

修改UMem内存空间名称
"""


class ModifyUMemSpaceNameRequestSchema(schema.RequestSchema):
    """ ModifyUMemSpaceName - 修改UMem内存空间名称
    """

    fields = {
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ModifyUMemSpaceNameResponseSchema(schema.ResponseSchema):
    """ ModifyUMemSpaceName - 修改UMem内存空间名称
    """

    fields = {}


"""
API: ResizeUMemSpace

调整内存空间容量
"""


class ResizeUMemSpaceRequestSchema(schema.RequestSchema):
    """ ResizeUMemSpace - 调整内存空间容量
    """

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class ResizeUMemSpaceResponseSchema(schema.ResponseSchema):
    """ ResizeUMemSpace - 调整内存空间容量
    """

    fields = {}


"""
API: DeleteURedisGroup

删除主备redis
"""


class DeleteURedisGroupRequestSchema(schema.RequestSchema):
    """ DeleteURedisGroup - 删除主备redis
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
    }


class DeleteURedisGroupResponseSchema(schema.ResponseSchema):
    """ DeleteURedisGroup - 删除主备redis
    """

    fields = {}


"""
API: DescribeUMemSpace

获取UMem内存空间列表
"""


class DescribeUMemSpaceRequestSchema(schema.RequestSchema):
    """ DescribeUMemSpace - 获取UMem内存空间列表
    """

    fields = {
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "SpaceId": fields.Str(required=False, dump_to="SpaceId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUMemSpaceResponseSchema(schema.ResponseSchema):
    """ DescribeUMemSpace - 获取UMem内存空间列表
    """

    fields = {
        "DataSet": fields.List(
            models.UMemSpaceSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: ResizeURedisGroup

调整主备redis容量
"""


class ResizeURedisGroupRequestSchema(schema.RequestSchema):
    """ ResizeURedisGroup - 调整主备redis容量
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "CouponId": fields.Int(required=False, dump_to="CouponId"),
    }


class ResizeURedisGroupResponseSchema(schema.ResponseSchema):
    """ ResizeURedisGroup - 调整主备redis容量
    """

    fields = {}


"""
API: RestartUMemcacheGroup

重启单机Memcache
"""


class RestartUMemcacheGroupRequestSchema(schema.RequestSchema):
    """ RestartUMemcacheGroup - 重启单机Memcache
    """

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class RestartUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """ RestartUMemcacheGroup - 重启单机Memcache
    """

    fields = {}


"""
API: DescribeURedisBackupURL

获取主备Redis备份下载链接
"""


class DescribeURedisBackupURLRequestSchema(schema.RequestSchema):
    """ DescribeURedisBackupURL - 获取主备Redis备份下载链接
    """

    fields = {
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupId": fields.Str(required=True, dump_to="BackupId"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
    }


class DescribeURedisBackupURLResponseSchema(schema.ResponseSchema):
    """ DescribeURedisBackupURL - 获取主备Redis备份下载链接
    """

    fields = {
        "BackupURL": fields.Str(required=False, load_from="BackupURL"),
        "InnerBackupPath": fields.Str(required=False, load_from="InnerBackupPath"),
        "BackupPath": fields.Str(required=False, load_from="BackupPath"),
    }


"""
API: ResizeUDredisSpace

调整内存空间容量
"""


class ResizeUDredisSpaceRequestSchema(schema.RequestSchema):
    """ ResizeUDredisSpace - 调整内存空间容量
    """

    fields = {
        "Size": fields.Int(required=True, dump_to="Size"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
    }


class ResizeUDredisSpaceResponseSchema(schema.ResponseSchema):
    """ ResizeUDredisSpace - 调整内存空间容量
    """

    fields = {}


"""
API: DeleteUMemSpace

删除UMem内存空间
"""


class DeleteUMemSpaceRequestSchema(schema.RequestSchema):
    """ DeleteUMemSpace - 删除UMem内存空间
    """

    fields = {
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DeleteUMemSpaceResponseSchema(schema.ResponseSchema):
    """ DeleteUMemSpace - 删除UMem内存空间
    """

    fields = {}


"""
API: DescribeURedisBackup

查询主备redis备份
"""


class DescribeURedisBackupRequestSchema(schema.RequestSchema):
    """ DescribeURedisBackup - 查询主备redis备份
    """

    fields = {
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeURedisBackupResponseSchema(schema.ResponseSchema):
    """ DescribeURedisBackup - 查询主备redis备份
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.URedisBackupSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DeleteUMemcacheGroup

删除单机Memcache
"""


class DeleteUMemcacheGroupRequestSchema(schema.RequestSchema):
    """ DeleteUMemcacheGroup - 删除单机Memcache
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
    }


class DeleteUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """ DeleteUMemcacheGroup - 删除单机Memcache
    """

    fields = {}


"""
API: GetUMemSpaceState

获取UMem内存空间列表
"""


class GetUMemSpaceStateRequestSchema(schema.RequestSchema):
    """ GetUMemSpaceState - 获取UMem内存空间列表
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
    }


class GetUMemSpaceStateResponseSchema(schema.ResponseSchema):
    """ GetUMemSpaceState - 获取UMem内存空间列表
    """

    fields = {"State": fields.Str(required=False, load_from="State")}


"""
API: CreateUMemSpace

创建UMem内存空间
"""


class CreateUMemSpaceRequestSchema(schema.RequestSchema):
    """ CreateUMemSpace - 创建UMem内存空间
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Password": fields.Base64(required=False, dump_to="Password"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class CreateUMemSpaceResponseSchema(schema.ResponseSchema):
    """ CreateUMemSpace - 创建UMem内存空间
    """

    fields = {"SpaceId": fields.Str(required=False, load_from="SpaceId")}


"""
API: CreateUMemcacheGroup

创建单机Memcache
"""


class CreateUMemcacheGroupRequestSchema(schema.RequestSchema):
    """ CreateUMemcacheGroup - 创建单机Memcache
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=False, dump_to="Size"),
        "ConfigId": fields.Str(required=False, dump_to="ConfigId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Version": fields.Str(required=False, dump_to="Version"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class CreateUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """ CreateUMemcacheGroup - 创建单机Memcache
    """

    fields = {"GroupId": fields.Str(required=False, load_from="GroupId")}
