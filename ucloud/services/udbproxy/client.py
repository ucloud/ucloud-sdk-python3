""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.udbproxy.schemas import apis


class UDBProxyClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UDBProxyClient, self).__init__(
            config, transport, middleware, logger
        )

    def list_udb_proxy_client(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUDBProxyClient - 查询代理客户端连接IP信息(实时）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **UDBProxyID** (str) - (Required) 代理ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **NodeClientInfos** (list) - 见 **NodeClientInfo** 模型定义
        - **UDBProxyID** (str) - 代理ID

        **Response Model**

        **NodeClientInfo**
        - **ID** (str) - 代理节点ID
        - **IP** (str) - 代理节点IP
        - **Records** (list) - 见 **ProxyProcesslist** 模型定义


        **ProxyProcesslist**
        - **ClientHost** (str) - 代理连接DB地址
        - **Command** (str) - 显示当前连接的执行的命令
        - **DB** (str) - 当前执行的命令是在哪一个数据库上。如果没有指定数据库，则该值为 NULL
        - **DBID** (str) - 数据库资源ID
        - **Host** (str) - 代理连接DB地址
        - **ID** (int) - 当前连接DB进程ID
        - **Info** (str) - 一般记录的是线程执行的语句
        - **Role** (str) - 数据库角色(主库/从库)
        - **State** (str) - 线程的状态，和 Command 对应
        - **Time** (int) - 表示该线程处于当前状态的时间
        - **User** (str) - 启动这个线程的用户


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUDBProxyClientRequestSchema().dumps(d)

        resp = self.invoke("ListUDBProxyClient", d, **kwargs)
        return apis.ListUDBProxyClientResponseSchema().loads(resp)
