import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.uhost.schemas import apis


class UHostClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(UHostClient, self).__init__(config, transport)

    def create_uhost_instance(self, req: dict = None) -> dict:
        """ CreateUHostInstance - 创建UHost实例。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ImageId: (Required) 镜像ID。 请通过 [DescribeImage](describe_image.html)获取
        :param LoginMode: (Required) 主机登陆模式。密码（默认选项）: Password。
        :param Password: (Required) UHost密码。请遵照[[api:uhost-api:specification|字段规范]]设定密码。密码需使用base64进行编码，举例如下：# echo -n Password1 | base64UGFzc3dvcmQx。
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param AlarmTemplateId: (Optional) 告警模板id，如果传了告警模板id，且告警模板id正确，则绑定告警模板。绑定告警模板失败只会在后台有日志，不会影响创建主机流程，也不会在前端报错。
        :param BootDiskSpace: (Optional) 【待废弃，不建议调用】系统盘大小。 单位：GB， 范围[20,100]， 步长：10
        :param CPU: (Optional) 虚拟CPU核数。可选参数：1-64（可选范围与UHostType相关）。默认值: 4，只有Intel/Cascadelake支持CPU 64。
        :param ChargeType: (Optional) 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Dynamic，按小时付费 \\ 默认为月付；\\ >Postpay ，后付费。
        :param CouponId: (Optional) 主机代金券ID。请通过DescribeCoupon接口查询，或登录用户中心查看
        :param DiskPassword: (Optional) 【待废弃，不建议调用】加密盘的密码。若输入此字段，自动选择加密盘。加密盘需要权限位。
        :param DiskSpace: (Optional) 【待废弃，不建议调用】数据盘大小。 单位：GB， 范围[0,8000]， 步长：10， 默认值：20，云盘支持0-8000；本地普通盘支持0-2000；本地SSD盘（包括所有GPU机型）支持100-1000
        :param Disks: (Optional) Disks
        :param GPU: (Optional) GPU卡核心数。仅GPU机型支持此字段（可选范围与UHostType相关）
        :param GpuType: (Optional) GPU类型，枚举值["K80", "P40", "V100"]
        :param HostType: (Optional) 【已废弃】宿主机类型，N2，N1
        :param HotplugFeature: (Optional) 【待废弃，不建议调用】是否开启热升级特性。True为开启，False为未开启，默认False。仅系列1云主机需要使用此字段，系列2云主机根据镜像是否支持云主机。
        :param InstallAgent: (Optional) 【暂不支持】是否安装UGA。'yes': 安装；其他或者不填：不安装。
        :param IsolationGroup: (Optional) 硬件隔离组id。可通过DescribeIsolationGroup获取。
        :param KeyPair: (Optional) 【暂不支持】Keypair公钥，LoginMode为KeyPair时此项必须
        :param MachineType: (Optional) 云主机类型，枚举值["N", "C", "G", "O"]
        :param MaxCount: (Optional) 【批量创建主机时必填】最大创建主机数量，取值范围是[1,100];
        :param Memory: (Optional) 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值：8192
        :param MinimalCpuPlatform: (Optional) 最低cpu平台，枚举值["Intel/Auto", "Intel/IvyBridge", "Intel/Haswell", "Intel/Broadwell", "Intel/Skylake", "Intel/Cascadelake"(只有O型云主机可选)]
        :param Name: (Optional) UHost实例名称。默认：UHost。请遵照[[api:uhost-api:specification|字段规范]]设定实例名称。
        :param NetCapability: (Optional) 网络增强。枚举值：Normal（默认），不开启;  Super，开启网络增强1.0； Ultra，开启网络增强2.0（仅支持部分可用区，请参考控制台）
        :param NetworkId: (Optional) 【已废弃】网络ID（VPC2.0情况下无需填写）。VPC1.0情况下，若不填写，代表优先选择基础网络； 若填写，代表选择子网。参见DescribeSubnet。
        :param NetworkInterface: (Optional) NetworkInterface
        :param PrivateIp: (Optional) 【数组】创建云主机时指定内网IP。若不传值，则随机分配当前子网下的IP。调用方式举例：PrivateIp.0=x.x.x.x。当前只支持一个内网IP。
        :param PrivateMac: (Optional) 【批量创建该参数无效】【内部字段】创建云主机时指定Mac。调用方式举例：PrivateMac="xx:xx:xx:xx:xx:xx"。
        :param Quantity: (Optional) 购买时长。默认:值 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表购买至月末。
        :param ResourceType: (Optional) 【内部参数】资源类型
        :param SecurityGroupId: (Optional) 防火墙Id，默认：Web推荐防火墙。如何查询SecurityGroupId请参见 [DescribeSecurityGroup](../unet-api/describe_security_group.html)。
        :param SetId: (Optional) 
        :param StorageType: (Optional) 【待废弃，不建议调用】磁盘类型，同时设定系统盘和数据盘的磁盘类型。枚举值为：LocalDisk，本地磁盘; UDisk，云硬盘；默认为LocalDisk。仅部分可用区支持云硬盘方式的主机存储方式，具体请查询控制台。
        :param SubnetId: (Optional) 子网 ID。默认为当前地域的默认子网。
        :param Tag: (Optional) 业务组。默认：Default（Default即为未分组）。请遵照[[api:uhost-api:specification|字段规范]]设定业务组。
        :param TimemachineFeature: (Optional) 【待废弃，不建议调用】是否开启方舟特性。Yes为开启方舟，No为关闭方舟。目前仅选择普通本地盘+普通本地盘 或 SSD云盘+普通云盘的组合支持开启方舟。
        :param UHostType: (Optional) 云主机机型。参考[[api:uhost-api:uhost_type|云主机机型说明]]。【待废弃，不建议调用】
        :param UserDataScript: (Optional) 【暂不支持】cloudinit方式下，用户初始化脚本
        :param VPCId: (Optional) VPC ID。默认为当前地域的默认VPC。
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("CreateUHostInstance", d)
        return apis.CreateUHostInstanceResponseSchema().loads(resp)

    def get_uhost_instance_vnc_info(self, req: dict = None) -> dict:
        """ GetUHostInstanceVncInfo - 获取指定UHost实例的管理VNC配置详细信息。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](./describe_uhost_instance.html)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUHostInstanceVncInfoRequestSchema().dumps(d)
        resp = self.invoke("GetUHostInstanceVncInfo", d)
        return apis.GetUHostInstanceVncInfoResponseSchema().loads(resp)

    def poweroff_uhost_instance(self, req: dict = None) -> dict:
        """ PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](./describe_uhost_instance.html)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PoweroffUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("PoweroffUHostInstance", d)
        return apis.PoweroffUHostInstanceResponseSchema().loads(resp)

    def reinstall_uhost_instance(self, req: dict = None) -> dict:
        """ ReinstallUHostInstance - 重新安装指定UHost实例的操作系统

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例资源ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param BootDiskSpace: (Optional) 系统盘大小。 单位：GB， 范围[20,100]， 步长：10
        :param DNSServers: (Optional) 针对非私有子网主机，可自定义DNS。n可为0-2
        :param ImageId: (Optional) 镜像Id，默认使用原镜像 参见 [DescribeImage](describe_image.html)
        :param Password: (Optional) 如果创建UHost实例时LoginMode为Password，则必须填写，如果LoginMode为KeyPair，不需要填写 （密码格式使用BASE64编码；LoginMode不可变更）
        :param ReserveDisk: (Optional) 是否保留数据盘，保留：Yes，不报留：No， 默认：Yes；如果是从Windows重装为Linux或反之，则无法保留数据盘
        :param ResourceType: (Optional) 云灾备指明191
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReinstallUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("ReinstallUHostInstance", d)
        return apis.ReinstallUHostInstanceResponseSchema().loads(resp)

    def resize_uhost_instance(self, req: dict = None) -> dict:
        """ ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param BootDiskSpace: (Optional) 【待废弃】系统盘大小，单位：GB，范围[20,100]，步长：10，系统盘不支持缩容，因此不允许输入比当前实例系统盘小的值
        :param CPU: (Optional) 虚拟CPU核数。可选参数：1-32（可选范围与UHostType相关）。默认值为当前实例的CPU核数
        :param DiskSpace: (Optional) 【待废弃】数据盘大小，单位：GB，范围[10,1000]； SSD机型，单位：GB，范围[100,500]；步长：10，默认值为当前实例的数据盘大小，数据盘不支持缩容，因此不允许输入比当前实例数据盘大小的值
        :param Memory: (Optional) 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值为当前实例的内存大小。
        :param NetCapValue: (Optional) 网卡升降级（1，表示升级，2表示降级，0表示不变）
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("ResizeUHostInstance", d)
        return apis.ResizeUHostInstanceResponseSchema().loads(resp)

    def stop_uhost_instance(self, req: dict = None) -> dict:
        """ StopUHostInstance - 指停止处于运行状态的UHost实例，需指定数据中心及UhostID。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StopUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("StopUHostInstance", d)
        return apis.StopUHostInstanceResponseSchema().loads(resp)

    def create_custom_image(self, req: dict = None) -> dict:
        """ CreateCustomImage - 从指定UHost实例，生成自定义镜像。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ImageName: (Required) 镜像名称
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param ImageDescription: (Optional) 镜像描述
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateCustomImageRequestSchema().dumps(d)
        resp = self.invoke("CreateCustomImage", d)
        return apis.CreateCustomImageResponseSchema().loads(resp)

    def describe_uhost_tags(self, req: dict = None) -> dict:
        """ DescribeUHostTags - 获取指定数据中心的业务组列表。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUHostTagsRequestSchema().dumps(d)
        resp = self.invoke("DescribeUHostTags", d)
        return apis.DescribeUHostTagsResponseSchema().loads(resp)

    def import_custom_image(self, req: dict = None) -> dict:
        """ ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Auth: (Required) 是否授权。必须填true
        :param Format: (Required) 镜像格式，可选RAW、VHD、VMDK、qcow2
        :param ImageName: (Required) 镜像名称
        :param OsName: (Required) 操作系统详细版本，请参考控制台的镜像版本；OsType为Other时，输入参数为Other
        :param OsType: (Required) 操作系统平台，比如CentOS、Ubuntu、Windows、RedHat等，请参考控制台的镜像版本；若导入控制台上没有的操作系统，参数为Other
        :param UFileUrl: (Required) UFile私有空间地址
        :param ImageDescription: (Optional) 镜像描述
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ImportCustomImageRequestSchema().dumps(d)
        resp = self.invoke("ImportCustomImage", d)
        return apis.ImportCustomImageResponseSchema().loads(resp)

    def modify_uhost_instance_name(self, req: dict = None) -> dict:
        """ ModifyUHostInstanceName - 修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param Name: (Optional) UHost实例名称
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUHostInstanceNameRequestSchema().dumps(d)
        resp = self.invoke("ModifyUHostInstanceName", d)
        return apis.ModifyUHostInstanceNameResponseSchema().loads(resp)

    def reset_uhost_instance_password(self, req: dict = None) -> dict:
        """ ResetUHostInstancePassword - 重置UHost实例的管理员密码。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Password: (Required) UHost新密码（密码格式使用BASE64编码）
        :param UHostId: (Required) UHost实例ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResetUHostInstancePasswordRequestSchema().dumps(d)
        resp = self.invoke("ResetUHostInstancePassword", d)
        return apis.ResetUHostInstancePasswordResponseSchema().loads(resp)

    def start_uhost_instance(self, req: dict = None) -> dict:
        """ StartUHostInstance - 启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param DiskPassword: (Optional) 加密盘密码
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StartUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("StartUHostInstance", d)
        return apis.StartUHostInstanceResponseSchema().loads(resp)

    def terminate_custom_image(self, req: dict = None) -> dict:
        """ TerminateCustomImage - 删除用户自定义镜像

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ImageId: (Required) 自制镜像ID 参见 [DescribeImage](describe_image.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.TerminateCustomImageRequestSchema().dumps(d)
        resp = self.invoke("TerminateCustomImage", d)
        return apis.TerminateCustomImageResponseSchema().loads(resp)

    def copy_custom_image(self, req: dict = None) -> dict:
        """ CopyCustomImage - 复制自制镜像

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SourceImageId: (Required) 源镜像Id, 参见 DescribeImage
        :param TargetProjectId: (Required) 目标项目Id, 参见 GetProjectList
        :param TargetImageDescription: (Optional) 目标镜像描述
        :param TargetImageName: (Optional) 目标镜像名称
        :param TargetRegion: (Optional) 目标地域，不跨地域不用填
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CopyCustomImageRequestSchema().dumps(d)
        resp = self.invoke("CopyCustomImage", d)
        return apis.CopyCustomImageResponseSchema().loads(resp)

    def describe_image(self, req: dict = None) -> dict:
        """ DescribeImage - 获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ImageId: (Optional) 镜像Id
        :param ImageType: (Optional) 镜像类型。标准镜像：Base，镜像市场：Business， 自定义镜像：Custom，默认返回所有类型
        :param Limit: (Optional) 返回数据长度，默认为20
        :param Offset: (Optional) 列表起始位置偏移量，默认为0
        :param OsType: (Optional) 操作系统类型：Linux， Windows 默认返回所有类型
        :param PriceSet: (Optional) 是否返回价格：1返回，0不返回；默认不返回
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeImageRequestSchema().dumps(d)
        resp = self.invoke("DescribeImage", d)
        return apis.DescribeImageResponseSchema().loads(resp)

    def describe_uhost_instance(self, req: dict = None) -> dict:
        """ DescribeUHostInstance - 获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param IsolationGroup: (Optional) 硬件隔离组id。通过硬件隔离组筛选主机。
        :param LifeCycle: (Optional) 1：普通云主机；2：抢占型云主机；如不传此参数，默认全部获取
        :param Limit: (Optional) 返回数据长度，默认为20，最大100
        :param Offset: (Optional) 列表起始位置偏移量，默认为0
        :param SubnetId: (Optional) 子网id。通过子网筛选主机。北京一地域无效。
        :param Tag: (Optional) 要查询的业务组名称
        :param UHostIds: (Optional) 【数组】UHost主机的资源ID，例如UHostIds.0代表希望获取信息 的主机1，UHostIds.1代表主机2。 如果不传入，则返回当前Region 所有符合条件的UHost实例。
        :param VPCId: (Optional) vpc id。通过VPC筛选主机。北京一地域无效。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUHostInstance", d)
        return apis.DescribeUHostInstanceResponseSchema().loads(resp)

    def get_uhost_instance_price(self, req: dict = None) -> dict:
        """ GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param CPU: (Required) 虚拟CPU核数。可选参数：1-32（可选范围与UHostType相关）。默认值: 4
        :param Count: (Required) 【未启用】购买台数，范围[1,5]
        :param ImageId: (Required) 镜像Id，可通过 [DescribeImage](describe_image.html) 获取镜像ID
        :param Memory: (Required) 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值：8192
        :param ChargeType: (Optional) 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Dynamic，按小时付费 \\ 默认为月付。
        :param DiskSpace: (Optional) 【待废弃】数据盘大小，单位: GB，范围[0,1000]，步长: 10，默认值: 0
        :param Disks: (Optional) Disks
        :param GPU: (Optional) GPU卡核心数。仅GPU机型支持此字段（可选范围与UHostType相关）。
        :param GpuType: (Optional) GPU类型，枚举值["K80", "P40", "V100"]
        :param LifeCycle: (Optional) 【未支持】1：普通云主机；2：抢占性云主机；默认普通
        :param MachineType: (Optional) 云主机类型，枚举值["N", "C", "G", "O"]
        :param NetCapability: (Optional) 网络增强。枚举值：Normal，不开启; Super，开启网络增强1.0; Ultra，开启网络增强2.0； 默认值为Normal。Normal和Ultra不计费。
        :param Quantity: (Optional) 购买时长。默认: 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表了购买至月末。
        :param StorageType: (Optional) 【待废弃】磁盘类型，同时设定系统盘和数据盘， 枚举值为：LocalDisk，本地磁盘; UDisk，云硬盘; 默认为LocalDisk 仅部分可用区支持云硬盘方式的主机存储方式，具体请查询控制台。
        :param TimemachineFeature: (Optional) 【待废弃】方舟机型。No，Yes。默认是No。
        :param UHostType: (Optional) 云主机机型。参考[[api:uhost-api:uhost_type|云主机机型说明]]。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUHostInstancePriceRequestSchema().dumps(d)
        resp = self.invoke("GetUHostInstancePrice", d)
        return apis.GetUHostInstancePriceResponseSchema().loads(resp)

    def modify_uhost_instance_tag(self, req: dict = None) -> dict:
        """ ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param Tag: (Optional) 业务组名称
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUHostInstanceTagRequestSchema().dumps(d)
        resp = self.invoke("ModifyUHostInstanceTag", d)
        return apis.ModifyUHostInstanceTagResponseSchema().loads(resp)

    def reboot_uhost_instance(self, req: dict = None) -> dict:
        """ RebootUHostInstance - 重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param DiskPassword: (Optional) 加密盘密码
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RebootUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("RebootUHostInstance", d)
        return apis.RebootUHostInstanceResponseSchema().loads(resp)

    def resize_attached_disk(self, req: dict = None) -> dict:
        """ ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DiskId: (Required) 磁盘ID。参见 [DescribeUHostInstance](describe_uhost_instance.html)返回值中的DiskSet。
        :param DiskSpace: (Required) 磁盘大小，单位GB，步长为10。取值范围需大于当前磁盘大小，最大值请参考[[api:uhost-api:disk_type|磁盘类型]]。
        :param UHostId: (Required) UHost实例ID。 参见 [DescribeUHostInstance](describe_uhost_instance.html)。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeAttachedDiskRequestSchema().dumps(d)
        resp = self.invoke("ResizeAttachedDisk", d)
        return apis.ResizeAttachedDiskResponseSchema().loads(resp)

    def terminate_uhost_instance(self, req: dict = None) -> dict:
        """ TerminateUHostInstance - 删除指定数据中心的UHost实例。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost资源Id 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param Destroy: (Optional) 是否直接删除，0表示按照原来的逻辑（有回收站权限，则进入回收站），1表示直接删除
        :param ReleaseEIP: (Optional) 是否释放绑定的EIP。true: 解绑EIP后，并释放；其他值或不填：解绑EIP。
        :param ReleaseUDisk: (Optional) 是否删除挂载的数据盘。true删除，其他不删除。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.TerminateUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("TerminateUHostInstance", d)
        return apis.TerminateUHostInstanceResponseSchema().loads(resp)

    def get_uhost_upgrade_price(self, req: dict = None) -> dict:
        """ GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID。 参见 [DescribeUHostInstance](describe_uhost_instance.html)。
        :param BootDiskSpace: (Optional) 【待废弃】系统大小，单位: GB，范围[20,100]，步长: 10。
        :param CPU: (Optional) 虚拟CPU核数。可选参数：1-32（可选范围与UHostType相关）。默认值为当前实例的CPU核数。
        :param DiskSpace: (Optional) 【待废弃】数据盘大小，单位: GB，范围[0,1000]，步长: 10， 默认值是该主机当前数据盘大小。
        :param HostType: (Optional) 【待废弃】主机系列，目前支持N1,N2
        :param Memory: (Optional) 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值为当前实例的内存大小。
        :param NetCapValue: (Optional) 网卡升降级（1，表示升级，2表示降级，0表示不变）
        :param TimemachineFeature: (Optional) 方舟机型。No，Yes。默认是No。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUHostUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("GetUHostUpgradePrice", d)
        return apis.GetUHostUpgradePriceResponseSchema().loads(resp)

    def modify_uhost_instance_remark(self, req: dict = None) -> dict:
        """ ModifyUHostInstanceRemark - 修改指定UHost实例备注信息。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostId: (Required) UHost实例ID 参见 [DescribeUHostInstance](describe_uhost_instance.html)
        :param Remark: (Optional) 备注
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUHostInstanceRemarkRequestSchema().dumps(d)
        resp = self.invoke("ModifyUHostInstanceRemark", d)
        return apis.ModifyUHostInstanceRemarkResponseSchema().loads(resp)

    def upgrade_to_ark_uhost_instance(self, req: dict = None) -> dict:
        """ UpgradeToArkUHostInstance - 普通升级为方舟机型

        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UHostIds: (Required) UHost主机的资源ID，例如UHostIds.0代表希望升级的主机1，UHostIds.1代表主机2。
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param CouponId: (Optional) 代金券ID 请参考DescribeCoupon接口
        """
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.UpgradeToArkUHostInstanceRequestSchema().dumps(d)
        resp = self.invoke("UpgradeToArkUHostInstance", d)
        return apis.UpgradeToArkUHostInstanceResponseSchema().loads(resp)
