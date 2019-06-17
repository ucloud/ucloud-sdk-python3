import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.ulb.schemas import apis


class ULBClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(ULBClient, self).__init__(config, transport)

    def describe_vserver(self, req: dict = None) -> dict:
        """ DescribeVServer - 获取ULB下的VServer的详细信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ULBId: (Required) 负载均衡实例的Id
        :param Limit: (Optional) 数据分页值
        :param Offset: (Optional) 数据偏移量
        :param VServerId: (Optional) VServer实例的Id；若指定则返回指定的VServer实例的信息； 若不指定则返回当前负载均衡实例下所有VServer的信息
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVServerRequestSchema().dumps(d)
        resp = self.invoke("DescribeVServer", d)
        return apis.DescribeVServerResponseSchema().loads(resp)

    def release_backend(self, req: dict = None) -> dict:
        """ ReleaseBackend - 从VServer释放后端资源实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackendId: (Required) 后端资源实例的ID(ULB后端ID，非资源自身ID)
        :param ULBId: (Required) 负载均衡实例的ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseBackendRequestSchema().dumps(d)
        resp = self.invoke("ReleaseBackend", d)
        return apis.ReleaseBackendResponseSchema().loads(resp)

    def update_backend_attribute(self, req: dict = None) -> dict:
        """ UpdateBackendAttribute - 更新ULB后端资源实例(服务节点)属性

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackendId: (Required) 后端资源实例的ID(ULB后端ID，非资源自身ID)
        :param ULBId: (Required) 负载均衡资源ID
        :param Enabled: (Optional) 后端实例状态开关
        :param Port: (Optional) 后端资源服务端口，取值范围[1-65535]
        :param Weight: (Optional) 所添加的后端RS权重（在加权轮询算法下有效），取值范围[0-100]，默认为1
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateBackendAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateBackendAttribute", d)
        return apis.UpdateBackendAttributeResponseSchema().loads(resp)

    def allocate_backend_batch(self, req: dict = None) -> dict:
        """ AllocateBackendBatch - 批量添加VServer后端节点

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Backends: (Required) 用| 分割字段，格式：ResourceId| ResourceType| Port| Enabled|IP| Weight。ResourceId:所添加的后端资源的资源ID；ResourceType:所添加的后端资源的类型，枚举值：UHost -> 云主机；UPM -> 物理云主机； UDHost -> 私有专区主机；UDocker -> 容器，默认值为“UHost”；Port:所添加的后端资源服务端口，取值范围[1-65535]；Enabled:后端实例状态开关，枚举值： 1：启用； 0：禁用；IP:后端资源内网ip；Weight：所添加的后端RS权重（在加权轮询算法下有效），取值范围[0-100]，默认为1
        :param ULBId: (Required) 负载均衡实例的ID
        :param VServerId: (Required) VServer实例的ID
        :param ApiVersion: (Optional) 
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateBackendBatchRequestSchema().dumps(d)
        resp = self.invoke("AllocateBackendBatch", d)
        return apis.AllocateBackendBatchResponseSchema().loads(resp)

    def bind_ssl(self, req: dict = None) -> dict:
        """ BindSSL - 将SSL证书绑定到VServer

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SSLId: (Required) SSL证书的Id
        :param ULBId: (Required) 所绑定ULB实例ID
        :param VServerId: (Required) 所绑定VServer实例ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BindSSLRequestSchema().dumps(d)
        resp = self.invoke("BindSSL", d)
        return apis.BindSSLResponseSchema().loads(resp)

    def describe_ulb(self, req: dict = None) -> dict:
        """ DescribeULB - 获取ULB详细信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BusinessId: (Optional) ULB所属的业务组ID
        :param Limit: (Optional) 数据分页值，默认为20
        :param Offset: (Optional) 数据偏移量，默认为0
        :param SubnetId: (Optional) ULB所属的子网ID
        :param ULBId: (Optional) 负载均衡实例的Id。 若指定则返回指定的负载均衡实例的信息； 若不指定则返回当前数据中心中所有的负载均衡实例的信息
        :param VPCId: (Optional) ULB所属的VPC
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeULBRequestSchema().dumps(d)
        resp = self.invoke("DescribeULB", d)
        return apis.DescribeULBResponseSchema().loads(resp)

    def delete_policy(self, req: dict = None) -> dict:
        """ DeletePolicy - 删除内容转发策略

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param PolicyId: (Required) 内容转发策略ID
        :param GroupId: (Optional) 内容转发策略组ID
        :param VServerId: (Optional) VServer 资源ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeletePolicyRequestSchema().dumps(d)
        resp = self.invoke("DeletePolicy", d)
        return apis.DeletePolicyResponseSchema().loads(resp)

    def unbind_ssl(self, req: dict = None) -> dict:
        """ UnbindSSL - 从VServer解绑SSL证书

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SSLId: (Required) SSL证书的Id
        :param ULBId: (Required) 所绑定ULB实例ID
        :param VServerId: (Required) 所绑定VServer实例ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UnbindSSLRequestSchema().dumps(d)
        resp = self.invoke("UnbindSSL", d)
        return apis.UnbindSSLResponseSchema().loads(resp)

    def update_ulb_attribute(self, req: dict = None) -> dict:
        """ UpdateULBAttribute - 更新ULB名字业务组备注等属性字段

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ULBId: (Required) ULB资源ID
        :param Name: (Optional) 名字
        :param Remark: (Optional) 备注
        :param Tag: (Optional) 业务
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateULBAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateULBAttribute", d)
        return apis.UpdateULBAttributeResponseSchema().loads(resp)

    def delete_ulb(self, req: dict = None) -> dict:
        """ DeleteULB - 删除负载均衡实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ULBId: (Required) 负载均衡实例的ID
        :param ReleaseEip: (Optional) 删除ulb时是否释放绑定的EIP，false标识只解绑EIP，true表示会释放绑定的EIP，默认是false
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteULBRequestSchema().dumps(d)
        resp = self.invoke("DeleteULB", d)
        return apis.DeleteULBResponseSchema().loads(resp)

    def delete_vserver(self, req: dict = None) -> dict:
        """ DeleteVServer - 删除VServer实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ULBId: (Required) 负载均衡实例的ID
        :param VServerId: (Required) VServer实例的ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteVServerRequestSchema().dumps(d)
        resp = self.invoke("DeleteVServer", d)
        return apis.DeleteVServerResponseSchema().loads(resp)

    def update_vserver_attribute(self, req: dict = None) -> dict:
        """ UpdateVServerAttribute - 更新VServer实例属性

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ULBId: (Required) 负载均衡实例ID
        :param VServerId: (Required) VServer实例ID
        :param ClientTimeout: (Optional) 请求代理的VServer下表示空闲连接的回收时间，单位：秒，取值范围：时(0，86400]，默认值为60；报文转发的VServer下表示回话保持的时间，单位：秒，取值范围：[60，900]，0 表示禁用连接保持
        :param Domain: (Optional) MonitorType 为 Path 时指定健康检查发送请求时HTTP HEADER 里的域名
        :param Method: (Optional) VServer负载均衡模式，枚举值：Roundrobin -> 轮询;Source -> 源地址；ConsistentHash -> 一致性哈希；SourcePort -> 源地址（计算端口）；ConsistentHashPort -> 一致性哈希（计算端口）; WeightRoundrobin -> 加权轮询; Leastconn -> 最小连接数。ConsistentHash，SourcePort，ConsistentHashPort 只在报文转发中使用；Leastconn只在请求代理中使用；Roundrobin、Source和WeightRoundrobin在请求代理和报文转发中使用。默认为："Roundrobin"
        :param MonitorType: (Optional) 健康检查的类型，Port:端口,Path:路径
        :param Path: (Optional) MonitorType 为 Path 时指定健康检查发送请求时的路径，默认为 /
        :param PersistenceInfo: (Optional) 根据PersistenceType确定: None或ServerInsert, 此字段无意义; UserDefined, 则此字段传入用户自定义会话保持String. 若无此字段则不做修改
        :param PersistenceType: (Optional) VServer会话保持模式，若无此字段则不做修改。枚举值：None：关闭；ServerInsert：自动生成KEY；UserDefined：用户自定义KEY。
        :param Protocol: (Optional) VServer协议类型，请求代理只支持修改为 HTTP/HTTPS，报文转发VServer只支持修改为 TCP/UDP
        :param VServerName: (Optional) VServer实例名称，若无此字段则不做修改
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateVServerAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateVServerAttribute", d)
        return apis.UpdateVServerAttributeResponseSchema().loads(resp)

    def create_policy(self, req: dict = None) -> dict:
        """ CreatePolicy - 创建VServer内容转发策略

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackendId: (Required) 内容转发策略应用的后端资源实例的ID，来源于 AllocateBackend 返回的 BackendId
        :param Match: (Required) 内容转发匹配字段
        :param ULBId: (Required) 需要添加内容转发策略的负载均衡实例ID
        :param VServerId: (Required) 需要添加内容转发策略的VServer实例ID
        :param Type: (Optional) 内容转发匹配字段的类型
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreatePolicyRequestSchema().dumps(d)
        resp = self.invoke("CreatePolicy", d)
        return apis.CreatePolicyResponseSchema().loads(resp)

    def create_vserver(self, req: dict = None) -> dict:
        """ CreateVServer - 创建VServer实例，定义监听的协议和端口以及负载均衡算法

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ULBId: (Required) 负载均衡实例ID
        :param ClientTimeout: (Optional) ListenType为RequestProxy时表示空闲连接的回收时间，单位：秒，取值范围：时(0，86400]，默认值为60；ListenType为PacketsTransmit时表示连接保持的时间，单位：秒，取值范围：[60，900]，0 表示禁用连接保持
        :param Domain: (Optional) 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查路径
        :param FrontendPort: (Optional) VServer后端端口，取值范围[1-65535]；默认值为80
        :param ListenType: (Optional) 监听器类型，枚举值为：RequestProxy -> 请求代理；PacketsTransmit -> 报文转发；默认为"RequestProxy"
        :param Method: (Optional) VServer负载均衡模式，枚举值：Roundrobin -> 轮询;Source -> 源地址；ConsistentHash -> 一致性哈希；SourcePort -> 源地址（计算端口）；ConsistentHashPort -> 一致性哈希（计算端口）; WeightRoundrobin -> 加权轮询; Leastconn -> 最小连接数。ConsistentHash，SourcePort，ConsistentHashPort 只在报文转发中使用；Leastconn只在请求代理中使用；Roundrobin、Source和WeightRoundrobin在请求代理和报文转发中使用。默认为："Roundrobin"
        :param MonitorType: (Optional) 健康检查类型，枚举值：Port -> 端口检查；Path -> 路径检查；
        :param Path: (Optional) 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查域名
        :param PersistenceInfo: (Optional) 根据PersistenceType确认； None和ServerInsert： 此字段无意义； UserDefined：此字段传入自定义会话保持String
        :param PersistenceType: (Optional) VServer会话保持方式，默认关闭会话保持。枚举值：None -> 关闭；ServerInsert -> 自动生成KEY；UserDefined -> 用户自定义KEY。
        :param Protocol: (Optional) VServer实例的协议，请求代理模式下有 HTTP、HTTPS、TCP，报文转发下有 TCP，UDP。默认为“HTTP"
        :param VServerName: (Optional) VServer实例名称，默认为"VServer"
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateVServerRequestSchema().dumps(d)
        resp = self.invoke("CreateVServer", d)
        return apis.CreateVServerResponseSchema().loads(resp)

    def delete_ssl(self, req: dict = None) -> dict:
        """ DeleteSSL - 删除SSL证书

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SSLId: (Required) SSL证书的ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteSSLRequestSchema().dumps(d)
        resp = self.invoke("DeleteSSL", d)
        return apis.DeleteSSLResponseSchema().loads(resp)

    def describe_ssl(self, req: dict = None) -> dict:
        """ DescribeSSL - 获取SSL证书信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Optional) 数据分页值，默认为20
        :param Offset: (Optional) 数据偏移量，默认值为0
        :param SSLId: (Optional) SSL证书的Id
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeSSLRequestSchema().dumps(d)
        resp = self.invoke("DescribeSSL", d)
        return apis.DescribeSSLResponseSchema().loads(resp)

    def update_policy(self, req: dict = None) -> dict:
        """ UpdatePolicy - 更新内容转发规则，包括转发规则后的服务节点

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackendId: (Required) 内容转发策略应用的后端资源实例的ID，来源于 AllocateBackend 返回的 BackendId
        :param Match: (Required) 内容转发匹配字段
        :param PolicyId: (Required) 转发规则的ID
        :param ULBId: (Required) 需要添加内容转发策略的负载均衡实例ID
        :param VServerId: (Required) 需要添加内容转发策略的VServer实例ID
        :param Type: (Optional) 内容转发匹配字段的类型
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdatePolicyRequestSchema().dumps(d)
        resp = self.invoke("UpdatePolicy", d)
        return apis.UpdatePolicyResponseSchema().loads(resp)

    def allocate_backend(self, req: dict = None) -> dict:
        """ AllocateBackend - 添加ULB后端资源实例

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param ResourceId: (Required) 所添加的后端资源的资源ID
        :param ResourceType: (Required) 所添加的后端资源的类型，枚举值：UHost -> 云主机；UPM -> 物理云主机； UDHost -> 私有专区主机；UDocker -> 容器，默认值为“UHost”
        :param ULBId: (Required) 负载均衡实例的ID
        :param VServerId: (Required) VServer实例的ID
        :param Enabled: (Optional) 后端实例状态开关，枚举值： 1：启用； 0：禁用 默认为启用
        :param Port: (Optional) 所添加的后端资源服务端口，取值范围[1-65535]，默认80
        :param Weight: (Optional) 所添加的后端RS权重（在加权轮询算法下有效），取值范围[0-100]，默认为1
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateBackendRequestSchema().dumps(d)
        resp = self.invoke("AllocateBackend", d)
        return apis.AllocateBackendResponseSchema().loads(resp)

    def create_ssl(self, req: dict = None) -> dict:
        """ CreateSSL - 创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SSLName: (Required) SSL证书的名字，默认值为空
        :param CaCert: (Optional) CA证书
        :param PrivateKey: (Optional) 加密证书的私钥
        :param SSLContent: (Optional) SSL证书的完整内容，包括用户证书、加密证书的私钥、CA证书
        :param SSLType: (Optional) 所添加的SSL证书类型，目前只支持Pem格式
        :param UserCert: (Optional) 用户的证书
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateSSLRequestSchema().dumps(d)
        resp = self.invoke("CreateSSL", d)
        return apis.CreateSSLResponseSchema().loads(resp)

    def create_ulb(self, req: dict = None) -> dict:
        """ CreateULB - 创建负载均衡实例，可以选择内网或者外网

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BusinessId: (Optional) ULB 所属的业务组ID，如果不传则使用默认的业务组
        :param ChargeType: (Optional) 付费方式
        :param InnerMode: (Optional) 创建的ULB是否为内网模式
        :param OuterMode: (Optional) 创建的ULB是否为外网模式，默认即为外网模式
        :param PrivateIp: (Optional) 创建内网ULB时指定内网IP。若不传值，则随机分配当前子网下的IP（暂时不对外开放，创建外网ULB该字段会忽略）
        :param Remark: (Optional) 备注
        :param SubnetId: (Optional) 内网ULB 所属的子网ID，如果不传则使用默认的子网
        :param Tag: (Optional) 业务组
        :param ULBName: (Optional) 负载均衡的名字，默认值为“ULB”
        :param VPCId: (Optional) ULB所在的VPC的ID, 如果不传则使用默认的VPC
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateULBRequestSchema().dumps(d)
        resp = self.invoke("CreateULB", d)
        return apis.CreateULBResponseSchema().loads(resp)
