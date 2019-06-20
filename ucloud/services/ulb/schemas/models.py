from ucloud.core.typesystem import schema, fields


class BackendSetSchema(schema.ResponseSchema):
    """ BackendSet - ulb添加rs时返回的信息
    """

    fields = {
        "BackendId": fields.Str(required=True, load_from="BackendId"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
    }


class PolicyBackendSetSchema(schema.ResponseSchema):
    """ PolicyBackendSet - 内容转发下rs详细信息
    """

    fields = {
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ObjectId": fields.Str(required=False, load_from="ObjectId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
    }


class ULBSSLSetSchema(schema.ResponseSchema):
    """ ULBSSLSet - DescribeULB
    """

    fields = {
        "SSLId": fields.Str(required=False, load_from="SSLId"),
        "SSLName": fields.Str(required=False, load_from="SSLName"),
        "HashValue": fields.Str(required=False, load_from="HashValue"),
    }


class ULBBackendSetSchema(schema.ResponseSchema):
    """ ULBBackendSet - DescribeULB
    """

    fields = {
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Enabled": fields.Int(required=False, load_from="Enabled"),
        "Status": fields.Int(required=False, load_from="Status"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
    }


class ULBPolicySetSchema(schema.ResponseSchema):
    """ ULBPolicySet - 内容转发详细列表
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "BackendSet": fields.List(PolicyBackendSetSchema()),
        "PolicyId": fields.Str(required=False, load_from="PolicyId"),
        "PolicyType": fields.Str(required=False, load_from="PolicyType"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Match": fields.Str(required=False, load_from="Match"),
        "PolicyPriority": fields.Int(required=False, load_from="PolicyPriority"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
    }


class ULBVServerSetSchema(schema.ResponseSchema):
    """ ULBVServerSet - DescribeULB
    """

    fields = {
        "PolicySet": fields.List(ULBPolicySetSchema()),
        "MonitorType": fields.Str(required=True, load_from="MonitorType"),
        "Path": fields.Str(required=True, load_from="Path"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "ClientTimeout": fields.Int(required=False, load_from="ClientTimeout"),
        "Status": fields.Int(required=False, load_from="Status"),
        "Domain": fields.Str(required=True, load_from="Domain"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
        "FrontendPort": fields.Int(required=False, load_from="FrontendPort"),
        "Method": fields.Str(required=False, load_from="Method"),
        "PersistenceInfo": fields.Str(required=False, load_from="PersistenceInfo"),
        "BackendSet": fields.List(ULBBackendSetSchema()),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
        "PersistenceType": fields.Str(required=False, load_from="PersistenceType"),
        "SSLSet": fields.List(ULBSSLSetSchema()),
    }


class ULBIPSetSchema(schema.ResponseSchema):
    """ ULBIPSet - DescribeULB
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "EIP": fields.Str(required=False, load_from="EIP"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
    }


class ULBSetSchema(schema.ResponseSchema):
    """ ULBSet - DescribeULB
    """

    fields = {
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBName": fields.Str(required=False, load_from="ULBName"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "VServerSet": fields.List(ULBVServerSetSchema()),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "IPSet": fields.List(ULBIPSetSchema()),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Resource": fields.List(fields.Str()),
        "ULBType": fields.Str(required=False, load_from="ULBType"),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
    }
