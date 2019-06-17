from ucloud.core.typesystem import schema, fields


class PolicyBackendSetSchema(schema.ResponseSchema):
    """ PolicyBackendSet - 内容转发下rs详细信息
    """

    fields = {
        "ObjectId": fields.Str(required=False, load_from="ObjectId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
    }


class ULBSSLSetSchema(schema.ResponseSchema):
    """ ULBSSLSet - DescribeULB
    """

    fields = {
        "SSLName": fields.Str(required=False, load_from="SSLName"),
        "HashValue": fields.Str(required=False, load_from="HashValue"),
        "SSLId": fields.Str(required=False, load_from="SSLId"),
    }


class ULBPolicySetSchema(schema.ResponseSchema):
    """ ULBPolicySet - 内容转发详细列表
    """

    fields = {
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "BackendSet": fields.List(PolicyBackendSetSchema()),
        "PolicyId": fields.Str(required=False, load_from="PolicyId"),
        "PolicyType": fields.Str(required=False, load_from="PolicyType"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Match": fields.Str(required=False, load_from="Match"),
        "PolicyPriority": fields.Int(required=False, load_from="PolicyPriority"),
    }


class ULBBackendSetSchema(schema.ResponseSchema):
    """ ULBBackendSet - DescribeULB
    """

    fields = {
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "Status": fields.Int(required=False, load_from="Status"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Enabled": fields.Int(required=False, load_from="Enabled"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Port": fields.Int(required=False, load_from="Port"),
    }


class ULBVServerSetSchema(schema.ResponseSchema):
    """ ULBVServerSet - DescribeULB
    """

    fields = {
        "MonitorType": fields.Str(required=True, load_from="MonitorType"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "Method": fields.Str(required=False, load_from="Method"),
        "BackendSet": fields.List(ULBBackendSetSchema()),
        "PolicySet": fields.List(ULBPolicySetSchema()),
        "Path": fields.Str(required=True, load_from="Path"),
        "PersistenceType": fields.Str(required=False, load_from="PersistenceType"),
        "ClientTimeout": fields.Int(required=False, load_from="ClientTimeout"),
        "Domain": fields.Str(required=True, load_from="Domain"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "FrontendPort": fields.Int(required=False, load_from="FrontendPort"),
        "PersistenceInfo": fields.Str(required=False, load_from="PersistenceInfo"),
        "Status": fields.Int(required=False, load_from="Status"),
        "SSLSet": fields.List(ULBSSLSetSchema()),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
    }


class BackendSetSchema(schema.ResponseSchema):
    """ BackendSet - ulb添加rs时返回的信息
    """

    fields = {
        "BackendId": fields.Str(required=True, load_from="BackendId"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
    }


class ULBIPSetSchema(schema.ResponseSchema):
    """ ULBIPSet - DescribeULB
    """

    fields = {
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "EIP": fields.Str(required=False, load_from="EIP"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
    }


class ULBSetSchema(schema.ResponseSchema):
    """ ULBSet - DescribeULB
    """

    fields = {
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Resource": fields.List(fields.Str()),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "IPSet": fields.List(ULBIPSetSchema()),
        "VServerSet": fields.List(ULBVServerSetSchema()),
        "ULBType": fields.Str(required=False, load_from="ULBType"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
        "ULBName": fields.Str(required=False, load_from="ULBName"),
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Remark": fields.Str(required=False, load_from="Remark"),
    }
