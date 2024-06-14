""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.umem.schemas import models

""" UMem API Schema
"""


"""
API: CheckUDredisSpaceAllowance

检查高性能UMem剩余资源，以及分片扩容前的资源预检查
"""


class CheckUDredisSpaceAllowanceRequestSchema(schema.RequestSchema):
    """CheckUDredisSpaceAllowance - 检查高性能UMem剩余资源，以及分片扩容前的资源预检查"""

    fields = {
        "Count": fields.Str(required=True, dump_to="Count"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CheckUDredisSpaceAllowanceResponseSchema(schema.ResponseSchema):
    """CheckUDredisSpaceAllowance - 检查高性能UMem剩余资源，以及分片扩容前的资源预检查"""

    fields = {
        "Count": fields.Int(required=True, load_from="Count"),
    }


"""
API: CheckURedisAllowance

检查主备Redis的资源是否足够创建新实例，以及主备Redis的扩容资源预检查
"""


class CheckURedisAllowanceRequestSchema(schema.RequestSchema):
    """CheckURedisAllowance - 检查主备Redis的资源是否足够创建新实例，以及主备Redis的扩容资源预检查"""

    fields = {
        "Count": fields.Int(required=True, dump_to="Count"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CheckURedisAllowanceResponseSchema(schema.ResponseSchema):
    """CheckURedisAllowance - 检查主备Redis的资源是否足够创建新实例，以及主备Redis的扩容资源预检查"""

    fields = {
        "Count": fields.Int(required=True, load_from="Count"),
    }


"""
API: CreateUMemBackup

创建分布式redis备份
"""


class CreateUMemBackupRequestSchema(schema.RequestSchema):
    """CreateUMemBackup - 创建分布式redis备份"""

    fields = {
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUMemBackupResponseSchema(schema.ResponseSchema):
    """CreateUMemBackup - 创建分布式redis备份"""

    fields = {
        "BackupId": fields.Str(required=False, load_from="BackupId"),
    }


"""
API: CreateUMemSpace

创建UMem内存空间
"""


class CreateUMemSpaceRequestSchema(schema.RequestSchema):
    """CreateUMemSpace - 创建UMem内存空间"""

    fields = {
        "BlockCnt": fields.Int(required=False, dump_to="BlockCnt"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "ClusterMode": fields.Str(required=False, dump_to="ClusterMode"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "HighPerformance": fields.Bool(
            required=False, dump_to="HighPerformance"
        ),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Password": fields.Base64(required=False, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "ProxySize": fields.Int(required=False, dump_to="ProxySize"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Version": fields.Str(required=False, dump_to="Version"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUMemSpaceResponseSchema(schema.ResponseSchema):
    """CreateUMemSpace - 创建UMem内存空间"""

    fields = {
        "SpaceId": fields.Str(required=False, load_from="SpaceId"),
    }


"""
API: CreateUMemcacheGroup

创建单机Memcache
"""


class CreateUMemcacheGroupRequestSchema(schema.RequestSchema):
    """CreateUMemcacheGroup - 创建单机Memcache"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "ConfigId": fields.Str(required=False, dump_to="ConfigId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=False, dump_to="Size"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Version": fields.Str(required=False, dump_to="Version"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class CreateUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """CreateUMemcacheGroup - 创建单机Memcache"""

    fields = {
        "GroupId": fields.Str(required=False, load_from="GroupId"),
    }


"""
API: CreateURedisBackup

创建主备Redis备份
"""


class CreateURedisBackupRequestSchema(schema.RequestSchema):
    """CreateURedisBackup - 创建主备Redis备份"""

    fields = {
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class CreateURedisBackupResponseSchema(schema.ResponseSchema):
    """CreateURedisBackup - 创建主备Redis备份"""

    fields = {
        "BackupId": fields.Str(required=True, load_from="BackupId"),
    }


"""
API: CreateURedisGroup

创建主备redis
"""


class CreateURedisGroupRequestSchema(schema.RequestSchema):
    """CreateURedisGroup - 创建主备redis"""

    fields = {
        "AutoBackup": fields.Str(required=False, dump_to="AutoBackup"),
        "BackupId": fields.Str(required=False, dump_to="BackupId"),
        "BackupTime": fields.Int(required=False, dump_to="BackupTime"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "ConfigId": fields.Str(required=False, dump_to="ConfigId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "EnableIpV6": fields.Bool(required=False, dump_to="EnableIpV6"),
        "HighAvailability": fields.Str(
            required=True, dump_to="HighAvailability"
        ),
        "HighPerformance": fields.Bool(
            required=False, dump_to="HighPerformance"
        ),
        "MasterGroupId": fields.Str(required=False, dump_to="MasterGroupId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Password": fields.Base64(required=False, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=False, dump_to="Size"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Version": fields.Str(required=False, dump_to="Version"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateURedisGroupResponseSchema(schema.ResponseSchema):
    """CreateURedisGroup - 创建主备redis"""

    fields = {
        "GroupId": fields.Str(required=False, load_from="GroupId"),
    }


"""
API: DeleteUMemSpace

删除UMem内存空间
"""


class DeleteUMemSpaceRequestSchema(schema.RequestSchema):
    """DeleteUMemSpace - 删除UMem内存空间"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DeleteUMemSpaceResponseSchema(schema.ResponseSchema):
    """DeleteUMemSpace - 删除UMem内存空间"""

    fields = {}


"""
API: DeleteUMemcacheGroup

删除单机Memcache
"""


class DeleteUMemcacheGroupRequestSchema(schema.RequestSchema):
    """DeleteUMemcacheGroup - 删除单机Memcache"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DeleteUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """DeleteUMemcacheGroup - 删除单机Memcache"""

    fields = {}


"""
API: DeleteURedisGroup

删除主备redis
"""


class DeleteURedisGroupRequestSchema(schema.RequestSchema):
    """DeleteURedisGroup - 删除主备redis"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DeleteURedisGroupResponseSchema(schema.ResponseSchema):
    """DeleteURedisGroup - 删除主备redis"""

    fields = {}


"""
API: DescribeUDRedisProxyInfo

拉取udredis所有的代理信息
"""


class DescribeUDRedisProxyInfoRequestSchema(schema.RequestSchema):
    """DescribeUDRedisProxyInfo - 拉取udredis所有的代理信息"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUDRedisProxyInfoResponseSchema(schema.ResponseSchema):
    """DescribeUDRedisProxyInfo - 拉取udredis所有的代理信息"""

    fields = {
        "DataSet": fields.List(
            models.UDRedisProxyInfoSchema(), required=True, load_from="DataSet"
        ),
    }


"""
API: DescribeUDRedisSlowlog

查询UDRedis慢日志
"""


class DescribeUDRedisSlowlogRequestSchema(schema.RequestSchema):
    """DescribeUDRedisSlowlog - 查询UDRedis慢日志"""

    fields = {
        "InstanceId": fields.Str(required=True, dump_to="InstanceId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ProxyId": fields.Str(required=False, dump_to="ProxyId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUDRedisSlowlogResponseSchema(schema.ResponseSchema):
    """DescribeUDRedisSlowlog - 查询UDRedis慢日志"""

    fields = {
        "DataSet": fields.List(
            models.UDRedisSlowlogSetSchema(), required=True, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeUMem

获取UMem列表
"""


class DescribeUMemRequestSchema(schema.RequestSchema):
    """DescribeUMem - 获取UMem列表"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=True, dump_to="Protocol"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceId": fields.Str(required=False, dump_to="ResourceId"),
        "ResourceType": fields.Str(required=False, dump_to="ResourceType"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUMemResponseSchema(schema.ResponseSchema):
    """DescribeUMem - 获取UMem列表"""

    fields = {
        "DataSet": fields.List(
            models.UMemDataSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUMemBackup

查询分布式redis备份
"""


class DescribeUMemBackupRequestSchema(schema.RequestSchema):
    """DescribeUMemBackup - 查询分布式redis备份"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUMemBackupResponseSchema(schema.ResponseSchema):
    """DescribeUMemBackup - 查询分布式redis备份"""

    fields = {
        "DataSet": fields.List(
            models.UMemBackupSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeUMemBackupURL

获取分布式redis 备份下载链接
"""


class DescribeUMemBackupURLRequestSchema(schema.RequestSchema):
    """DescribeUMemBackupURL - 获取分布式redis 备份下载链接"""

    fields = {
        "BackupId": fields.Str(required=True, dump_to="BackupId"),
        "BlockId": fields.Str(required=False, dump_to="BlockId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUMemBackupURLResponseSchema(schema.ResponseSchema):
    """DescribeUMemBackupURL - 获取分布式redis 备份下载链接"""

    fields = {
        "BackupURL": fields.List(
            fields.Str(), required=True, load_from="BackupURL"
        ),
    }


"""
API: DescribeUMemBlockInfo

拉取UDRedis分片信息
"""


class DescribeUMemBlockInfoRequestSchema(schema.RequestSchema):
    """DescribeUMemBlockInfo - 拉取UDRedis分片信息"""

    fields = {
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUMemBlockInfoResponseSchema(schema.ResponseSchema):
    """DescribeUMemBlockInfo - 拉取UDRedis分片信息"""

    fields = {
        "DataSet": fields.List(
            models.UMemBlockInfoSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeUMemPrice

获取UMem实例价格信息
"""


class DescribeUMemPriceRequestSchema(schema.RequestSchema):
    """DescribeUMemPrice - 获取UMem实例价格信息"""

    fields = {
        "BlockCnt": fields.Int(required=False, dump_to="BlockCnt"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "HighPerformance": fields.Bool(
            required=False, dump_to="HighPerformance"
        ),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ProxySize": fields.Int(required=False, dump_to="ProxySize"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUMemPriceResponseSchema(schema.ResponseSchema):
    """DescribeUMemPrice - 获取UMem实例价格信息"""

    fields = {
        "DataSet": fields.List(
            models.UMemPriceSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeUMemSpace

获取UMem内存空间列表
"""


class DescribeUMemSpaceRequestSchema(schema.RequestSchema):
    """DescribeUMemSpace - 获取UMem内存空间列表"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=False, dump_to="SpaceId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUMemSpaceResponseSchema(schema.ResponseSchema):
    """DescribeUMemSpace - 获取UMem内存空间列表"""

    fields = {
        "DataSet": fields.List(
            models.UMemSpaceSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUMemUpgradePrice

获取UMem升级价格信息
"""


class DescribeUMemUpgradePriceRequestSchema(schema.RequestSchema):
    """DescribeUMemUpgradePrice - 获取UMem升级价格信息"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUMemUpgradePriceResponseSchema(schema.ResponseSchema):
    """DescribeUMemUpgradePrice - 获取UMem升级价格信息"""

    fields = {
        "DataSet": models.PriceDataSetSchema(
            required=False, load_from="DataSet"
        ),  # Deprecated, will be removed at 1.0
        "OriginalPrice": fields.Int(required=False, load_from="OriginalPrice"),
        "Price": fields.Int(required=False, load_from="Price"),
    }


"""
API: DescribeUMemcacheGroup

显示Memcache
"""


class DescribeUMemcacheGroupRequestSchema(schema.RequestSchema):
    """DescribeUMemcacheGroup - 显示Memcache"""

    fields = {
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """DescribeUMemcacheGroup - 显示Memcache"""

    fields = {
        "DataSet": fields.List(
            models.UMemcacheGroupSetSchema(),
            required=False,
            load_from="DataSet",
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUMemcachePrice

获取umemcache组价格信息
"""


class DescribeUMemcachePriceRequestSchema(schema.RequestSchema):
    """DescribeUMemcachePrice - 获取umemcache组价格信息"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUMemcachePriceResponseSchema(schema.ResponseSchema):
    """DescribeUMemcachePrice - 获取umemcache组价格信息"""

    fields = {
        "DataSet": fields.List(
            models.UMemcachePriceSetSchema(),
            required=False,
            load_from="DataSet",
        ),
    }


"""
API: DescribeUMemcacheUpgradePrice

获取umemcache升级价格信息
"""


class DescribeUMemcacheUpgradePriceRequestSchema(schema.RequestSchema):
    """DescribeUMemcacheUpgradePrice - 获取umemcache升级价格信息"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Size": fields.Int(required=True, dump_to="Size"),
    }


class DescribeUMemcacheUpgradePriceResponseSchema(schema.ResponseSchema):
    """DescribeUMemcacheUpgradePrice - 获取umemcache升级价格信息"""

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
    }


"""
API: DescribeURedisBackup

查询主备redis备份
"""


class DescribeURedisBackupRequestSchema(schema.RequestSchema):
    """DescribeURedisBackup - 查询主备redis备份"""

    fields = {
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeURedisBackupResponseSchema(schema.ResponseSchema):
    """DescribeURedisBackup - 查询主备redis备份"""

    fields = {
        "DataSet": fields.List(
            models.URedisBackupSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeURedisBackupURL

获取主备Redis备份下载链接
"""


class DescribeURedisBackupURLRequestSchema(schema.RequestSchema):
    """DescribeURedisBackupURL - 获取主备Redis备份下载链接"""

    fields = {
        "BackupId": fields.Str(required=True, dump_to="BackupId"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeURedisBackupURLResponseSchema(schema.ResponseSchema):
    """DescribeURedisBackupURL - 获取主备Redis备份下载链接"""

    fields = {
        "BackupPath": fields.Str(required=False, load_from="BackupPath"),
        "BackupURL": fields.Str(required=False, load_from="BackupURL"),
    }


"""
API: DescribeURedisConfig

查询主备Redis所有配置文件
"""


class DescribeURedisConfigRequestSchema(schema.RequestSchema):
    """DescribeURedisConfig - 查询主备Redis所有配置文件"""

    fields = {
        "ConfigId": fields.Str(required=False, dump_to="ConfigId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RegionFlag": fields.Bool(required=True, dump_to="RegionFlag"),
        "Version": fields.Str(required=False, dump_to="Version"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeURedisConfigResponseSchema(schema.ResponseSchema):
    """DescribeURedisConfig - 查询主备Redis所有配置文件"""

    fields = {
        "DataSet": fields.List(
            models.URedisConfigSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeURedisGroup

查询主备Redis
"""


class DescribeURedisGroupRequestSchema(schema.RequestSchema):
    """DescribeURedisGroup - 查询主备Redis"""

    fields = {
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeURedisGroupResponseSchema(schema.ResponseSchema):
    """DescribeURedisGroup - 查询主备Redis"""

    fields = {
        "DataSet": fields.List(
            models.URedisGroupSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeURedisPrice

获取URedis价格信息
"""


class DescribeURedisPriceRequestSchema(schema.RequestSchema):
    """DescribeURedisPrice - 获取URedis价格信息"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "HighPerformance": fields.Bool(
            required=False, dump_to="HighPerformance"
        ),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeURedisPriceResponseSchema(schema.ResponseSchema):
    """DescribeURedisPrice - 获取URedis价格信息"""

    fields = {
        "DataSet": fields.List(
            models.URedisPriceSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeURedisSlowlog

查询URedis慢日志
"""


class DescribeURedisSlowlogRequestSchema(schema.RequestSchema):
    """DescribeURedisSlowlog - 查询URedis慢日志"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeURedisSlowlogResponseSchema(schema.ResponseSchema):
    """DescribeURedisSlowlog - 查询URedis慢日志"""

    fields = {
        "DataSet": fields.List(
            models.URedisSlowlogSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeURedisUpgradePrice

获取uredis升级价格信息
"""


class DescribeURedisUpgradePriceRequestSchema(schema.RequestSchema):
    """DescribeURedisUpgradePrice - 获取uredis升级价格信息"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeURedisUpgradePriceResponseSchema(schema.ResponseSchema):
    """DescribeURedisUpgradePrice - 获取uredis升级价格信息"""

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
    }


"""
API: DescribeURedisVersion

获取主Redis可用版本
"""


class DescribeURedisVersionRequestSchema(schema.RequestSchema):
    """DescribeURedisVersion - 获取主Redis可用版本"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeURedisVersionResponseSchema(schema.ResponseSchema):
    """DescribeURedisVersion - 获取主Redis可用版本"""

    fields = {
        "DataSet": fields.List(
            models.URedisVersionSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: FlushallURedisGroup

清除主备redis数据
"""


class FlushallURedisGroupRequestSchema(schema.RequestSchema):
    """FlushallURedisGroup - 清除主备redis数据"""

    fields = {
        "DbNum": fields.Int(required=False, dump_to="DbNum"),
        "FlushType": fields.Str(required=True, dump_to="FlushType"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "OrganizationId": fields.Int(required=False, dump_to="OrganizationId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "TopOrganizationId": fields.Int(
            required=False, dump_to="TopOrganizationId"
        ),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class FlushallURedisGroupResponseSchema(schema.ResponseSchema):
    """FlushallURedisGroup - 清除主备redis数据"""

    fields = {}


"""
API: GetUMemSpaceState

获取UMem内存空间列表
"""


class GetUMemSpaceStateRequestSchema(schema.RequestSchema):
    """GetUMemSpaceState - 获取UMem内存空间列表"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetUMemSpaceStateResponseSchema(schema.ResponseSchema):
    """GetUMemSpaceState - 获取UMem内存空间列表"""

    fields = {
        "State": fields.Str(required=False, load_from="State"),
    }


"""
API: ISolationURedisGroup

打开/关闭URedis
"""


class ISolationURedisGroupRequestSchema(schema.RequestSchema):
    """ISolationURedisGroup - 打开/关闭URedis"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "TransformType": fields.Str(required=True, dump_to="TransformType"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ISolationURedisGroupResponseSchema(schema.ResponseSchema):
    """ISolationURedisGroup - 打开/关闭URedis"""

    fields = {}


"""
API: ModifyUMemSpaceName

修改UMem内存空间名称
"""


class ModifyUMemSpaceNameRequestSchema(schema.RequestSchema):
    """ModifyUMemSpaceName - 修改UMem内存空间名称"""

    fields = {
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ModifyUMemSpaceNameResponseSchema(schema.ResponseSchema):
    """ModifyUMemSpaceName - 修改UMem内存空间名称"""

    fields = {}


"""
API: ModifyURedisConfig

修改主备Redis配置文件参数
"""


class ModifyURedisConfigRequestSchema(schema.RequestSchema):
    """ModifyURedisConfig - 修改主备Redis配置文件参数"""

    fields = {
        "ConfigId": fields.Str(required=True, dump_to="ConfigId"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Key": fields.Str(required=True, dump_to="Key"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Value": fields.Str(required=True, dump_to="Value"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ModifyURedisConfigResponseSchema(schema.ResponseSchema):
    """ModifyURedisConfig - 修改主备Redis配置文件参数"""

    fields = {}


"""
API: ModifyURedisGroupName

修改主备redis名称
"""


class ModifyURedisGroupNameRequestSchema(schema.RequestSchema):
    """ModifyURedisGroupName - 修改主备redis名称"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class ModifyURedisGroupNameResponseSchema(schema.ResponseSchema):
    """ModifyURedisGroupName - 修改主备redis名称"""

    fields = {}


"""
API: ModifyURedisGroupPassword

修改主备密码/重置密码
"""


class ModifyURedisGroupPasswordRequestSchema(schema.RequestSchema):
    """ModifyURedisGroupPassword - 修改主备密码/重置密码"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceType": fields.Str(required=False, dump_to="ResourceType"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ModifyURedisGroupPasswordResponseSchema(schema.ResponseSchema):
    """ModifyURedisGroupPassword - 修改主备密码/重置密码"""

    fields = {}


"""
API: RemoveUDRedisData

清除udredis实例数据
"""


class RemoveUDRedisDataRequestSchema(schema.RequestSchema):
    """RemoveUDRedisData - 清除udredis实例数据"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class RemoveUDRedisDataResponseSchema(schema.ResponseSchema):
    """RemoveUDRedisData - 清除udredis实例数据"""

    fields = {}


"""
API: ResizeUMemSpace

调整内存空间容量，只支持存量老分布式产品，不支持高性能分布式
"""


class ResizeUMemSpaceRequestSchema(schema.RequestSchema):
    """ResizeUMemSpace - 调整内存空间容量，只支持存量老分布式产品，不支持高性能分布式"""

    fields = {
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SpaceId": fields.Str(required=True, dump_to="SpaceId"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ResizeUMemSpaceResponseSchema(schema.ResponseSchema):
    """ResizeUMemSpace - 调整内存空间容量，只支持存量老分布式产品，不支持高性能分布式"""

    fields = {}


"""
API: ResizeURedisGroup

通过调用CheckURedisAllowance接口，检查资源情况，根据不同情形来调整主备redis容量，其中主要包括可用区资源不足无法扩容，主备所在宿主机资源不足需要迁移完成扩容（需要主从切换，会闪断及负载升高），以及直接扩容（业务无感知）
"""


class ResizeURedisGroupRequestSchema(schema.RequestSchema):
    """ResizeURedisGroup - 通过调用CheckURedisAllowance接口，检查资源情况，根据不同情形来调整主备redis容量，其中主要包括可用区资源不足无法扩容，主备所在宿主机资源不足需要迁移完成扩容（需要主从切换，会闪断及负载升高），以及直接扩容（业务无感知）"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Int(required=False, dump_to="CouponId"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ResizeURedisGroupResponseSchema(schema.ResponseSchema):
    """ResizeURedisGroup - 通过调用CheckURedisAllowance接口，检查资源情况，根据不同情形来调整主备redis容量，其中主要包括可用区资源不足无法扩容，主备所在宿主机资源不足需要迁移完成扩容（需要主从切换，会闪断及负载升高），以及直接扩容（业务无感知）"""

    fields = {}


"""
API: RestartUMemcacheGroup

重启单机Memcache
"""


class RestartUMemcacheGroupRequestSchema(schema.RequestSchema):
    """RestartUMemcacheGroup - 重启单机Memcache"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class RestartUMemcacheGroupResponseSchema(schema.ResponseSchema):
    """RestartUMemcacheGroup - 重启单机Memcache"""

    fields = {}


"""
API: RestartURedisGroup

重启主备实例
"""


class RestartURedisGroupRequestSchema(schema.RequestSchema):
    """RestartURedisGroup - 重启主备实例"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class RestartURedisGroupResponseSchema(schema.ResponseSchema):
    """RestartURedisGroup - 重启主备实例"""

    fields = {}


"""
API: ShutdownURedisGroup

关闭主备实例
"""


class ShutdownURedisGroupRequestSchema(schema.RequestSchema):
    """ShutdownURedisGroup - 关闭主备实例"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class ShutdownURedisGroupResponseSchema(schema.ResponseSchema):
    """ShutdownURedisGroup - 关闭主备实例"""

    fields = {}


"""
API: StartURedisGroup

实例关闭状态下，启动实例
"""


class StartURedisGroupRequestSchema(schema.RequestSchema):
    """StartURedisGroup - 实例关闭状态下，启动实例"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class StartURedisGroupResponseSchema(schema.ResponseSchema):
    """StartURedisGroup - 实例关闭状态下，启动实例"""

    fields = {}


"""
API: UpdateURedisBackupStrategy

URedisBackupStrategy
"""


class UpdateURedisBackupStrategyRequestSchema(schema.RequestSchema):
    """UpdateURedisBackupStrategy - URedisBackupStrategy"""

    fields = {
        "AutoBackup": fields.Str(required=False, dump_to="AutoBackup"),
        "BackupTime": fields.Str(required=True, dump_to="BackupTime"),
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class UpdateURedisBackupStrategyResponseSchema(schema.ResponseSchema):
    """UpdateURedisBackupStrategy - URedisBackupStrategy"""

    fields = {}


"""
API: UpdateURedisRewriteTime

修改主备redis重写时间
"""


class UpdateURedisRewriteTimeRequestSchema(schema.RequestSchema):
    """UpdateURedisRewriteTime - 修改主备redis重写时间"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RewriteTime": fields.Int(required=True, dump_to="RewriteTime"),
        "SlaveZone": fields.Str(required=False, dump_to="SlaveZone"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UpdateURedisRewriteTimeResponseSchema(schema.ResponseSchema):
    """UpdateURedisRewriteTime - 修改主备redis重写时间"""

    fields = {}
