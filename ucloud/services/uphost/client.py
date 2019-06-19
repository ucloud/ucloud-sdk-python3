import typing

from ucloud.core.client import Client
from ucloud.services.uphost.schemas import apis


class UPHostClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        super(UPHostClient, self).__init__(config, transport, middleware)

    def reboot_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ RebootPHost - 重启物理机

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param PHostId: (Required) PHost资源ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RebootPHostRequestSchema().dumps(d)

        resp = self.invoke("RebootPHost", d, **kwargs)
        return apis.RebootPHostResponseSchema().loads(resp)

    def reinstall_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ReinstallPHost - 重装物理机操作系统

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param PHostId: (Required) PHost资源ID
        :param Password: (Required) 密码
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ImageId: (Optional) 镜像Id，参考镜像列表，默认使用原镜像
        :param Name: (Optional) 物理机名称，默认不更改
        :param Raid: (Optional) 不保留数据盘重装，可选Raid
        :param Remark: (Optional) 物理机备注，默认为不更改。
        :param ReserveDisk: (Optional) 是否保留数据盘，保留：Yes，不报留：No， 默认：Yes
        :param Tag: (Optional) 业务组，默认不更改。
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReinstallPHostRequestSchema().dumps(d)

        resp = self.invoke("ReinstallPHost", d, **kwargs)
        return apis.ReinstallPHostResponseSchema().loads(resp)

    def terminate_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ TerminatePHost - 删除物理云主机

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param PHostId: (Required) PHost资源ID
        :param ReleaseEIP: (Optional) 是否释放绑定的EIP。true: 解绑EIP后，并释放；其他值或不填：解绑EIP。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.TerminatePHostRequestSchema().dumps(d)

        resp = self.invoke("TerminatePHost", d, **kwargs)
        return apis.TerminatePHostResponseSchema().loads(resp)

    def describe_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribePHost - 获取物理机详细信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Optional) 返回数据长度，默认为20
        :param Offset: (Optional) 数据偏移量，默认为0
        :param PHostId: (Optional) PHost资源ID，若为空，则返回当前Region所有PHost。
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostRequestSchema().dumps(d)

        resp = self.invoke("DescribePHost", d, **kwargs)
        return apis.DescribePHostResponseSchema().loads(resp)

    def describe_phost_tags(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribePHostTags - 获取物理机tag列表（业务组）

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostTagsRequestSchema().dumps(d)

        resp = self.invoke("DescribePHostTags", d, **kwargs)
        return apis.DescribePHostTagsResponseSchema().loads(resp)

    def get_phost_price(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetPHostPrice - 获取物理机价格列表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ChargeType: (Required) 计费模式，枚举值为： Year/Month/Trial/Dynamic
        :param Count: (Required) 购买数量，范围[1-5]
        :param Quantity: (Required) 购买时长，1-10个月或1-10年
        :param Cluster: (Optional) 网络环境，可选千兆：1G ，万兆：10G
        :param Type: (Optional) 默认为：DB(数据库型)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetPHostPriceRequestSchema().dumps(d)

        resp = self.invoke("GetPHostPrice", d, **kwargs)
        return apis.GetPHostPriceResponseSchema().loads(resp)

    def poweroff_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ PoweroffPHost - 断电物理云主机

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param PHostId: (Required) PHost资源ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PoweroffPHostRequestSchema().dumps(d)

        resp = self.invoke("PoweroffPHost", d, **kwargs)
        return apis.PoweroffPHostResponseSchema().loads(resp)

    def start_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ StartPHost - 启动物理机

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param PHostId: (Required) PHost资源ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StartPHostRequestSchema().dumps(d)

        resp = self.invoke("StartPHost", d, **kwargs)
        return apis.StartPHostResponseSchema().loads(resp)

    def create_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreatePHost - 指定数据中心，根据资源使用量创建指定数量的UPHost物理云主机实例。

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ImageId: (Required) 镜像ID。 请通过 [DescribePHostImage]获取
        :param Password: (Required) 密码（密码需使用base64进行编码）
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) 计费模式，枚举值为：year, 按年付费； month,按月付费；dynamic，按需付费，（需开启权限） trial, 试用（需开启权限）。默认为按月付费
        :param Cluster: (Optional) 网络环境，可选千兆：1G ，万兆：10G， 默认1G
        :param Count: (Optional) 购买数量，默认为1，（暂不支持）
        :param CouponId: (Optional) 代金券
        :param Name: (Optional) 物理机名称，默认为phost
        :param Quantity: (Optional) 购买时长，默认为1，范围[1-10]
        :param Raid: (Optional) Raid配置，默认Raid10  支持:Raid0、Raid1、Raid5、Raid10，NoRaid
        :param Remark: (Optional) 物理机备注，默认为空
        :param SecurityGroupId: (Optional) 防火墙Id，默认：Web推荐防火墙。如何查询SecurityGroupId请参见 [DescribeSecurityGroup](../unet-api/describe_security_group.html)
        :param SubnetId: (Optional) 子网ID，不填为默认，VPC2.0下需要填写此字段。
        :param Tag: (Optional) 业务组，默认为default
        :param Type: (Optional) 物理机类型，默认为：db-2(基础型-SAS-V3)
        :param VPCId: (Optional) VPC ID，不填为默认，VPC2.0下需要填写此字段。
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreatePHostRequestSchema().dumps(d)

        resp = self.invoke("CreatePHost", d, **kwargs)
        return apis.CreatePHostResponseSchema().loads(resp)

    def describe_phost_image(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribePHostImage - 获取物理云主机镜像列表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ImageId: (Optional) 镜像ID
        :param ImageType: (Optional) 镜像类别，枚举为：Base,标准镜像；默认为标准镜像。
        :param Limit: (Optional) 返回数据长度，默认为20
        :param Offset: (Optional) 数据偏移量，默认为0
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostImageRequestSchema().dumps(d)

        resp = self.invoke("DescribePHostImage", d, **kwargs)
        return apis.DescribePHostImageResponseSchema().loads(resp)

    def modify_phost_info(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ModifyPHostInfo - 更改物理机信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param PHostId: (Required) 物理机资源ID
        :param Name: (Optional) 物理机名称，默认不更改
        :param Remark: (Optional) 物理机备注，默认不更改
        :param Tag: (Optional) 业务组，默认不更改
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyPHostInfoRequestSchema().dumps(d)

        resp = self.invoke("ModifyPHostInfo", d, **kwargs)
        return apis.ModifyPHostInfoResponseSchema().loads(resp)
