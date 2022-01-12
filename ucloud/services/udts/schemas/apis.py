""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.udts.schemas import models

""" UDTS API Schema
"""


"""
API: CheckUDTSTask

对UDTS 任务提供预检查功能
"""


class CheckUDTSTaskParamSourceMySQLNodeQueryDataSchema(schema.RequestSchema):
    """CheckUDTSTaskParamSourceMySQLNodeQueryData -"""

    fields = {
        "DBName": fields.Str(required=False, dump_to="DBName"),
        "NewDBName": fields.Str(required=False, dump_to="NewDBName"),
    }


class CheckUDTSTaskParamSourceMySQLNodeSchema(schema.RequestSchema):
    """CheckUDTSTaskParamSourceMySQLNode -"""

    fields = {
        "DataRegion": fields.Str(required=False, dump_to="DataRegion"),
        "Database": fields.Str(required=False, dump_to="Database"),
        "Host": fields.Str(required=False, dump_to="Host"),
        "Password": fields.Str(required=False, dump_to="Password"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "QueryData": fields.List(
            CheckUDTSTaskParamSourceMySQLNodeQueryDataSchema()
        ),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "SyncData": CheckUDTSTaskParamSourceMySQLNodeSyncDataSchema(
            required=False, dump_to="SyncData"
        ),
        "Table": fields.Str(required=False, dump_to="Table"),
        "User": fields.Str(required=False, dump_to="User"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class CheckUDTSTaskParamSourceMySQLNodeSyncDataSchema(schema.RequestSchema):
    """CheckUDTSTaskParamSourceMySQLNodeSyncData -"""

    fields = {
        "BinlogGTID": fields.Str(required=False, dump_to="BinlogGTID"),
        "BinlogName": fields.Str(required=False, dump_to="BinlogName"),
        "BinlogPos": fields.Int(required=False, dump_to="BinlogPos"),
        "ServerID": fields.Int(required=False, dump_to="ServerID"),
    }


class CheckUDTSTaskParamSourceSchema(schema.RequestSchema):
    """CheckUDTSTaskParamSource -"""

    fields = {
        "DataType": fields.Str(required=False, dump_to="DataType"),
        "Mode": fields.Str(required=False, dump_to="Mode"),
        "MySQLNode": CheckUDTSTaskParamSourceMySQLNodeSchema(
            required=False, dump_to="MySQLNode"
        ),
        "NWType": fields.Str(required=False, dump_to="NWType"),
        "ServiceType": fields.Str(required=True, dump_to="ServiceType"),
    }


class CheckUDTSTaskParamTargetMySQLNodeSchema(schema.RequestSchema):
    """CheckUDTSTaskParamTargetMySQLNode -"""

    fields = {
        "DataRegion": fields.Str(required=False, dump_to="DataRegion"),
        "Host": fields.Str(required=False, dump_to="Host"),
        "Password": fields.Str(required=False, dump_to="Password"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "User": fields.Str(required=False, dump_to="User"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class CheckUDTSTaskParamTargetSchema(schema.RequestSchema):
    """CheckUDTSTaskParamTarget -"""

    fields = {
        "DataType": fields.Str(required=False, dump_to="DataType"),
        "MySQLNode": CheckUDTSTaskParamTargetMySQLNodeSchema(
            required=False, dump_to="MySQLNode"
        ),
        "NWType": fields.Str(required=False, dump_to="NWType"),
    }


class CheckUDTSTaskRequestSchema(schema.RequestSchema):
    """CheckUDTSTask - 对UDTS 任务提供预检查功能"""

    fields = {
        "MaxRetryCount": fields.Str(required=True, dump_to="MaxRetryCount"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Query": fields.Str(required=False, dump_to="Query"),
        "Source": fields.List(CheckUDTSTaskParamSourceSchema()),
        "Target": CheckUDTSTaskParamTargetSchema(
            required=False, dump_to="Target"
        ),
        "Type": fields.Str(required=True, dump_to="Type"),
    }


class CheckUDTSTaskResponseSchema(schema.ResponseSchema):
    """CheckUDTSTask - 对UDTS 任务提供预检查功能"""

    fields = {
        "Action": fields.Str(required=True, load_from="Action"),
        "Data": models.CheckUDTSTaskResultSchema(),
        "Message": fields.Str(required=True, load_from="Message"),
        "RetCode": fields.Str(required=True, load_from="RetCode"),
    }


"""
API: CreateUDTSTask

创建UDTS任务
"""


class CreateUDTSTaskParamSourceMySQLNodeQueryDataSchema(schema.RequestSchema):
    """CreateUDTSTaskParamSourceMySQLNodeQueryData -"""

    fields = {
        "DBName": fields.Str(required=False, dump_to="DBName"),
        "NewDBName": fields.Str(required=False, dump_to="NewDBName"),
        "TableData": CreateUDTSTaskParamSourceMySQLNodeQueryDataTableDataSchema(
            required=False, dump_to="TableData"
        ),
        "TableMaps": fields.List(
            CreateUDTSTaskParamSourceMySQLNodeQueryDataTableMapsSchema()
        ),
    }


class CreateUDTSTaskParamSourceMySQLNodeQueryDataTableDataSchema(
    schema.RequestSchema
):
    """CreateUDTSTaskParamSourceMySQLNodeQueryDataTableData -"""

    fields = {
        "ExcludeTables": fields.Bool(required=False, dump_to="ExcludeTables"),
        "TableNames": fields.Str(required=False, dump_to="TableNames"),
    }


class CreateUDTSTaskParamSourceMySQLNodeQueryDataTableMapsSchema(
    schema.RequestSchema
):
    """CreateUDTSTaskParamSourceMySQLNodeQueryDataTableMaps -"""

    fields = {
        "NewTableName": fields.Str(required=False, dump_to="NewTableName"),
        "TableName": fields.Str(required=False, dump_to="TableName"),
    }


class CreateUDTSTaskParamSourceMySQLNodeSchema(schema.RequestSchema):
    """CreateUDTSTaskParamSourceMySQLNode -"""

    fields = {
        "DataRegion": fields.Str(required=False, dump_to="DataRegion"),
        "Database": fields.Str(required=False, dump_to="Database"),
        "DupAction": fields.Str(required=False, dump_to="DupAction"),
        "Host": fields.Str(required=False, dump_to="Host"),
        "KeepExistData": fields.Bool(required=False, dump_to="KeepExistData"),
        "Password": fields.Str(required=False, dump_to="Password"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "QueryData": fields.List(
            CreateUDTSTaskParamSourceMySQLNodeQueryDataSchema()
        ),
        "SSLSecurity": CreateUDTSTaskParamSourceMySQLNodeSSLSecuritySchema(
            required=False, dump_to="SSLSecurity"
        ),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "SyncData": CreateUDTSTaskParamSourceMySQLNodeSyncDataSchema(
            required=False, dump_to="SyncData"
        ),
        "Table": fields.Str(required=False, dump_to="Table"),
        "User": fields.Str(required=False, dump_to="User"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class CreateUDTSTaskParamSourceMySQLNodeSyncDataSchema(schema.RequestSchema):
    """CreateUDTSTaskParamSourceMySQLNodeSyncData -"""

    fields = {
        "BinlogGTID": fields.Str(required=False, dump_to="BinlogGTID"),
        "BinlogName": fields.Str(required=False, dump_to="BinlogName"),
        "BinlogPos": fields.Int(required=False, dump_to="BinlogPos"),
        "ServerID": fields.Int(required=False, dump_to="ServerID"),
    }


class CreateUDTSTaskParamSourceSchema(schema.RequestSchema):
    """CreateUDTSTaskParamSource -"""

    fields = {
        "BandwidthLimit": fields.Int(required=False, dump_to="BandwidthLimit"),
        "DataType": fields.Str(required=True, dump_to="DataType"),
        "Mode": fields.Str(required=True, dump_to="Mode"),
        "MySQLNode": CreateUDTSTaskParamSourceMySQLNodeSchema(
            required=False, dump_to="MySQLNode"
        ),
        "NWType": fields.Str(required=True, dump_to="NWType"),
        "ServiceType": fields.Str(required=True, dump_to="ServiceType"),
    }


class CreateUDTSTaskParamTargetMySQLNodeSchema(schema.RequestSchema):
    """CreateUDTSTaskParamTargetMySQLNode -"""

    fields = {
        "DataRegion": fields.Str(required=False, dump_to="DataRegion"),
        "Host": fields.Str(required=False, dump_to="Host"),
        "NoBinlog": fields.Bool(required=False, dump_to="NoBinlog"),
        "Password": fields.Str(required=False, dump_to="Password"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "User": fields.Str(required=False, dump_to="User"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class CreateUDTSTaskParamTargetSchema(schema.RequestSchema):
    """CreateUDTSTaskParamTarget -"""

    fields = {
        "BandwidthLimit": fields.Str(required=False, dump_to="BandwidthLimit"),
        "DataType": fields.Str(required=True, dump_to="DataType"),
        "Mode": fields.Str(required=True, dump_to="Mode"),
        "MySQLNode": CreateUDTSTaskParamTargetMySQLNodeSchema(
            required=False, dump_to="MySQLNode"
        ),
        "NWType": fields.Str(required=True, dump_to="NWType"),
    }


class CreateUDTSTaskParamSourceMySQLNodeSSLSecuritySchema(schema.RequestSchema):
    """CreateUDTSTaskParamSourceMySQLNodeSSLSecurity -"""

    fields = {
        "SSLCA": fields.Str(required=False, dump_to="SSLCA"),
        "SSLCert": fields.Str(required=False, dump_to="SSLCert"),
        "SSLKey": fields.Str(required=False, dump_to="SSLKey"),
    }


class CreateUDTSTaskRequestSchema(schema.RequestSchema):
    """CreateUDTSTask - 创建UDTS任务"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "IsUnidirection": fields.Str(required=False, dump_to="IsUnidirection"),
        "MaxRetryCount": fields.Str(required=False, dump_to="MaxRetryCount"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Query": fields.Str(required=False, dump_to="Query"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Source": fields.List(CreateUDTSTaskParamSourceSchema()),
        "Target": CreateUDTSTaskParamTargetSchema(
            required=False, dump_to="Target"
        ),
        "Type": fields.Str(required=True, dump_to="Type"),
    }


class CreateUDTSTaskResponseSchema(schema.ResponseSchema):
    """CreateUDTSTask - 创建UDTS任务"""

    fields = {
        "Data": fields.Str(),
        "Message": fields.Str(required=True, load_from="Message"),
        "TaskId": fields.Str(required=False, load_from="TaskId"),
    }


"""
API: GetUDTSTaskHistory

获取任务历史状态
"""


class GetUDTSTaskHistoryRequestSchema(schema.RequestSchema):
    """GetUDTSTaskHistory - 获取任务历史状态"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "TaskId": fields.Str(required=True, dump_to="TaskId"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class GetUDTSTaskHistoryResponseSchema(schema.ResponseSchema):
    """GetUDTSTaskHistory - 获取任务历史状态"""

    fields = {
        "Data": fields.List(
            models.TaskHistoryItemSchema(), required=True, load_from="Data"
        ),
    }


"""
API: GetUDTSTaskStatus

查看服务状态
"""


class GetUDTSTaskStatusRequestSchema(schema.RequestSchema):
    """GetUDTSTaskStatus - 查看服务状态"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "TaskId": fields.Str(required=True, dump_to="TaskId"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class GetUDTSTaskStatusResponseSchema(schema.ResponseSchema):
    """GetUDTSTaskStatus - 查看服务状态"""

    fields = {
        "Data": models.StatusDataSchema(),
        "Message": fields.Str(required=False, load_from="Message"),
    }


"""
API: ListUDTSTask

获取用户创建的 Task 信息
"""


class ListUDTSTaskRequestSchema(schema.RequestSchema):
    """ListUDTSTask - 获取用户创建的 Task 信息"""

    fields = {
        "Limit": fields.Str(required=False, dump_to="Limit"),
        "Offset": fields.Str(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class ListUDTSTaskResponseSchema(schema.ResponseSchema):
    """ListUDTSTask - 获取用户创建的 Task 信息"""

    fields = {
        "Data": fields.List(
            models.ListDataItemSchema(), required=True, load_from="Data"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: StartUDTSTask

启动UDTS服务
"""


class StartUDTSTaskRequestSchema(schema.RequestSchema):
    """StartUDTSTask - 启动UDTS服务"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "TaskId": fields.Str(required=True, dump_to="TaskId"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class StartUDTSTaskResponseSchema(schema.ResponseSchema):
    """StartUDTSTask - 启动UDTS服务"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: StopUDTSTask

停止UDTS任务
"""


class StopUDTSTaskRequestSchema(schema.RequestSchema):
    """StopUDTSTask - 停止UDTS任务"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "TaskId": fields.Str(required=True, dump_to="TaskId"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class StopUDTSTaskResponseSchema(schema.ResponseSchema):
    """StopUDTSTask - 停止UDTS任务"""

    fields = {
        "Message": fields.Str(required=False, load_from="Message"),
    }
