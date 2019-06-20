from ucloud.core.typesystem import schema, fields
from ucloud.services.ulb.schemas import models


""" ULB API Schema
"""


"""
API: DeletePolicy

删除内容转发策略
"""


class DeletePolicyRequestSchema(schema.RequestSchema):
    """ DeletePolicy - 删除内容转发策略
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "PolicyId": fields.Str(required=True, dump_to="PolicyId"),
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "VServerId": fields.Str(required=False, dump_to="VServerId"),
    }


class DeletePolicyResponseSchema(schema.ResponseSchema):
    """ DeletePolicy - 删除内容转发策略
    """

    fields = {}


"""
API: UpdateVServerAttribute

更新VServer实例属性
"""


class UpdateVServerAttributeRequestSchema(schema.RequestSchema):
    """ UpdateVServerAttribute - 更新VServer实例属性
    """

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "VServerName": fields.Str(required=False, dump_to="VServerName"),
        "PersistenceType": fields.Str(required=False, dump_to="PersistenceType"),
        "PersistenceInfo": fields.Str(required=False, dump_to="PersistenceInfo"),
        "MonitorType": fields.Str(required=False, dump_to="MonitorType"),
        "Path": fields.Str(required=False, dump_to="Path"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Method": fields.Str(required=False, dump_to="Method"),
        "ClientTimeout": fields.Int(required=False, dump_to="ClientTimeout"),
        "Domain": fields.Str(required=False, dump_to="Domain"),
    }


class UpdateVServerAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateVServerAttribute - 更新VServer实例属性
    """

    fields = {}


"""
API: BindSSL

将SSL证书绑定到VServer
"""


class BindSSLRequestSchema(schema.RequestSchema):
    """ BindSSL - 将SSL证书绑定到VServer
    """

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "SSLId": fields.Str(required=True, dump_to="SSLId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class BindSSLResponseSchema(schema.ResponseSchema):
    """ BindSSL - 将SSL证书绑定到VServer
    """

    fields = {}


"""
API: CreateVServer

创建VServer实例，定义监听的协议和端口以及负载均衡算法
"""


class CreateVServerRequestSchema(schema.RequestSchema):
    """ CreateVServer - 创建VServer实例，定义监听的协议和端口以及负载均衡算法
    """

    fields = {
        "Method": fields.Str(required=False, dump_to="Method"),
        "PersistenceInfo": fields.Str(required=False, dump_to="PersistenceInfo"),
        "MonitorType": fields.Str(required=False, dump_to="MonitorType"),
        "VServerName": fields.Str(required=False, dump_to="VServerName"),
        "FrontendPort": fields.Int(required=False, dump_to="FrontendPort"),
        "PersistenceType": fields.Str(required=False, dump_to="PersistenceType"),
        "ClientTimeout": fields.Int(required=False, dump_to="ClientTimeout"),
        "Path": fields.Str(required=False, dump_to="Path"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ListenType": fields.Str(required=False, dump_to="ListenType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Domain": fields.Str(required=False, dump_to="Domain"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
    }


class CreateVServerResponseSchema(schema.ResponseSchema):
    """ CreateVServer - 创建VServer实例，定义监听的协议和端口以及负载均衡算法
    """

    fields = {"VServerId": fields.Str(required=False, load_from="VServerId")}


"""
API: DeleteSSL

删除SSL证书
"""


class DeleteSSLRequestSchema(schema.RequestSchema):
    """ DeleteSSL - 删除SSL证书
    """

    fields = {
        "SSLId": fields.Str(required=True, dump_to="SSLId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class DeleteSSLResponseSchema(schema.ResponseSchema):
    """ DeleteSSL - 删除SSL证书
    """

    fields = {}


"""
API: DeleteULB

删除负载均衡实例
"""


class DeleteULBRequestSchema(schema.RequestSchema):
    """ DeleteULB - 删除负载均衡实例
    """

    fields = {
        "ReleaseEip": fields.Bool(required=False, dump_to="ReleaseEip"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
    }


class DeleteULBResponseSchema(schema.ResponseSchema):
    """ DeleteULB - 删除负载均衡实例
    """

    fields = {}


"""
API: DescribeSSL

获取SSL证书信息
"""


class DescribeSSLRequestSchema(schema.RequestSchema):
    """ DescribeSSL - 获取SSL证书信息
    """

    fields = {
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "SSLId": fields.Str(required=False, dump_to="SSLId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
    }


class DescribeSSLResponseSchema(schema.ResponseSchema):
    """ DescribeSSL - 获取SSL证书信息
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.ULBSSLSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeULB

获取ULB详细信息
"""


class DescribeULBRequestSchema(schema.RequestSchema):
    """ DescribeULB - 获取ULB详细信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "ULBId": fields.Str(required=False, dump_to="ULBId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
    }


class DescribeULBResponseSchema(schema.ResponseSchema):
    """ DescribeULB - 获取ULB详细信息
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.ULBSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: UpdateBackendAttribute

更新ULB后端资源实例(服务节点)属性
"""


class UpdateBackendAttributeRequestSchema(schema.RequestSchema):
    """ UpdateBackendAttribute - 更新ULB后端资源实例(服务节点)属性
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "BackendId": fields.Str(required=True, dump_to="BackendId"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "Weight": fields.Int(required=False, dump_to="Weight"),
        "Enabled": fields.Int(required=False, dump_to="Enabled"),
    }


class UpdateBackendAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateBackendAttribute - 更新ULB后端资源实例(服务节点)属性
    """

    fields = {}


"""
API: UpdatePolicy

更新内容转发规则，包括转发规则后的服务节点
"""


class UpdatePolicyRequestSchema(schema.RequestSchema):
    """ UpdatePolicy - 更新内容转发规则，包括转发规则后的服务节点
    """

    fields = {
        "Type": fields.Str(required=False, dump_to="Type"),
        "BackendId": fields.List(fields.Str()),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "Match": fields.Str(required=True, dump_to="Match"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "PolicyId": fields.Str(required=True, dump_to="PolicyId"),
    }


class UpdatePolicyResponseSchema(schema.ResponseSchema):
    """ UpdatePolicy - 更新内容转发规则，包括转发规则后的服务节点
    """

    fields = {"PolicyId": fields.Str(required=False, load_from="PolicyId")}


"""
API: AllocateBackend

添加ULB后端资源实例
"""


class AllocateBackendRequestSchema(schema.RequestSchema):
    """ AllocateBackend - 添加ULB后端资源实例
    """

    fields = {
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
        "Weight": fields.Int(required=False, dump_to="Weight"),
        "Enabled": fields.Int(required=False, dump_to="Enabled"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Port": fields.Int(required=False, dump_to="Port"),
    }


class AllocateBackendResponseSchema(schema.ResponseSchema):
    """ AllocateBackend - 添加ULB后端资源实例
    """

    fields = {"BackendId": fields.Str(required=False, load_from="BackendId")}


"""
API: AllocateBackendBatch

批量添加VServer后端节点
"""


class AllocateBackendBatchRequestSchema(schema.RequestSchema):
    """ AllocateBackendBatch - 批量添加VServer后端节点
    """

    fields = {
        "Backends": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "ApiVersion": fields.Int(required=False, dump_to="ApiVersion"),
    }


class AllocateBackendBatchResponseSchema(schema.ResponseSchema):
    """ AllocateBackendBatch - 批量添加VServer后端节点
    """

    fields = {
        "BackendSet": fields.List(
            models.BackendSetSchema(), required=False, load_from="BackendSet"
        )
    }


"""
API: UpdateULBAttribute

更新ULB名字业务组备注等属性字段
"""


class UpdateULBAttributeRequestSchema(schema.RequestSchema):
    """ UpdateULBAttribute - 更新ULB名字业务组备注等属性字段
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
    }


class UpdateULBAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateULBAttribute - 更新ULB名字业务组备注等属性字段
    """

    fields = {}


"""
API: DeleteVServer

删除VServer实例
"""


class DeleteVServerRequestSchema(schema.RequestSchema):
    """ DeleteVServer - 删除VServer实例
    """

    fields = {
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
    }


class DeleteVServerResponseSchema(schema.ResponseSchema):
    """ DeleteVServer - 删除VServer实例
    """

    fields = {}


"""
API: UnbindSSL

从VServer解绑SSL证书
"""


class UnbindSSLRequestSchema(schema.RequestSchema):
    """ UnbindSSL - 从VServer解绑SSL证书
    """

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "SSLId": fields.Str(required=True, dump_to="SSLId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class UnbindSSLResponseSchema(schema.ResponseSchema):
    """ UnbindSSL - 从VServer解绑SSL证书
    """

    fields = {}


"""
API: CreateULB

创建负载均衡实例，可以选择内网或者外网
"""


class CreateULBRequestSchema(schema.RequestSchema):
    """ CreateULB - 创建负载均衡实例，可以选择内网或者外网
    """

    fields = {
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "PrivateIp": fields.Str(required=False, dump_to="PrivateIp"),
        "OuterMode": fields.Str(required=False, dump_to="OuterMode"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "ULBName": fields.Str(required=False, dump_to="ULBName"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "IPVersion": fields.Str(required=False, dump_to="IPVersion"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "InnerMode": fields.Str(required=False, dump_to="InnerMode"),
        "ListenType": fields.Str(required=False, dump_to="ListenType"),
    }


class CreateULBResponseSchema(schema.ResponseSchema):
    """ CreateULB - 创建负载均衡实例，可以选择内网或者外网
    """

    fields = {"ULBId": fields.Str(required=False, load_from="ULBId")}


"""
API: DescribeVServer

获取ULB下的VServer的详细信息
"""


class DescribeVServerRequestSchema(schema.RequestSchema):
    """ DescribeVServer - 获取ULB下的VServer的详细信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=False, dump_to="VServerId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
    }


class DescribeVServerResponseSchema(schema.ResponseSchema):
    """ DescribeVServer - 获取ULB下的VServer的详细信息
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.ULBVServerSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: ReleaseBackend

从VServer释放后端资源实例
"""


class ReleaseBackendRequestSchema(schema.RequestSchema):
    """ ReleaseBackend - 从VServer释放后端资源实例
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "BackendId": fields.Str(required=True, dump_to="BackendId"),
    }


class ReleaseBackendResponseSchema(schema.ResponseSchema):
    """ ReleaseBackend - 从VServer释放后端资源实例
    """

    fields = {}


"""
API: CreatePolicy

创建VServer内容转发策略
"""


class CreatePolicyRequestSchema(schema.RequestSchema):
    """ CreatePolicy - 创建VServer内容转发策略
    """

    fields = {
        "Match": fields.Str(required=True, dump_to="Match"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "BackendId": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
    }


class CreatePolicyResponseSchema(schema.ResponseSchema):
    """ CreatePolicy - 创建VServer内容转发策略
    """

    fields = {"PolicyId": fields.Str(required=False, load_from="PolicyId")}


"""
API: CreateSSL

创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来
"""


class CreateSSLRequestSchema(schema.RequestSchema):
    """ CreateSSL - 创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来
    """

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "SSLName": fields.Str(required=True, dump_to="SSLName"),
        "SSLType": fields.Str(required=False, dump_to="SSLType"),
        "SSLContent": fields.Str(required=False, dump_to="SSLContent"),
        "UserCert": fields.Str(required=False, dump_to="UserCert"),
        "PrivateKey": fields.Str(required=False, dump_to="PrivateKey"),
        "CaCert": fields.Str(required=False, dump_to="CaCert"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class CreateSSLResponseSchema(schema.ResponseSchema):
    """ CreateSSL - 创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来
    """

    fields = {"SSLId": fields.Str(required=False, load_from="SSLId")}
