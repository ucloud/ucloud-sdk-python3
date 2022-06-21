""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.ulb.schemas import models

""" ULB API Schema
"""


"""
API: AllocateBackend

添加ULB后端资源实例
"""


class AllocateBackendRequestSchema(schema.RequestSchema):
    """AllocateBackend - 添加ULB后端资源实例"""

    fields = {
        "Enabled": fields.Int(required=False, dump_to="Enabled"),
        "IsBackup": fields.Int(required=False, dump_to="IsBackup"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceIP": fields.Str(required=False, dump_to="ResourceIP"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "Weight": fields.Int(required=False, dump_to="Weight"),
    }


class AllocateBackendResponseSchema(schema.ResponseSchema):
    """AllocateBackend - 添加ULB后端资源实例"""

    fields = {
        "BackendId": fields.Str(required=False, load_from="BackendId"),
    }


"""
API: AllocateBackendBatch


"""


class AllocateBackendBatchRequestSchema(schema.RequestSchema):
    """AllocateBackendBatch -"""

    fields = {
        "ApiVersion": fields.Int(required=False, dump_to="ApiVersion"),
        "Backends": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
    }


class AllocateBackendBatchResponseSchema(schema.ResponseSchema):
    """AllocateBackendBatch -"""

    fields = {
        "BackendSet": fields.List(
            models.BackendSetSchema(), required=False, load_from="BackendSet"
        ),
    }


"""
API: BindSSL

将SSL证书绑定到VServer
"""


class BindSSLRequestSchema(schema.RequestSchema):
    """BindSSL - 将SSL证书绑定到VServer"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SSLId": fields.Str(required=True, dump_to="SSLId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
    }


class BindSSLResponseSchema(schema.ResponseSchema):
    """BindSSL - 将SSL证书绑定到VServer"""

    fields = {}


"""
API: CreatePolicy

创建VServer内容转发策略
"""


class CreatePolicyRequestSchema(schema.RequestSchema):
    """CreatePolicy - 创建VServer内容转发策略"""

    fields = {
        "BackendId": fields.List(fields.Str()),
        "Match": fields.Str(required=True, dump_to="Match"),
        "PolicyPriority": fields.Int(required=False, dump_to="PolicyPriority"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
    }


class CreatePolicyResponseSchema(schema.ResponseSchema):
    """CreatePolicy - 创建VServer内容转发策略"""

    fields = {
        "PolicyId": fields.Str(required=False, load_from="PolicyId"),
    }


"""
API: CreateSSL

创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来
"""


class CreateSSLRequestSchema(schema.RequestSchema):
    """CreateSSL - 创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来"""

    fields = {
        "CaCert": fields.Str(required=False, dump_to="CaCert"),
        "PrivateKey": fields.Str(required=False, dump_to="PrivateKey"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SSLContent": fields.Str(required=False, dump_to="SSLContent"),
        "SSLName": fields.Str(required=True, dump_to="SSLName"),
        "SSLType": fields.Str(required=False, dump_to="SSLType"),
        "UserCert": fields.Str(required=False, dump_to="UserCert"),
    }


class CreateSSLResponseSchema(schema.ResponseSchema):
    """CreateSSL - 创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来"""

    fields = {
        "SSLId": fields.Str(required=False, load_from="SSLId"),
    }


"""
API: CreateULB

创建负载均衡实例，可以选择内网或者外网
"""


class CreateULBRequestSchema(schema.RequestSchema):
    """CreateULB - 创建负载均衡实例，可以选择内网或者外网"""

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "FirewallId": fields.Str(required=False, dump_to="FirewallId"),
        "IPVersion": fields.Str(
            required=False, dump_to="IPVersion"
        ),  # Deprecated, will be removed at 1.0
        "InnerMode": fields.Str(required=False, dump_to="InnerMode"),
        "ListenType": fields.Str(required=False, dump_to="ListenType"),
        "OuterMode": fields.Str(required=False, dump_to="OuterMode"),
        "PrivateIp": fields.Str(
            required=False, dump_to="PrivateIp"
        ),  # Deprecated, will be removed at 1.0
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "ULBName": fields.Str(required=False, dump_to="ULBName"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class CreateULBResponseSchema(schema.ResponseSchema):
    """CreateULB - 创建负载均衡实例，可以选择内网或者外网"""

    fields = {
        "IPv6AddressId": fields.Str(required=False, load_from="IPv6AddressId"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
    }


"""
API: CreateVServer

创建VServer实例，定义监听的协议和端口以及负载均衡算法
"""


class CreateVServerRequestSchema(schema.RequestSchema):
    """CreateVServer - 创建VServer实例，定义监听的协议和端口以及负载均衡算法"""

    fields = {
        "ClientTimeout": fields.Int(required=False, dump_to="ClientTimeout"),
        "Domain": fields.Str(required=False, dump_to="Domain"),
        "FrontendPort": fields.Int(required=False, dump_to="FrontendPort"),
        "ListenType": fields.Str(required=False, dump_to="ListenType"),
        "Method": fields.Str(required=False, dump_to="Method"),
        "MonitorType": fields.Str(required=False, dump_to="MonitorType"),
        "Path": fields.Str(required=False, dump_to="Path"),
        "PersistenceInfo": fields.Str(
            required=False, dump_to="PersistenceInfo"
        ),
        "PersistenceType": fields.Str(
            required=False, dump_to="PersistenceType"
        ),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RequestMsg": fields.Str(required=False, dump_to="RequestMsg"),
        "ResponseMsg": fields.Str(required=False, dump_to="ResponseMsg"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerName": fields.Str(required=False, dump_to="VServerName"),
    }


class CreateVServerResponseSchema(schema.ResponseSchema):
    """CreateVServer - 创建VServer实例，定义监听的协议和端口以及负载均衡算法"""

    fields = {
        "VServerId": fields.Str(required=False, load_from="VServerId"),
    }


"""
API: DeletePolicy

删除内容转发策略
"""


class DeletePolicyRequestSchema(schema.RequestSchema):
    """DeletePolicy - 删除内容转发策略"""

    fields = {
        "GroupId": fields.Str(
            required=False, dump_to="GroupId"
        ),  # Deprecated, will be removed at 1.0
        "PolicyId": fields.Str(required=True, dump_to="PolicyId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VServerId": fields.Str(required=False, dump_to="VServerId"),
    }


class DeletePolicyResponseSchema(schema.ResponseSchema):
    """DeletePolicy - 删除内容转发策略"""

    fields = {}


"""
API: DeleteSSL

删除SSL证书
"""


class DeleteSSLRequestSchema(schema.RequestSchema):
    """DeleteSSL - 删除SSL证书"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SSLId": fields.Str(required=True, dump_to="SSLId"),
    }


class DeleteSSLResponseSchema(schema.ResponseSchema):
    """DeleteSSL - 删除SSL证书"""

    fields = {}


"""
API: DeleteULB

删除负载均衡实例
"""


class DeleteULBRequestSchema(schema.RequestSchema):
    """DeleteULB - 删除负载均衡实例"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ReleaseEip": fields.Bool(required=False, dump_to="ReleaseEip"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
    }


class DeleteULBResponseSchema(schema.ResponseSchema):
    """DeleteULB - 删除负载均衡实例"""

    fields = {}


"""
API: DeleteVServer

删除VServer实例
"""


class DeleteVServerRequestSchema(schema.RequestSchema):
    """DeleteVServer - 删除VServer实例"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
    }


class DeleteVServerResponseSchema(schema.ResponseSchema):
    """DeleteVServer - 删除VServer实例"""

    fields = {}


"""
API: DescribeSSL

获取SSL证书信息
"""


class DescribeSSLRequestSchema(schema.RequestSchema):
    """DescribeSSL - 获取SSL证书信息"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SSLId": fields.Str(required=False, dump_to="SSLId"),
    }


class DescribeSSLResponseSchema(schema.ResponseSchema):
    """DescribeSSL - 获取SSL证书信息"""

    fields = {
        "DataSet": fields.List(
            models.ULBSSLSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeULB

获取ULB详细信息
"""


class DescribeULBRequestSchema(schema.RequestSchema):
    """DescribeULB - 获取ULB详细信息"""

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "ULBId": fields.Str(required=False, dump_to="ULBId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class DescribeULBResponseSchema(schema.ResponseSchema):
    """DescribeULB - 获取ULB详细信息"""

    fields = {
        "DataSet": fields.List(
            models.ULBSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeULBSimple

获取ULB信息
"""


class DescribeULBSimpleRequestSchema(schema.RequestSchema):
    """DescribeULBSimple - 获取ULB信息"""

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "ULBId": fields.Str(required=False, dump_to="ULBId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class DescribeULBSimpleResponseSchema(schema.ResponseSchema):
    """DescribeULBSimple - 获取ULB信息"""

    fields = {
        "DataSet": fields.List(
            models.ULBSimpleSetSchema(), required=True, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeVServer

获取ULB下的VServer的详细信息
"""


class DescribeVServerRequestSchema(schema.RequestSchema):
    """DescribeVServer - 获取ULB下的VServer的详细信息"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ULBId": fields.Str(required=False, dump_to="ULBId"),
        "VServerId": fields.Str(required=False, dump_to="VServerId"),
    }


class DescribeVServerResponseSchema(schema.ResponseSchema):
    """DescribeVServer - 获取ULB下的VServer的详细信息"""

    fields = {
        "DataSet": fields.List(
            models.ULBVServerSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: ReleaseBackend

从VServer释放后端资源实例
"""


class ReleaseBackendRequestSchema(schema.RequestSchema):
    """ReleaseBackend - 从VServer释放后端资源实例"""

    fields = {
        "BackendId": fields.Str(required=True, dump_to="BackendId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
    }


class ReleaseBackendResponseSchema(schema.ResponseSchema):
    """ReleaseBackend - 从VServer释放后端资源实例"""

    fields = {}


"""
API: UnbindSSL

从VServer解绑SSL证书
"""


class UnbindSSLRequestSchema(schema.RequestSchema):
    """UnbindSSL - 从VServer解绑SSL证书"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SSLId": fields.Str(required=True, dump_to="SSLId"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
    }


class UnbindSSLResponseSchema(schema.ResponseSchema):
    """UnbindSSL - 从VServer解绑SSL证书"""

    fields = {}


"""
API: UpdateBackendAttribute

更新ULB后端资源实例(服务节点)属性
"""


class UpdateBackendAttributeRequestSchema(schema.RequestSchema):
    """UpdateBackendAttribute - 更新ULB后端资源实例(服务节点)属性"""

    fields = {
        "BackendId": fields.Str(required=True, dump_to="BackendId"),
        "Enabled": fields.Int(required=False, dump_to="Enabled"),
        "IsBackup": fields.Int(required=False, dump_to="IsBackup"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "Weight": fields.Int(required=False, dump_to="Weight"),
    }


class UpdateBackendAttributeResponseSchema(schema.ResponseSchema):
    """UpdateBackendAttribute - 更新ULB后端资源实例(服务节点)属性"""

    fields = {}


"""
API: UpdatePolicy

更新内容转发规则，包括转发规则后的服务节点
"""


class UpdatePolicyRequestSchema(schema.RequestSchema):
    """UpdatePolicy - 更新内容转发规则，包括转发规则后的服务节点"""

    fields = {
        "BackendId": fields.List(fields.Str()),
        "Match": fields.Str(required=True, dump_to="Match"),
        "PolicyId": fields.Str(required=False, dump_to="PolicyId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Type": fields.Str(required=False, dump_to="Type"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
    }


class UpdatePolicyResponseSchema(schema.ResponseSchema):
    """UpdatePolicy - 更新内容转发规则，包括转发规则后的服务节点"""

    fields = {
        "PolicyId": fields.Str(
            required=False, load_from="PolicyId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: UpdateSSLAttribute

更新修改SSL的属性，如：修改SSLName
"""


class UpdateSSLAttributeRequestSchema(schema.RequestSchema):
    """UpdateSSLAttribute - 更新修改SSL的属性，如：修改SSLName"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SSLId": fields.Str(required=True, dump_to="SSLId"),
        "SSLName": fields.Str(required=True, dump_to="SSLName"),
    }


class UpdateSSLAttributeResponseSchema(schema.ResponseSchema):
    """UpdateSSLAttribute - 更新修改SSL的属性，如：修改SSLName"""

    fields = {}


"""
API: UpdateULBAttribute

更新ULB名字业务组备注等属性字段
"""


class UpdateULBAttributeRequestSchema(schema.RequestSchema):
    """UpdateULBAttribute - 更新ULB名字业务组备注等属性字段"""

    fields = {
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
    }


class UpdateULBAttributeResponseSchema(schema.ResponseSchema):
    """UpdateULBAttribute - 更新ULB名字业务组备注等属性字段"""

    fields = {}


"""
API: UpdateVServerAttribute

更新VServer实例属性
"""


class UpdateVServerAttributeRequestSchema(schema.RequestSchema):
    """UpdateVServerAttribute - 更新VServer实例属性"""

    fields = {
        "ClientTimeout": fields.Int(required=False, dump_to="ClientTimeout"),
        "Domain": fields.Str(required=False, dump_to="Domain"),
        "Method": fields.Str(required=False, dump_to="Method"),
        "MonitorType": fields.Str(required=False, dump_to="MonitorType"),
        "Path": fields.Str(required=False, dump_to="Path"),
        "PersistenceInfo": fields.Str(
            required=False, dump_to="PersistenceInfo"
        ),
        "PersistenceType": fields.Str(
            required=False, dump_to="PersistenceType"
        ),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Protocol": fields.Str(
            required=False, dump_to="Protocol"
        ),  # Deprecated, will be removed at 1.0
        "Region": fields.Str(required=True, dump_to="Region"),
        "RequestMsg": fields.Str(required=False, dump_to="RequestMsg"),
        "ResponseMsg": fields.Str(required=False, dump_to="ResponseMsg"),
        "ULBId": fields.Str(required=True, dump_to="ULBId"),
        "VServerId": fields.Str(required=True, dump_to="VServerId"),
        "VServerName": fields.Str(required=False, dump_to="VServerName"),
    }


class UpdateVServerAttributeResponseSchema(schema.ResponseSchema):
    """UpdateVServerAttribute - 更新VServer实例属性"""

    fields = {}
