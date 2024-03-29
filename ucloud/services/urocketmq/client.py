""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.urocketmq.schemas import apis


class URocketMQClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(URocketMQClient, self).__init__(
            config, transport, middleware, logger
        )

    def create_u_rocket_mq_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateURocketMQGroup - 创建一个 Group, 如果同名 Group 在当前 Service 中已存在, 则会失败.

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - (Required) Group 名称，支持大小写字母、数字及-, _ ，长度1~36
        - **ServiceId** (str) - (Required) Service ID
        - **Remark** (str) - Group 描述.

        **Response**

        - **GroupId** (str) - 新建 Group 的 ID
        - **Message** (str) - 返回信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateURocketMQGroupRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateURocketMQGroup", d, **kwargs)
        return apis.CreateURocketMQGroupResponseSchema().loads(resp)

    def delete_u_rocket_mq_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteURocketMQGroup - 删除一个已存在的 Group

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **GroupName** (str) - (Required) Group名称
        - **ServiceId** (str) - (Required) Service ID

        **Response**

        - **Message** (str) - 返回信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteURocketMQGroupRequestSchema().dumps(d)

        resp = self.invoke("DeleteURocketMQGroup", d, **kwargs)
        return apis.DeleteURocketMQGroupResponseSchema().loads(resp)

    def list_u_rocket_mq_group(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListURocketMQGroup - 获取一个 RocketMQ 服务下的所有 Group

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ServiceId** (str) - (Required) Service ID
        - **Limit** (int) - 最多返回的条目数量, (0, 1000], 默认 50 条
        - **Offset** (int) - 查询起始位置, [0, ∞)

        **Response**

        - **GroupList** (list) - 见 **GroupBaseInfo** 模型定义
        - **Message** (str) - 返回信息
        - **TotalCount** (int) - 记录总数

        **Response Model**

        **GroupBaseInfo**
        - **CreateTime** (int) - Group 创建时间
        - **GroupName** (str) - Group 名称
        - **Id** (str) - Group ID
        - **Remark** (str) - Group 描述


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListURocketMQGroupRequestSchema().dumps(d)

        resp = self.invoke("ListURocketMQGroup", d, **kwargs)
        return apis.ListURocketMQGroupResponseSchema().loads(resp)
