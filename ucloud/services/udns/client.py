""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.udns.schemas import apis


class UDNSClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UDNSClient, self).__init__(config, transport, middleware, logger)

    def associate_udns_zone_vpc(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """AssociateUDNSZoneVPC - 绑定域名与VPC

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneId** (str) - (Required) 域名资源ID
        - **VPCId** (str) - (Required) VPC资源ID
        - **VPCProjectId** (str) - (Required) VPC所属项目ID

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.AssociateUDNSZoneVPCRequestSchema().dumps(d)

        resp = self.invoke("AssociateUDNSZoneVPC", d, **kwargs)
        return apis.AssociateUDNSZoneVPCResponseSchema().loads(resp)

    def create_udns_record(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUDNSRecord - 创建域名记录

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneId** (str) - (Required) 域名资源ID
        - **Name** (str) - (Required) 主机记录
        - **Type** (str) - (Required) 记录类型。枚举值，“A”,"CNAME","MX","AAAA","SRV","PTR","TXT"。
        - **Value** (str) - (Required) 数值组，支持逗号分割。格式为：Value|权重|IsEnabled，其中权重支持1-10，IsEnabled为枚举值（1为启用，0为禁用）。输入格式示例：192.168.1.1|1|1,192.168.1.2|10|0。
        - **ValueType** (str) - (Required) 值类型。枚举值，“Normal”，标准；“Multivalue”，多值返回。仅在值为“Multivalue”时，Value的权重生效。
        - **Remark** (str) - 记录的备注信息
        - **TTL** (int) - TTL值，范围为5-600，单位为秒。默认为5

        **Response**

        - **DNSRecordId** (str) - 域名记录的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUDNSRecordRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDNSRecord", d, **kwargs)
        return apis.CreateUDNSRecordResponseSchema().loads(resp)

    def create_udns_zone(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUDNSZone - 创建域名

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneName** (str) - (Required) 域名字符串
        - **Type** (str) - (Required) 域名类型。枚举值，“private”，内网DNS；“public”，公网DNS，暂只支持private。
        - **ChargeType** (str) - 付费方式, 枚举值为: Year, 按年付费; Month, 按月付费; Dynamic, 按需付费，默认为按月付费
        - **CouponId** (str) - 代金券ID，默认不使用
        - **IsRecursionEnabled** (str) - 是否支持迭代。枚举值,"enable",支持迭代; "disable",不支持迭代
        - **Quantity** (int) - 购买时长，默认为1
        - **Remark** (str) - 备注
        - **Tag** (str) - 所属业务组名称

        **Response**

        - **DNSZoneId** (str) - 域名资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUDNSZoneRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDNSZone", d, **kwargs)
        return apis.CreateUDNSZoneResponseSchema().loads(resp)

    def delete_udns_record(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUDNSRecord - 删除域名记录

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneId** (str) - (Required) 域名资源ID
        - **RecordIds** (list) - (Required) 域名记录资源ID

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteUDNSRecordRequestSchema().dumps(d)

        resp = self.invoke("DeleteUDNSRecord", d, **kwargs)
        return apis.DeleteUDNSRecordResponseSchema().loads(resp)

    def describe_udns_domain(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUDNSDomain - zone下所有域名的rr记录

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneName** (str) - (Required) zone名称
        - **VPCId** (str) - (Required) VPI资源ID
        - **Limit** (int) - 返回数量
        - **Offset** (int) - 查询数量偏移

        **Response**

        - **RecordInfos** (list) - 见 **RecordInfo** 模型定义
        - **TotalCount** (int) - 总条数

        **Response Model**

        **ValueSet**
        - **Data** (str) - 主机记录
        - **IsEnabled** (int) - 是否启用
        - **Weight** (int) - 权重


        **RecordInfo**
        - **Name** (str) - 主机记录
        - **RecordId** (str) - 域名记录资源ID
        - **Remark** (str) - 记录备注信息
        - **TTL** (int) - TTL值，单位为秒
        - **Type** (str) - 记录类型
        - **ValueSet** (list) - 见 **ValueSet** 模型定义
        - **ValueType** (str) - 记录策略，标准或随机应答


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUDNSDomainRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDNSDomain", d, **kwargs)
        return apis.DescribeUDNSDomainResponseSchema().loads(resp)

    def describe_udns_record(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUDNSRecord - 获取域名记录

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneId** (str) - (Required) 域名资源ID
        - **Limit** (int) - 数据分页值, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0
        - **RecordIds** (list) - 域名记录资源ID

        **Response**

        - **RecordInfos** (list) - 见 **RecordInfo** 模型定义
        - **TotalCount** (int) - 资源数量

        **Response Model**

        **ValueSet**
        - **Data** (str) - 主机记录
        - **IsEnabled** (int) - 是否启用
        - **Weight** (int) - 权重


        **RecordInfo**
        - **Name** (str) - 主机记录
        - **RecordId** (str) - 域名记录资源ID
        - **Remark** (str) - 记录备注信息
        - **TTL** (int) - TTL值，单位为秒
        - **Type** (str) - 记录类型
        - **ValueSet** (list) - 见 **ValueSet** 模型定义
        - **ValueType** (str) - 记录策略，标准或随机应答


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUDNSRecordRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDNSRecord", d, **kwargs)
        return apis.DescribeUDNSRecordResponseSchema().loads(resp)

    def describe_udns_zone(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUDNSZone - 获取域名信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneIds** (list) - 域名资源ID
        - **Limit** (int) - 数据分页值, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0

        **Response**

        - **DNSZoneInfos** (list) - 见 **ZoneInfo** 模型定义
        - **TotalCount** (int) - 符合查询条件的域名数量

        **Response Model**

        **VPCInfo**
        - **Name** (str) - VPC名称
        - **Network** (list) - VPC地址空间
        - **VPCId** (str) - VPC ID
        - **VPCProjectId** (str) - VPC所属项目ID
        - **VPCType** (str) - VPC类型：Normal 公有云 Hybrid 托管云


        **ZoneInfo**
        - **ChargeType** (str) - 计费类型（Dynamic、Month、Year）
        - **CreateTime** (int) - 创建时间
        - **DNSZoneName** (str) - 域名名称
        - **ExpireTime** (int) - 过期时间
        - **IsAutoRenew** (str) - 是否开启自动续费（Yes No）
        - **IsRecursionEnabled** (str) - 是否支持迭代。枚举值,"enable",支持迭代; "disable",不支持迭代
        - **RecordInfos** (list) - 记录相关ID
        - **Remark** (str) - 备注
        - **Tag** (str) - 业务组
        - **VPCInfos** (list) - 见 **VPCInfo** 模型定义


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUDNSZoneRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDNSZone", d, **kwargs)
        return apis.DescribeUDNSZoneResponseSchema().loads(resp)

    def disassociate_udns_zone_vpc(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DisassociateUDNSZoneVPC - 解绑域名和VPC

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneId** (str) - (Required) 域名资源ID
        - **VPCId** (str) - (Required) VPC资源ID
        - **VPCProjectId** (str) - (Required) VPC所属项目ID

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DisassociateUDNSZoneVPCRequestSchema().dumps(d)

        resp = self.invoke("DisassociateUDNSZoneVPC", d, **kwargs)
        return apis.DisassociateUDNSZoneVPCResponseSchema().loads(resp)

    def modify_udns_record(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyUDNSRecord - 修改域名记录

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneId** (str) - (Required) 域名资源ID
        - **RecordId** (str) - (Required) 域名记录资源ID
        - **Remark** (str) - 记录的备注信息
        - **TTL** (int) - TTL值，单位为秒
        - **Value** (str) - 数值组，支持逗号分割。格式为：Value|权重|Enable，其中权重支持1-10，Enable为枚举值（1为启用，0为禁用）。输入格式示例：192.168.1.1|1|1,192.168.1.2|10|0。
        - **ValueType** (str) - 值类型。枚举值，“Normal”，标准；“Multivalue”，多值返回。仅在值为“Multivalue”时，Value的权重生效。

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyUDNSRecordRequestSchema().dumps(d)

        resp = self.invoke("ModifyUDNSRecord", d, **kwargs)
        return apis.ModifyUDNSRecordResponseSchema().loads(resp)

    def modify_udns_zone(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyUDNSZone - 修改域名备注/递归查询状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DNSZoneId** (str) - (Required) 域名资源ID
        - **IsRecursionEnabled** (str) - 是否支持迭代。枚举值,"enable",支持迭代; "disable",不支持迭代
        - **Remark** (str) - 备注

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyUDNSZoneRequestSchema().dumps(d)

        resp = self.invoke("ModifyUDNSZone", d, **kwargs)
        return apis.ModifyUDNSZoneResponseSchema().loads(resp)