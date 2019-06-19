import typing

from ucloud.core.client import Client
from ucloud.services.uaccount.schemas import apis


class UAccountClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        super(UAccountClient, self).__init__(config, transport, middleware)

    def get_project_list(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetProjectList - 获取项目列表

        :param IsFinance: (Optional) 是否是财务账号(Yes: 是, No: 否)
        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetProjectListRequestSchema().dumps(d)

        resp = self.invoke("GetProjectList", d, **kwargs)
        return apis.GetProjectListResponseSchema().loads(resp)

    def get_region(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetRegion - 获取用户在各数据中心的权限等信息

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetRegionRequestSchema().dumps(d)

        resp = self.invoke("GetRegion", d, **kwargs)
        return apis.GetRegionResponseSchema().loads(resp)

    def get_user_info(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetUserInfo - 获取用户信息

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetUserInfoRequestSchema().dumps(d)

        resp = self.invoke("GetUserInfo", d, **kwargs)
        return apis.GetUserInfoResponseSchema().loads(resp)

    def modify_project(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ModifyProject - 修改项目

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param ProjectName: (Required) 新的项目名称
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.ModifyProjectRequestSchema().dumps(d)

        resp = self.invoke("ModifyProject", d, **kwargs)
        return apis.ModifyProjectResponseSchema().loads(resp)

    def terminate_project(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ TerminateProject - 删除项目

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.TerminateProjectRequestSchema().dumps(d)

        resp = self.invoke("TerminateProject", d, **kwargs)
        return apis.TerminateProjectResponseSchema().loads(resp)

    def create_project(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateProject - 创建项目

        :param ProjectName: (Required) 项目名称
        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.CreateProjectRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateProject", d, **kwargs)
        return apis.CreateProjectResponseSchema().loads(resp)
