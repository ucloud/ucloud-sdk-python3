import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.pathx.schemas import apis


class PathXClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(PathXClient, self).__init__(config, transport)

    def describe_global_ssh_area(self, req: dict = None) -> dict:
        """ DescribeGlobalSSHArea - 获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性

        :param ProjectId: (Config) 项目ID,如org-xxxx。请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 机房地域代号，如hk、 us-ca、 us-ws等。不填默认为空，返回所有支持地区。
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeGlobalSSHAreaRequestSchema().dumps(d)
        resp = self.invoke("DescribeGlobalSSHArea", d)
        return apis.DescribeGlobalSSHAreaResponseSchema().loads(resp)

    def describe_global_ssh_instance(self, req: dict = None) -> dict:
        """ DescribeGlobalSSHInstance - 获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）

        :param ProjectId: (Config) 项目ID，如org-xxxx。请参考[GetProjectList接口](../summary/get_project_list.html)
        :param InstanceId: (Optional) 实例ID，资源唯一标识
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.DescribeGlobalSSHInstanceRequestSchema().dumps(d)
        resp = self.invoke("DescribeGlobalSSHInstance", d)
        return apis.DescribeGlobalSSHInstanceResponseSchema().loads(resp)

    def modify_global_ssh_port(self, req: dict = None) -> dict:
        """ ModifyGlobalSSHPort - 修改GlobalSSH端口

        :param ProjectId: (Config) 项目ID，如org-xxxx。请参考[GetProjectList接口](../summary/get_project_list.html)
        :param InstanceId: (Required) 实例ID,资源唯一标识
        :param Port: (Required) 调整后的SSH登陆端口
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.ModifyGlobalSSHPortRequestSchema().dumps(d)
        resp = self.invoke("ModifyGlobalSSHPort", d)
        return apis.ModifyGlobalSSHPortResponseSchema().loads(resp)

    def modify_global_ssh_remark(self, req: dict = None) -> dict:
        """ ModifyGlobalSSHRemark - 修改GlobalSSH备注

        :param ProjectId: (Config) 项目ID，如org-xxxx。请参考[GetProjectList接口](../summary/get_project_list.html)
        :param InstanceId: (Required) 实例ID,资源唯一标识
        :param Remark: (Optional) 备注信息，不填默认为空字符串
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.ModifyGlobalSSHRemarkRequestSchema().dumps(d)
        resp = self.invoke("ModifyGlobalSSHRemark", d)
        return apis.ModifyGlobalSSHRemarkResponseSchema().loads(resp)

    def create_global_ssh_instance(self, req: dict = None) -> dict:
        """ CreateGlobalSSHInstance - 创建GlobalSSH实例

        :param ProjectId: (Config) 项目ID,如org-xxxx。请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Area: (Required) 填写支持SSH访问IP的地区名称，如“洛杉矶”，“新加坡”，“香港”，“东京”，“华盛顿”，“法兰克福”。Area和AreaCode两者必填一个
        :param AreaCode: (Required) AreaCode, 区域航空港国际通用代码。Area和AreaCode两者必填一个
        :param Port: (Required) SSH端口，1-65535且不能使用80，443端口
        :param TargetIP: (Required) 被SSH访问的IP
        :param ChargeType: (Optional) 支付方式，如按月、按年、按时
        :param CouponId: (Optional) 使用代金券可冲抵部分费用
        :param Quantity: (Optional) 购买数量
        :param Remark: (Optional) 备注信息
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.CreateGlobalSSHInstanceRequestSchema().dumps(d)
        resp = self.invoke("CreateGlobalSSHInstance", d)
        return apis.CreateGlobalSSHInstanceResponseSchema().loads(resp)

    def delete_global_ssh_instance(self, req: dict = None) -> dict:
        """ DeleteGlobalSSHInstance - 删除GlobalSSH实例

        :param ProjectId: (Config) 项目ID,如org-xxxx。请参考[GetProjectList接口](../summary/get_project_list.html)
        :param InstanceId: (Required) 实例Id,资源的唯一标识
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.DeleteGlobalSSHInstanceRequestSchema().dumps(d)
        resp = self.invoke("DeleteGlobalSSHInstance", d)
        return apis.DeleteGlobalSSHInstanceResponseSchema().loads(resp)
