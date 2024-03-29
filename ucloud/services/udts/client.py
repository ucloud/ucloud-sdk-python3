""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.udts.schemas import apis


class UDTSClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UDTSClient, self).__init__(config, transport, middleware, logger)

    def check_udts_task(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CheckUDTSTask - 对UDTS 任务提供预检查功能

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **MaxRetryCount** (str) - (Required) 重试次数，最大为 5。 默认为0
        - **Name** (str) - (Required) task 名称，长度不能超过 128
        - **Type** (str) - (Required) 任务类型，值为 transfer 或 integration， transfer 时任务为 数据迁移，integration 时任务为 数据集成。
        - **Query** (str) - 废弃
        - **Source** (list) - 见 **CheckUDTSTaskParamSource** 模型定义
        - **Target** (dict) - 见 **CheckUDTSTaskParamTarget** 模型定义

        **Response**

        - **Action** (str) - 操作名称
        - **Data** (dict) - 见 **CheckUDTSTaskResult** 模型定义
        - **Message** (str) - 返回消息
        - **RetCode** (str) - 返回码

        **Request Model**

        **CheckUDTSTaskParamSourceMySQLNodeSyncData**
        - **BinlogGTID** (str) - 增量时需要指定的 binlog gtid，可以通过 show master status 获取，或者全量+增量任务会自动设置
        - **BinlogName** (str) - 增量时需要指定的 binlog name，可以通过 show master status 获取，或者全量+增量任务会自动设置
        - **BinlogPos** (int) - 增量时需要指定的 binlog pos，可以通过 show master status 获取，或者全量+增量任务会自动设置
        - **ServerID** (int) - 增量时需要指定的 serverID，不能和现有的 slave 重复，预检查时会检查该值


        **CheckUDTSTaskParamSourceMySQLNodeQueryData**
        - **DBName** (str) - 数据集成时需要迁移的 DB 名
        - **NewDBName** (str) - 数据集成时迁移后的 DB 名


        **CheckUDTSTaskParamTargetMySQLNode**
        - **DataRegion** (str) - 目标数据库地域，比如 cn-bj2
        - **Host** (str) - 目标数据库地址， 比如 10.9.37.212
        - **Password** (str) - 目标数据库密码
        - **Port** (int) - 目标数据库端口，比如 3306
        - **SubnetId** (str) - 目标数据库子网 ID ,比如 subnet-zl44fktq
        - **User** (str) - 目标数据库用户名，比如 root
        - **VPCId** (str) - 目标数据库 VPC,比如 uvnet-1wz5rqte


        **CheckUDTSTaskParamSourceMySQLNode**
        - **DataRegion** (str) - 数据库地域，比如 cn-bj2
        - **Database** (str) - 需要迁移的 DB 名称
        - **Host** (str) - 源数据库地址， 比如 10.9.37.200
        - **Password** (str) - 源 MySQL 密码
        - **Port** (int) - 源 MySQL 端口，如 3306
        - **QueryData** (list) - 见 **CheckUDTSTaskParamSourceMySQLNodeQueryData** 模型定义
        - **SubnetId** (str) - 子网 ID
        - **SyncData** (dict) - 见 **CheckUDTSTaskParamSourceMySQLNodeSyncData** 模型定义
        - **Table** (str) - 需要迁移的 table 名
        - **User** (str) - 源 MySQL 用户名，如 root
        - **VPCId** (str) - VPC


        **CheckUDTSTaskParamTarget**
        - **DataType** (str) - 目标数据库类型，比如 mysql
        - **MySQLNode** (dict) - 见 **CheckUDTSTaskParamTargetMySQLNode** 模型定义
        - **NWType** (str) - 目标 db 网络类型，目前进支持 user


        **CheckUDTSTaskParamSource**
        - **DataType** (str) - 数据库类型
        - **Mode** (str) - // 任务类型，值可以是 full, incremental, full+incremental, bidirectional
        - **MySQLNode** (dict) - 见 **CheckUDTSTaskParamSourceMySQLNode** 模型定义
        - **NWType** (str) - 源网络类型，可以是 public,user,dedicated_line


        **Response Model**

        **CheckResultItem**
        - **ErrMessage** (str) -
        - **State** (str) - 状态


        **CheckResult**
        - **Config** (dict) - 见 **CheckResultItem** 模型定义
        - **Connection** (dict) - 见 **CheckResultItem** 模型定义
        - **Privileges** (dict) - 见 **CheckResultItem** 模型定义


        **CheckUDTSTaskResult**
        - **Source** (dict) - 见 **CheckResult** 模型定义
        - **Target** (dict) - 见 **CheckResult** 模型定义


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CheckUDTSTaskRequestSchema().dumps(d)

        resp = self.invoke("CheckUDTSTask", d, **kwargs)
        return apis.CheckUDTSTaskResponseSchema().loads(resp)

    def create_udts_task(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUDTSTask - 创建UDTS任务

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Name** (str) - (Required) task 名称，长度不能超过 128
        - **Type** (str) - (Required) 任务类型，transfer(数据传输) 或 integration(数据集成)
        - **IsUnidirection** (str) - 暂时未使用该字段
        - **MaxRetryCount** (str) - 重试次数，最大为 5。 默认为0
        - **Query** (str) - 暂时未使用该字段
        - **Remark** (str) - 备注信息，长度不能大于 255
        - **Source** (list) - 见 **CreateUDTSTaskParamSource** 模型定义
        - **Target** (dict) - 见 **CreateUDTSTaskParamTarget** 模型定义

        **Response**

        - **Data** (dict) -
        - **Message** (str) - 返回消息

        **Request Model**

        **CreateUDTSTaskParamSourceMySQLNodeQueryDataTableData**
        - **ExcludeTables** (bool) - 暂时未使用该字段
        - **TableNames** (str) - 暂时未使用该字段


        **CreateUDTSTaskParamSourceMySQLNodeQueryDataTableMaps**
        - **NewTableName** (str) - 数据集成时迁移后的 Table 名
        - **TableName** (str) - 数据集成时需要迁移的 Table 名


        **CreateUDTSTaskParamSourceMySQLNodeSyncData**
        - **BinlogGTID** (str) - 增量时需要指定的 binlog gtid，可以通过 show master status 获取，或者全量+增量任务会自动设置
        - **BinlogName** (str) - 增量时需要指定的 binlog name，可以通过 show master status 获取，或者全量+增量任务会自动设置
        - **BinlogPos** (int) - 增量时需要指定的 binlog pos，可以通过 show master status 获取，或者全量+增量任务会自动设置
        - **ServerID** (int) - 增量时需要指定的 serverID，不能和现有的 slave 重复，预检查时会检查该值


        **CreateUDTSTaskParamSourceMySQLNodeQueryData**
        - **DBName** (str) - 数据集成时需要迁移的 DB 名
        - **NewDBName** (str) - 数据集成时迁移后的 DB 名
        - **TableData** (dict) - 见 **CreateUDTSTaskParamSourceMySQLNodeQueryDataTableData** 模型定义
        - **TableMaps** (list) - 见 **CreateUDTSTaskParamSourceMySQLNodeQueryDataTableMaps** 模型定义


        **CreateUDTSTaskParamSourceMySQLNode**
        - **DataRegion** (str) - 数据库地域，比如 cn-bj2
        - **Database** (str) - 需要迁移的 DB 名称
        - **DupAction** (str) - 重复数据处理规则，数据集成时该参数才有效，值为 ignore或者replace
        - **Host** (str) - 源数据库地址
        - **KeepExistData** (bool) - 是否保留原有数据，只有数据集成时该参数才有效
        - **Password** (str) - 源数据库密码
        - **Port** (int) - 源数据库端口
        - **QueryData** (list) - 见 **CreateUDTSTaskParamSourceMySQLNodeQueryData** 模型定义
        - **SubnetId** (str) - 源数据库子网 ID，当网络类型为 user 时需要填写
        - **SyncData** (dict) - 见 **CreateUDTSTaskParamSourceMySQLNodeSyncData** 模型定义
        - **Table** (str) - 需要迁移的 table 名
        - **User** (str) - 源数据库用户名
        - **VPCId** (str) - 源数据库 VPC ID，当网络类型为 user 时需要填写


        **CreateUDTSTaskParamTargetMySQLNode**
        - **DataRegion** (str) - 目标数据库地域，比如 cn-bj2
        - **Host** (str) - 目标数据库地址， 比如 10.9.37.212
        - **NoBinlog** (bool) - 是否在全量过程中，临时禁用目标 MySQL 产生 binlog，在目标磁盘空间不足，或者需要获取更快的迁移速度时可以使用，该参数会破坏目标 MySQL 的高可用
        - **Password** (str) - 目标数据库密码
        - **Port** (int) - 目标数据库端口，比如 3306
        - **SubnetId** (str) - 目标数据库子网 ID ,比如 subnet-zl44fktq
        - **User** (str) - 目标数据库用户名，比如 root
        - **VPCId** (str) - 目标数据库 VPC,比如 uvnet-1wz5rqte


        **CreateUDTSTaskParamSource**
        - **BandwidthLimit** (int) - 源端限速值，单位为  MB/s
        - **DataType** (str) - 数据库类型，比如 mysql
        - **Mode** (str) - 任务类型，值可以是 full, incremental, full+incremental, bidirectional
        - **MySQLNode** (dict) - 见 **CreateUDTSTaskParamSourceMySQLNode** 模型定义
        - **NWType** (str) - 源网络类型，可以是 public,user,dedicated_line


        **CreateUDTSTaskParamTarget**
        - **BandwidthLimit** (str) - 目标端限速，单位为 MB/s
        - **DataType** (str) - 目标数据库类型，比如 mysql
        - **Mode** (str) -
        - **MySQLNode** (dict) - 见 **CreateUDTSTaskParamTargetMySQLNode** 模型定义
        - **NWType** (str) - 目标 db 网络类型，目前仅支持 user


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CreateUDTSTaskRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDTSTask", d, **kwargs)
        return apis.CreateUDTSTaskResponseSchema().loads(resp)

    def get_udts_task_history(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUDTSTaskHistory - 获取任务历史状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **TaskId** (str) - (Required) 任务短 id
        - **Type** (str) - 任务类型

        **Response**

        - **Data** (list) - 见 **TaskHistoryItem** 模型定义

        **Response Model**

        **TaskHistoryItem**
        - **AntID** (str) - 任务 ID
        - **AntState** (str) - 任务状态
        - **CreateTime** (int) - 事件时间，值为 timestamp
        - **CreateTimeH** (str) - 事件时间，为可读的日期时间


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.GetUDTSTaskHistoryRequestSchema().dumps(d)

        resp = self.invoke("GetUDTSTaskHistory", d, **kwargs)
        return apis.GetUDTSTaskHistoryResponseSchema().loads(resp)

    def get_udts_task_status(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUDTSTaskStatus - 查看服务状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **TaskId** (str) - (Required) 任务ID
        - **Type** (str) - 任务类型，值为 transfer 或 integration， transfer 时任务为 数据迁移，integration 时任务为 数据集成。

        **Response**

        - **Data** (dict) - 见 **StatusData** 模型定义
        - **Message** (str) - 返回信息

        **Response Model**

        **SyncData**
        - **BinlogGTID** (str) - GTID
        - **BinlogName** (str) - Binlog 文件名， 长度不超过128字符
        - **BinlogPos** (int) - Binlog Pos
        - **ServerId** (int) - 分配给UDTS task的server ID, 必须在MySQL集群中唯一


        **Progress**
        - **CurCount** (int) - 已迁移条目数
        - **CurDuration** (int) - 已耗时间（单位秒）
        - **Percentage** (float) - 完成进度
        - **TotalCount** (int) - 总条目数
        - **TotalDuration** (int) - 估算总耗时间（单位秒）


        **StatusData**
        - **CurRetryCount** (int) - 当前失败重试次数
        - **FailedMessage** (str) - 当Status为Failed时, 显示失败原因
        - **MaxRetryCount** (int) - 用户设置的最大失败重试次数
        - **Progress** (dict) - 见 **Progress** 模型定义
        - **Status** (str) - 任务状态, 状态有 Created:已创建,Checking:检查中,Dumping:转储中,Loading:加载中,Syncing:同步中,Synced:已同步,Done:完成,Failed:失败,Stopping:停止中,Stopped:停止,RetryPending:重试等待中,Starting:启动中,FailedUnrecoverable:异常,StoppedUnrecoverable:异常,Success:成功,Started:已启动
        - **Sync** (dict) - 见 **SyncData** 模型定义


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.GetUDTSTaskStatusRequestSchema().dumps(d)

        resp = self.invoke("GetUDTSTaskStatus", d, **kwargs)
        return apis.GetUDTSTaskStatusResponseSchema().loads(resp)

    def list_udts_task(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUDTSTask - 获取用户创建的 Task 信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Limit** (str) - 请求数量，默认为 20
        - **Offset** (str) - 偏移量，默认为 0
        - **Type** (str) - 任务类型

        **Response**

        - **Data** (list) - 见 **ListDataItem** 模型定义
        - **Message** (str) - 返回信息

        **Response Model**

        **Progress**
        - **CurCount** (int) - 已迁移条目数
        - **CurDuration** (int) - 已耗时间（单位秒）
        - **Percentage** (float) - 完成进度
        - **TotalCount** (int) - 总条目数
        - **TotalDuration** (int) - 估算总耗时间（单位秒）


        **ListDataItem**
        - **CreateTime** (int) - 创建时间
        - **CurRetryCount** (int) - 当前失败重试次数
        - **MaxRetryCount** (int) - 最大失败重试次数
        - **Name** (str) - 任务名称
        - **Progress** (dict) - 见 **Progress** 模型定义
        - **Status** (str) - 任务状态
        - **TaskId** (str) - 任务 ID
        - **Type** (str) - 任务类型, full全量, incremental增量，full+incremental全量+增量。


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.ListUDTSTaskRequestSchema().dumps(d)

        resp = self.invoke("ListUDTSTask", d, **kwargs)
        return apis.ListUDTSTaskResponseSchema().loads(resp)

    def start_udts_task(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """StartUDTSTask - 启动UDTS服务

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **TaskId** (str) - (Required) 任务ID
        - **Type** (str) - 任务类型

        **Response**

        - **Message** (str) - 返回信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.StartUDTSTaskRequestSchema().dumps(d)

        resp = self.invoke("StartUDTSTask", d, **kwargs)
        return apis.StartUDTSTaskResponseSchema().loads(resp)

    def stop_udts_task(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """StopUDTSTask - 停止UDTS任务

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **TaskId** (str) - (Required) 任务 ID
        - **Type** (str) - 任务类型

        **Response**

        - **Message** (str) - 返回信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.StopUDTSTaskRequestSchema().dumps(d)

        resp = self.invoke("StopUDTSTask", d, **kwargs)
        return apis.StopUDTSTaskResponseSchema().loads(resp)
