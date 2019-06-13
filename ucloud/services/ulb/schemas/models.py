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
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ObjectId": fields.Str(required=False, load_from="ObjectId"),
        "Port": fields.Int(required=False, load_from="Port"),
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
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "Enabled": fields.Int(required=False, load_from="Enabled"),
        "Status": fields.Int(required=False, load_from="Status"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Weight": fields.Int(required=False, load_from="Weight"),
    }


class ULBPolicySetSchema(schema.ResponseSchema):
    """ ULBPolicySet - 内容转发详细列表
    """

    fields = {
        "BackendSet": fields.List(PolicyBackendSetSchema()),
        "PolicyId": fields.Str(required=False, load_from="PolicyId"),
        "PolicyType": fields.Str(required=False, load_from="PolicyType"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Match": fields.Str(required=False, load_from="Match"),
        "PolicyPriority": fields.Int(required=False, load_from="PolicyPriority"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


class ULBVServerSetSchema(schema.ResponseSchema):
    """ ULBVServerSet - DescribeULB
    """

    fields = {
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "Status": fields.Int(required=False, load_from="Status"),
        "MonitorType": fields.Str(required=True, load_from="MonitorType"),
        "Domain": fields.Str(required=True, load_from="Domain"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
        "Method": fields.Str(required=False, load_from="Method"),
        "BackendSet": fields.List(ULBBackendSetSchema()),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
        "PolicySet": fields.List(ULBPolicySetSchema()),
        "Path": fields.Str(required=True, load_from="Path"),
        "PersistenceType": fields.Str(required=False, load_from="PersistenceType"),
        "PersistenceInfo": fields.Str(required=False, load_from="PersistenceInfo"),
        "ClientTimeout": fields.Int(required=False, load_from="ClientTimeout"),
        "SSLSet": fields.List(ULBSSLSetSchema()),
        "FrontendPort": fields.Int(required=False, load_from="FrontendPort"),
    }


class ULBIPSetSchema(schema.ResponseSchema):
    """ ULBIPSet - DescribeULB
    """

    fields = {
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "EIP": fields.Str(required=False, load_from="EIP"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
    }


class ULBSetSchema(schema.ResponseSchema):
    """ ULBSet - DescribeULB
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "IPSet": fields.List(ULBIPSetSchema()),
        "VServerSet": fields.List(ULBVServerSetSchema()),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBName": fields.Str(required=False, load_from="ULBName"),
        "Resource": fields.List(fields.Str()),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ULBType": fields.Str(required=False, load_from="ULBType"),
    }
