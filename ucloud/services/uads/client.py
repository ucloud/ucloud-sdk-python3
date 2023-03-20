""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.uads.schemas import apis


class UADSClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UADSClient, self).__init__(config, transport, middleware, logger)

    def add_high_protect_game_ip_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """AddHighProtectGameIPInfo - 添加代理ip

        **Request**

        - **LineType** (str) - (Required) 套餐线路类型, 如果是BGP的线路, 则为BGP;如果为双线, 则可选TELECOM, UNICOM;如果为海外, 则为INTERNATIONAL;
        - **ResourceId** (str) - (Required) 资源Id
        - **TypeIP** (str) - (Required) IP类型,取值范围为:TypeFree,  TypeCharge
        - **UserIP** (str) - (Required) 用户的源站ip
        - **CouponId** (str) - 代金券ID
        - **Remark** (str) - 备注,默认为空.

        **Response**

        - **Cname** (str) - cname记录
        - **DefenceIP** (str) - 防御IP
        - **IPId** (int) - IPId
        - **SrcIP** (str) - 源IP

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.AddHighProtectGameIPInfoRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AddHighProtectGameIPInfo", d, **kwargs)
        return apis.AddHighProtectGameIPInfoResponseSchema().loads(resp)

    def add_nap_allow_list_domain(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """AddNapAllowListDomain - 添加域名允许列表

        **Request**

        - **Domain** (list) - (Required) 域名，N从0开始，多个域名：Domain.0、Domain.1、...
        - **ResourceId** (str) - (Required) 资源ID

        **Response**

        - **Data** (list) - 见 **DomainConfigResult** 模型定义

        **Response Model**

        **DomainConfigResult**
        - **Code** (int) - 错误码
        - **Domain** (str) - 域名
        - **Message** (str) - 提示信息


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.AddNapAllowListDomainRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AddNapAllowListDomain", d, **kwargs)
        return apis.AddNapAllowListDomainResponseSchema().loads(resp)

    def bind_nap_ip(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """BindNapIP - 直连高防：将尚未使用的高防EIP绑定到指定的资源

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **BindResourceId** (str) - (Required) 绑定的资源ID
        - **EIPId** (str) - (Required) EIP资源ID
        - **NapIp** (str) - (Required) 高防IP
        - **ResourceId** (str) - (Required) 高防资源ID
        - **ResourceType** (str) - (Required) 绑定的资源类型(uhost:云主机,ulb:负载均衡,upm:物理机)

        **Response**

        - **Message** (str) - 错误信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.BindNapIPRequestSchema().dumps(d)

        resp = self.invoke("BindNapIP", d, **kwargs)
        return apis.BindNapIPResponseSchema().loads(resp)

    def buy_high_protect_game_service(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """BuyHighProtectGameService - 购买高防服务

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **AreaLine** (str) - (Required) 线路区域, 可取范围{"SouthChina",   "EastChina"}
        - **ChargeType** (str) - (Required) 计费方式 ,取值范围 {"Month",  "Year", "Dynamic", "Day"};其中华东双线周付使用Day,其他支持的周付使用Dynamic;
        - **EngineRoom** (list) - (Required) 购买的套餐所在机房，取值范围{"Hangzhou2",  "Hangzhou", "Xiamen"}
        - **LineType** (str) - (Required) 'default': 'DUPLET',  取值范围 {"DUPLET", "BGP"}
        - **Quantity** (int) - (Required) 计费时长
        - **SrcBandwidth** (int) - (Required) 带宽
        - **AccessMode** (str) - 接入模式，默认为：IP；Domain：网站接入、IP：非网站接入
        - **CouponId** (str) - 代金券ID
        - **DefenceDDosBaseFlowArr** (list) - DDoS基础防护值（当购买套餐为多种线路的时候，顺序为，电信，联通，移动...，当为单线的时候只传DefenceDDosBaseFlowArr.0）
        - **DefenceDDosMaxFlowArr** (list) - DDoS最大防护值（当购买套餐为多种线路的时候，顺序为，电信，联通，移动...；当为单线的时候只传DefenceDDosMaxFlowArr.0）
        - **DefenceType** (str) - 防御类型，默认为TypeFixed; 取值范围{"TypeFixed",  "TypeDynamic"}
        - **ForwardType** (str) - 转发类型，默认为：Proxy；Proxy：代理、Passthrough：直连
        - **HighProtectGameServiceName** (str) - 高防服务名称
        - **Vendor** (int) - 供应商编号

        **Response**

        - **ResourceInfo** (dict) - 见 **ResourceInfo** 模型定义

        **Response Model**

        **ResourceInfo**
        - **ResourceId** (str) - 资源id


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.BuyHighProtectGameServiceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("BuyHighProtectGameService", d, **kwargs)
        return apis.BuyHighProtectGameServiceResponseSchema().loads(resp)

    def create_bgp_service_fwd_rule(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateBGPServiceFwdRule - 创建BGP高防转发规则

        **Request**

        - **BgpIP** (str) - (Required) BGP的IP
        - **ResourceId** (str) - (Required) 资源id
        - **BackupIP** (str) - 备份源站的IP
        - **BackupPort** (int) - 备份源站的端口
        - **BgpIPPort** (int) - 默认为0，为IP协议的转发端口，其余的自定义
        - **FwdType** (str) - 转发协议的类型包括三种：默认为“IP”，还可以选择为“TCP”
        - **LoadBalance** (str) - 转发协议的类型是否为负载均衡的：默认为“No”，还可以选择为“Yes”。负载均衡模式下必须配置BackupIP
        - **Remark** (str) - 备注，默认为空
        - **SourceAddrArr** (list) - 回源地址，可填 IP地址 或 域名
        - **SourceDetect** (int) - 表示对源站进行检测：默认为0表示关闭，还可以选择为1表示开启
        - **SourcePortArr** (list) - 回源端口
        - **SourceToaIDArr** (list) - 回源TOA
        - **SourceType** (str) - 回源类型，分 “IP”、“Domain”

        **Response**

        - **RuleIndex** (int) - 转发规则的数据库索引值

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.CreateBGPServiceFwdRuleRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateBGPServiceFwdRule", d, **kwargs)
        return apis.CreateBGPServiceFwdRuleResponseSchema().loads(resp)

    def create_bgp_service_ip(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateBGPServiceIP - 分配一个BGP IP

        **Request**

        - **ResourceId** (str) - (Required) 资源id，表示归属在哪个高防服务下
        - **EIPRegion** (str) - 高防IP对应机房（直连高防必须携带）
        - **Remark** (str) - 备注,默认为空
        - **TypeIP** (str) - ip的类型, 默认是TypeFree

        **Response**

        - **Cname** (str) - cname记录
        - **DefenceIP** (str) - 分配的BGP高防IP的IP地址
        - **EnableSwitch** (int) - 是否热备份开启
        - **IPId** (int) - IPId

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.CreateBGPServiceIPRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateBGPServiceIP", d, **kwargs)
        return apis.CreateBGPServiceIPResponseSchema().loads(resp)

    def delete_bgp_service_fwd_rule(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteBGPServiceFwdRule - 删除转发规则

        **Request**

        - **ResourceId** (str) - (Required) 资源id
        - **RuleIndex** (int) - (Required) 需要删除的转发规则ID

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DeleteBGPServiceFwdRuleRequestSchema().dumps(d)

        resp = self.invoke("DeleteBGPServiceFwdRule", d, **kwargs)
        return apis.DeleteBGPServiceFwdRuleResponseSchema().loads(resp)

    def delete_bgp_service_ip(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteBGPServiceIP - 删除BGP高防IP

        **Request**

        - **Region** (str) - (Config) 机房(直接模式高防需要传)
        - **DefenceIp** (str) - (Required) 需要删除的高防IP
        - **ResourceId** (str) - (Required) 资源id

        **Response**


        """
        # build request
        d = {
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteBGPServiceIPRequestSchema().dumps(d)

        resp = self.invoke("DeleteBGPServiceIP", d, **kwargs)
        return apis.DeleteBGPServiceIPResponseSchema().loads(resp)

    def delete_high_protect_game_ip_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteHighProtectGameIPInfo - 删除高防IP

        **Request**

        - **DefenceIp** (str) - (Required) 要删除的高防ip
        - **ResourceId** (str) - (Required) 资源ID

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DeleteHighProtectGameIPInfoRequestSchema().dumps(d)

        resp = self.invoke("DeleteHighProtectGameIPInfo", d, **kwargs)
        return apis.DeleteHighProtectGameIPInfoResponseSchema().loads(resp)

    def delete_high_protect_game_service(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteHighProtectGameService - 删除高防

        **Request**

        - **ResourceId** (str) - (Required) 删除的资源Id

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DeleteHighProtectGameServiceRequestSchema().dumps(d)

        resp = self.invoke("DeleteHighProtectGameService", d, **kwargs)
        return apis.DeleteHighProtectGameServiceResponseSchema().loads(resp)

    def delete_nap_allow_list_domain(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteNapAllowListDomain - 删除域名允许列表

        **Request**

        - **Domain** (list) - (Required) 域名，N从0开始，多个域名：Domain.0、Domain.1、...
        - **ResourceId** (str) - (Required) 资源ID

        **Response**

        - **Data** (list) - 见 **DomainConfigResult** 模型定义

        **Response Model**

        **DomainConfigResult**
        - **Code** (int) - 错误码
        - **Domain** (str) - 域名
        - **Message** (str) - 提示信息


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DeleteNapAllowListDomainRequestSchema().dumps(d)

        resp = self.invoke("DeleteNapAllowListDomain", d, **kwargs)
        return apis.DeleteNapAllowListDomainResponseSchema().loads(resp)

    def describe_buy_high_protect_game_ip_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeBuyHighProtectGameIPPrice - 获取购买IP的价格

        **Request**

        - **ChargeType** (str) - (Required) 付费方式, 枚举值为: Year, 按年付费; Month, 按月付费; Dynamic, 按需付费(需开启权限); Trial
        - **Quantity** (int) - (Required) 购买数量
        - **ResourceId** (str) - (Required) 资源ID

        **Response**

        - **PremiumPrice** (float) - 溢价
        - **UnitPrice** (float) - 单位价格

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DescribeBuyHighProtectGameIPPriceRequestSchema().dumps(d)

        resp = self.invoke("DescribeBuyHighProtectGameIPPrice", d, **kwargs)
        return apis.DescribeBuyHighProtectGameIPPriceResponseSchema().loads(
            resp
        )

    def describe_high_protect_game_ip_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeHighProtectGameIPInfo - 获取高防IP信息

        **Request**

        - **ResourceId** (str) - (Required) 资源短id
        - **Limit** (int) - 返回数据长度，默认为50。
        - **Offset** (int) - 列表起始位置偏移量，默认为0。

        **Response**

        - **AvailableIPQuota** (int) - 可用剩余ip配额数
        - **GameIPInfo** (list) - 见 **GameIpInfoTotal** 模型定义
        - **TotalCount** (int) - 已经配置的总数

        **Response Model**

        **GameIpInfoTotal**
        - **Cname** (str) - 高防IP Cname
        - **DefenceIP** (str) - 高防IP
        - **LineType** (str) - 线路类型
        - **Remark** (str) - 用户mark
        - **RuleCnt** (int) - 规则的个数
        - **SrcIP** (list) - 回源ip列表
        - **Status** (str) - ip配置状态


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DescribeHighProtectGameIPInfoRequestSchema().dumps(d)

        resp = self.invoke("DescribeHighProtectGameIPInfo", d, **kwargs)
        return apis.DescribeHighProtectGameIPInfoResponseSchema().loads(resp)

    def describe_nap_history_statistic(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeNapHistoryStatistic - 获取高防历史统计

        **Request**

        - **BeginTime** (int) - (Required) 开始时间，Unix时间戳
        - **EndTime** (int) - (Required) 结束时间，Unix时间戳
        - **ResourceId** (str) - (Required) 资源ID
        - **Accuracy** (int) - 查询粒度。1.分钟粒度 2.小时粒度 3.天粒度 默认为21.分钟粒度，BeginTime开始时间是7天内，EndTime-BeginTime时间跨度最大是1小时2.小时粒度，BeginTime开始时间是30天内，EndTime-BeginTime时间跨度最大是7天3.天粒度，BeginTime开始时间是180天内，EndTime-BeginTime时间跨度最大是90天
        - **Limit** (int) - 返回数据长度，默认不限制
        - **NapIP** (str) - 高防IP
        - **Offset** (int) - 列表起始位置偏移量，默认为0

        **Response**

        - **NetStats** (list) - 见 **NetStats** 模型定义

        **Response Model**

        **NetStatEntry**
        - **Bps** (float) - 流量，单位：Mbits
        - **Pps** (int) - 包量，单位：pps


        **NetStats**
        - **Drop** (dict) - 见 **NetStatEntry** 模型定义
        - **Egress** (dict) - 见 **NetStatEntry** 模型定义
        - **Ingress** (dict) - 见 **NetStatEntry** 模型定义
        - **Time** (int) - Unix时间戳


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DescribeNapHistoryStatisticRequestSchema().dumps(d)

        resp = self.invoke("DescribeNapHistoryStatistic", d, **kwargs)
        return apis.DescribeNapHistoryStatisticResponseSchema().loads(resp)

    def describe_nap_real_time_statistic(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeNapRealTimeStatistic - 获取高防实时统计

        **Request**

        - **BeginTime** (int) - (Required) 开始时间，Unix时间戳
        - **EndTime** (int) - (Required) 结束时间，Unix时间戳（时间跨度不超过1小时）
        - **ResourceId** (str) - (Required) 资源ID
        - **Limit** (int) - 返回数据长度，默认不限制
        - **NapIP** (str) - 高防IP
        - **Offset** (int) - 列表起始位置偏移量，默认为0

        **Response**

        - **NetStats** (list) - 见 **NetStats** 模型定义

        **Response Model**

        **NetStatEntry**
        - **Bps** (float) - 流量，单位：Mbits
        - **Pps** (int) - 包量，单位：pps


        **NetStats**
        - **Drop** (dict) - 见 **NetStatEntry** 模型定义
        - **Egress** (dict) - 见 **NetStatEntry** 模型定义
        - **Ingress** (dict) - 见 **NetStatEntry** 模型定义
        - **Time** (int) - Unix时间戳


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DescribeNapRealTimeStatisticRequestSchema().dumps(d)

        resp = self.invoke("DescribeNapRealTimeStatistic", d, **kwargs)
        return apis.DescribeNapRealTimeStatisticResponseSchema().loads(resp)

    def describe_nap_service_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeNapServiceInfo - 获取高防服务信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Limit** (int) - 返回数据长度，默认为10
        - **NapType** (int) - 高防类型；0：全部、1：内地高防、2：海外高防
        - **Offset** (int) - 列表起始位置偏移量，默认为0
        - **ResourceId** (str) - 资源ID

        **Response**

        - **ServiceInfo** (list) - 见 **ServiceInfo** 模型定义
        - **TotalCount** (int) - 总数

        **Response Model**

        **ServiceInfo**
        - **AccessMode** (str) - 接入模式，Domain：网站接入、IP：非网站接入
        - **AreaLine** (str) - 防护机房所在区域
        - **AutoRenew** (str) - 是否开启自动续费
        - **ChargeType** (str) - 付费类型
        - **CreateTime** (int) - 创建时间
        - **DefenceDDosBaseFlowArr** (list) - 套餐基础防护组
        - **DefenceDDosMaxFlowArr** (list) - 套餐最大防护组
        - **DefenceStatus** (str) - 防护状态，Started：正常、Stopped：关闭、Expired：过期
        - **DefenceType** (str) - 防护类型
        - **EngineRoom** (list) - 防护机房名称
        - **ExpiredTime** (int) - 过期时间
        - **ForwardType** (str) - 转发类型，Proxy：代理、Passthrough：直连
        - **GameId** (int) - 套餐ID
        - **LineType** (str) - 线路类型
        - **Name** (str) - 套餐名称
        - **NapType** (int) - 高防类型，1：内地高防、2：海外高防
        - **ProjectId** (str) - 项目ID
        - **RegionId** (int) - region id
        - **ResourceId** (str) - 资源ID
        - **SrcBandwidth** (int) - 业务带宽
        - **Vendor** (int) - 供应商ID


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DescribeNapServiceInfoRequestSchema().dumps(d)

        resp = self.invoke("DescribeNapServiceInfo", d, **kwargs)
        return apis.DescribeNapServiceInfoResponseSchema().loads(resp)

    def describe_passthrough_nap_ip(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePassthroughNapIP - 获取直连高防IP信息

        **Request**

        - **ResourceId** (str) - (Required) 高防资源ID
        - **Limit** (int) - 限制(传EIPs.0时暂时无效)
        - **NapIp** (str) - 高防IP
        - **Offset** (int) - 位偏移(传EIPs.0时暂时无效)

        **Response**

        - **AvailableIPQuota** (int) - 合法IP配额
        - **IPInfo** (list) - 见 **IPInfo** 模型定义
        - **Message** (str) - 错误信息
        - **TotalCount** (int) - IP总个数

        **Response Model**

        **EIPAddrSet**
        - **EIPType** (str) - IP类型：gaofang
        - **IP** (str) - 弹性IP地址
        - **OperatorName** (str) - 运营商信息, 枚举值为:  BGP: BGP; International: 国际.


        **Resouce**
        - **EIPId** (str) - EIP资源ID
        - **ResourceId** (str) - 资源ID
        - **ResourceName** (str) - 资源名
        - **ResourceType** (str) - 资源类型
        - **Zone** (str) - 地区


        **IPInfo**
        - **CreateTime** (int) - 创建时间
        - **EIPAddr** (list) - 见 **EIPAddrSet** 模型定义
        - **EIPId** (str) - EIP资源ID
        - **EIPRegion** (str) - EIP Region
        - **Resource** (dict) - 见 **Resouce** 模型定义
        - **Status** (str) - 状态
        - **Tag** (str) - 业务组


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DescribePassthroughNapIPRequestSchema().dumps(d)

        resp = self.invoke("DescribePassthroughNapIP", d, **kwargs)
        return apis.DescribePassthroughNapIPResponseSchema().loads(resp)

    def describe_upgrade_high_protect_game_service_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUpgradeHighProtectGameServicePrice - 获取高防升降级价格

        **Request**

        - **ResourceId** (str) - (Required) 资源ID
        - **AreaLine** (str) - 区域，华东和华南，EastChina 和SouthChina
        - **DefenceDDosBaseFlowArr** (list) - DDoS弹性防护值
        - **DefenceDDosMaxFlowArr** (list) - DDoS基础防护值
        - **DefenceType** (str) - 防御类型，默认为TypeFixed
        - **EngineRoom** (list) - 代表机房，例如Dongguan  Hangzhou
        - **LineType** (str) - 线路
        - **SrcBandwidth** (int) - 带宽，默认100M

        **Response**

        - **ChargeIPQuota** (int) - 收费IP配额
        - **FreeIPQuota** (int) - 免费IP配额
        - **Price** (int) - 价格

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.DescribeUpgradeHighProtectGameServicePriceRequestSchema().dumps(
            d
        )

        resp = self.invoke(
            "DescribeUpgradeHighProtectGameServicePrice", d, **kwargs
        )
        return apis.DescribeUpgradeHighProtectGameServicePriceResponseSchema().loads(
            resp
        )

    def get_bgp_service_fwd_rule(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetBGPServiceFwdRule - 获取转发规则

        **Request**

        - **ResourceId** (str) - (Required) 资源id
        - **BgpIP** (str) - 指定需要查询的IP下的规则
        - **Limit** (int) - 分页显示的条目数，默认值为32
        - **Offset** (int) - 分页显示的起始偏移，默认值为0
        - **RuleIndex** (int) - 查询指定的rule_id, 不填写则默认获取所有的转发规则

        **Response**

        - **AvailLoad** (int) - 负载模式下可添加的规则数量（根据IP查询才返回此参数）
        - **AvailNonload** (int) - 非负载模式下可添加的规则数量（根据IP查询才返回此参数）
        - **IpRuleExist** (bool) - 当前配置的规则中是否存在IP规则（根据IP查询才返回此参数）
        - **RuleCnt** (int) - 满足要求的数据条目
        - **RuleInfo** (list) - 见 **BGPFwdRule** 模型定义

        **Response Model**

        **FwdSourceInfoConf**
        - **IPList** (list) - 源站IP列表
        - **Port** (int) - 源站端口
        - **Source** (str) - 源站，兼容IP和域名
        - **Toa** (int) - 源站Toa


        **FwdSourceInfo**
        - **Conf** (list) - 见 **FwdSourceInfoConf** 模型定义
        - **Type** (str) - 回源类型，分 IP 和 Domain


        **FwdClientProxyInfo**
        - **Count** (int) - 回源IP个数
        - **IPList** (list) - 回源IP列表


        **BGPFwdRule**
        - **BackupIP** (str) - 备份源站的IP
        - **BackupPort** (int) - 备份源站的端口
        - **BgpIP** (str) - 转发规则对应的BGP高防的IP
        - **BgpIPPort** (int) - 默认为0，为IP协议的转发端口，其余的自定义，在0~65535范围内即可,但是同一IP下配置的规则端口不能重复
        - **ClientProxyInfo** (dict) - 见 **FwdClientProxyInfo** 模型定义
        - **CreateTime** (int) - 创建时间，unix格式
        - **FwdType** (str) - 配置的规则的转发类型
        - **LoadBalance** (str) - 转发协议的类型是否为负载均衡的：默认为“No”，还可以选择为“Yes”。负载模式的规则最多添加2条，非负载模式的规则最多添加8条
        - **Remark** (str) - 备注
        - **RuleID** (str) - 转发规则的ID
        - **RuleIndex** (int) - 生成的规则的数据库索引值
        - **SourceDetect** (int) - 表示对源站进行检测：默认为0表示关闭，还可以选择为1表示开启
        - **SourceInfo** (dict) - 见 **FwdSourceInfo** 模型定义
        - **Status** (str) - 规则的状态
        - **UpdateTime** (int) - 更新时间，unix格式


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetBGPServiceFwdRuleRequestSchema().dumps(d)

        resp = self.invoke("GetBGPServiceFwdRule", d, **kwargs)
        return apis.GetBGPServiceFwdRuleResponseSchema().loads(resp)

    def get_bgp_service_ip(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetBGPServiceIP - 获取BGP高防IP的信息

        **Request**

        - **ResourceId** (str) - (Required) 资源id
        - **BgpIP** (str) - BGP高防IP
        - **Limit** (int) - 分页显示的条目数，默认值为32
        - **Offset** (int) - 分页显示的起始偏移，默认值为0

        **Response**

        - **AvailableIPQuota** (int) - 套餐可用的ip配额
        - **GameIPInfo** (list) - 见 **GameIpInfoTotal** 模型定义
        - **TotalCount** (int) - 套餐中已经配置的ip数量

        **Response Model**

        **GameIpInfoTotal**
        - **Cname** (str) - 高防IP Cname
        - **DefenceIP** (str) - 高防IP
        - **LineType** (str) - 线路类型
        - **Remark** (str) - 用户mark
        - **RuleCnt** (int) - 规则的个数
        - **SrcIP** (list) - 回源ip列表
        - **Status** (str) - ip配置状态


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetBGPServiceIPRequestSchema().dumps(d)

        resp = self.invoke("GetBGPServiceIP", d, **kwargs)
        return apis.GetBGPServiceIPResponseSchema().loads(resp)

    def get_buy_nap_service_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetBuyNapServicePrice - 获取高防价格

        **Request**

        - **AreaLine** (str) - (Required) 地区线路
        - **ChargeType** (str) - (Required) 计费方式
        - **DefenceDDosBaseFlowArr** (list) - (Required) DDoS基础防护流量
        - **DefenceDDosMaxFlowArr** (list) - (Required) DDoS最大防护流量
        - **EngineRoom** (list) - (Required) 地区
        - **LineType** (str) - (Required) 线路类型
        - **Quantity** (str) - (Required) 计费时长
        - **SrcBandwidth** (str) - (Required) 带宽
        - **AccessMode** (str) - 接入模式，Domain：网站接入、IP：非网站接入；默认为：IP

        **Response**

        - **ChargeIPQuota** (int) - 收费IP配额
        - **FreeIPQuota** (int) - 免费IP配额
        - **Message** (str) - 错误信息
        - **Price** (float) - 价格
        - **UdpFreeIpQuota** (int) - UDP免费IP配额

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetBuyNapServicePriceRequestSchema().dumps(d)

        resp = self.invoke("GetBuyNapServicePrice", d, **kwargs)
        return apis.GetBuyNapServicePriceResponseSchema().loads(resp)

    def get_nap_allow_list_domain(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetNapAllowListDomain - 获取域名允许列表

        **Request**

        - **ResourceId** (str) - (Required) 资源ID
        - **Domain** (str) - 获取指定域名信息
        - **DomainLike** (str) - 域名模糊查找
        - **Limit** (int) - 返回数据长度，默认为1000
        - **Offset** (int) - 列表起始位置偏移量，默认为0

        **Response**

        - **DomainList** (list) - 见 **BlockAllowDomainEntry** 模型定义
        - **TotalCount** (int) - 列表总条目数

        **Response Model**

        **BlockAllowDomainEntry**
        - **CreateTime** (int) - 创建时间戳，例如：1581991500
        - **Domain** (str) - 域名
        - **Remark** (str) - 备注
        - **Status** (int) - 状态；1：添加中，2：成功，3：删除中，4：失败，5：已删除


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetNapAllowListDomainRequestSchema().dumps(d)

        resp = self.invoke("GetNapAllowListDomain", d, **kwargs)
        return apis.GetNapAllowListDomainResponseSchema().loads(resp)

    def get_nap_service_config(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetNapServiceConfig - 获取高防服务配置

        **Request**

        - **AreaLine** (str) - 线路区域
        - **EngineRoom** (str) - 购买的套餐所在机房
        - **LineType** (str) - 线路类型
        - **NapType** (int) - 高防类型；0：全部、1：内地高防、:2：海外高防

        **Response**

        - **NapServiceConfig** (list) - 见 **NapServiceConfigEntry** 模型定义

        **Response Model**

        **NapServiceConfigEntry**
        - **AreaLine** (str) - 线路区域
        - **DR** (dict) - 灾备配置
        - **DayPay** (dict) - 按天购买配置
        - **Domain** (dict) - 域名配置
        - **DomainSrc** (dict) - 是否可以配置域名回源
        - **DynamicPay** (dict) - 按需购买配置
        - **EngineRoom** (str) - 购买的套餐所在机房
        - **LineType** (str) - 线路类型
        - **MonthPay** (dict) - 按月购买配置
        - **NapType** (int) - 高防类型，1：内地高防、2：海外高防
        - **YearPay** (dict) - 按年购买配置


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetNapServiceConfigRequestSchema().dumps(d)

        resp = self.invoke("GetNapServiceConfig", d, **kwargs)
        return apis.GetNapServiceConfigResponseSchema().loads(resp)

    def modify_high_protect_game_ip_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyHighProtectGameIPInfo - 修改高防IP信息

        **Request**

        - **DefenceIp** (str) - (Required) 高防ip
        - **ResourceId** (str) - (Required) 资源Id
        - **UserIP** (str) - (Required) 源站IP

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.ModifyHighProtectGameIPInfoRequestSchema().dumps(d)

        resp = self.invoke("ModifyHighProtectGameIPInfo", d, **kwargs)
        return apis.ModifyHighProtectGameIPInfoResponseSchema().loads(resp)

    def modify_high_protect_game_service(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyHighProtectGameService - 修改高防信息

        **Request**

        - **ResourceId** (str) - (Required) 资源Id
        - **HighProtectGameServiceName** (str) - 高防名称

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.ModifyHighProtectGameServiceRequestSchema().dumps(d)

        resp = self.invoke("ModifyHighProtectGameService", d, **kwargs)
        return apis.ModifyHighProtectGameServiceResponseSchema().loads(resp)

    def modify_nap_service_auto_renew(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyNapServiceAutoRenew - 修改高防服务自动续费开关

        **Request**

        - **AutoRenew** (int) - (Required) 自动续费开关， 0：关闭；1：开启
        - **ResourceId** (str) - (Required) 资源Id

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.ModifyNapServiceAutoRenewRequestSchema().dumps(d)

        resp = self.invoke("ModifyNapServiceAutoRenew", d, **kwargs)
        return apis.ModifyNapServiceAutoRenewResponseSchema().loads(resp)

    def renew_high_protect_game_service(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RenewHighProtectGameService - 续费高防服务

        **Request**

        - **AreaLine** (str) - (Required) 区域，华东和华南，EastChina 和SouthChina
        - **ChargeType** (str) - (Required) 计费方式
        - **EngineRoom** (list) - (Required) 代表机房，例如Dongguan  Hangzhou
        - **LineType** (str) - (Required) 线路
        - **Quantity** (int) - (Required) 购买数量
        - **ResourceId** (str) - (Required) 资源ID
        - **SrcBandwidth** (int) - (Required) 带宽，默认100M
        - **CouponId** (str) - 代金券ID
        - **DefenceDDosBaseFlowArr** (list) - DDoS基础防御值
        - **DefenceDDosMaxFlowArr** (list) - DDoS弹性防御值
        - **DefenceType** (str) - 防御类型，默认为TypeFixed

        **Response**

        - **ResourceInfo** (dict) - 见 **ResourceInfo** 模型定义

        **Response Model**

        **ResourceInfo**
        - **ResourceId** (str) - 资源id


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.RenewHighProtectGameServiceRequestSchema().dumps(d)

        resp = self.invoke("RenewHighProtectGameService", d, **kwargs)
        return apis.RenewHighProtectGameServiceResponseSchema().loads(resp)

    def set_nap_domain_entry_remark(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """SetNapDomainEntryRemark - 设置域名条目备注

        **Request**

        - **Domain** (str) - (Required) 域名
        - **ResourceId** (str) - (Required) 资源ID
        - **Remark** (str) - 备注,默认为空

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.SetNapDomainEntryRemarkRequestSchema().dumps(d)

        resp = self.invoke("SetNapDomainEntryRemark", d, **kwargs)
        return apis.SetNapDomainEntryRemarkResponseSchema().loads(resp)

    def set_nap_fwd_rule_remark(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """SetNapFwdRuleRemark - 设置高防转发规则备注信息

        **Request**

        - **ResourceId** (str) - (Required) 资源ID
        - **RuleIndex** (str) - (Required) 要修改的规则index
        - **Remark** (str) - 备注,默认为空

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.SetNapFwdRuleRemarkRequestSchema().dumps(d)

        resp = self.invoke("SetNapFwdRuleRemark", d, **kwargs)
        return apis.SetNapFwdRuleRemarkResponseSchema().loads(resp)

    def set_nap_ip_remark(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """SetNapIpRemark - 设置高防IP的备注信息

        **Request**

        - **NapIp** (str) - (Required) 高防IP
        - **ResourceId** (str) - (Required) 资源ID
        - **Remark** (str) - 备注，默认为空

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.SetNapIpRemarkRequestSchema().dumps(d)

        resp = self.invoke("SetNapIpRemark", d, **kwargs)
        return apis.SetNapIpRemarkResponseSchema().loads(resp)

    def un_bind_nap_ip(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UnBindNapIP - 直连高防：将高防EIP从资源上解绑

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **BindResourceId** (str) - (Required) 需要解绑的资源ID
        - **EIPId** (str) - (Required) 高防EIP资源ID
        - **NapIp** (str) - (Required) 高防Ip
        - **ResourceId** (str) - (Required) 高防资源ID
        - **ResourceType** (str) - (Required) 解绑的资源类型(uhost:云主机,ulb:负载均衡,upm:物理机)

        **Response**

        - **Message** (str) - 错误信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.UnBindNapIPRequestSchema().dumps(d)

        resp = self.invoke("UnBindNapIP", d, **kwargs)
        return apis.UnBindNapIPResponseSchema().loads(resp)

    def update_bgp_service_fwd_rule(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateBGPServiceFwdRule - 用于修改BGP高防的规则信息

        **Request**

        - **BgpIP** (str) - (Required) BGP的IP
        - **ResourceId** (str) - (Required) 资源id
        - **RuleID** (str) - (Required) 规则uuid
        - **RuleIndex** (int) - (Required) 要修改的规则index
        - **BackupIP** (str) - 备份源站的IP
        - **BackupPort** (int) - 备份源站的端口
        - **BgpIPPort** (int) - 默认为0，为IP协议的转发端口，其余的自定义
        - **FwdType** (str) - 转发协议的类型包括三种：默认为“IP”，还可以选择为“TCP”或"UDP"
        - **LoadBalance** (str) - 转发协议的类型是否为负载均衡的：默认为“No”，还可以选择为“Yes”。负载模式的规则最多添加2条，非负载模式的规则最多添加8条
        - **SourceAddrArr** (list) - 回源地址,可填 IP地址 或 域名
        - **SourceDetect** (int) - 表示对源站进行检测：默认为0表示关闭，还可以选择为1表示开启
        - **SourcePortArr** (list) - 回源端口
        - **SourceToaIDArr** (list) - 回源TOA

        **Response**

        - **RuleIndex** (int) - 转发规则的数据库索引

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.UpdateBGPServiceFwdRuleRequestSchema().dumps(d)

        resp = self.invoke("UpdateBGPServiceFwdRule", d, **kwargs)
        return apis.UpdateBGPServiceFwdRuleResponseSchema().loads(resp)

    def update_nap_fwd_rule_domain_resolution(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateNapFwdRuleDomainResolution - 手动触发域名回源转发规则更新

        **Request**

        - **ResourceId** (str) - (Required) 资源ID
        - **RuleIndex** (int) - (Required) 要修改的规则index

        **Response**


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.UpdateNapFwdRuleDomainResolutionRequestSchema().dumps(d)

        resp = self.invoke("UpdateNapFwdRuleDomainResolution", d, **kwargs)
        return apis.UpdateNapFwdRuleDomainResolutionResponseSchema().loads(resp)

    def upgrade_high_protect_game_service(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpgradeHighProtectGameService - 升降级高防服务

        **Request**

        - **AreaLine** (str) - (Required) 区域，华东和华南，EastChina 和SouthChina
        - **EngineRoom** (list) - (Required) 机房
        - **LineType** (str) - (Required) 线路类型
        - **ResourceId** (str) - (Required) 资源ID
        - **SrcBandwidth** (int) - (Required) 业务带宽
        - **CouponId** (str) - 代金券ID
        - **DefenceDDosBaseFlowArr** (list) - DDoS基础防御值
        - **DefenceDDosMaxFlowArr** (list) - DDoS弹性防御值
        - **DefenceType** (str) - 防御类型，默认为TypeFixed

        **Response**

        - **ResourceInfo** (dict) - 见 **ResourceInfo** 模型定义

        **Response Model**

        **ResourceInfo**
        - **ResourceId** (str) - 资源id


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.UpgradeHighProtectGameServiceRequestSchema().dumps(d)

        resp = self.invoke("UpgradeHighProtectGameService", d, **kwargs)
        return apis.UpgradeHighProtectGameServiceResponseSchema().loads(resp)