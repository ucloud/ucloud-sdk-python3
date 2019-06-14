import typing

from ucloud.core.client import Client
from ucloud.services.unet.schemas import apis


class UNetClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        super(UNetClient, self).__init__(config, transport, middleware)

    def get_e_ip_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetEIPUpgradePrice - 获取弹性IP带宽改动价格

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 弹性IP的外网带宽, 单位为Mbps, 范围 [1-800]
        :param EIPId: (Required) 弹性IP的资源ID
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetEIPUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("GetEIPUpgradePrice", d, **kwargs)
        return apis.GetEIPUpgradePriceResponseSchema().loads(resp)

    def resize_share_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ResizeShareBandwidth - 调整共享带宽的带宽值

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ShareBandwidth: (Required) 带宽值，单位为Mb，范围 [20-5000] (最大值受地域限制)
        :param ShareBandwidthId: (Required) 共享带宽的Id
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeShareBandwidthRequestSchema().dumps(d)

        resp = self.invoke("ResizeShareBandwidth", d, **kwargs)
        return apis.ResizeShareBandwidthResponseSchema().loads(resp)

    def update_firewall_attribute(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ UpdateFirewallAttribute - 更新防火墙规则

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param FWId: (Required) 防火墙资源ID
        :param Name: (Optional) 防火墙名称，默认为空，为空则不做修改。Name,Tag,Remark必须填写1个及以上
        :param Remark: (Optional) 防火墙备注，默认为空，为空则不做修改。Name,Tag,Remark必须填写1个及以上
        :param Tag: (Optional) 防火墙业务组，默认为空，为空则不做修改。Name,Tag,Remark必须填写1个及以上
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateFirewallAttributeRequestSchema().dumps(d)

        resp = self.invoke("UpdateFirewallAttribute", d, **kwargs)
        return apis.UpdateFirewallAttributeResponseSchema().loads(resp)

    def allocate_share_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ AllocateShareBandwidth - 开通共享带宽

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ChargeType: (Required) 付费方式:Year 按年,Month 按月,Dynamic 按时;
        :param Name: (Required) 共享带宽名字
        :param ShareBandwidth: (Required) 共享带宽值
        :param Quantity: (Optional) 购买时长
        :param ShareBandwidthGuarantee: (Optional) 共享带宽保底值(后付费)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateShareBandwidthRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AllocateShareBandwidth", d, **kwargs)
        return apis.AllocateShareBandwidthResponseSchema().loads(resp)

    def get_e_ip_price(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetEIPPrice - 获取弹性IP价格

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 弹性IP的外网带宽, 单位为Mbps, 范围 [0-800]
        :param OperatorName: (Required) 弹性IP的线路如下: 国际: International BGP: Bgp 各地域允许的线路参数如下: cn-sh1: Bgp cn-sh2: Bgp cn-gd: Bgp cn-bj1: Bgp cn-bj2: Bgp hk: International us-ca: International th-bkk: International kr-seoul:International us-ws:International ge-fra:International sg:International tw-kh:International.其他海外线路均为 International,泉州为移动单线cn-qz:ChinaMobile
        :param ChargeType: (Optional) 付费方式, 枚举值为: Year, 按年付费; Month, 按月付费; Dynamic, 按时付费; 默认为获取三种价格
        :param PayMode: (Optional) 弹性IP计费方式r. 枚举值为: Traffic, 流量计费; Bandwidth, 带宽计费; "ShareBandwidth",共享带宽模式. 默认为Bandwidth
        :param Quantity: (Optional) 购买时长。默认: 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表了购买至月末
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetEIPPriceRequestSchema().dumps(d)

        resp = self.invoke("GetEIPPrice", d, **kwargs)
        return apis.GetEIPPriceResponseSchema().loads(resp)

    def release_v_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ReleaseVIP - 释放VIP资源

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param VIPId: (Required) 内网VIP的id
        :param Zone: (Optional) 可用区
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseVIPRequestSchema().dumps(d)

        resp = self.invoke("ReleaseVIP", d, **kwargs)
        return apis.ReleaseVIPResponseSchema().loads(resp)

    def update_firewall(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ UpdateFirewall - 更新防火墙规则

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param FWId: (Required) 防火墙资源ID
        :param Rule: (Required) 防火墙规则，例如：TCP|22|192.168.1.1/22|DROP|LOW|禁用22端口，第一个参数代表协议：第二个参数代表端口号，第三个参数为ip，第四个参数为ACCEPT（接受）和DROP（拒绝），第五个参数优先级：HIGH（高），MEDIUM（中），LOW（低），第六个参数为该条规则的自定义备注
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateFirewallRequestSchema().dumps(d)

        resp = self.invoke("UpdateFirewall", d, **kwargs)
        return apis.UpdateFirewallResponseSchema().loads(resp)

    def describe_v_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeVIP - 获取内网VIP详细信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BusinessId: (Optional) 业务组
        :param SubnetId: (Optional) 子网id，不指定则获取VPCId下的所有vip
        :param Tag: (Optional) 业务组名称, 默认为 Default
        :param VPCId: (Optional) vpc的id,指定SubnetId时必填
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVIPRequestSchema().dumps(d)

        resp = self.invoke("DescribeVIP", d, **kwargs)
        return apis.DescribeVIPResponseSchema().loads(resp)

    def get_e_ip_pay_mode(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetEIPPayMode - 获取弹性IP计费模式

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param EIPId: (Required) 弹性IP的资源Id
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetEIPPayModeRequestSchema().dumps(d)

        resp = self.invoke("GetEIPPayMode", d, **kwargs)
        return apis.GetEIPPayModeResponseSchema().loads(resp)

    def grant_firewall(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GrantFirewall - 将防火墙应用到资源上

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param FWId: (Required) 防火墙资源ID
        :param ResourceId: (Required) 所应用资源ID
        :param ResourceType: (Required) 绑定防火墙组的资源类型，默认为全部资源类型。枚举值为："unatgw"，NAT网关； "uhost"，云主机； "upm"，物理云主机； "hadoophost"，hadoop节点； "fortresshost"，堡垒机； "udhost"，私有专区主机；"udockhost"，容器；"dbaudit"，数据库审计，”uni“，虚拟网卡。
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GrantFirewallRequestSchema().dumps(d)

        resp = self.invoke("GrantFirewall", d, **kwargs)
        return apis.GrantFirewallResponseSchema().loads(resp)

    def allocate_e_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ AllocateEIP - 根据提供信息, 申请弹性IP

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        :param Region: (Config) 地域。
        :param Bandwidth: (Required) 弹性IP的外网带宽, 单位为Mbps. 共享带宽模式必须指定0M带宽, 非共享带宽模式必须指定非0Mbps带宽. 各地域非共享带宽的带宽范围如下： 流量计费[1-200]，带宽计费[1-800]
        :param OperatorName: (Required) 弹性IP的线路如下: 国际: International BGP: Bgp  各地域允许的线路参数如下:  cn-sh1: Bgp cn-sh2: Bgp cn-gd: Bgp cn-bj1: Bgp cn-bj2: Bgp hk: International us-ca: International th-bkk: International  kr-seoul:International  us-ws:International  ge-fra:International  sg:International  tw-kh:International.其他海外线路均为 International
        :param ChargeType: (Optional) 付费方式, 枚举值为: Year, 按年付费; Month, 按月付费; Dynamic, 按需付费(需开启权限); Trial, 试用(需开启权限) 默认为按月付费
        :param CouponId: (Optional) 代金券ID, 默认不使用
        :param Name: (Optional) 弹性IP的名称, 默认为 "EIP"
        :param PayMode: (Optional) 弹性IP的计费模式. 枚举值: "Traffic", 流量计费; "Bandwidth", 带宽计费; "ShareBandwidth",共享带宽模式. 默认为 "Bandwidth".
        :param Quantity: (Optional) 购买时长, 默认: 1
        :param Remark: (Optional) 弹性IP的备注, 默认为空
        :param ShareBandwidthId: (Optional) 绑定的共享带宽Id，仅当PayMode为ShareBandwidth时有效
        :param Tag: (Optional) 业务组名称, 默认为 "Default"
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateEIPRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AllocateEIP", d, **kwargs)
        return apis.AllocateEIPResponseSchema().loads(resp)

    def allocate_v_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ AllocateVIP - 根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域
        :param SubnetId: (Required) 子网id
        :param VPCId: (Required) 指定vip所属的VPC
        :param BusinessId: (Optional) 业务组
        :param Count: (Optional) 申请数量，默认: 1
        :param Name: (Optional) vip名，默认为VIP
        :param Remark: (Optional) 备注
        :param Tag: (Optional) 业务组名称，默认为Default
        :param Zone: (Optional) 可用区
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateVIPRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AllocateVIP", d, **kwargs)
        return apis.AllocateVIPResponseSchema().loads(resp)

    def associate_e_ip_with_share_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ AssociateEIPWithShareBandwidth - 将EIP加入共享带宽

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        :param Region: (Config) 地域。
        :param EIPIds: (Required) 要加入共享带宽的EIP的资源Id
        :param ShareBandwidthId: (Required) 共享带宽ID
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AssociateEIPWithShareBandwidthRequestSchema().dumps(d)

        resp = self.invoke("AssociateEIPWithShareBandwidth", d, **kwargs)
        return apis.AssociateEIPWithShareBandwidthResponseSchema().loads(resp)

    def bind_e_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ BindEIP - 将尚未使用的弹性IP绑定到指定的资源

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param EIPId: (Required) 弹性IP的资源Id
        :param ResourceId: (Required) 弹性IP请求绑定的资源ID
        :param ResourceType: (Required) 弹性IP请求绑定的资源类型, 枚举值为: uhost: 云主机; ulb, 负载均衡器 upm: 物理机; hadoophost: 大数据集群;fortresshost：堡垒机；udockhost：容器；udhost：私有专区主机；natgw：natgw；udb：udb；vpngw：ipsec vpn；ucdr：云灾备；dbaudit：数据库审计；uni：虚拟网卡。
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BindEIPRequestSchema().dumps(d)

        resp = self.invoke("BindEIP", d, **kwargs)
        return apis.BindEIPResponseSchema().loads(resp)

    def describe_share_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeShareBandwidth - 获取共享带宽信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ShareBandwidthIds: (Optional) 需要返回的共享带宽Id
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeShareBandwidthRequestSchema().dumps(d)

        resp = self.invoke("DescribeShareBandwidth", d, **kwargs)
        return apis.DescribeShareBandwidthResponseSchema().loads(resp)

    def set_e_ip_pay_mode(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ SetEIPPayMode - 设置弹性IP计费模式, 切换时会涉及付费/退费.

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 调整的目标带宽值, 单位Mbps. 各地域的带宽值范围如下: 流量计费[1-200],其余情况[1-800]
        :param EIPId: (Required) 弹性IP的资源Id
        :param PayMode: (Required) 计费模式. 枚举值："Traffic", 流量计费模式; "Bandwidth", 带宽计费模式
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.SetEIPPayModeRequestSchema().dumps(d)

        resp = self.invoke("SetEIPPayMode", d, **kwargs)
        return apis.SetEIPPayModeResponseSchema().loads(resp)

    def describe_e_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeEIP - 获取弹性IP信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param EIPIds: (Optional) 弹性IP的资源ID如果为空, 则返回当前 Region中符合条件的的所有EIP
        :param Limit: (Optional) 数据分页值, 默认为20
        :param Offset: (Optional) 数据偏移量, 默认为0
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeEIPRequestSchema().dumps(d)

        resp = self.invoke("DescribeEIP", d, **kwargs)
        return apis.DescribeEIPResponseSchema().loads(resp)

    def describe_firewall(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeFirewall - 获取防火墙组信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param FWId: (Optional) 防火墙ID，默认为返回所有防火墙
        :param Limit: (Optional) 返回数据长度，默认为20，最大10000000
        :param Offset: (Optional) 列表起始位置偏移量，默认为0
        :param ResourceId: (Optional) 绑定防火墙组的资源ID
        :param ResourceType: (Optional) 绑定防火墙组的资源类型，默认为全部资源类型。枚举值为："unatgw"，NAT网关； "uhost"，云主机； "upm"，物理云主机； "hadoophost"，hadoop节点； "fortresshost"，堡垒机； "udhost"，私有专区主机；"udockhost"，容器；"dbaudit"，数据库审计.
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeFirewallRequestSchema().dumps(d)

        resp = self.invoke("DescribeFirewall", d, **kwargs)
        return apis.DescribeFirewallResponseSchema().loads(resp)

    def describe_firewall_resource(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeFirewallResource - 获取防火墙组所绑定资源的外网IP

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param FWId: (Required) 防火墙ID
        :param Limit: (Optional) 返回数据长度，默认为20，最大10000000
        :param Offset: (Optional) 列表起始位置偏移量，默认为0
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeFirewallResourceRequestSchema().dumps(d)

        resp = self.invoke("DescribeFirewallResource", d, **kwargs)
        return apis.DescribeFirewallResourceResponseSchema().loads(resp)

    def modify_e_ip_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ModifyEIPBandwidth - 调整弹性IP的外网带宽

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 弹性IP的外网带宽, 单位为Mbps. 各地域的带宽值范围如下：流量计费[1-200],带宽计费[1-800]
        :param EIPId: (Required) 弹性IP的资源ID
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyEIPBandwidthRequestSchema().dumps(d)

        resp = self.invoke("ModifyEIPBandwidth", d, **kwargs)
        return apis.ModifyEIPBandwidthResponseSchema().loads(resp)

    def release_share_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ReleaseShareBandwidth - 关闭共享带宽

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param EIPBandwidth: (Required) 关闭共享带宽后，各EIP恢复为的带宽值
        :param ShareBandwidthId: (Required) 共享带宽ID
        :param PayMode: (Optional) Bandwidth 带宽计费, Traffic 转流量计费
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseShareBandwidthRequestSchema().dumps(d)

        resp = self.invoke("ReleaseShareBandwidth", d, **kwargs)
        return apis.ReleaseShareBandwidthResponseSchema().loads(resp)

    def update_e_ip_attribute(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ UpdateEIPAttribute - 更新弹性IP名称，业务组，备注等属性字段

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param EIPId: (Required) EIP资源ID
        :param Name: (Optional) 名字（Name Tag Remark都为空则报错）
        :param Remark: (Optional) 备注
        :param Tag: (Optional) 业务
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateEIPAttributeRequestSchema().dumps(d)

        resp = self.invoke("UpdateEIPAttribute", d, **kwargs)
        return apis.UpdateEIPAttributeResponseSchema().loads(resp)

    def disassociate_e_ip_with_share_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DisassociateEIPWithShareBandwidth - 将EIP移出共享带宽

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 移出共享带宽后，EIP的外网带宽, 单位为Mbps. 各地域带宽范围如下：  流量计费[1-200],带宽计费[1-800]
        :param ShareBandwidthId: (Required) 共享带宽ID
        :param EIPIds: (Optional) EIP的资源Id；默认移出该共享带宽下所有的EIP
        :param PayMode: (Optional) 移出共享带宽后，EIP的计费模式. 枚举值: "Traffic", 流量计费; "Bandwidth", 带宽计费;  默认为 "Bandwidth".
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DisassociateEIPWithShareBandwidthRequestSchema().dumps(d)

        resp = self.invoke("DisassociateEIPWithShareBandwidth", d, **kwargs)
        return apis.DisassociateEIPWithShareBandwidthResponseSchema().loads(resp)

    def delete_firewall(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DeleteFirewall - 删除防火墙

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param FWId: (Required) 防火墙资源ID
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteFirewallRequestSchema().dumps(d)

        resp = self.invoke("DeleteFirewall", d, **kwargs)
        return apis.DeleteFirewallResponseSchema().loads(resp)

    def describe_bandwidth_package(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeBandwidthPackage - 获取某地域下的带宽包信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Optional) 返回数据分页值, 取值范围为 [0,10000000] 之间的整数, 默认为20
        :param Offset: (Optional) 返回数据偏移量, 默认为0
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeBandwidthPackageRequestSchema().dumps(d)

        resp = self.invoke("DescribeBandwidthPackage", d, **kwargs)
        return apis.DescribeBandwidthPackageResponseSchema().loads(resp)

    def release_e_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ReleaseEIP - 释放弹性IP资源, 所释放弹性IP必须为非绑定状态.

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param EIPId: (Required) 弹性IP的资源ID
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseEIPRequestSchema().dumps(d)

        resp = self.invoke("ReleaseEIP", d, **kwargs)
        return apis.ReleaseEIPResponseSchema().loads(resp)

    def un_bind_e_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ UnBindEIP - 将弹性IP从资源上解绑

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param EIPId: (Required) 弹性IP的资源Id
        :param ResourceId: (Required) 弹性IP请求解绑的资源ID
        :param ResourceType: (Required) 弹性IP请求解绑的资源类型, 枚举值为: uhost: 云主机; ulb, 负载均衡器 upm: 物理机; hadoophost: 大数据集群;fortresshost：堡垒机；udockhost：容器；udhost：私有专区主机；natgw：NAT网关；udb：udb；vpngw：ipsec vpn；ucdr：云灾备；dbaudit：数据库审计；uni，虚拟网卡。
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UnBindEIPRequestSchema().dumps(d)

        resp = self.invoke("UnBindEIP", d, **kwargs)
        return apis.UnBindEIPResponseSchema().loads(resp)

    def create_bandwidth_package(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CreateBandwidthPackage - 为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        :param Region: (Config) 地域
        :param Bandwidth: (Required) 带宽大小(单位Mbps), 取值范围[2,800] (最大值受地域限制)
        :param EIPId: (Required) 所绑定弹性IP的资源ID
        :param TimeRange: (Required) 带宽包有效时长, 取值范围为大于0的整数, 即该带宽包在EnableTime到 EnableTime+TimeRange时间段内生效
        :param CouponId: (Optional) 代金券ID
        :param EnableTime: (Optional) 生效时间, 格式为 Unix timestamp, 默认为立即开通
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateBandwidthPackageRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateBandwidthPackage", d, **kwargs)
        return apis.CreateBandwidthPackageResponseSchema().loads(resp)

    def create_firewall(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateFirewall - 创建防火墙

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param Name: (Required) 防火墙名称
        :param Rule: (Required) 防火墙规则，例如：TCP|22|192.168.1.1/22|DROP|LOW|禁用22端口，第一个参数代表协议：第二个参数代表端口号，第三个参数为ip，第四个参数为ACCEPT（接受）和DROP（拒绝），第五个参数优先级：HIGH（高），MEDIUM（中），LOW（低），第六个参数为该条规则的自定义备注
        :param Remark: (Optional) 防火墙描述，默认为空
        :param Tag: (Optional) 防火墙业务组，默认为Default
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateFirewallRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateFirewall", d, **kwargs)
        return apis.CreateFirewallResponseSchema().loads(resp)

    def delete_bandwidth_package(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DeleteBandwidthPackage - 删除弹性IP上已附加带宽包

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写
        :param Region: (Config) 地域
        :param BandwidthPackageId: (Required) 带宽包资源ID
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteBandwidthPackageRequestSchema().dumps(d)

        resp = self.invoke("DeleteBandwidthPackage", d, **kwargs)
        return apis.DeleteBandwidthPackageResponseSchema().loads(resp)

    def describe_bandwidth_usage(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeBandwidthUsage - 获取带宽用量信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param EIPIds: (Optional) 弹性IP的资源Id. 如果为空, 则返回当前 Region中符合条件的所有EIP的带宽用量, n为自然数
        :param Limit: (Optional) 返回数据分页值, 取值范围为 [0,10000000] 之间的整数, 默认为20
        :param OffSet: (Optional) 返回数据偏移量, 默认为0
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeBandwidthUsageRequestSchema().dumps(d)

        resp = self.invoke("DescribeBandwidthUsage", d, **kwargs)
        return apis.DescribeBandwidthUsageResponseSchema().loads(resp)

    def modify_e_ip_weight(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ModifyEIPWeight - 修改弹性IP的外网出口权重

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param EIPId: (Required) 弹性IP的资源ID
        :param Weight: (Required) 外网出口权重, 范围[0-100] 取值为0时, 该弹性IP不会被使用. 取值为100时, 同主机下只会使用这个弹性IP，其他弹性IP不会被使用 请勿将多个绑定在同一资源的弹性IP设置为相同权重
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyEIPWeightRequestSchema().dumps(d)

        resp = self.invoke("ModifyEIPWeight", d, **kwargs)
        return apis.ModifyEIPWeightResponseSchema().loads(resp)
