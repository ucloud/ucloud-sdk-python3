""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.cube.schemas import apis


class CubeClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(CubeClient, self).__init__(config, transport, middleware, logger)

    def create_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateCubePod - 创建Pod

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Pod** (str) - (Required) base64编码的Pod的yaml
        - **SubnetId** (str) - (Required) 子网Id
        - **VPCId** (str) - (Required) VPCId
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ChargeType** (str) - 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Postpay， \\ 后付费；默认为后付费
        - **CpuPlatform** (str) - Cpu平台（V6、A2），默认V6
        - **Group** (str) - pod所在组
        - **Name** (str) - pod的名字
        - **Quantity** (int) - 购买时长。默认:值 1。 月付时，此参数传0，代表购买至月末。
        - **Tag** (str) - 业务组。默认：Default（Default即为未分组）

        **Response**

        - **Action** (str) - 操作名称
        - **CubeId** (str) - cube的资源Id
        - **Pod** (str) - base64编码的yaml
        - **RetCode** (int) - 返回码

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateCubePod", d, **kwargs)
        return apis.CreateCubePodResponseSchema().loads(resp)

    def delete_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteCubePod - 删除Pod

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - cubeid和uid任意一个（必须）
        - **ReleaseEIP** (bool) - 删除cube时是否释放绑定的EIP。默认为false。
        - **Uid** (str) - cubeid和uid任意一个（必须）
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteCubePodRequestSchema().dumps(d)

        resp = self.invoke("DeleteCubePod", d, **kwargs)
        return apis.DeleteCubePodResponseSchema().loads(resp)

    def get_cube_extend_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeExtendInfo - 获取Cube的额外信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeIds** (str) - (Required) id列表以逗号(,)分割
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **ExtendInfo** (list) - 见 **CubeExtendInfo** 模型定义

        **Response Model**

        **EIPAddr**

        - **IP** (str) - IP地址
        - **OperatorName** (str) - 线路名称BGP或者internalation

        **EIPSet**

        - **Bandwidth** (int) - EIP带宽值
        - **BandwidthType** (int) - 带宽类型0标准普通带宽，1表示共享带宽
        - **CreateTime** (int) - EIP创建时间
        - **EIPAddr** (list) - 见 **EIPAddr** 模型定义
        - **EIPId** (str) - EIPId
        - **PayMode** (str) - 付费模式，带宽付费或者流量付费
        - **Resource** (str) - EIP绑定对象的资源Id
        - **Status** (str) - EIP状态，表示使用中或者空闲
        - **Weight** (int) - EIP权重

        **CubeExtendInfo**

        - **CubeId** (str) - Cube的Id
        - **Eip** (list) - 见 **EIPSet** 模型定义
        - **Expiration** (int) - 资源有效期
        - **Name** (str) - Cube的名称
        - **Tag** (str) - 业务组名称

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeExtendInfoRequestSchema().dumps(d)

        resp = self.invoke("GetCubeExtendInfo", d, **kwargs)
        return apis.GetCubeExtendInfoResponseSchema().loads(resp)

    def get_cube_pod(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """GetCubePod - 获取Pod的详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - CubeId和Uid任意一个
        - **Uid** (str) - CubeId和Uid任意一个
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Pod** (str) - base64编码的pod的yaml

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubePodRequestSchema().dumps(d)

        resp = self.invoke("GetCubePod", d, **kwargs)
        return apis.GetCubePodResponseSchema().loads(resp)

    def list_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListCubePod - 获取Pods列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Group** (str) - 组名称
        - **Limit** (int) - 默认20
        - **Offset** (int) - 默认0
        - **SubnetId** (str) - 子网Id
        - **VPCId** (str) - VPC的Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Pods** (list) - Pod列表，每条数据都做了base64编码
        - **TotalCount** (int) - Cube的总数

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListCubePodRequestSchema().dumps(d)

        resp = self.invoke("ListCubePod", d, **kwargs)
        return apis.ListCubePodResponseSchema().loads(resp)

    def modify_cube_extend_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyCubeExtendInfo - 修改Cube额外信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - (Required) cube的id
        - **Name** (str) - 修改的名字，规则（^[a-zA-Z0-9-_.\u4e00-\u9fa5]{1,32}）
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyCubeExtendInfoRequestSchema().dumps(d)

        resp = self.invoke("ModifyCubeExtendInfo", d, **kwargs)
        return apis.ModifyCubeExtendInfoResponseSchema().loads(resp)

    def renew_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RenewCubePod - 更新Pod

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - (Required) 容器Id
        - **Pod** (str) - (Required) base64编码的Pod的yaml
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Pod** (str) - base64编码过的yaml，需要解码获取信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RenewCubePodRequestSchema().dumps(d)

        resp = self.invoke("RenewCubePod", d, **kwargs)
        return apis.RenewCubePodResponseSchema().loads(resp)
