import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.udisk.schemas import apis


class UDiskClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(UDiskClient, self).__init__(config, transport)

    def describe_udisk(self, req: dict = None) -> dict:
        """ DescribeUDisk - 获取UDisk实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DiskType: (Optional) 普通数据盘:DataDisk; 普通系统盘:SystemDisk; SSD数据盘:SSDDataDisk; RSSD数据盘:RSSDDataDisk; 为空拉取所有
        :param Limit: (Optional) 返回数据长度, 默认为20
        :param Offset: (Optional) 数据偏移量, 默认为0
        :param UDiskId: (Optional) UDisk Id(留空返回全部)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDisk", d)
        return apis.DescribeUDiskResponseSchema().loads(resp)

    def resize_udisk(self, req: dict = None) -> dict:
        """ ResizeUDisk - 调整UDisk容量

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 调整后大小, 单位:GB, 范围[1~2000],权限位控制可达8000,若需要请申请开通相关权限。
        :param UDiskId: (Required) UDisk Id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param CouponId: (Optional) 使用的代金券id
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUDiskRequestSchema().dumps(d)
        resp = self.invoke("ResizeUDisk", d)
        return apis.ResizeUDiskResponseSchema().loads(resp)

    def create_udisk_snapshot(self, req: dict = None) -> dict:
        """ CreateUDiskSnapshot - 创建snapshot快照

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 快照名称
        :param UDiskId: (Required) 快照的UDisk的Id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) Year , Month, Dynamic 默认: Dynamic
        :param Comment: (Optional) 快照描述
        :param Quantity: (Optional) 购买时长 默认: 1
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDiskSnapshotRequestSchema().dumps(d)
        resp = self.invoke("CreateUDiskSnapshot", d)
        return apis.CreateUDiskSnapshotResponseSchema().loads(resp)

    def describe_udisk_snapshot(self, req: dict = None) -> dict:
        """ DescribeUDiskSnapshot - 获取UDisk快照

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Optional) 返回数据长度, 默认为20
        :param Offset: (Optional) 数据偏移量, 默认为0
        :param SnapshotId: (Optional) 快照id，SnapshotId , UDiskId 同时传SnapshotId优先
        :param UDiskId: (Optional) UDiskId,返回该盘所做快照.(必须同时传Zone)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskSnapshotRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDiskSnapshot", d)
        return apis.DescribeUDiskSnapshotResponseSchema().loads(resp)

    def rename_udisk(self, req: dict = None) -> dict:
        """ RenameUDisk - 重命名UDisk

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UDiskId: (Required) 重命名的UDisk的Id
        :param UDiskName: (Required) 重命名UDisk的name
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RenameUDiskRequestSchema().dumps(d)
        resp = self.invoke("RenameUDisk", d)
        return apis.RenameUDiskResponseSchema().loads(resp)

    def restore_udisk(self, req: dict = None) -> dict:
        """ RestoreUDisk - 从备份恢复数据至UDisk

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UDiskId: (Required) 需要恢复的盘id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param SnapshotId: (Optional) 从指定的快照恢复
        :param SnapshotTime: (Optional) 指定从方舟恢复的备份时间点
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RestoreUDiskRequestSchema().dumps(d)
        resp = self.invoke("RestoreUDisk", d)
        return apis.RestoreUDiskResponseSchema().loads(resp)

    def attach_udisk(self, req: dict = None) -> dict:
        """ AttachUDisk - 将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UDiskId: (Required) 需要挂载的UDisk实例ID.
        :param UHostId: (Required) UHost实例ID
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param MultiAttach: (Optional) 是否允许多点挂载（Yes: 允许多点挂载， No: 不允许多点挂载， 不填默认Yes ）
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AttachUDiskRequestSchema().dumps(d)
        resp = self.invoke("AttachUDisk", d)
        return apis.AttachUDiskResponseSchema().loads(resp)

    def delete_udisk_snapshot(self, req: dict = None) -> dict:
        """ DeleteUDiskSnapshot - 删除Snapshot

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SnapshotId: (Required) 快照Id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param UDiskId: (Optional) UDisk Id,删除该盘所创建出来的所有快照
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDiskSnapshotRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDiskSnapshot", d)
        return apis.DeleteUDiskSnapshotResponseSchema().loads(resp)

    def describe_udisk_price(self, req: dict = None) -> dict:
        """ DescribeUDiskPrice - 获取UDisk实例价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 购买UDisk大小,单位:GB,范围[1~1000]
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) Year， Month， Dynamic，Trial，默认: Dynamic 如果不指定，则一次性获取三种计费
        :param DiskType: (Optional) UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），默认值（DataDisk）
        :param Quantity: (Optional) 购买UDisk的时长，默认值为1
        :param UDataArkMode: (Optional) 是否打开数据方舟, 打开"Yes",关闭"No", 默认关闭
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskPriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDiskPrice", d)
        return apis.DescribeUDiskPriceResponseSchema().loads(resp)

    def describe_udisk_upgrade_price(self, req: dict = None) -> dict:
        """ DescribeUDiskUpgradePrice - 获取UDisk升级价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 购买UDisk大小,单位:GB,范围[1~2000], 权限位控制可达8T,若需要请申请开通相关权限。
        :param SourceId: (Required) 升级目标UDisk ID
        :param UDataArkMode: (Required) 是否打开数据方舟, 打开"Yes",关闭"No", 默认关闭
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param DiskType: (Optional) 磁盘类型，SSDDataDisk:ssd数据盘,DataDisk:普通数据盘,SystemDisk:普通系统盘,SSDSystemDisk:ssd系统盘。默认为DataDisk
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDiskUpgradePrice", d)
        return apis.DescribeUDiskUpgradePriceResponseSchema().loads(resp)

    def delete_udisk(self, req: dict = None) -> dict:
        """ DeleteUDisk - 删除UDisk

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UDiskId: (Required) 要删除的UDisk的Id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDiskRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDisk", d)
        return apis.DeleteUDiskResponseSchema().loads(resp)

    def clone_udisk_snapshot(self, req: dict = None) -> dict:
        """ CloneUDiskSnapshot - 从快照创建UDisk克隆

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 实例名称
        :param Size: (Required) 购买UDisk大小,单位:GB,范围[1~2000], 权限位控制可达8T,若需要请申请开通相关权限。
        :param SourceId: (Required) 克隆父Snapshot的Id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) Year , Month, Dynamic，Postpay 默认: Dynamic
        :param Comment: (Optional) Disk注释
        :param CouponId: (Optional) 使用的代金券id
        :param Quantity: (Optional) 购买时长 默认: 1
        :param UDataArkMode: (Optional) 是否开启数据方舟   默认:No
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CloneUDiskSnapshotRequestSchema().dumps(d)
        resp = self.invoke("CloneUDiskSnapshot", d)
        return apis.CloneUDiskSnapshotResponseSchema().loads(resp)

    def create_udisk(self, req: dict = None) -> dict:
        """ CreateUDisk - 创建UDisk磁盘

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 实例名称
        :param Size: (Required) 购买UDisk大小,单位:GB,普通盘: 范围[1~2000], 权限位控制可达8T,若需要请申请开通相关权限;SSD盘： 范围[1~4000]。
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) Year , Month, Dynamic, Postpay, Trial 默认: Dynamic
        :param CmkId: (Optional) 加密需要的cmk id，UKmsMode为Yes时，必填
        :param CouponId: (Optional) 使用的代金券id
        :param DiskType: (Optional) UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），RSSDDataDisk（RSSD数据盘），默认值（DataDisk）
        :param Quantity: (Optional) 购买时长 默认: 1
        :param Tag: (Optional) 业务组 默认：Default
        :param UDataArkMode: (Optional) 是否开启数据方舟
        :param UKmsMode: (Optional) 是否加密。Yes：加密，No：不加密，默认值（No）
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDiskRequestSchema().dumps(d)
        resp = self.invoke("CreateUDisk", d)
        return apis.CreateUDiskResponseSchema().loads(resp)

    def detach_udisk(self, req: dict = None) -> dict:
        """ DetachUDisk - 卸载某个已经挂载在指定UHost实例上的UDisk

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UDiskId: (Required) 需要卸载的UDisk实例ID
        :param UHostId: (Required) UHost实例ID
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DetachUDiskRequestSchema().dumps(d)
        resp = self.invoke("DetachUDisk", d)
        return apis.DetachUDiskResponseSchema().loads(resp)

    def set_udisk__udataark_mode(self, req: dict = None) -> dict:
        """ SetUDiskUDataArkMode - 设置UDisk数据方舟的状态

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UDataArkMode: (Required) 是否开启数据方舟，开启:"Yes", 不支持:"No"
        :param UDiskId: (Required) 需要设置数据方舟的UDisk的Id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.SetUDiskUDataArkModeRequestSchema().dumps(d)
        resp = self.invoke("SetUDiskUDataArkMode", d)
        return apis.SetUDiskUDataArkModeResponseSchema().loads(resp)

    def clone_udisk(self, req: dict = None) -> dict:
        """ CloneUDisk - 从UDisk创建UDisk克隆

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 实例名称
        :param SourceId: (Required) 克隆父Disk的Id
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) Year , Month, Dynamic，Postpay 默认: Dynamic
        :param Comment: (Optional) Disk注释
        :param CouponId: (Optional) 使用的代金券id
        :param Quantity: (Optional) 购买时长 默认: 1
        :param UDataArkMode: (Optional) 方舟是否开启，"Yes":开启，"No":关闭；默认为"No"
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CloneUDiskRequestSchema().dumps(d)
        resp = self.invoke("CloneUDisk", d)
        return apis.CloneUDiskResponseSchema().loads(resp)
