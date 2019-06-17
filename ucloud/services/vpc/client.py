import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.vpc.schemas import apis


class VPCClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(VPCClient, self).__init__(config, transport)

    def delete_route_table(self, req: dict = None) -> dict:
        """ DeleteRouteTable - 删除自定义路由表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param RouteTableId: (Required) 路由ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteRouteTableRequestSchema().dumps(d)
        resp = self.invoke("DeleteRouteTable", d)
        return apis.DeleteRouteTableResponseSchema().loads(resp)

    def describe_route_table(self, req: dict = None) -> dict:
        """ DescribeRouteTable - 获取路由表详细信息(包括路由策略)

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BusinessId: (Optional) 业务组ID
        :param Limit: (Optional) Limit
        :param OffSet: (Optional) OffSet
        :param RouteTableId: (Optional) 路由表ID
        :param VPCId: (Optional) VPC ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeRouteTableRequestSchema().dumps(d)
        resp = self.invoke("DescribeRouteTable", d)
        return apis.DescribeRouteTableResponseSchema().loads(resp)

    def update_subnet_attribute(self, req: dict = None) -> dict:
        """ UpdateSubnetAttribute - 更新子网信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SubnetId: (Required) 子网ID
        :param Name: (Optional) 子网名称(如果Name不填写，Tag必须填写)
        :param Tag: (Optional) 业务组名称(如果Tag不填写，Name必须填写)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateSubnetAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateSubnetAttribute", d)
        return apis.UpdateSubnetAttributeResponseSchema().loads(resp)

    def add_vpc_network(self, req: dict = None) -> dict:
        """ AddVPCNetwork - 添加VPC网段

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Network: (Required) 增加网段
        :param VPCId: (Required) 源VPC短ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AddVPCNetworkRequestSchema().dumps(d)
        resp = self.invoke("AddVPCNetwork", d)
        return apis.AddVPCNetworkResponseSchema().loads(resp)

    def delete_vpc(self, req: dict = None) -> dict:
        """ DeleteVPC - 删除VPC

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param VPCId: (Required) VPC资源Id
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteVPCRequestSchema().dumps(d)
        resp = self.invoke("DeleteVPC", d)
        return apis.DeleteVPCResponseSchema().loads(resp)

    def describe_vpc_intercom(self, req: dict = None) -> dict:
        """ DescribeVPCIntercom - 获取VPC互通信息

        :param ProjectId: (Config) 源VPC所在项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 源VPC所在地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param VPCId: (Required) VPC短ID
        :param DstProjectId: (Optional) 目的项目ID，默认为全部项目
        :param DstRegion: (Optional) 目的VPC所在地域，默认为全部地域
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVPCIntercomRequestSchema().dumps(d)
        resp = self.invoke("DescribeVPCIntercom", d)
        return apis.DescribeVPCIntercomResponseSchema().loads(resp)

    def update_vpc_network(self, req: dict = None) -> dict:
        """ UpdateVPCNetwork - 更新VPC网段

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Network: (Required) 需要保留的VPC网段。当前仅支持删除VPC网段，添加网段请参考[AddVPCNetwork](../vpc2.0-api/add_vpc_network)
        :param VPCId: (Required) VPC的ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateVPCNetworkRequestSchema().dumps(d)
        resp = self.invoke("UpdateVPCNetwork", d)
        return apis.UpdateVPCNetworkResponseSchema().loads(resp)

    def clone_route_table(self, req: dict = None) -> dict:
        """ CloneRouteTable - 根据一张现有路由表复制一张新的路由表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param RouteTableId: (Required) 被克隆的路由表ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CloneRouteTableRequestSchema().dumps(d)
        resp = self.invoke("CloneRouteTable", d)
        return apis.CloneRouteTableResponseSchema().loads(resp)

    def create_route_table(self, req: dict = None) -> dict:
        """ CreateRouteTable - 创建路由表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param VPCId: (Required) VPC ID
        :param Name: (Optional) 路由表名称 Default RouteTable
        :param Remark: (Optional) 备注
        :param Tag: (Optional) 业务组
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateRouteTableRequestSchema().dumps(d)
        resp = self.invoke("CreateRouteTable", d)
        return apis.CreateRouteTableResponseSchema().loads(resp)

    def create_vpc_intercom(self, req: dict = None) -> dict:
        """ CreateVPCIntercom - 新建VPC互通关系

        :param ProjectId: (Config) 源VPC所在项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 源VPC所在地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DstVPCId: (Required) 目的VPC短ID
        :param VPCId: (Required) 源VPC短ID
        :param DstProjectId: (Optional) 目的VPC项目ID。默认与源VPC同项目。
        :param DstRegion: (Optional) 目的VPC所在地域，默认与源VPC同地域。
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateVPCIntercomRequestSchema().dumps(d)
        resp = self.invoke("CreateVPCIntercom", d)
        return apis.CreateVPCIntercomResponseSchema().loads(resp)

    def delete_subnet(self, req: dict = None) -> dict:
        """ DeleteSubnet - 删除子网

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SubnetId: (Required) 子网ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteSubnetRequestSchema().dumps(d)
        resp = self.invoke("DeleteSubnet", d)
        return apis.DeleteSubnetResponseSchema().loads(resp)

    def describe_subnet(self, req: dict = None) -> dict:
        """ DescribeSubnet - 获取子网信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BusinessId: (Optional) 业务组
        :param Limit: (Optional) 列表长度，默认为20
        :param Offset: (Optional) 偏移量，默认为0
        :param RouteTableId: (Optional) 路由表Id
        :param SubnetId: (Optional) 子网id，适用于一次查询一个子网信息
        :param SubnetIds: (Optional) 子网id数组，适用于一次查询多个子网信息
        :param Tag: (Optional) 业务组名称，默认为Default
        :param VPCId: (Optional) VPC资源id
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeSubnetRequestSchema().dumps(d)
        resp = self.invoke("DescribeSubnet", d)
        return apis.DescribeSubnetResponseSchema().loads(resp)

    def describe_subnet_resource(self, req: dict = None) -> dict:
        """ DescribeSubnetResource - 展示子网资源

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SubnetId: (Required) 子网id
        :param Limit: (Optional) 单页返回数据长度，默认为20
        :param Offset: (Optional) 列表起始位置偏移量，默认为0
        :param ResourceType: (Optional) 资源类型，默认为全部资源类型。枚举值为：UHOST，云主机；PHOST，物理云主机；ULB，负载均衡；UHADOOP_HOST，hadoop节点；UFORTRESS_HOST，堡垒机；UNATGW，NAT网关；UKAFKA，Kafka消息队列；UMEM，内存存储；DOCKER，容器集群；UDB，数据库；UDW，数据仓库；VIP，内网VIP.
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeSubnetResourceRequestSchema().dumps(d)
        resp = self.invoke("DescribeSubnetResource", d)
        return apis.DescribeSubnetResourceResponseSchema().loads(resp)

    def modify_route_rule(self, req: dict = None) -> dict:
        """ ModifyRouteRule - 路由策略增、删、改

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param RouteRule: (Required) 格式: RouteRuleId | 目的网段 | 下一跳类型 | 下一跳 |优先级| 备注 | 增、删、改标志  (下一跳类型为instance或者vip，下一跳为云主机id或者vip的id，优先级使用0，动作标志为add/delete/update)   。"添加"示例: test_id | 10.8.0.0/16 | instance | uhost-xd8ja | 0 | Default Route Rule| add (添加的RouteRuleId填任意非空字符串)     。"删除"示例: routerule-xk3jxa | 10.8.0.0/16 | instance | uhost-xd8ja | 0 | Default Route Rule| delete (RouteRuleId来自DescribeRouteTable中)     。“修改”示例: routerule-xk3jxa | 10.8.0.0/16 | instance | uhost-cjksa2 | 0 | Default Route Rule| update (RouteRuleId来自DescribeRouteTable中)
        :param RouteTableId: (Required) 通过DescribeRouteTable拿到
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyRouteRuleRequestSchema().dumps(d)
        resp = self.invoke("ModifyRouteRule", d)
        return apis.ModifyRouteRuleResponseSchema().loads(resp)

    def associate_route_table(self, req: dict = None) -> dict:
        """ AssociateRouteTable - 绑定子网的路由表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param RouteTableId: (Required) 路由表ID，仅限自定义路由表
        :param SubnetId: (Required) 子网ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AssociateRouteTableRequestSchema().dumps(d)
        resp = self.invoke("AssociateRouteTable", d)
        return apis.AssociateRouteTableResponseSchema().loads(resp)

    def create_subnet(self, req: dict = None) -> dict:
        """ CreateSubnet - 创建子网

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Subnet: (Required) 子网网络地址，例如192.168.0.0
        :param VPCId: (Required) VPC资源ID
        :param Netmask: (Optional) 子网网络号位数，默认为24
        :param Remark: (Optional) 备注
        :param SubnetName: (Optional) 子网名称，默认为Subnet
        :param Tag: (Optional) 业务组名称，默认为Default
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateSubnetRequestSchema().dumps(d)
        resp = self.invoke("CreateSubnet", d)
        return apis.CreateSubnetResponseSchema().loads(resp)

    def create_vpc(self, req: dict = None) -> dict:
        """ CreateVPC - 创建VPC

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) VPC名称
        :param Network: (Required) VPC网段
        :param Remark: (Optional) 备注
        :param Tag: (Optional) 业务组名称
        :param Type: (Optional) VPC类型
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateVPCRequestSchema().dumps(d)
        resp = self.invoke("CreateVPC", d)
        return apis.CreateVPCResponseSchema().loads(resp)

    def delete_vpc_intercom(self, req: dict = None) -> dict:
        """ DeleteVPCIntercom - 删除VPC互通关系

        :param ProjectId: (Config) 源VPC所在项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 源VPC所在地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param DstVPCId: (Required) 目的VPC短ID
        :param VPCId: (Required) 源VPC短ID
        :param DstProjectId: (Optional) 目的VPC所在项目ID，默认为源VPC所在项目ID
        :param DstRegion: (Optional) 目的VPC所在地域，默认为源VPC所在地域
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteVPCIntercomRequestSchema().dumps(d)
        resp = self.invoke("DeleteVPCIntercom", d)
        return apis.DeleteVPCIntercomResponseSchema().loads(resp)

    def describe_vpc(self, req: dict = None) -> dict:
        """ DescribeVPC - 获取VPC信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Optional) 
        :param Offset: (Optional) 
        :param Tag: (Optional) 业务组名称
        :param VPCIds: (Optional) VPCId
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVPCRequestSchema().dumps(d)
        resp = self.invoke("DescribeVPC", d)
        return apis.DescribeVPCResponseSchema().loads(resp)

    def update_route_table_attribute(self, req: dict = None) -> dict:
        """ UpdateRouteTableAttribute - 更新路由表基本信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param RouteTableId: (Required) 路由表ID
        :param Name: (Optional) 名称
        :param Remark: (Optional) 备注
        :param Tag: (Optional) 业务组名称
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateRouteTableAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateRouteTableAttribute", d)
        return apis.UpdateRouteTableAttributeResponseSchema().loads(resp)
