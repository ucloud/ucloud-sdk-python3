""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.ucompshare.schemas import apis


class UCompShareClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UCompShareClient, self).__init__(
            config, transport, middleware, logger
        )

    def create_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateULHostInstance - 创建轻量应用云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BundleId** (str) - (Required) 套餐ID。如："ulh.c1m1s40b30t800"
        - **ImageId** (str) - (Required) 镜像ID。 请通过  `DescribeImage <https://docs.ucloud.cn/api/ucompshare-api/describe_image.html>`_ 获取
        - **Password** (str) - (Required) ULHost密码。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定密码。密码需使用base64进行编码，举例如下：# echo -n Password1 | base64
        - **ChargeType** (str) - 计费模式。枚举值： \\ > Year，按年付费； \\ > Month，按月付费；默认：Month
        - **CouponId** (str) - 主机代金券ID。请通过DescribeCoupon接口查询，或登录用户中心查看
        - **Name** (str) - 轻量应用主机名称。默认：套餐ID。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定实例名称。
        - **Quantity** (int) - 购买时长。默认：1。不支持购买到月末

        **Response**

        - **Message** (str) - 错误信息
        - **ULHostId** (str) - 实例ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateULHostInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateULHostInstance", d, **kwargs)
        return apis.CreateULHostInstanceResponseSchema().loads(resp)

    def describe_ul_host_bundles(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeULHostBundles - 获取轻量应用云主机套餐列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Bundles** (list) - 见 **Bundle** 模型定义
        - **Message** (str) - 错误信息

        **Response Model**

        **Bundle**
        - **Bandwidth** (int) - 外网带宽。单位：Mbps。
        - **BundleId** (str) - 套餐ID。
        - **CPU** (int) - CPU核数。
        - **Memory** (int) - 内存大小。单位：MB。
        - **SysDiskSpace** (int) - 系统盘大小。单位：GB。
        - **TrafficPacket** (int) - 流量包大小。单位：GB。


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeULHostBundlesRequestSchema().dumps(d)

        resp = self.invoke("DescribeULHostBundles", d, **kwargs)
        return apis.DescribeULHostBundlesResponseSchema().loads(resp)

    def describe_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeULHostInstance - 获取轻量应用云主机列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Limit** (int) - 返回数据长度，默认为20，最大100
        - **Offset** (int) - 列表起始位置偏移量，默认为0
        - **ULHostIds** (list) - 【数组】轻量应用云主机ID。

        **Response**

        - **Message** (str) - 错误信息
        - **ULHostInstanceSets** (list) - 见 **ULHostInstanceSet** 模型定义

        **Response Model**

        **ULHostInstanceSet**
        - **Apps** (list) - 【数组】镜像包含的应用列表。
        - **AutoRenew** (str) - 是否自动续费。枚举值：Yes/No
        - **CPU** (int) - CPU核数。
        - **ChargeType** (str) - 计费模式。枚举值：Month/Year
        - **CreateTime** (int) - 创建时间。Unix时间戳
        - **DiskSet** (list) - 见 **ULHostDiskSet** 模型定义
        - **ExpireTime** (int) - 过期时间。Unix时间戳
        - **IPSet** (list) - 见 **UHostIPSet** 模型定义
        - **ImageId** (str) - 镜像Id。
        - **ImageName** (str) - 镜像名称。
        - **IsExpire** (str) - 是否过期。枚举值：Yes/No
        - **Memory** (int) - 内存。单位：MB
        - **Name** (str) - 实例名称。默认套餐Id
        - **Remark** (str) - 备注。
        - **State** (str) - 实例状态。枚举值：\\ >初始化: Initializing; \\ >启动中: Starting; \\> 运行中: Running; \\> 关机中: Stopping; \\ >关机: Stopped \\ >安装失败: Install Fail; \\ >重启中: Rebooting; \\ > 未知(空字符串，获取状态超时或出错)：""
        - **Tag** (str) - 业务组。
        - **ULHostId** (str) - 实例Id。
        - **Zone** (str) - 可用区。


        **ULHostDiskSet**
        - **DiskId** (str) - 磁盘Id
        - **DiskType** (str) - 磁盘类型。如："CLOUD_RSSD"、"CLOUD_SSD"
        - **Drive** (str) - 磁盘盘符。系统盘："vda"
        - **IsBoot** (str) - 是否为系统盘。是："True"；否："False"
        - **Size** (int) - 磁盘大小。单位：GB
        - **Type** (str) - 磁盘类型。系统盘："Boot"；数据盘："Data"


        **UHostIPSet**
        - **Bandwidth** (int) - IP对应的带宽, 单位: Mb  (内网IP不显示带宽信息)
        - **Default** (str) - 内网 Private 类型下，表示是否为默认网卡。true: 是默认网卡；其他值：不是。
        - **IP** (str) - IP地址
        - **IPId** (str) - 外网IP资源ID 。(内网IP无对应的资源ID)
        - **IPMode** (str) - IPv4/IPv6；
        - **Mac** (str) - 内网 Private 类型下，当前网卡的Mac。
        - **NetworkInterfaceId** (str) - 弹性网卡为默认网卡时，返回对应的 ID 值
        - **SubnetId** (str) - IP地址对应的子网 ID。（北京一不支持，字段返回为空）
        - **Type** (str) - 国际: Internation，BGP: Bgp，内网: Private
        - **VPCId** (str) - IP地址对应的VPC ID。（北京一不支持，字段返回为空）
        - **Weight** (int) - 当前EIP的权重。权重最大的为当前的出口IP。


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeULHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("DescribeULHostInstance", d, **kwargs)
        return apis.DescribeULHostInstanceResponseSchema().loads(resp)

    def get_ul_host_instance_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetULHostInstancePrice - 获取轻量应用云主机套餐价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BundleId** (str) - (Required) 套餐ID
        - **ChargeType** (str) - 获取指定计费模式的价格。枚举值：\\ > Year，按年付费； \\ > Month。未指定时，返回所有计费模式价格
        - **Count** (int) - 购买台数，范围[1,5]。默认：1
        - **Quantity** (int) - 购买时长。默认: 1。不支持购买到月末

        **Response**

        - **Message** (str) - 错误信息
        - **PriceSet** (list) - 见 **ULHostPriceSet** 模型定义

        **Response Model**

        **ULHostPriceSet**
        - **ChargeType** (str) - 计费模式
        - **OriginalPrice** (float) - 原价
        - **Price** (float) - 价格


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetULHostInstancePriceRequestSchema().dumps(d)

        resp = self.invoke("GetULHostInstancePrice", d, **kwargs)
        return apis.GetULHostInstancePriceResponseSchema().loads(resp)

    def get_ul_host_renew_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetULHostRenewPrice - 获取主机续费价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ULHostId** (str) - (Required) ULHost实例ID
        - **ChargeType** (str) - 计费类型。支持：Year/Month；默认：Month

        **Response**

        - **PriceSet** (list) - 见 **ULHostPriceSet** 模型定义

        **Response Model**

        **ULHostPriceSet**
        - **ChargeType** (str) - 计费模式
        - **OriginalPrice** (float) - 原价
        - **Price** (float) - 价格


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetULHostRenewPriceRequestSchema().dumps(d)

        resp = self.invoke("GetULHostRenewPrice", d, **kwargs)
        return apis.GetULHostRenewPriceResponseSchema().loads(resp)

    def modify_ul_host_attribute(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyULHostAttribute - 修改指定ULHost实例属性信息，包含名称和备注

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ULHostId** (str) - (Required) ULHost实例Id
        - **Name** (str) - 名称。和Remark至少选择一个进行修改
        - **Remark** (str) - 备注。和Name至少选择一个进行修改

        **Response**

        - **Message** (str) - 错误信息
        - **ULHostId** (str) - ULHost实例Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyULHostAttributeRequestSchema().dumps(d)

        resp = self.invoke("ModifyULHostAttribute", d, **kwargs)
        return apis.ModifyULHostAttributeResponseSchema().loads(resp)

    def poweroff_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """PoweroffULHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ULHostId** (str) - (Required) ULHost实例ID

        **Response**

        - **ULHostId** (str) - ULHost实例ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.PoweroffULHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("PoweroffULHostInstance", d, **kwargs)
        return apis.PoweroffULHostInstanceResponseSchema().loads(resp)

    def reboot_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RebootULHostInstance - 重新启动UHost实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ULHostId** (str) - (Required) ULHost实例ID

        **Response**

        - **ULHostId** (str) - ULHost实例ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RebootULHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("RebootULHostInstance", d, **kwargs)
        return apis.RebootULHostInstanceResponseSchema().loads(resp)

    def reinstall_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ReinstallULHostInstance - 重装轻量应用云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ImageId** (str) - (Required) 镜像Id。暂不支持使用自定义镜像重装
        - **Password** (str) - (Required) 登陆密码
        - **ULHostId** (str) - (Required) 实例Id

        **Response**

        - **Message** (str) - 错误信息
        - **ULHostId** (str) - 实例Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ReinstallULHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("ReinstallULHostInstance", d, **kwargs)
        return apis.ReinstallULHostInstanceResponseSchema().loads(resp)

    def reset_ul_host_instance_password(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ResetULHostInstancePassword - 重置轻量应用云主机管理员密码。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Password** (str) - (Required) ULHost新密码（密码格式使用BASE64编码）
        - **ULHostId** (str) - (Required) ULHost实例ID

        **Response**

        - **ULHostId** (str) - ULHost实例ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ResetULHostInstancePasswordRequestSchema().dumps(d)

        resp = self.invoke("ResetULHostInstancePassword", d, **kwargs)
        return apis.ResetULHostInstancePasswordResponseSchema().loads(resp)

    def start_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """StartULHostInstance - 启动处于关闭状态的UHost实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ULHostId** (str) - (Required) ULHost实例ID

        **Response**

        - **ULHostId** (str) - ULHost实例ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.StartULHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("StartULHostInstance", d, **kwargs)
        return apis.StartULHostInstanceResponseSchema().loads(resp)

    def stop_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """StopULHostInstance - 指停止处于运行状态的ULHost实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ULHostId** (str) - (Required) ULHost实例ID。

        **Response**

        - **ULHostId** (str) - ULHost实例ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.StopULHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("StopULHostInstance", d, **kwargs)
        return apis.StopULHostInstanceResponseSchema().loads(resp)

    def terminate_ul_host_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """TerminateULHostInstance - 删除指定数据中心的ULHost实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ULHostId** (str) - (Required) ULHost资源Id
        - **ReleaseUDisk** (bool) - 删除主机时是否同时删除挂载的数据盘。默认为false。

        **Response**

        - **InRecycle** (str) - 用于判断主机删除时是否进入回收站。放入回收站:"Yes", 彻底删除：“No”。
        - **ULHostId** (str) - ULHost 实例 Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.TerminateULHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("TerminateULHostInstance", d, **kwargs)
        return apis.TerminateULHostInstanceResponseSchema().loads(resp)
