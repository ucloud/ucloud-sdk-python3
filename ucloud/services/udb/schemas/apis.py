from ucloud.core.typesystem import schema, fields
from ucloud.services.udb.schemas import models


""" UDB API Schema
"""


"""
API: BackupUDBInstance

备份UDB实例
"""


class BackupUDBInstanceRequestSchema(schema.RequestSchema):
    """ BackupUDBInstance - 备份UDB实例
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
        "Blacklist": fields.Str(required=False, dump_to="Blacklist"),
        "ForceBackup": fields.Bool(required=False, dump_to="ForceBackup"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UseBlacklist": fields.Bool(required=False, dump_to="UseBlacklist"),
        "BackupMethod": fields.Str(required=False, dump_to="BackupMethod"),
    }


class BackupUDBInstanceResponseSchema(schema.ResponseSchema):
    """ BackupUDBInstance - 备份UDB实例
    """

    fields = {}


"""
API: BackupUDBInstanceBinlog

备份UDB指定时间段的binlog列表
"""


class BackupUDBInstanceBinlogRequestSchema(schema.RequestSchema):
    """ BackupUDBInstanceBinlog - 备份UDB指定时间段的binlog列表
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupFile": fields.Str(required=True, dump_to="BackupFile"),
        "BackupName": fields.Str(required=False, dump_to="BackupName"),
    }


class BackupUDBInstanceBinlogResponseSchema(schema.ResponseSchema):
    """ BackupUDBInstanceBinlog - 备份UDB指定时间段的binlog列表
    """

    fields = {}


"""
API: BackupUDBInstanceErrorLog

备份UDB指定时间段的errorlog
"""


class BackupUDBInstanceErrorLogRequestSchema(schema.RequestSchema):
    """ BackupUDBInstanceErrorLog - 备份UDB指定时间段的errorlog
    """

    fields = {
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class BackupUDBInstanceErrorLogResponseSchema(schema.ResponseSchema):
    """ BackupUDBInstanceErrorLog - 备份UDB指定时间段的errorlog
    """

    fields = {}


"""
API: BackupUDBInstanceSlowLog

备份UDB指定时间段的slowlog分析结果
"""


class BackupUDBInstanceSlowLogRequestSchema(schema.RequestSchema):
    """ BackupUDBInstanceSlowLog - 备份UDB指定时间段的slowlog分析结果
    """

    fields = {
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class BackupUDBInstanceSlowLogResponseSchema(schema.ResponseSchema):
    """ BackupUDBInstanceSlowLog - 备份UDB指定时间段的slowlog分析结果
    """

    fields = {}


"""
API: CheckRecoverUDBInstance

核查db是否可以使用回档功能
"""


class CheckRecoverUDBInstanceRequestSchema(schema.RequestSchema):
    """ CheckRecoverUDBInstance - 核查db是否可以使用回档功能
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SrcDBId": fields.Str(required=True, dump_to="SrcDBId"),
    }


class CheckRecoverUDBInstanceResponseSchema(schema.ResponseSchema):
    """ CheckRecoverUDBInstance - 核查db是否可以使用回档功能
    """

    fields = {"LastestTime": fields.Int(required=False, load_from="LastestTime")}


"""
API: CheckUDBInstanceToHAAllowance

核查db是否可以升级为高可用
"""


class CheckUDBInstanceToHAAllowanceRequestSchema(schema.RequestSchema):
    """ CheckUDBInstanceToHAAllowance - 核查db是否可以升级为高可用
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class CheckUDBInstanceToHAAllowanceResponseSchema(schema.ResponseSchema):
    """ CheckUDBInstanceToHAAllowance - 核查db是否可以升级为高可用
    """

    fields = {"Allowance": fields.Str(required=False, load_from="Allowance")}


"""
API: ClearUDBLog

清除UDB实例的log
"""


class ClearUDBLogRequestSchema(schema.RequestSchema):
    """ ClearUDBLog - 清除UDB实例的log
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "LogType": fields.Int(required=True, dump_to="LogType"),
        "BeforeTime": fields.Int(required=False, dump_to="BeforeTime"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class ClearUDBLogResponseSchema(schema.ResponseSchema):
    """ ClearUDBLog - 清除UDB实例的log
    """

    fields = {}


"""
API: CreateUDBInstance

创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）
"""


class CreateUDBInstanceRequestSchema(schema.RequestSchema):
    """ CreateUDBInstance - 创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）
    """

    fields = {
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ParamGroupId": fields.Int(required=True, dump_to="ParamGroupId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "DisableSemisync": fields.Bool(required=False, dump_to="DisableSemisync"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "BackupCount": fields.Int(required=False, dump_to="BackupCount"),
        "BackupTime": fields.Int(required=False, dump_to="BackupTime"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "ClusterRole": fields.Str(required=False, dump_to="ClusterRole"),
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "BackupDuration": fields.Int(required=False, dump_to="BackupDuration"),
        "InstanceType": fields.Str(required=False, dump_to="InstanceType"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "AdminPassword": fields.Str(required=True, dump_to="AdminPassword"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "BackupId": fields.Int(required=False, dump_to="BackupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "AdminUser": fields.Str(required=False, dump_to="AdminUser"),
        "HAArch": fields.Str(required=False, dump_to="HAArch"),
    }


class CreateUDBInstanceResponseSchema(schema.ResponseSchema):
    """ CreateUDBInstance - 创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: CreateUDBInstanceByRecovery

创建db，将新创建的db恢复到指定db某个指定时间点
"""


class CreateUDBInstanceByRecoveryRequestSchema(schema.RequestSchema):
    """ CreateUDBInstanceByRecovery - 创建db，将新创建的db恢复到指定db某个指定时间点
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "SrcDBId": fields.Str(required=True, dump_to="SrcDBId"),
        "RecoveryTime": fields.Int(required=True, dump_to="RecoveryTime"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
    }


class CreateUDBInstanceByRecoveryResponseSchema(schema.ResponseSchema):
    """ CreateUDBInstanceByRecovery - 创建db，将新创建的db恢复到指定db某个指定时间点
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: CreateUDBParamGroup

从已有配置文件创建新配置文件
"""


class CreateUDBParamGroupRequestSchema(schema.RequestSchema):
    """ CreateUDBParamGroup - 从已有配置文件创建新配置文件
    """

    fields = {
        "GroupName": fields.Str(required=True, dump_to="GroupName"),
        "Description": fields.Str(required=True, dump_to="Description"),
        "SrcGroupId": fields.Int(required=True, dump_to="SrcGroupId"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class CreateUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ CreateUDBParamGroup - 从已有配置文件创建新配置文件
    """

    fields = {"GroupId": fields.Int(required=False, load_from="GroupId")}


"""
API: CreateUDBReplicationInstance

创建MongoDB的副本节点（包括仲裁）
"""


class CreateUDBReplicationInstanceRequestSchema(schema.RequestSchema):
    """ CreateUDBReplicationInstance - 创建MongoDB的副本节点（包括仲裁）
    """

    fields = {
        "Port": fields.Int(required=False, dump_to="Port"),
        "IsArbiter": fields.Bool(required=False, dump_to="IsArbiter"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SrcId": fields.Str(required=True, dump_to="SrcId"),
    }


class CreateUDBReplicationInstanceResponseSchema(schema.ResponseSchema):
    """ CreateUDBReplicationInstance - 创建MongoDB的副本节点（包括仲裁）
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: CreateUDBRouteInstance

创建mongos实例
"""


class CreateUDBRouteInstanceRequestSchema(schema.RequestSchema):
    """ CreateUDBRouteInstance - 创建mongos实例
    """

    fields = {
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ConfigsvrId": fields.List(fields.Str()),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ParamGroupId": fields.Int(required=True, dump_to="ParamGroupId"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
    }


class CreateUDBRouteInstanceResponseSchema(schema.ResponseSchema):
    """ CreateUDBRouteInstance - 创建mongos实例
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: CreateUDBSlave

创建UDB实例的slave
"""


class CreateUDBSlaveRequestSchema(schema.RequestSchema):
    """ CreateUDBSlave - 创建UDB实例的slave
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "SrcId": fields.Str(required=True, dump_to="SrcId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "InstanceType": fields.Str(required=False, dump_to="InstanceType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "MemoryLimit": fields.Int(required=False, dump_to="MemoryLimit"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "IsLock": fields.Bool(required=False, dump_to="IsLock"),
    }


class CreateUDBSlaveResponseSchema(schema.ResponseSchema):
    """ CreateUDBSlave - 创建UDB实例的slave
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: DeleteUDBBackup

删除UDB实例备份
"""


class DeleteUDBBackupRequestSchema(schema.RequestSchema):
    """ DeleteUDBBackup - 删除UDB实例备份
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
    }


class DeleteUDBBackupResponseSchema(schema.ResponseSchema):
    """ DeleteUDBBackup - 删除UDB实例备份
    """

    fields = {}


"""
API: DeleteUDBInstance

删除UDB实例
"""


class DeleteUDBInstanceRequestSchema(schema.RequestSchema):
    """ DeleteUDBInstance - 删除UDB实例
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
    }


class DeleteUDBInstanceResponseSchema(schema.ResponseSchema):
    """ DeleteUDBInstance - 删除UDB实例
    """

    fields = {}


"""
API: DeleteUDBLogPackage

删除UDB日志包
"""


class DeleteUDBLogPackageRequestSchema(schema.RequestSchema):
    """ DeleteUDBLogPackage - 删除UDB日志包
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
    }


class DeleteUDBLogPackageResponseSchema(schema.ResponseSchema):
    """ DeleteUDBLogPackage - 删除UDB日志包
    """

    fields = {}


"""
API: DeleteUDBParamGroup

删除配置参数组
"""


class DeleteUDBParamGroupRequestSchema(schema.RequestSchema):
    """ DeleteUDBParamGroup - 删除配置参数组
    """

    fields = {
        "GroupId": fields.Int(required=True, dump_to="GroupId"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DeleteUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ DeleteUDBParamGroup - 删除配置参数组
    """

    fields = {}


"""
API: DescribeUDBBackup

列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区
"""


class DescribeUDBBackupRequestSchema(schema.RequestSchema):
    """ DescribeUDBBackup - 列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "ClassType": fields.Str(required=False, dump_to="ClassType"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "BackupId": fields.Int(required=False, dump_to="BackupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "DBId": fields.Str(required=False, dump_to="DBId"),
        "BackupType": fields.Int(required=False, dump_to="BackupType"),
    }


class DescribeUDBBackupResponseSchema(schema.ResponseSchema):
    """ DescribeUDBBackup - 列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.UDBBackupSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeUDBBackupBlacklist

获取UDB实例的备份黑名单
"""


class DescribeUDBBackupBlacklistRequestSchema(schema.RequestSchema):
    """ DescribeUDBBackupBlacklist - 获取UDB实例的备份黑名单
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeUDBBackupBlacklistResponseSchema(schema.ResponseSchema):
    """ DescribeUDBBackupBlacklist - 获取UDB实例的备份黑名单
    """

    fields = {"Blacklist": fields.Str(required=False, load_from="Blacklist")}


"""
API: DescribeUDBBinlogBackupURL

获取UDB的Binlog备份地址
"""


class DescribeUDBBinlogBackupURLRequestSchema(schema.RequestSchema):
    """ DescribeUDBBinlogBackupURL - 获取UDB的Binlog备份地址
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
    }


class DescribeUDBBinlogBackupURLResponseSchema(schema.ResponseSchema):
    """ DescribeUDBBinlogBackupURL - 获取UDB的Binlog备份地址
    """

    fields = {
        "BackupPath": fields.Str(required=False, load_from="BackupPath"),
        "InnerBackupPath": fields.Str(required=False, load_from="InnerBackupPath"),
    }


"""
API: DescribeUDBInstance

获取UDB实例信息，支持两类操作：（1）指定DBId用于获取该db的信息；（2）指定ClassType、Offset、Limit用于列表操作，查询某一个类型db。
"""


class DescribeUDBInstanceRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstance - 获取UDB实例信息，支持两类操作：（1）指定DBId用于获取该db的信息；（2）指定ClassType、Offset、Limit用于列表操作，查询某一个类型db。
    """

    fields = {
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "ClassType": fields.Str(required=True, dump_to="ClassType"),
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "DBId": fields.Str(required=False, dump_to="DBId"),
        "IsInUDBC": fields.Bool(required=False, dump_to="IsInUDBC"),
        "IncludeSlaves": fields.Bool(required=False, dump_to="IncludeSlaves"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUDBInstanceResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstance - 获取UDB实例信息，支持两类操作：（1）指定DBId用于获取该db的信息；（2）指定ClassType、Offset、Limit用于列表操作，查询某一个类型db。
    """

    fields = {
        "DataSet": fields.List(
            models.UDBInstanceSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUDBInstanceBackupState

获取UDB实例备份状态
"""


class DescribeUDBInstanceBackupStateRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceBackupState - 获取UDB实例备份状态
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUDBInstanceBackupStateResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceBackupState - 获取UDB实例备份状态
    """

    fields = {
        "State": fields.Str(required=False, load_from="State"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupEndTime": fields.Int(required=False, load_from="BackupEndTime"),
    }


"""
API: DescribeUDBInstanceBackupURL

获取UDB备份下载地址
"""


class DescribeUDBInstanceBackupURLRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceBackupURL - 获取UDB备份下载地址
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUDBInstanceBackupURLResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceBackupURL - 获取UDB备份下载地址
    """

    fields = {
        "BackupPath": fields.Str(required=False, load_from="BackupPath"),
        "InnerBackupPath": fields.Str(required=False, load_from="InnerBackupPath"),
    }


"""
API: DescribeUDBInstanceBinlog

获取UDB指定时间段的binlog列表
"""


class DescribeUDBInstanceBinlogRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceBinlog - 获取UDB指定时间段的binlog列表
    """

    fields = {
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUDBInstanceBinlogResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceBinlog - 获取UDB指定时间段的binlog列表
    """

    fields = {
        "DataSet": fields.List(
            models.UDBInstanceBinlogSetSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: DescribeUDBInstanceBinlogBackupState

获取udb实例备份状态
"""


class DescribeUDBInstanceBinlogBackupStateRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceBinlogBackupState - 获取udb实例备份状态
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
    }


class DescribeUDBInstanceBinlogBackupStateResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceBinlogBackupState - 获取udb实例备份状态
    """

    fields = {
        "State": fields.Str(required=False, load_from="State"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
    }


"""
API: DescribeUDBInstancePrice

获取UDB实例价格信息
"""


class DescribeUDBInstancePriceRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstancePrice - 获取UDB实例价格信息
    """

    fields = {
        "Count": fields.Int(required=False, dump_to="Count"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
    }


class DescribeUDBInstancePriceResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstancePrice - 获取UDB实例价格信息
    """

    fields = {
        "DataSet": fields.List(
            models.UDBInstancePriceSetSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: DescribeUDBInstanceState

获取UDB实例状态
"""


class DescribeUDBInstanceStateRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceState - 获取UDB实例状态
    """

    fields = {
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUDBInstanceStateResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceState - 获取UDB实例状态
    """

    fields = {"State": fields.Str(required=False, load_from="State")}


"""
API: DescribeUDBInstanceUpgradePrice

获取UDB实例升降级价格信息
"""


class DescribeUDBInstanceUpgradePriceRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceUpgradePrice - 获取UDB实例升降级价格信息
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeUDBInstanceUpgradePriceResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceUpgradePrice - 获取UDB实例升降级价格信息
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: DescribeUDBLogBackupURL

获取UDB的slowlog备份地址
"""


class DescribeUDBLogBackupURLRequestSchema(schema.RequestSchema):
    """ DescribeUDBLogBackupURL - 获取UDB的slowlog备份地址
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
    }


class DescribeUDBLogBackupURLResponseSchema(schema.ResponseSchema):
    """ DescribeUDBLogBackupURL - 获取UDB的slowlog备份地址
    """

    fields = {
        "BackupPath": fields.Str(required=False, load_from="BackupPath"),
        "UsernetPath": fields.Str(required=False, load_from="UsernetPath"),
    }


"""
API: DescribeUDBLogPackage

列表UDB实例binlog或slowlog或errorlog备份信息
"""


class DescribeUDBLogPackageRequestSchema(schema.RequestSchema):
    """ DescribeUDBLogPackage - 列表UDB实例binlog或slowlog或errorlog备份信息
    """

    fields = {
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "Type": fields.Int(required=False, dump_to="Type"),
        "DBId": fields.Str(required=False, dump_to="DBId"),
        "Types": fields.List(fields.Int()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
    }


class DescribeUDBLogPackageResponseSchema(schema.ResponseSchema):
    """ DescribeUDBLogPackage - 列表UDB实例binlog或slowlog或errorlog备份信息
    """

    fields = {
        "DataSet": fields.List(
            models.LogPackageDataSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUDBParamGroup

获取参数组详细参数信息
"""


class DescribeUDBParamGroupRequestSchema(schema.RequestSchema):
    """ DescribeUDBParamGroup - 获取参数组详细参数信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "IsInUDBC": fields.Bool(required=False, dump_to="IsInUDBC"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "ClassType": fields.Str(required=False, dump_to="ClassType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "GroupId": fields.Int(required=False, dump_to="GroupId"),
    }


class DescribeUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ DescribeUDBParamGroup - 获取参数组详细参数信息
    """

    fields = {
        "DataSet": fields.List(
            models.UDBParamGroupSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUDBType

获取UDB支持的类型信息
"""


class DescribeUDBTypeRequestSchema(schema.RequestSchema):
    """ DescribeUDBType - 获取UDB支持的类型信息
    """

    fields = {
        "DBClusterType": fields.Str(required=False, dump_to="DBClusterType"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUDBTypeResponseSchema(schema.ResponseSchema):
    """ DescribeUDBType - 获取UDB支持的类型信息
    """

    fields = {
        "DataSet": fields.List(
            models.UDBTypeSetSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: EditUDBBackupBlacklist

编辑UDB实例的备份黑名单
"""


class EditUDBBackupBlacklistRequestSchema(schema.RequestSchema):
    """ EditUDBBackupBlacklist - 编辑UDB实例的备份黑名单
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Blacklist": fields.Str(required=True, dump_to="Blacklist"),
    }


class EditUDBBackupBlacklistResponseSchema(schema.ResponseSchema):
    """ EditUDBBackupBlacklist - 编辑UDB实例的备份黑名单
    """

    fields = {}


"""
API: FetchUDBInstanceEarliestRecoverTime

获取UDB最早可回档的时间点
"""


class FetchUDBInstanceEarliestRecoverTimeRequestSchema(schema.RequestSchema):
    """ FetchUDBInstanceEarliestRecoverTime - 获取UDB最早可回档的时间点
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class FetchUDBInstanceEarliestRecoverTimeResponseSchema(schema.ResponseSchema):
    """ FetchUDBInstanceEarliestRecoverTime - 获取UDB最早可回档的时间点
    """

    fields = {"EarliestTime": fields.Int(required=False, load_from="EarliestTime")}


"""
API: ModifyUDBInstanceName

重命名UDB实例
"""


class ModifyUDBInstanceNameRequestSchema(schema.RequestSchema):
    """ ModifyUDBInstanceName - 重命名UDB实例
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ModifyUDBInstanceNameResponseSchema(schema.ResponseSchema):
    """ ModifyUDBInstanceName - 重命名UDB实例
    """

    fields = {}


"""
API: ModifyUDBInstancePassword

修改DB实例的管理员密码
"""


class ModifyUDBInstancePasswordRequestSchema(schema.RequestSchema):
    """ ModifyUDBInstancePassword - 修改DB实例的管理员密码
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "AccountName": fields.Str(required=False, dump_to="AccountName"),
    }


class ModifyUDBInstancePasswordResponseSchema(schema.ResponseSchema):
    """ ModifyUDBInstancePassword - 修改DB实例的管理员密码
    """

    fields = {}


"""
API: PromoteUDBInstanceToHA

普通db升级为高可用(只针对mysql5.5及以上版本)
"""


class PromoteUDBInstanceToHARequestSchema(schema.RequestSchema):
    """ PromoteUDBInstanceToHA - 普通db升级为高可用(只针对mysql5.5及以上版本)
    """

    fields = {
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class PromoteUDBInstanceToHAResponseSchema(schema.ResponseSchema):
    """ PromoteUDBInstanceToHA - 普通db升级为高可用(只针对mysql5.5及以上版本)
    """

    fields = {}


"""
API: PromoteUDBSlave

从库提升为独立库
"""


class PromoteUDBSlaveRequestSchema(schema.RequestSchema):
    """ PromoteUDBSlave - 从库提升为独立库
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "IsForce": fields.Bool(required=False, dump_to="IsForce"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class PromoteUDBSlaveResponseSchema(schema.ResponseSchema):
    """ PromoteUDBSlave - 从库提升为独立库
    """

    fields = {}


"""
API: ResizeUDBInstance

修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高
"""


class ResizeUDBInstanceRequestSchema(schema.RequestSchema):
    """ ResizeUDBInstance - 修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高
    """

    fields = {
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Int(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "StartAfterUpgrade": fields.Bool(required=False, dump_to="StartAfterUpgrade"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "InstanceType": fields.Str(required=False, dump_to="InstanceType"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
    }


class ResizeUDBInstanceResponseSchema(schema.ResponseSchema):
    """ ResizeUDBInstance - 修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高
    """

    fields = {}


"""
API: RestartUDBInstance

重启UDB实例
"""


class RestartUDBInstanceRequestSchema(schema.RequestSchema):
    """ RestartUDBInstance - 重启UDB实例
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class RestartUDBInstanceResponseSchema(schema.ResponseSchema):
    """ RestartUDBInstance - 重启UDB实例
    """

    fields = {}


"""
API: StartUDBInstance

启动UDB实例
"""


class StartUDBInstanceRequestSchema(schema.RequestSchema):
    """ StartUDBInstance - 启动UDB实例
    """

    fields = {
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class StartUDBInstanceResponseSchema(schema.ResponseSchema):
    """ StartUDBInstance - 启动UDB实例
    """

    fields = {}


"""
API: StopUDBInstance

关闭UDB实例
"""


class StopUDBInstanceRequestSchema(schema.RequestSchema):
    """ StopUDBInstance - 关闭UDB实例
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "ForceToKill": fields.Bool(required=False, dump_to="ForceToKill"),
    }


class StopUDBInstanceResponseSchema(schema.ResponseSchema):
    """ StopUDBInstance - 关闭UDB实例
    """

    fields = {}


"""
API: SwitchUDBInstanceToHA

普通UDB切换为高可用，原db状态为WaitForSwitch时，调用该api
"""


class SwitchUDBInstanceToHARequestSchema(schema.RequestSchema):
    """ SwitchUDBInstanceToHA - 普通UDB切换为高可用，原db状态为WaitForSwitch时，调用该api
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Str(required=False, dump_to="Quantity"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class SwitchUDBInstanceToHAResponseSchema(schema.ResponseSchema):
    """ SwitchUDBInstanceToHA - 普通UDB切换为高可用，原db状态为WaitForSwitch时，调用该api
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: UpdateUDBInstanceBackupStrategy

修改UDB自动备份策略
"""


class UpdateUDBInstanceBackupStrategyRequestSchema(schema.RequestSchema):
    """ UpdateUDBInstanceBackupStrategy - 修改UDB自动备份策略
    """

    fields = {
        "BackupMethod": fields.Str(required=False, dump_to="BackupMethod"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupTime": fields.Int(required=False, dump_to="BackupTime"),
        "BackupDate": fields.Str(required=False, dump_to="BackupDate"),
        "ForceDump": fields.Bool(required=False, dump_to="ForceDump"),
    }


class UpdateUDBInstanceBackupStrategyResponseSchema(schema.ResponseSchema):
    """ UpdateUDBInstanceBackupStrategy - 修改UDB自动备份策略
    """

    fields = {}


"""
API: UpdateUDBInstanceSlaveBackupSwitch

开启或者关闭UDB从库备份
"""


class UpdateUDBInstanceSlaveBackupSwitchRequestSchema(schema.RequestSchema):
    """ UpdateUDBInstanceSlaveBackupSwitch - 开启或者关闭UDB从库备份
    """

    fields = {
        "BackupSwitch": fields.Int(required=True, dump_to="BackupSwitch"),
        "SlaveDBId": fields.Str(required=False, dump_to="SlaveDBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "MasterDBId": fields.Str(required=True, dump_to="MasterDBId"),
    }


class UpdateUDBInstanceSlaveBackupSwitchResponseSchema(schema.ResponseSchema):
    """ UpdateUDBInstanceSlaveBackupSwitch - 开启或者关闭UDB从库备份
    """

    fields = {}


"""
API: UpdateUDBParamGroup

更新UDB配置参数项
"""


class UpdateUDBParamGroupRequestSchema(schema.RequestSchema):
    """ UpdateUDBParamGroup - 更新UDB配置参数项
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Int(required=True, dump_to="GroupId"),
        "Key": fields.Str(required=False, dump_to="Key"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Description": fields.Str(required=False, dump_to="Description"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Value": fields.Str(required=False, dump_to="Value"),
    }


class UpdateUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ UpdateUDBParamGroup - 更新UDB配置参数项
    """

    fields = {}


"""
API: UploadUDBParamGroup

导入UDB配置
"""


class UploadUDBParamGroupRequestSchema(schema.RequestSchema):
    """ UploadUDBParamGroup - 导入UDB配置
    """

    fields = {
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "Description": fields.Str(required=True, dump_to="Description"),
        "Content": fields.Str(required=True, dump_to="Content"),
        "ParamGroupTypeId": fields.Int(required=False, dump_to="ParamGroupTypeId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupName": fields.Str(required=True, dump_to="GroupName"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
    }


class UploadUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ UploadUDBParamGroup - 导入UDB配置
    """

    fields = {"GroupId": fields.Int(required=False, load_from="GroupId")}
