from ucloud.core.typesystem import schema, fields
from ucloud.services.udb.schemas import models


""" UDB API Schema
"""


"""
API: DescribeUDBInstanceUpgradePrice

获取UDB实例升降级价格信息
"""


class DescribeUDBInstanceUpgradePriceRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceUpgradePrice - 获取UDB实例升降级价格信息
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUDBInstanceUpgradePriceResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceUpgradePrice - 获取UDB实例升降级价格信息
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: DescribeUDBParamGroup

获取参数组详细参数信息
"""


class DescribeUDBParamGroupRequestSchema(schema.RequestSchema):
    """ DescribeUDBParamGroup - 获取参数组详细参数信息
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "GroupId": fields.Int(required=False, dump_to="GroupId"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "ClassType": fields.Str(required=False, dump_to="ClassType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "IsInUDBC": fields.Bool(required=False, dump_to="IsInUDBC"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
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
API: UpdateUDBParamGroup

更新UDB配置参数项
"""


class UpdateUDBParamGroupRequestSchema(schema.RequestSchema):
    """ UpdateUDBParamGroup - 更新UDB配置参数项
    """

    fields = {
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Description": fields.Str(required=False, dump_to="Description"),
        "Key": fields.Str(required=False, dump_to="Key"),
        "Value": fields.Str(required=False, dump_to="Value"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Int(required=True, dump_to="GroupId"),
    }


class UpdateUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ UpdateUDBParamGroup - 更新UDB配置参数项
    """

    fields = {}


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
API: BackupUDBInstanceErrorLog

备份UDB指定时间段的errorlog
"""


class BackupUDBInstanceErrorLogRequestSchema(schema.RequestSchema):
    """ BackupUDBInstanceErrorLog - 备份UDB指定时间段的errorlog
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
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
API: DeleteUDBLogPackage

删除UDB日志包
"""


class DeleteUDBLogPackageRequestSchema(schema.RequestSchema):
    """ DeleteUDBLogPackage - 删除UDB日志包
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DeleteUDBLogPackageResponseSchema(schema.ResponseSchema):
    """ DeleteUDBLogPackage - 删除UDB日志包
    """

    fields = {}


"""
API: DescribeUDBInstance

获取UDB实例信息，支持两类操作：（1）指定DBId用于获取该db的信息；（2）指定ClassType、Offset、Limit用于列表操作，查询某一个类型db。
"""


class DescribeUDBInstanceRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstance - 获取UDB实例信息，支持两类操作：（1）指定DBId用于获取该db的信息；（2）指定ClassType、Offset、Limit用于列表操作，查询某一个类型db。
    """

    fields = {
        "DBId": fields.Str(required=False, dump_to="DBId"),
        "IsInUDBC": fields.Bool(required=False, dump_to="IsInUDBC"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ClassType": fields.Str(required=True, dump_to="ClassType"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "IncludeSlaves": fields.Bool(required=False, dump_to="IncludeSlaves"),
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
API: DescribeUDBLogPackage

列表UDB实例binlog或slowlog或errorlog备份信息
"""


class DescribeUDBLogPackageRequestSchema(schema.RequestSchema):
    """ DescribeUDBLogPackage - 列表UDB实例binlog或slowlog或errorlog备份信息
    """

    fields = {
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "Types": fields.List(fields.Int()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "Type": fields.Int(required=False, dump_to="Type"),
        "DBId": fields.Str(required=False, dump_to="DBId"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
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
API: BackupUDBInstance

备份UDB实例
"""


class BackupUDBInstanceRequestSchema(schema.RequestSchema):
    """ BackupUDBInstance - 备份UDB实例
    """

    fields = {
        "BackupMethod": fields.Str(required=False, dump_to="BackupMethod"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "UseBlacklist": fields.Bool(required=False, dump_to="UseBlacklist"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
        "Blacklist": fields.Str(required=False, dump_to="Blacklist"),
        "ForceBackup": fields.Bool(required=False, dump_to="ForceBackup"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class BackupUDBInstanceResponseSchema(schema.ResponseSchema):
    """ BackupUDBInstance - 备份UDB实例
    """

    fields = {}


"""
API: CreateUDBReplicationInstance

创建MongoDB的副本节点（包括仲裁）
"""


class CreateUDBReplicationInstanceRequestSchema(schema.RequestSchema):
    """ CreateUDBReplicationInstance - 创建MongoDB的副本节点（包括仲裁）
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SrcId": fields.Str(required=True, dump_to="SrcId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "IsArbiter": fields.Bool(required=False, dump_to="IsArbiter"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
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
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "ParamGroupId": fields.Int(required=True, dump_to="ParamGroupId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "ConfigsvrId": fields.List(fields.Str()),
    }


class CreateUDBRouteInstanceResponseSchema(schema.ResponseSchema):
    """ CreateUDBRouteInstance - 创建mongos实例
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: DescribeUDBBackup

列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区
"""


class DescribeUDBBackupRequestSchema(schema.RequestSchema):
    """ DescribeUDBBackup - 列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区
    """

    fields = {
        "ClassType": fields.Str(required=False, dump_to="ClassType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Offset": fields.Int(required=True, dump_to="Offset"),
        "Limit": fields.Int(required=True, dump_to="Limit"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "BackupId": fields.Int(required=False, dump_to="BackupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=False, dump_to="DBId"),
        "BackupType": fields.Int(required=False, dump_to="BackupType"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
    }


class DescribeUDBBackupResponseSchema(schema.ResponseSchema):
    """ DescribeUDBBackup - 列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区
    """

    fields = {
        "DataSet": fields.List(
            models.UDBBackupSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUDBInstanceBinlog

获取UDB指定时间段的binlog列表
"""


class DescribeUDBInstanceBinlogRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceBinlog - 获取UDB指定时间段的binlog列表
    """

    fields = {
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
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
API: FetchUDBInstanceEarliestRecoverTime

获取UDB最早可回档的时间点
"""


class FetchUDBInstanceEarliestRecoverTimeRequestSchema(schema.RequestSchema):
    """ FetchUDBInstanceEarliestRecoverTime - 获取UDB最早可回档的时间点
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class FetchUDBInstanceEarliestRecoverTimeResponseSchema(schema.ResponseSchema):
    """ FetchUDBInstanceEarliestRecoverTime - 获取UDB最早可回档的时间点
    """

    fields = {"EarliestTime": fields.Int(required=False, load_from="EarliestTime")}


"""
API: RestartUDBInstance

重启UDB实例
"""


class RestartUDBInstanceRequestSchema(schema.RequestSchema):
    """ RestartUDBInstance - 重启UDB实例
    """

    fields = {
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class RestartUDBInstanceResponseSchema(schema.ResponseSchema):
    """ RestartUDBInstance - 重启UDB实例
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
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SrcDBId": fields.Str(required=True, dump_to="SrcDBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class CheckRecoverUDBInstanceResponseSchema(schema.ResponseSchema):
    """ CheckRecoverUDBInstance - 核查db是否可以使用回档功能
    """

    fields = {"LastestTime": fields.Int(required=False, load_from="LastestTime")}


"""
API: ResizeUDBInstance

修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高
"""


class ResizeUDBInstanceRequestSchema(schema.RequestSchema):
    """ ResizeUDBInstance - 修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高
    """

    fields = {
        "ProjectId": fields.Int(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "InstanceType": fields.Str(required=False, dump_to="InstanceType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "StartAfterUpgrade": fields.Bool(required=False, dump_to="StartAfterUpgrade"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ResizeUDBInstanceResponseSchema(schema.ResponseSchema):
    """ ResizeUDBInstance - 修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高
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
API: DescribeUDBBackupBlacklist

获取UDB实例的备份黑名单
"""


class DescribeUDBBackupBlacklistRequestSchema(schema.RequestSchema):
    """ DescribeUDBBackupBlacklist - 获取UDB实例的备份黑名单
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class DescribeUDBBackupBlacklistResponseSchema(schema.ResponseSchema):
    """ DescribeUDBBackupBlacklist - 获取UDB实例的备份黑名单
    """

    fields = {"Blacklist": fields.Str(required=False, load_from="Blacklist")}


"""
API: StartUDBInstance

启动UDB实例
"""


class StartUDBInstanceRequestSchema(schema.RequestSchema):
    """ StartUDBInstance - 启动UDB实例
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class StartUDBInstanceResponseSchema(schema.ResponseSchema):
    """ StartUDBInstance - 启动UDB实例
    """

    fields = {}


"""
API: UpdateUDBInstanceBackupStrategy

修改UDB自动备份策略
"""


class UpdateUDBInstanceBackupStrategyRequestSchema(schema.RequestSchema):
    """ UpdateUDBInstanceBackupStrategy - 修改UDB自动备份策略
    """

    fields = {
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupTime": fields.Int(required=False, dump_to="BackupTime"),
        "BackupDate": fields.Str(required=False, dump_to="BackupDate"),
        "ForceDump": fields.Bool(required=False, dump_to="ForceDump"),
        "BackupMethod": fields.Str(required=False, dump_to="BackupMethod"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
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
        "MasterDBId": fields.Str(required=True, dump_to="MasterDBId"),
        "BackupSwitch": fields.Int(required=True, dump_to="BackupSwitch"),
        "SlaveDBId": fields.Str(required=False, dump_to="SlaveDBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class UpdateUDBInstanceSlaveBackupSwitchResponseSchema(schema.ResponseSchema):
    """ UpdateUDBInstanceSlaveBackupSwitch - 开启或者关闭UDB从库备份
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Description": fields.Str(required=True, dump_to="Description"),
        "Content": fields.Str(required=True, dump_to="Content"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "GroupName": fields.Str(required=True, dump_to="GroupName"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "ParamGroupTypeId": fields.Int(required=False, dump_to="ParamGroupTypeId"),
    }


class UploadUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ UploadUDBParamGroup - 导入UDB配置
    """

    fields = {"GroupId": fields.Int(required=False, load_from="GroupId")}


"""
API: DeleteUDBInstance

删除UDB实例
"""


class DeleteUDBInstanceRequestSchema(schema.RequestSchema):
    """ DeleteUDBInstance - 删除UDB实例
    """

    fields = {
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class DeleteUDBInstanceResponseSchema(schema.ResponseSchema):
    """ DeleteUDBInstance - 删除UDB实例
    """

    fields = {}


"""
API: DescribeUDBInstanceBackupState

获取UDB实例备份状态
"""


class DescribeUDBInstanceBackupStateRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceBackupState - 获取UDB实例备份状态
    """

    fields = {
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
    }


class DescribeUDBInstanceBackupURLResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceBackupURL - 获取UDB备份下载地址
    """

    fields = {
        "BackupPath": fields.Str(required=False, load_from="BackupPath"),
        "InnerBackupPath": fields.Str(required=False, load_from="InnerBackupPath"),
    }


"""
API: DescribeUDBInstancePrice

获取UDB实例价格信息
"""


class DescribeUDBInstancePriceRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstancePrice - 获取UDB实例价格信息
    """

    fields = {
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "Count": fields.Int(required=False, dump_to="Count"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
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
API: DescribeUDBType

获取UDB支持的类型信息
"""


class DescribeUDBTypeRequestSchema(schema.RequestSchema):
    """ DescribeUDBType - 获取UDB支持的类型信息
    """

    fields = {
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "DBClusterType": fields.Str(required=False, dump_to="DBClusterType"),
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
API: ModifyUDBInstanceName

重命名UDB实例
"""


class ModifyUDBInstanceNameRequestSchema(schema.RequestSchema):
    """ ModifyUDBInstanceName - 重命名UDB实例
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Name": fields.Str(required=True, dump_to="Name"),
    }


class ModifyUDBInstanceNameResponseSchema(schema.ResponseSchema):
    """ ModifyUDBInstanceName - 重命名UDB实例
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class PromoteUDBInstanceToHAResponseSchema(schema.ResponseSchema):
    """ PromoteUDBInstanceToHA - 普通db升级为高可用(只针对mysql5.5及以上版本)
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
        "BackupName": fields.Str(required=False, dump_to="BackupName"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "BackupFile": fields.Str(required=True, dump_to="BackupFile"),
    }


class BackupUDBInstanceBinlogResponseSchema(schema.ResponseSchema):
    """ BackupUDBInstanceBinlog - 备份UDB指定时间段的binlog列表
    """

    fields = {}


"""
API: CreateUDBInstanceByRecovery

创建db，将新创建的db恢复到指定db某个指定时间点
"""


class CreateUDBInstanceByRecoveryRequestSchema(schema.RequestSchema):
    """ CreateUDBInstanceByRecovery - 创建db，将新创建的db恢复到指定db某个指定时间点
    """

    fields = {
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RecoveryTime": fields.Int(required=True, dump_to="RecoveryTime"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "SrcDBId": fields.Str(required=True, dump_to="SrcDBId"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
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
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupName": fields.Str(required=True, dump_to="GroupName"),
        "Description": fields.Str(required=True, dump_to="Description"),
        "SrcGroupId": fields.Int(required=True, dump_to="SrcGroupId"),
    }


class CreateUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ CreateUDBParamGroup - 从已有配置文件创建新配置文件
    """

    fields = {"GroupId": fields.Int(required=False, load_from="GroupId")}


"""
API: CreateUDBSlave

创建UDB实例的slave
"""


class CreateUDBSlaveRequestSchema(schema.RequestSchema):
    """ CreateUDBSlave - 创建UDB实例的slave
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "MemoryLimit": fields.Int(required=False, dump_to="MemoryLimit"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "SrcId": fields.Str(required=True, dump_to="SrcId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "InstanceType": fields.Str(required=False, dump_to="InstanceType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
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
API: DeleteUDBParamGroup

删除配置参数组
"""


class DeleteUDBParamGroupRequestSchema(schema.RequestSchema):
    """ DeleteUDBParamGroup - 删除配置参数组
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "GroupId": fields.Int(required=True, dump_to="GroupId"),
        "RegionFlag": fields.Bool(required=False, dump_to="RegionFlag"),
    }


class DeleteUDBParamGroupResponseSchema(schema.ResponseSchema):
    """ DeleteUDBParamGroup - 删除配置参数组
    """

    fields = {}


"""
API: DescribeUDBBinlogBackupURL

获取UDB的Binlog备份地址
"""


class DescribeUDBBinlogBackupURLRequestSchema(schema.RequestSchema):
    """ DescribeUDBBinlogBackupURL - 获取UDB的Binlog备份地址
    """

    fields = {
        "BackupId": fields.Int(required=True, dump_to="BackupId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
    }


class DescribeUDBBinlogBackupURLResponseSchema(schema.ResponseSchema):
    """ DescribeUDBBinlogBackupURL - 获取UDB的Binlog备份地址
    """

    fields = {
        "InnerBackupPath": fields.Str(required=False, load_from="InnerBackupPath"),
        "BackupPath": fields.Str(required=False, load_from="BackupPath"),
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
API: CreateUDBInstance

创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）
"""


class CreateUDBInstanceRequestSchema(schema.RequestSchema):
    """ CreateUDBInstance - 创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）
    """

    fields = {
        "InstanceType": fields.Str(required=False, dump_to="InstanceType"),
        "MemoryLimit": fields.Int(required=True, dump_to="MemoryLimit"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "AdminPassword": fields.Str(required=True, dump_to="AdminPassword"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "BackupTime": fields.Int(required=False, dump_to="BackupTime"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "DBTypeId": fields.Str(required=True, dump_to="DBTypeId"),
        "DisableSemisync": fields.Bool(required=False, dump_to="DisableSemisync"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "ParamGroupId": fields.Int(required=True, dump_to="ParamGroupId"),
        "BackupDuration": fields.Int(required=False, dump_to="BackupDuration"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "AdminUser": fields.Str(required=False, dump_to="AdminUser"),
        "UseSSD": fields.Bool(required=False, dump_to="UseSSD"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BackupCount": fields.Int(required=False, dump_to="BackupCount"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "ClusterRole": fields.Str(required=False, dump_to="ClusterRole"),
        "HAArch": fields.Str(required=False, dump_to="HAArch"),
        "BackupId": fields.Int(required=False, dump_to="BackupId"),
        "SSDType": fields.Str(required=False, dump_to="SSDType"),
        "UDBCId": fields.Str(required=False, dump_to="UDBCId"),
        "BackupZone": fields.Str(required=False, dump_to="BackupZone"),
    }


class CreateUDBInstanceResponseSchema(schema.ResponseSchema):
    """ CreateUDBInstance - 创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: DescribeUDBInstanceState

获取UDB实例状态
"""


class DescribeUDBInstanceStateRequestSchema(schema.RequestSchema):
    """ DescribeUDBInstanceState - 获取UDB实例状态
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeUDBInstanceStateResponseSchema(schema.ResponseSchema):
    """ DescribeUDBInstanceState - 获取UDB实例状态
    """

    fields = {"State": fields.Str(required=False, load_from="State")}


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
API: PromoteUDBSlave

从库提升为独立库
"""


class PromoteUDBSlaveRequestSchema(schema.RequestSchema):
    """ PromoteUDBSlave - 从库提升为独立库
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "IsForce": fields.Bool(required=False, dump_to="IsForce"),
    }


class PromoteUDBSlaveResponseSchema(schema.ResponseSchema):
    """ PromoteUDBSlave - 从库提升为独立库
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
        "Quantity": fields.Str(required=False, dump_to="Quantity"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
    }


class SwitchUDBInstanceToHAResponseSchema(schema.ResponseSchema):
    """ SwitchUDBInstanceToHA - 普通UDB切换为高可用，原db状态为WaitForSwitch时，调用该api
    """

    fields = {"DBId": fields.Str(required=False, load_from="DBId")}


"""
API: ClearUDBLog

清除UDB实例的log
"""


class ClearUDBLogRequestSchema(schema.RequestSchema):
    """ ClearUDBLog - 清除UDB实例的log
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "LogType": fields.Int(required=True, dump_to="LogType"),
        "BeforeTime": fields.Int(required=False, dump_to="BeforeTime"),
    }


class ClearUDBLogResponseSchema(schema.ResponseSchema):
    """ ClearUDBLog - 清除UDB实例的log
    """

    fields = {}
