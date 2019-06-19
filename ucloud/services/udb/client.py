import typing

from ucloud.core.client import Client
from ucloud.services.udb.schemas import apis


class UDBClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        super(UDBClient, self).__init__(config, transport, middleware)

    def delete_udb_log_package(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DeleteUDBLogPackage - 删除UDB日志包

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) 日志包id，可通过DescribeUDBLogPackage获得
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param BackupZone: (Optional) 跨可用区高可用备库所在可用区
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBLogPackageRequestSchema().dumps(d)

        resp = self.invoke("DeleteUDBLogPackage", d, **kwargs)
        return apis.DeleteUDBLogPackageResponseSchema().loads(resp)

    def describe_udb_backup(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeUDBBackup - 列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Required) 分页显示的条目数，列表操作则指定
        :param Offset: (Required) 分页显示的起始偏移，列表操作则指定
        :param BackupId: (Optional) 如果填了BackupId, 那么只拉取这个备份的记录
        :param BackupType: (Optional) 备份类型,取值为0或1，0表示自动，1表示手动
        :param BeginTime: (Optional) 过滤条件:起始时间(Unix时间戳)
        :param ClassType: (Optional) 如果未指定GroupId，则可选是否选取特定DB类型的配置(sql, nosql, postgresql, sqlserver)
        :param DBId: (Optional) DB实例Id，如果指定，则只获取该db的备份信息 该值可以通过DescribeUDBInstance获取
        :param EndTime: (Optional) 过滤条件:结束时间(Unix时间戳)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBBackupRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBBackup", d, **kwargs)
        return apis.DescribeUDBBackupResponseSchema().loads(resp)

    def describe_udb_log_package(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBLogPackage - 列表UDB实例binlog或slowlog或errorlog备份信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Required) 分页显示的条目数，列表操作则指定
        :param Offset: (Required) 分页显示的起始偏移，列表操作则指定
        :param BeginTime: (Optional) 过滤条件:起始时间(时间戳)
        :param DBId: (Optional) DB实例Id，如果指定，则只获取该db的备份信息
        :param EndTime: (Optional) 过滤条件:结束时间(时间戳)
        :param Type: (Optional) 需要列出的备份文件类型，每种文件的值如下 2 : BINLOG\_BACKUP 3 : SLOW\_QUERY\_BACKUP 4 : ERRORLOG\_BACKUP
        :param Types: (Optional) Types作为Type的补充，支持多值传入，可以获取多个类型的日志记录，如：Types.0=2&Types.1=3
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBLogPackageRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBLogPackage", d, **kwargs)
        return apis.DescribeUDBLogPackageResponseSchema().loads(resp)

    def describe_udb_param_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBParamGroup - 获取参数组详细参数信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Required) 分页显示的条目数，列表操作则指定
        :param Offset: (Required) 分页显示的起始偏移，列表操作则指定
        :param ClassType: (Optional) 如果未指定GroupId，则可选是否选取特定DB类型的配置(sql, nosql, postgresql, sqlserver)
        :param GroupId: (Optional) 参数组id，如果指定则获取描述，否则是列表操作，需要 指定Offset/Limit
        :param IsInUDBC: (Optional) 是否选取专区中配置
        :param RegionFlag: (Optional) 当请求没有填写Zone时，如果指定为true，表示只拉取跨可用区的相关配置文件，否则，拉取所有机房的配置文件（包括每个单可用区和跨可用区）
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBParamGroupRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBParamGroup", d, **kwargs)
        return apis.DescribeUDBParamGroupResponseSchema().loads(resp)

    def promote_udb_instance_to_ha(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ PromoteUDBInstanceToHA - 普通db升级为高可用(只针对mysql5.5及以上版本)

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PromoteUDBInstanceToHARequestSchema().dumps(d)

        resp = self.invoke("PromoteUDBInstanceToHA", d, **kwargs)
        return apis.PromoteUDBInstanceToHAResponseSchema().loads(resp)

    def check_udb_instance_to_ha_allowance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CheckUDBInstanceToHAAllowance - 核查db是否可以升级为高可用

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CheckUDBInstanceToHAAllowanceRequestSchema().dumps(d)

        resp = self.invoke("CheckUDBInstanceToHAAllowance", d, **kwargs)
        return apis.CheckUDBInstanceToHAAllowanceResponseSchema().loads(resp)

    def describe_udb_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstance - 获取UDB实例信息，支持两类操作：（1）指定DBId用于获取该db的信息；（2）指定ClassType、Offset、Limit用于列表操作，查询某一个类型db。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ClassType: (Required) DB种类，如果是列表操作，则需要指定,不区分大小写，其取值如下：mysql: SQL；mongo: NOSQL；postgresql: postgresql
        :param Limit: (Required) 分页显示数量，列表操作则指定
        :param Offset: (Required) 分页显示起始偏移位置，列表操作则指定
        :param DBId: (Optional) DB实例id，如果指定则获取描述，否则为列表操作， 指定Offset/Limit/ClassType DBId可通过DescribeUDBInstance获取
        :param IncludeSlaves: (Optional) 当只获取这个特定DBId的信息时，如果有该选项，那么把这个DBId实例的所有从库信息一起拉取并返回
        :param IsInUDBC: (Optional) 是否查看专区里面DB
        :param UDBCId: (Optional) IsInUDBC为True,UDBCId为空，说明查看整个可用区的专区的db，如果UDBId不为空则只查看此专区下面的db
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstance", d, **kwargs)
        return apis.DescribeUDBInstanceResponseSchema().loads(resp)

    def edit_udb_backup_blacklist(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ EditUDBBackupBlacklist - 编辑UDB实例的备份黑名单

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Blacklist: (Required) 黑名单，规范示例,指定库mysql.%;test.%; 指定表city.address;
        :param DBId: (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.EditUDBBackupBlacklistRequestSchema().dumps(d)

        resp = self.invoke("EditUDBBackupBlacklist", d, **kwargs)
        return apis.EditUDBBackupBlacklistResponseSchema().loads(resp)

    def promote_udb_slave(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ PromoteUDBSlave - 从库提升为独立库

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        :param IsForce: (Optional) 是否强制(如果从库落后可能会禁止提升)，默认false 如果落后情况下，强制提升丢失数据
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PromoteUDBSlaveRequestSchema().dumps(d)

        resp = self.invoke("PromoteUDBSlave", d, **kwargs)
        return apis.PromoteUDBSlaveResponseSchema().loads(resp)

    def upload_udb_param_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ UploadUDBParamGroup - 导入UDB配置

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Content: (Required) 配置内容，导入的配置内容采用base64编码
        :param DBTypeId: (Required) DB类型id，DB类型id，mysql/mongodb/postgesql按版本细分 1：mysql-5.1，2：mysql-5.5，3：percona-5.5，4：mysql-5.6，5：percona-5.6，6：mysql-5.7，7：percona-5.7，8：mariadb-10.0，9：mongodb-2.4，10：mongodb-2.6，11：mongodb-3.0，12：mongodb-3.2,13：postgresql-9.4，14：postgresql-9.6
        :param Description: (Required) 参数组描述
        :param GroupName: (Required) 配置参数组名称
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ParamGroupTypeId: (Optional) 配置文件子类型 0-未知, 1-Shardsvr-MMAPv1, 2-Shardsvr-WiredTiger, 3-Configsvr-MMAPv1, 4-Configsvr-WiredTiger, 5-Mongos
        :param RegionFlag: (Optional) 该配置文件是否是地域级别配置文件，默认是false
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UploadUDBParamGroupRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("UploadUDBParamGroup", d, **kwargs)
        return apis.UploadUDBParamGroupResponseSchema().loads(resp)

    def describe_udb_instance_backup_url(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstanceBackupURL - 获取UDB备份下载地址

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) DB实例备份ID,该值可以通过DescribeUDBBackup获取
        :param DBId: (Required) DB实例Id,该值可通过DescribeUDBInstance获取
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBackupURLRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstanceBackupURL", d, **kwargs)
        return apis.DescribeUDBInstanceBackupURLResponseSchema().loads(resp)

    def fetch_udb_instance_earliest_recover_time(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ FetchUDBInstanceEarliestRecoverTime - 获取UDB最早可回档的时间点

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) DB实例Id
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.FetchUDBInstanceEarliestRecoverTimeRequestSchema().dumps(d)

        resp = self.invoke("FetchUDBInstanceEarliestRecoverTime", d, **kwargs)
        return apis.FetchUDBInstanceEarliestRecoverTimeResponseSchema().loads(resp)

    def backup_udb_instance_slow_log(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ BackupUDBInstanceSlowLog - 备份UDB指定时间段的slowlog分析结果

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupName: (Required) 备份文件名称
        :param BeginTime: (Required) 过滤条件:起始时间(时间戳)
        :param DBId: (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        :param EndTime: (Required) 过滤条件:结束时间(时间戳)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceSlowLogRequestSchema().dumps(d)

        resp = self.invoke("BackupUDBInstanceSlowLog", d, **kwargs)
        return apis.BackupUDBInstanceSlowLogResponseSchema().loads(resp)

    def create_udb_slave(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateUDBSlave - 创建UDB实例的slave

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 实例名称，至少6位
        :param SrcId: (Required) master实例的DBId,该值可以通过DescribeUDBInstance获取
        :param CouponId: (Optional) 使用的代金券id
        :param DiskSpace: (Optional) 磁盘空间(GB), 暂时支持20G - 3000G（API支持，前端暂时只开放内存定制）
        :param InstanceMode: (Optional) UDB实例部署模式，可选值如下：Normal: 普通单点实例HA: 高可用部署实例
        :param InstanceType: (Optional) UDB实例类型：Normal和SATA_SSD
        :param IsLock: (Optional) 是否锁主库，默认为true
        :param MemoryLimit: (Optional) 内存限制(MB)，目前支持以下几档 1000M/2000M/4000M/ 6000M/8000M/12000M/16000M/ 24000M/32000M/48000M/ 64000M/96000M
        :param Port: (Optional) 端口号，mysql默认3306
        :param SSDType: (Optional) SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        :param UseSSD: (Optional) 是否使用SSD，默认为false
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBSlaveRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDBSlave", d, **kwargs)
        return apis.CreateUDBSlaveResponseSchema().loads(resp)

    def delete_udb_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DeleteUDBInstance - 删除UDB实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) DB实例的id,该值可以通过DescribeUDBInstance获取
        :param UDBCId: (Optional) 专区ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBInstanceRequestSchema().dumps(d)

        resp = self.invoke("DeleteUDBInstance", d, **kwargs)
        return apis.DeleteUDBInstanceResponseSchema().loads(resp)

    def describe_udb_type(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeUDBType - 获取UDB支持的类型信息

        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param DBClusterType: (Optional) DB实例类型，如mysql，sqlserver，mongo，postgresql
        :param DiskType: (Optional) 返回支持某种磁盘类型的DB类型。如果没传，则表示任何磁盘类型均可。
        :param InstanceMode: (Optional) 返回支持某种实例类型的DB类型。如果没传，则表示任何实例类型均可。normal:单点,ha:高可用,sharded_cluster:分片集群
        """
        # build request
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBTypeRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBType", d, **kwargs)
        return apis.DescribeUDBTypeResponseSchema().loads(resp)

    def modify_udb_instance_name(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ModifyUDBInstanceName - 重命名UDB实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        :param Name: (Required) 实例的新名字, 长度要求为6~63位
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUDBInstanceNameRequestSchema().dumps(d)

        resp = self.invoke("ModifyUDBInstanceName", d, **kwargs)
        return apis.ModifyUDBInstanceNameResponseSchema().loads(resp)

    def start_udb_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ StartUDBInstance - 启动UDB实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StartUDBInstanceRequestSchema().dumps(d)

        resp = self.invoke("StartUDBInstance", d, **kwargs)
        return apis.StartUDBInstanceResponseSchema().loads(resp)

    def update_udb_instance_backup_strategy(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ UpdateUDBInstanceBackupStrategy - 修改UDB自动备份策略

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 主节点的Id
        :param BackupDate: (Optional) 备份时期标记位。共7位，每一位为一周中一天的备份情况，0表示关闭当天备份，1表示打开当天备份。最右边的一位为星期天的备份开关，其余从右到左依次为星期一到星期六的备份配置开关，每周必须至少设置两天备份。例如：1100000表示打开星期六和星期五的备份功能
        :param BackupMethod: (Optional) 选择默认的备份方式，可选 snapshot 表示使用快照/物理备份，填 logic 表示使用逻辑备份。需要同时设置BackupDate字段。（注意现在只有SSD 版本的 MySQL实例支持物理备份）
        :param BackupTime: (Optional) 备份的整点时间，范围[0,23]
        :param ForceDump: (Optional) 当导出某些数据遇到问题后，是否强制导出其他剩余数据默认是false需要同时设置BackupDate字段
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateUDBInstanceBackupStrategyRequestSchema().dumps(d)

        resp = self.invoke("UpdateUDBInstanceBackupStrategy", d, **kwargs)
        return apis.UpdateUDBInstanceBackupStrategyResponseSchema().loads(resp)

    def backup_udb_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ BackupUDBInstance - 备份UDB实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupName: (Required) 备份名称
        :param DBId: (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        :param BackupMethod: (Optional) 使用的备份方式。（快照备份即物理备份。注意只有SSD版本的mysql实例支持设置为snapshot）
        :param Blacklist: (Optional) 备份黑名单列表，以 ; 分隔。注意：只有逻辑备份下备份黑名单才生效，快照备份备份黑名单下无效
        :param ForceBackup: (Optional) true表示逻辑备份时是使用 --force 参数，false表示不使用 --force 参数。物理备份此参数无效。
        :param UseBlacklist: (Optional) 是否使用黑名单备份，默认false
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("BackupUDBInstance", d, **kwargs)
        return apis.BackupUDBInstanceResponseSchema().loads(resp)

    def backup_udb_instance_binlog(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ BackupUDBInstanceBinlog - 备份UDB指定时间段的binlog列表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupFile: (Required) 需要备份文件,可通过DescribeUDBInstanceBinlog获得 如果要传入多个文件名，以空格键分割,用单引号包含.
        :param DBId: (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        :param BackupName: (Optional) DB备份文件名称
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceBinlogRequestSchema().dumps(d)

        resp = self.invoke("BackupUDBInstanceBinlog", d, **kwargs)
        return apis.BackupUDBInstanceBinlogResponseSchema().loads(resp)

    def clear_udb_log(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ClearUDBLog - 清除UDB实例的log

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) DB实例的id,该值可以通过DescribeUDBInstance获取
        :param LogType: (Required) 日志类型，10-error（暂不支持）、20-slow（暂不支持 ）、30-binlog
        :param BeforeTime: (Optional) 删除时间点(至少前一天)之前log，采用时间戳(秒)，默认当 前时间点前一天
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ClearUDBLogRequestSchema().dumps(d)

        resp = self.invoke("ClearUDBLog", d, **kwargs)
        return apis.ClearUDBLogResponseSchema().loads(resp)

    def create_udb_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateUDBInstance - 创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param AdminPassword: (Required) 管理员密码
        :param DBTypeId: (Required) DB类型id，mysql/mongodb/postgesql按版本细分 1：mysql-5.1，2：mysql-5.5，3：percona-5.5，4：mysql-5.6，5：percona-5.6，6：mysql-5.7，7：percona-5.7，8：mariadb-10.0，9：mongodb-2.4，10：mongodb-2.6，11：mongodb-3.0，12：mongodb-3.2,13：postgresql-9.4，14：postgresql-9.6，14：postgresql-10.4
        :param DiskSpace: (Required) 磁盘空间(GB), 暂时支持20G - 3000G
        :param MemoryLimit: (Required) 内存限制(MB)，目前支持以下几档 1000M/2000M/4000M/ 6000M/8000M/12000M/16000M/ 24000M/32000M/48000M/ 64000M/96000M
        :param Name: (Required) 实例名称，至少6位
        :param ParamGroupId: (Required) DB实例使用的配置参数组id
        :param Port: (Required) 端口号，mysql默认3306，mongodb默认27017，postgresql默认5432
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param AdminUser: (Optional) 管理员帐户名，默认root
        :param BackupCount: (Optional) 备份策略，每周备份数量，默认7次
        :param BackupDuration: (Optional) 备份策略，备份时间间隔，单位小时计，默认24小时
        :param BackupId: (Optional) 备份id，如果指定，则表明从备份恢复实例
        :param BackupTime: (Optional) 备份策略，备份开始时间，单位小时计，默认1点
        :param BackupZone: (Optional) 跨可用区高可用备库所在可用区，参见 [可用区列表](../summary/regionlist.html)
        :param CPU: (Optional) cpu核数
        :param ChargeType: (Optional) Year， Month， Dynamic，Trial，默认: Month
        :param ClusterRole: (Optional) 当DB类型(DBTypeId)为mongodb时，需要指定mongo的角色，可选值为configsrv (配置节点)，shardsrv (数据节点)
        :param CouponId: (Optional) 使用的代金券id
        :param DisableSemisync: (Optional) 是否开启异步高可用，默认不填，可置为true
        :param HAArch: (Optional) 高可用架构:1） haproxy（默认）: 当前仅支持mysql。2） sentinel: 基于vip和哨兵节点的架构，当前支持mysql和pg。
        :param InstanceMode: (Optional) UDB实例模式类型, 可选值如下: "Normal": 普通版UDB实例 "HA": 高可用版UDB实例 默认是"Normal"
        :param InstanceType: (Optional) UDB数据库机型
        :param Quantity: (Optional) 购买时长，默认值1
        :param SSDType: (Optional) SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        :param SubnetId: (Optional) 子网ID
        :param Tag: (Optional) 
        :param UDBCId: (Optional) 专区ID信息（如果这个参数存在这说明是在专区中创建DB）
        :param UseSSD: (Optional) 是否使用SSD，默认为false。目前主要可用区、海外机房、新机房只提供SSD资源，非SSD资源不再提供。
        :param VPCId: (Optional) VPC的ID
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDBInstance", d, **kwargs)
        return apis.CreateUDBInstanceResponseSchema().loads(resp)

    def create_udb_instance_by_recovery(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CreateUDBInstanceByRecovery - 创建db，将新创建的db恢复到指定db某个指定时间点

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 实例名称，至少6位
        :param RecoveryTime: (Required) 恢复到某个时间点的时间戳(UTC时间格式，默认单位秒)
        :param SrcDBId: (Required) 源实例的Id
        :param ChargeType: (Optional) Year， Month， Dynamic，Trial，默认: Dynamic
        :param CouponId: (Optional) 使用的代金券id
        :param Quantity: (Optional) 购买时长，默认值1
        :param SubnetId: (Optional) 子网ID
        :param UDBCId: (Optional) 专区的Id
        :param UseSSD: (Optional) 指定是否是否使用SSD，默认使用主库的配置
        :param VPCId: (Optional) VPC的ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBInstanceByRecoveryRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDBInstanceByRecovery", d, **kwargs)
        return apis.CreateUDBInstanceByRecoveryResponseSchema().loads(resp)

    def create_udb_replication_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CreateUDBReplicationInstance - 创建MongoDB的副本节点（包括仲裁）

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 实例名称，至少6位
        :param SrcId: (Required) primary节点的DBId,该值可以通过DescribeUDBInstance获取
        :param CouponId: (Optional) 使用的代金券id
        :param IsArbiter: (Optional) 是否是仲裁节点，默认false，仲裁节点按最小机型创建
        :param Port: (Optional) 端口号，默认27017，取值范围3306至65535。
        :param UseSSD: (Optional) 是否使用SSD，默认不使用
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBReplicationInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDBReplicationInstance", d, **kwargs)
        return apis.CreateUDBReplicationInstanceResponseSchema().loads(resp)

    def describe_udb_instance_binlog_backup_state(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstanceBinlogBackupState - 获取udb实例备份状态

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) 备份记录ID
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param BackupZone: (Optional) 跨可用区高可用备库所在可用区
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBinlogBackupStateRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstanceBinlogBackupState", d, **kwargs)
        return apis.DescribeUDBInstanceBinlogBackupStateResponseSchema().loads(resp)

    def describe_udb_instance_state(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstanceState - 获取UDB实例状态

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceStateRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstanceState", d, **kwargs)
        return apis.DescribeUDBInstanceStateResponseSchema().loads(resp)

    def describe_udb_log_backup_url(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBLogBackupURL - 获取UDB的slowlog备份地址

        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) DB实例备份ID
        :param DBId: (Required) DB实例Id
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBLogBackupURLRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBLogBackupURL", d, **kwargs)
        return apis.DescribeUDBLogBackupURLResponseSchema().loads(resp)

    def restart_udb_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ RestartUDBInstance - 重启UDB实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RestartUDBInstanceRequestSchema().dumps(d)

        resp = self.invoke("RestartUDBInstance", d, **kwargs)
        return apis.RestartUDBInstanceResponseSchema().loads(resp)

    def update_udb_param_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ UpdateUDBParamGroup - 更新UDB配置参数项

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 配置参数组id，使用DescribeUDBParamGroup获得
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param Description: (Optional) 参数组的描述
        :param Key: (Optional) 参数名称（与Value配合使用）
        :param Name: (Optional) 参数组的名字
        :param RegionFlag: (Optional) 该配置文件是否是地域级别配置文件，默认是false
        :param Value: (Optional) 参数值（与Key配合使用）
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateUDBParamGroupRequestSchema().dumps(d)

        resp = self.invoke("UpdateUDBParamGroup", d, **kwargs)
        return apis.UpdateUDBParamGroupResponseSchema().loads(resp)

    def backup_udb_instance_error_log(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ BackupUDBInstanceErrorLog - 备份UDB指定时间段的errorlog

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupName: (Required) 备份名称
        :param DBId: (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceErrorLogRequestSchema().dumps(d)

        resp = self.invoke("BackupUDBInstanceErrorLog", d, **kwargs)
        return apis.BackupUDBInstanceErrorLogResponseSchema().loads(resp)

    def delete_udb_param_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DeleteUDBParamGroup - 删除配置参数组

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 参数组id,可通过DescribeUDBParamGroup获取
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param RegionFlag: (Optional) 是否属于地域级别
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBParamGroupRequestSchema().dumps(d)

        resp = self.invoke("DeleteUDBParamGroup", d, **kwargs)
        return apis.DeleteUDBParamGroupResponseSchema().loads(resp)

    def describe_udb_instance_binlog(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstanceBinlog - 获取UDB指定时间段的binlog列表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BeginTime: (Required) 过滤条件:起始时间(时间戳)
        :param DBId: (Required) DB实例Id
        :param EndTime: (Required) 过滤条件:结束时间(时间戳)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBinlogRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstanceBinlog", d, **kwargs)
        return apis.DescribeUDBInstanceBinlogResponseSchema().loads(resp)

    def modify_udb_instance_password(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ModifyUDBInstancePassword - 修改DB实例的管理员密码

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的ID,该值可以通过DescribeUDBInstance获取
        :param Password: (Required) 实例的新密码
        :param AccountName: (Optional) sqlserver帐号，仅在sqlserver的情况下填该参数
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUDBInstancePasswordRequestSchema().dumps(d)

        resp = self.invoke("ModifyUDBInstancePassword", d, **kwargs)
        return apis.ModifyUDBInstancePasswordResponseSchema().loads(resp)

    def switch_udb_instance_to_ha(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ SwitchUDBInstanceToHA - 普通UDB切换为高可用，原db状态为WaitForSwitch时，调用该api

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        :param ChargeType: (Optional) Year， Month， Dynamic，Trial，不填则按现在单点计费执行
        :param Quantity: (Optional) 购买时长，需要和 ChargeType 搭配使用，否则使用单点计费策略的值
        :param Tag: (Optional) 业务组
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.SwitchUDBInstanceToHARequestSchema().dumps(d)

        resp = self.invoke("SwitchUDBInstanceToHA", d, **kwargs)
        return apis.SwitchUDBInstanceToHAResponseSchema().loads(resp)

    def create_udb_route_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CreateUDBRouteInstance - 创建mongos实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ConfigsvrId: (Required) 配置服务器的dbid，允许一个或者三个。
        :param DBTypeId: (Required) DB类型id，mongodb按版本细分有1：mongodb-2.4，2：mongodb-2.6,3：mongodb-3.0，4：mongodb-3.2
        :param DiskSpace: (Required) 磁盘空间(GB), 暂时支持20G - 500G
        :param MemoryLimit: (Required) 内存限制(MB)，目前支持以下几档 600M/1500M/3000M /6000M/15000M/30000M
        :param Name: (Required) 实例名称，至少6位
        :param ParamGroupId: (Required) DB实例使用的配置参数组id
        :param Port: (Required) 端口号，mongodb默认27017
        :param ChargeType: (Optional) Year， Month， Dynamic，Trial，默认: Month
        :param CouponId: (Optional) 使用的代金券id
        :param Quantity: (Optional) 购买时长，默认值1
        :param UseSSD: (Optional) 是否使用SSD，默认为false
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBRouteInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDBRouteInstance", d, **kwargs)
        return apis.CreateUDBRouteInstanceResponseSchema().loads(resp)

    def describe_udb_instance_backup_state(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstanceBackupState - 获取UDB实例备份状态

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) 备份记录ID
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param BackupZone: (Optional) 跨可用区高可用备库所在可用区，参见［可用区列表］
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBackupStateRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstanceBackupState", d, **kwargs)
        return apis.DescribeUDBInstanceBackupStateResponseSchema().loads(resp)

    def describe_udb_instance_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstancePrice - 获取UDB实例价格信息

        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBTypeId: (Required) UDB实例的DB版本字符串
        :param DiskSpace: (Required) 磁盘空间(GB),暂时支持20(GB) - 3000(GB), 输入不带单位
        :param MemoryLimit: (Required) 内存限制(MB)，单位为MB.目前支持：1000-96000
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) Year，按年付费； Month，按月付费 Dynamic，按需付费（需开启权限) Trial，试用（需开启权限）默认为月付
        :param Count: (Optional) 购买DB实例数量,最大数量为10台, 默认为1台
        :param InstanceMode: (Optional) 实例的部署类型。可选值为：Normal: 普通单点实例，Slave: 从库实例,HA: 高可用部署实例，默认是Normal
        :param Quantity: (Optional) DB购买多少个"计费时间单位"，默认值为1。比如：买2个月，Quantity就是2。如果计费单位是“按月”，并且Quantity为0，表示“购买到月底”
        :param SSDType: (Optional) SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必填
        :param UseSSD: (Optional) 是否使用SSD，默认为false
        """
        # build request
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstancePriceRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstancePrice", d, **kwargs)
        return apis.DescribeUDBInstancePriceResponseSchema().loads(resp)

    def resize_udb_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ResizeUDBInstance - 修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id
        :param DiskSpace: (Required) 磁盘空间(GB), 暂时支持20G-3000G
        :param MemoryLimit: (Required) 内存限制(MB)，目前支持以下几档 1000M/2000M/4000M/ 6000M/8000M/ 12000M/16000M/ 24000M/32000M/ 48000M/64000M/96000M。
        :param CouponId: (Optional) 使用的代金券id
        :param InstanceMode: (Optional) UDB实例模式类型, 可选值如下: "Normal": 普通版UDB实例 "HA": 高可用版UDB实例 默认是"Normal"
        :param InstanceType: (Optional) UDB数据库机型: "Normal": "标准机型" ,  "SATA_SSD": "SSD机型" , "PCIE_SSD": "SSD高性能机型" ,  "Normal_Volume": "标准大容量机型",  "SATA_SSD_Volume": "SSD大容量机型" ,  "PCIE_SSD_Volume": "SSD高性能大容量机型"
        :param SSDType: (Optional) SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        :param StartAfterUpgrade: (Optional) DB关闭状态下升降级，升降级后是否启动DB，默认为false
        :param UDBCId: (Optional) 专区的ID，如果有值表示专区中的DB配置升降级
        :param UseSSD: (Optional) 是否使用SSD，默认为false
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUDBInstanceRequestSchema().dumps(d)

        resp = self.invoke("ResizeUDBInstance", d, **kwargs)
        return apis.ResizeUDBInstanceResponseSchema().loads(resp)

    def check_recover_udb_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CheckRecoverUDBInstance - 核查db是否可以使用回档功能

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SrcDBId: (Required) 源实例的Id(只支持普通版DB不支持高可用)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CheckRecoverUDBInstanceRequestSchema().dumps(d)

        resp = self.invoke("CheckRecoverUDBInstance", d, **kwargs)
        return apis.CheckRecoverUDBInstanceResponseSchema().loads(resp)

    def create_udb_param_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CreateUDBParamGroup - 从已有配置文件创建新配置文件

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBTypeId: (Required) DB类型id，mysql/mongodb/postgesql按版本细分 1：mysql-5.1，2：mysql-5.5，3：percona-5.5，4：mysql-5.6，5：percona-5.6，6：mysql-5.7，7：percona-5.7，8：mariadb-10.0，9：mongodb-2.4，10：mongodb-2.6，11：mongodb-3.0，12：mongodb-3.2,13：postgresql-9.4，14：postgresql-9.6
        :param Description: (Required) 参数组描述
        :param GroupName: (Required) 新配置参数组名称
        :param SrcGroupId: (Required) 源参数组id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param RegionFlag: (Optional) 是否是地域级别的配置文件，默认是false
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBParamGroupRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDBParamGroup", d, **kwargs)
        return apis.CreateUDBParamGroupResponseSchema().loads(resp)

    def delete_udb_backup(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DeleteUDBBackup - 删除UDB实例备份

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) 备份id，可通过DescribeUDBBackup获得
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param BackupZone: (Optional) 跨可用区高可用备库所在可用区，参见［可用区列表］
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBBackupRequestSchema().dumps(d)

        resp = self.invoke("DeleteUDBBackup", d, **kwargs)
        return apis.DeleteUDBBackupResponseSchema().loads(resp)

    def describe_udb_backup_blacklist(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBBackupBlacklist - 获取UDB实例的备份黑名单

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBBackupBlacklistRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBBackupBlacklist", d, **kwargs)
        return apis.DescribeUDBBackupBlacklistResponseSchema().loads(resp)

    def describe_udb_binlog_backup_url(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBBinlogBackupURL - 获取UDB的Binlog备份地址

        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) DB实例备份ID
        :param DBId: (Required) DB实例Id
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBBinlogBackupURLRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBBinlogBackupURL", d, **kwargs)
        return apis.DescribeUDBBinlogBackupURLResponseSchema().loads(resp)

    def describe_udb_instance_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUDBInstanceUpgradePrice - 获取UDB实例升降级价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id
        :param DiskSpace: (Required) 磁盘空间(GB), 暂时支持20G - 500G
        :param MemoryLimit: (Required) 内存限制(MB)
        :param SSDType: (Optional) SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        :param UseSSD: (Optional) 是否使用SSD，默认为false
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDBInstanceUpgradePrice", d, **kwargs)
        return apis.DescribeUDBInstanceUpgradePriceResponseSchema().loads(resp)

    def stop_udb_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ StopUDBInstance - 关闭UDB实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DBId: (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        :param ForceToKill: (Optional) 是否使用强制手段关闭DB，默认是false
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StopUDBInstanceRequestSchema().dumps(d)

        resp = self.invoke("StopUDBInstance", d, **kwargs)
        return apis.StopUDBInstanceResponseSchema().loads(resp)

    def update_udb_instance_slave_backup_switch(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ UpdateUDBInstanceSlaveBackupSwitch - 开启或者关闭UDB从库备份

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupSwitch: (Required) 从库的备份开关，范围[0,1],0表示从库备份功能关闭,1 表示从库备份开关打开。
        :param MasterDBId: (Required) 主库的Id
        :param SlaveDBId: (Optional) 从库的Id,如果从库备份开关设定为打开，则必须赋值。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateUDBInstanceSlaveBackupSwitchRequestSchema().dumps(d)

        resp = self.invoke("UpdateUDBInstanceSlaveBackupSwitch", d, **kwargs)
        return apis.UpdateUDBInstanceSlaveBackupSwitchResponseSchema().loads(resp)
