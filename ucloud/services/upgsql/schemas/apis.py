""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.upgsql.schemas import models

""" UPgSQL API Schema
"""


"""
API: BackupUPgSQLLog

备份日志包
"""


class BackupUPgSQLLogRequestSchema(schema.RequestSchema):
    """BackupUPgSQLLog - 备份日志包"""

    fields = {
        "BackupFile": fields.Str(required=True, dump_to="BackupFile"),
        "BackupName": fields.Str(required=True, dump_to="BackupName"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "LogType": fields.Str(required=False, dump_to="LogType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class BackupUPgSQLLogResponseSchema(schema.ResponseSchema):
    """BackupUPgSQLLog - 备份日志包"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: CreateUPgSQLInstance

创建PG云数据库
"""


class CreateUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """CreateUPgSQLInstance - 创建PG云数据库"""

    fields = {
        "AdminPassword": fields.Str(required=True, dump_to="AdminPassword"),
        "DBVersion": fields.Str(required=True, dump_to="DBVersion"),
        "DiskSpace": fields.Str(required=True, dump_to="DiskSpace"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "MachineType": fields.Str(required=True, dump_to="MachineType"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ParamGroupID": fields.Int(required=True, dump_to="ParamGroupID"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetID": fields.Str(required=True, dump_to="SubnetID"),
        "VPCID": fields.Str(required=True, dump_to="VPCID"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """CreateUPgSQLInstance - 创建PG云数据库"""

    fields = {
        "InstanceID": fields.Str(required=False, load_from="InstanceID"),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: CreateUPgSQLParamTemplate

创建PG参数模板
"""


class CreateUPgSQLParamTemplateRequestSchema(schema.RequestSchema):
    """CreateUPgSQLParamTemplate - 创建PG参数模板"""

    fields = {
        "DBVersion": fields.Str(required=True, dump_to="DBVersion"),
        "Description": fields.Str(required=False, dump_to="Description"),
        "GroupName": fields.Str(required=True, dump_to="GroupName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SrcGroupID": fields.Int(required=True, dump_to="SrcGroupID"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUPgSQLParamTemplateResponseSchema(schema.ResponseSchema):
    """CreateUPgSQLParamTemplate - 创建PG参数模板"""

    fields = {
        "GroupID": fields.Int(required=True, load_from="GroupID"),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: CreateUPgSQLReadonly

创建PG从库
"""


class CreateUPgSQLReadonlyRequestSchema(schema.RequestSchema):
    """CreateUPgSQLReadonly - 创建PG从库"""

    fields = {
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "MachineType": fields.Str(required=True, dump_to="MachineType"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SrcInstanceID": fields.Str(required=True, dump_to="SrcInstanceID"),
        "SubnetID": fields.Str(required=False, dump_to="SubnetID"),
        "VPCID": fields.Str(required=False, dump_to="VPCID"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUPgSQLReadonlyResponseSchema(schema.ResponseSchema):
    """CreateUPgSQLReadonly - 创建PG从库"""

    fields = {
        "InstanceID": fields.Str(required=False, load_from="InstanceID"),
    }


"""
API: DeleteUPgSQLInstance

删除PG实例
"""


class DeleteUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """DeleteUPgSQLInstance - 删除PG实例"""

    fields = {
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DeleteUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """DeleteUPgSQLInstance - 删除PG实例"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: DeleteUPgSQLParamTemplate

删除参数模板
"""


class DeleteUPgSQLParamTemplateRequestSchema(schema.RequestSchema):
    """DeleteUPgSQLParamTemplate - 删除参数模板"""

    fields = {
        "GroupID": fields.Int(required=True, dump_to="GroupID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DeleteUPgSQLParamTemplateResponseSchema(schema.ResponseSchema):
    """DeleteUPgSQLParamTemplate - 删除参数模板"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: DownloadUPgSQLParamTemplate

下载参数模板信息
"""


class DownloadUPgSQLParamTemplateRequestSchema(schema.RequestSchema):
    """DownloadUPgSQLParamTemplate - 下载参数模板信息"""

    fields = {
        "GroupID": fields.Int(required=True, dump_to="GroupID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DownloadUPgSQLParamTemplateResponseSchema(schema.ResponseSchema):
    """DownloadUPgSQLParamTemplate - 下载参数模板信息"""

    fields = {
        "Content": fields.Str(required=True, load_from="Content"),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: GetUPgSQLBackupStrategy

获取备份策略
"""


class GetUPgSQLBackupStrategyRequestSchema(schema.RequestSchema):
    """GetUPgSQLBackupStrategy - 获取备份策略"""

    fields = {
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class GetUPgSQLBackupStrategyResponseSchema(schema.ResponseSchema):
    """GetUPgSQLBackupStrategy - 获取备份策略"""

    fields = {
        "BackupMethod": fields.Str(required=True, load_from="BackupMethod"),
        "BackupTimeRange": fields.Str(
            required=True, load_from="BackupTimeRange"
        ),
        "BackupWeek": fields.Str(required=True, load_from="BackupWeek"),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: GetUPgSQLBackupURL

获取备份下载地址
"""


class GetUPgSQLBackupURLRequestSchema(schema.RequestSchema):
    """GetUPgSQLBackupURL - 获取备份下载地址"""

    fields = {
        "BackupID": fields.Str(required=True, dump_to="BackupID"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class GetUPgSQLBackupURLResponseSchema(schema.ResponseSchema):
    """GetUPgSQLBackupURL - 获取备份下载地址"""

    fields = {
        "BackupPath": fields.Str(required=True, load_from="BackupPath"),
        "InnerBackupPath": fields.Str(
            required=True, load_from="InnerBackupPath"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: GetUPgSQLInstance

获取PG云数据库实例描述
"""


class GetUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """GetUPgSQLInstance - 获取PG云数据库实例描述"""

    fields = {
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """GetUPgSQLInstance - 获取PG云数据库实例描述"""

    fields = {
        "DataSet": models.UDBInstanceSchema(),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: GetUPgSQLInstanceLog

可以查询DB的错误日志和满查询日志
"""


class GetUPgSQLInstanceLogRequestSchema(schema.RequestSchema):
    """GetUPgSQLInstanceLog - 可以查询DB的错误日志和满查询日志"""

    fields = {
        "AccountID": fields.Int(required=True, dump_to="AccountID"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "CompanyID": fields.Int(required=True, dump_to="CompanyID"),
        "DBId": fields.Str(required=True, dump_to="DBId"),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "LogType": fields.Str(required=True, dump_to="LogType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ZoneID": fields.Int(required=True, dump_to="ZoneID"),
    }


class GetUPgSQLInstanceLogResponseSchema(schema.ResponseSchema):
    """GetUPgSQLInstanceLog - 可以查询DB的错误日志和满查询日志"""

    fields = {
        "Log": fields.Str(required=True, load_from="Log"),
    }


"""
API: GetUPgSQLInstancePrice

获取创建PG云数据库价格
"""


class GetUPgSQLInstancePriceRequestSchema(schema.RequestSchema):
    """GetUPgSQLInstancePrice - 获取创建PG云数据库价格"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "InstanceMode": fields.Str(required=True, dump_to="InstanceMode"),
        "MachineType": fields.Str(required=True, dump_to="MachineType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class GetUPgSQLInstancePriceResponseSchema(schema.ResponseSchema):
    """GetUPgSQLInstancePrice - 获取创建PG云数据库价格"""

    fields = {
        "PriceSet": fields.List(
            models.UPgSQLInstancePriceSetSchema(),
            required=False,
            load_from="PriceSet",
        ),
    }


"""
API: GetUPgSQLParamTemplate

获取模板信息
"""


class GetUPgSQLParamTemplateRequestSchema(schema.RequestSchema):
    """GetUPgSQLParamTemplate - 获取模板信息"""

    fields = {
        "GroupID": fields.Int(required=True, dump_to="GroupID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class GetUPgSQLParamTemplateResponseSchema(schema.ResponseSchema):
    """GetUPgSQLParamTemplate - 获取模板信息"""

    fields = {
        "Data": fields.List(
            models.ParamSchema(), required=False, load_from="Data"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: GetUPgSQLUpgradePrice

 获取 PG 云数据库升降级价格
"""


class GetUPgSQLUpgradePriceRequestSchema(schema.RequestSchema):
    """GetUPgSQLUpgradePrice -  获取 PG 云数据库升降级价格"""

    fields = {
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "InstanceMode": fields.Str(required=False, dump_to="InstanceMode"),
        "MachineType": fields.Str(required=True, dump_to="MachineType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class GetUPgSQLUpgradePriceResponseSchema(schema.ResponseSchema):
    """GetUPgSQLUpgradePrice -  获取 PG 云数据库升降级价格"""

    fields = {
        "OriginalPrice": fields.Float(required=True, load_from="OriginalPrice"),
        "Price": fields.Float(required=True, load_from="Price"),
    }


"""
API: ListUPgSQLBackup

获取备份列表
"""


class ListUPgSQLBackupRequestSchema(schema.RequestSchema):
    """ListUPgSQLBackup - 获取备份列表"""

    fields = {
        "BackupType": fields.Int(required=False, dump_to="BackupType"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ListUPgSQLBackupResponseSchema(schema.ResponseSchema):
    """ListUPgSQLBackup - 获取备份列表"""

    fields = {
        "DataSet": fields.List(
            models.UPgSQLBackupSchema(), required=True, load_from="DataSet"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: ListUPgSQLInstance

获取PG云数据库列表
"""


class ListUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """ListUPgSQLInstance - 获取PG云数据库列表"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ListUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """ListUPgSQLInstance - 获取PG云数据库列表"""

    fields = {
        "DataSet": fields.List(
            models.UDBInstanceSetSchema(), required=True, load_from="DataSet"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: ListUPgSQLLog

获取数据库日志
"""


class ListUPgSQLLogRequestSchema(schema.RequestSchema):
    """ListUPgSQLLog - 获取数据库日志"""

    fields = {
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ListUPgSQLLogResponseSchema(schema.ResponseSchema):
    """ListUPgSQLLog - 获取数据库日志"""

    fields = {
        "DataSet": fields.List(
            models.LogSetSchema(), required=True, load_from="DataSet"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: ListUPgSQLMachineType

获取UPgSQL支持机器类型列表
"""


class ListUPgSQLMachineTypeRequestSchema(schema.RequestSchema):
    """ListUPgSQLMachineType - 获取UPgSQL支持机器类型列表"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ListUPgSQLMachineTypeResponseSchema(schema.ResponseSchema):
    """ListUPgSQLMachineType - 获取UPgSQL支持机器类型列表"""

    fields = {
        "DataSet": fields.List(
            models.PgSQLMachineTypeSchema(), required=True, load_from="DataSet"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: ListUPgSQLVersion

获取UPgSQL支持版本列表
"""


class ListUPgSQLVersionRequestSchema(schema.RequestSchema):
    """ListUPgSQLVersion - 获取UPgSQL支持版本列表"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ListUPgSQLVersionResponseSchema(schema.ResponseSchema):
    """ListUPgSQLVersion - 获取UPgSQL支持版本列表"""

    fields = {
        "DataSet": fields.List(
            models.PgSQLVersionSchema(), required=True, load_from="DataSet"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: RestartUPgSQLInstance

重启PG实例
"""


class RestartUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """RestartUPgSQLInstance - 重启PG实例"""

    fields = {
        "ForceToRestart": fields.Bool(required=False, dump_to="ForceToRestart"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RestartHost": fields.Bool(required=False, dump_to="RestartHost"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class RestartUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """RestartUPgSQLInstance - 重启PG实例"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: StartUPgSQLInstance

启动 PG实例
"""


class StartUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """StartUPgSQLInstance - 启动 PG实例"""

    fields = {
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class StartUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """StartUPgSQLInstance - 启动 PG实例"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: StopUPgSQLCreatingReadonly

停止创建从库
"""


class StopUPgSQLCreatingReadonlyRequestSchema(schema.RequestSchema):
    """StopUPgSQLCreatingReadonly - 停止创建从库"""

    fields = {
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class StopUPgSQLCreatingReadonlyResponseSchema(schema.ResponseSchema):
    """StopUPgSQLCreatingReadonly - 停止创建从库"""

    fields = {}


"""
API: StopUPgSQLInstance

关闭PG实例
"""


class StopUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """StopUPgSQLInstance - 关闭PG实例"""

    fields = {
        "ForceToStop": fields.Bool(required=False, dump_to="ForceToStop"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "StopHost": fields.Bool(required=False, dump_to="StopHost"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class StopUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """StopUPgSQLInstance - 关闭PG实例"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: UpdateUPgSQLAttribute

更新数据库属性
"""


class UpdateUPgSQLAttributeRequestSchema(schema.RequestSchema):
    """UpdateUPgSQLAttribute - 更新数据库属性"""

    fields = {
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UpdateUPgSQLAttributeResponseSchema(schema.ResponseSchema):
    """UpdateUPgSQLAttribute - 更新数据库属性"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: UpdateUPgSQLBackupStrategy

修改备份策略
"""


class UpdateUPgSQLBackupStrategyRequestSchema(schema.RequestSchema):
    """UpdateUPgSQLBackupStrategy - 修改备份策略"""

    fields = {
        "BackupMethod": fields.Str(required=False, dump_to="BackupMethod"),
        "BackupTimeRange": fields.Str(
            required=False, dump_to="BackupTimeRange"
        ),
        "BackupWeek": fields.Str(required=False, dump_to="BackupWeek"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UpdateUPgSQLBackupStrategyResponseSchema(schema.ResponseSchema):
    """UpdateUPgSQLBackupStrategy - 修改备份策略"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: UpdateUPgSQLPassword

更新数据库密码
"""


class UpdateUPgSQLPasswordRequestSchema(schema.RequestSchema):
    """UpdateUPgSQLPassword - 更新数据库密码"""

    fields = {
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UpdateUPgSQLPasswordResponseSchema(schema.ResponseSchema):
    """UpdateUPgSQLPassword - 更新数据库密码"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: UpgradeUPgSQLInstance

硬件规格升降级
"""


class UpgradeUPgSQLInstanceRequestSchema(schema.RequestSchema):
    """UpgradeUPgSQLInstance - 硬件规格升降级"""

    fields = {
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "InstanceID": fields.Str(required=True, dump_to="InstanceID"),
        "MachineType": fields.Str(required=True, dump_to="MachineType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UpgradeUPgSQLInstanceResponseSchema(schema.ResponseSchema):
    """UpgradeUPgSQLInstance - 硬件规格升降级"""

    fields = {
        "Message": fields.Str(required=False, load_from="Message"),
    }


"""
API: UploadUPgSQLParamTemplate

上传参数模板
"""


class UploadUPgSQLParamTemplateRequestSchema(schema.RequestSchema):
    """UploadUPgSQLParamTemplate - 上传参数模板"""

    fields = {
        "Content": fields.Str(required=True, dump_to="Content"),
        "DBVersion": fields.Str(required=True, dump_to="DBVersion"),
        "Description": fields.Str(required=False, dump_to="Description"),
        "GroupName": fields.Str(required=True, dump_to="GroupName"),
        "ParamGroupType": fields.Str(required=False, dump_to="ParamGroupType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UploadUPgSQLParamTemplateResponseSchema(schema.ResponseSchema):
    """UploadUPgSQLParamTemplate - 上传参数模板"""

    fields = {
        "GroupID": fields.Int(required=True, load_from="GroupID"),
        "Message": fields.Str(required=True, load_from="Message"),
    }
