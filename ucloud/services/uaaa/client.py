""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.uaaa.schemas import apis


class UAAAClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UAAAClient, self).__init__(config, transport, middleware, logger)

    def create_app_repo(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateAppRepo - 创建应用仓库加速实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - (Required) 计费类型(年:'Year', 月:'Month',小时:'Dynamic')
        - **Name** (str) - (Required) 名称
        - **VPCId** (list) - (Required) 待加速的VPCId ( 目前只允许一个)
        - **CouponId** (str) - 代金券
        - **Description** (str) - 应用仓库描述
        - **Quantity** (int) - 数量(ChargeType对应的数值): ChargeType = Month 时，默认0 ，其他条件为必须字段
        - **RecordName** (list) - 记录名称，需在给定列表中

        **Response**

        - **InstanceId** (str) - 应用仓库加速实例ID
        - **Message** (str) - 错误信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateAppRepoRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateAppRepo", d, **kwargs)
        return apis.CreateAppRepoResponseSchema().loads(resp)

    def delete_app_repo(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteAppRepo - 删除应用仓库加速实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceId** (str) - (Required) 实例 ID

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteAppRepoRequestSchema().dumps(d)

        resp = self.invoke("DeleteAppRepo", d, **kwargs)
        return apis.DeleteAppRepoResponseSchema().loads(resp)

    def describe_app_repo(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeAppRepo - 查询应用仓库实例信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceId** (str) - 应用仓库加速实例ID

        **Response**

        - **DataSet** (list) - 见 **AppRepoInstance** 模型定义
        - **Message** (str) - 错误信息

        **Response Model**

        **AppRepoInstance**
        - **ChargeType** (str) - 计费类型
        - **CreateTime** (int) - 创建时间。格式为Unix Timestamp
        - **Description** (str) - 应用仓库描述信息
        - **ExpireTime** (int) - 到期时间
        - **InstanceId** (str) - 应用仓库实例ID
        - **Name** (str) - 应用仓库名
        - **RecordName** (list) - 应用仓库绑定的加速域名
        - **VPC** (list) - 应用仓库绑定的vpc 信息


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeAppRepoRequestSchema().dumps(d)

        resp = self.invoke("DescribeAppRepo", d, **kwargs)
        return apis.DescribeAppRepoResponseSchema().loads(resp)

    def describe_app_repo_permit_domain(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeAppRepoPermitDomain - 查询允许加速的域名白名单

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (list) - 见 **DomainDetail** 模型定义
        - **Message** (str) - 错误信息

        **Response Model**

        **DomainDetail**
        - **Info** (dict) - 见 **DomainInfo** 模型定义
        - **Redirect** (list) - 见 **DomainInfo** 模型定义


        **DomainInfo**
        - **Desc** (str) - 备注信息
        - **DomainName** (str) - 域名解析记录名称


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeAppRepoPermitDomainRequestSchema().dumps(d)

        resp = self.invoke("DescribeAppRepoPermitDomain", d, **kwargs)
        return apis.DescribeAppRepoPermitDomainResponseSchema().loads(resp)

    def describe_app_repo_post_paid_record(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeAppRepoPostPaidRecord - 查询应用仓库实例后付费记录

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **EndTime** (int) - (Required) 结束时间 (StartTime <EndTime )
        - **InstanceId** (str) - (Required) 应用仓库实例
        - **StartTime** (int) - (Required) 开始时间 (StartTime <EndTime )
        - **Limit** (int) - 最大查询数量（默认30,  最大值200 ）
        - **Offset** (int) - 偏移量（默认0，最小值 0）

        **Response**

        - **DataSet** (list) - 见 **TPostpaidBase** 模型定义
        - **TotalCount** (int) - 记录总数

        **Response Model**

        **TPostpaidBase**
        - **EndTime** (int) - 结束时间
        - **InstanceId** (str) - 应用仓库资源ID
        - **StartTime** (int) - 开始时间
        - **TrafficSum** (int) - 流量（单位: MB）


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeAppRepoPostPaidRecordRequestSchema().dumps(d)

        resp = self.invoke("DescribeAppRepoPostPaidRecord", d, **kwargs)
        return apis.DescribeAppRepoPostPaidRecordResponseSchema().loads(resp)

    def get_app_repo_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetAppRepoPrice - 获取应用仓库实例价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - (Required) 计费类型
        - **DomainQuantity** (int) - 域名绑定数量( >= 0) ,默认: 0
        - **Quantity** (int) - 数量（和ChargeType相关）: ChargeType = Month， 默认值为0 ， 其他情况为必传字段

        **Response**

        - **Price** (float) - 价格

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetAppRepoPriceRequestSchema().dumps(d)

        resp = self.invoke("GetAppRepoPrice", d, **kwargs)
        return apis.GetAppRepoPriceResponseSchema().loads(resp)

    def get_app_repo_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetAppRepoUpgradePrice - 获取改配后的退/补金额

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceId** (str) - (Required) 实例资源id
        - **DomainQuantity** (int) - 绑定域名的数量

        **Response**

        - **Price** (float) - 应补差价（单位：元）

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetAppRepoUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("GetAppRepoUpgradePrice", d, **kwargs)
        return apis.GetAppRepoUpgradePriceResponseSchema().loads(resp)

    def update_app_repo(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateAppRepo - 修改应用仓库实例基本信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceId** (str) - (Required) 应用仓库实例ID
        - **Description** (str) - 应用仓库备注信息
        - **Name** (str) - 应用仓库名称

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpdateAppRepoRequestSchema().dumps(d)

        resp = self.invoke("UpdateAppRepo", d, **kwargs)
        return apis.UpdateAppRepoResponseSchema().loads(resp)

    def update_app_repo_domain_name(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateAppRepoDomainName - 更新应用仓库实例绑定的加速域名

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceId** (str) - (Required) 应用仓库实例ID
        - **CouponId** (str) - 代金券
        - **RecordName** (list) - 加速域名列表。 不填写，相当于清空所有加速域名

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpdateAppRepoDomainNameRequestSchema().dumps(d)

        resp = self.invoke("UpdateAppRepoDomainName", d, **kwargs)
        return apis.UpdateAppRepoDomainNameResponseSchema().loads(resp)
