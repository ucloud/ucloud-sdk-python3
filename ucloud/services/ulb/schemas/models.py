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
        "HashValue": fields.Str(required=False, load_from="HashValue"),
        "SSLId": fields.Str(required=False, load_from="SSLId"),
        "SSLName": fields.Str(required=False, load_from="SSLName"),
    }


class ULBPolicySetSchema(schema.ResponseSchema):
    """ ULBPolicySet - 内容转发详细列表
    """

    fields = {
        "PolicyId": fields.Str(required=False, load_from="PolicyId"),
        "PolicyType": fields.Str(required=False, load_from="PolicyType"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Match": fields.Str(required=False, load_from="Match"),
        "PolicyPriority": fields.Int(required=False, load_from="PolicyPriority"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "BackendSet": fields.List(PolicyBackendSetSchema()),
    }


class ULBBackendSetSchema(schema.ResponseSchema):
    """ ULBBackendSet - DescribeULB
    """

    fields = {
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Enabled": fields.Int(required=False, load_from="Enabled"),
        "Status": fields.Int(required=False, load_from="Status"),
    }


class ULBVServerSetSchema(schema.ResponseSchema):
    """ ULBVServerSet - DescribeULB
    """

    fields = {
        "PersistenceInfo": fields.Str(required=False, load_from="PersistenceInfo"),
        "Status": fields.Int(required=False, load_from="Status"),
        "BackendSet": fields.List(ULBBackendSetSchema()),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
        "FrontendPort": fields.Int(required=False, load_from="FrontendPort"),
        "PersistenceType": fields.Str(required=False, load_from="PersistenceType"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "ClientTimeout": fields.Int(required=False, load_from="ClientTimeout"),
        "Domain": fields.Str(required=True, load_from="Domain"),
        "PolicySet": fields.List(ULBPolicySetSchema()),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
        "Method": fields.Str(required=False, load_from="Method"),
        "SSLSet": fields.List(ULBSSLSetSchema()),
        "MonitorType": fields.Str(required=True, load_from="MonitorType"),
        "Path": fields.Str(required=True, load_from="Path"),
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
        "Name": fields.Str(required=False, load_from="Name"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "Resource": fields.List(fields.Str()),
        "ULBType": fields.Str(required=False, load_from="ULBType"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "IPSet": fields.List(ULBIPSetSchema()),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBName": fields.Str(required=False, load_from="ULBName"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "VServerSet": fields.List(ULBVServerSetSchema()),
    }
