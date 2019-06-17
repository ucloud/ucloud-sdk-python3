import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.udpn.schemas import apis


class UDPNClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(UDPNClient, self).__init__(config, transport)

    def get_udpn_price(self, req: dict = None) -> dict:
        """ GetUDPNPrice - 获取 UDPN 价格

        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 带宽信息
        :param Peer1: (Required) 专线可用区1，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg, 洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        :param Peer2: (Required) 专线可用区2，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg, 洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        :param ChargeType: (Optional) 计费类型
        :param Quantity: (Optional) 购买时长
        """
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.GetUDPNPriceRequestSchema().dumps(d)
        resp = self.invoke("GetUDPNPrice", d)
        return apis.GetUDPNPriceResponseSchema().loads(resp)

    def get_udpn_upgrade_price(self, req: dict = None) -> dict:
        """ GetUDPNUpgradePrice - 获取专线升级价格

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 带宽
        :param UDPNId: (Required) 专线带宽资源 Id
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUDPNUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("GetUDPNUpgradePrice", d)
        return apis.GetUDPNUpgradePriceResponseSchema().loads(resp)

    def modify_udpn_bandwidth(self, req: dict = None) -> dict:
        """ ModifyUDPNBandwidth - 修改带宽值

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 调整后专线带宽, 单位为Mbps，取值范围为大于等于2且小于等于1000([2-1000])的整数
        :param UDPNId: (Required) UDPN Id
        :param CouponId: (Optional) 代金劵 ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUDPNBandwidthRequestSchema().dumps(d)
        resp = self.invoke("ModifyUDPNBandwidth", d)
        return apis.ModifyUDPNBandwidthResponseSchema().loads(resp)

    def release_udpn(self, req: dict = None) -> dict:
        """ ReleaseUDPN - 释放 UDPN

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param UDPNId: (Required) UDPN 资源 Id
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseUDPNRequestSchema().dumps(d)
        resp = self.invoke("ReleaseUDPN", d)
        return apis.ReleaseUDPNResponseSchema().loads(resp)

    def allocate_udpn(self, req: dict = None) -> dict:
        """ AllocateUDPN - 分配一条 UDPN 专线

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Bandwidth: (Required) 带宽
        :param Peer1: (Required) 专线可用区1，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg,  洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        :param Peer2: (Required) 专线可用区2，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg,  洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        :param ChargeType: (Optional) 计费类型，枚举值为： Year，按年付费； Month，按月付费； Dynamic，按需付费
        :param CouponId: (Optional) 代金劵
        :param Quantity: (Optional) 计费时长，默认 1
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateUDPNRequestSchema().dumps(d)
        resp = self.invoke("AllocateUDPN", d)
        return apis.AllocateUDPNResponseSchema().loads(resp)

    def describe_udpn(self, req: dict = None) -> dict:
        """ DescribeUDPN - 描述 UDPN

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Optional) 返回数据长度，默认为 20
        :param Offset: (Optional) 列表起始位置偏移量，默认为 0
        :param UDPNId: (Optional) 申请到的 UDPN 资源 ID。若为空，则查询该用户在机房所有的专线信息。非默认项目资源，需填写ProjectId
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDPNRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDPN", d)
        return apis.DescribeUDPNResponseSchema().loads(resp)

    def get_udpn_line_list(self, req: dict = None) -> dict:
        """ GetUDPNLineList - 获取当前支持的专线线路列表

        :param ProjectId: (Config) 
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUDPNLineListRequestSchema().dumps(d)
        resp = self.invoke("GetUDPNLineList", d)
        return apis.GetUDPNLineListResponseSchema().loads(resp)
