from ucloud.core.typesystem import schema, fields


class BackendSetSchema(schema.ResponseSchema):
    """ BackendSet - ulb添加rs时返回的信息
    """

    fields = {
        "BackendId": fields.Str(required=True, load_from="BackendId"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
    }


class ULBSSLSetSchema(schema.ResponseSchema):
    """ ULBSSLSet - DescribeULB
    """

    fields = {
        "SSLId": fields.Str(required=False, load_from="SSLId"),
        "SSLName": fields.Str(required=False, load_from="SSLName"),
        "HashValue": fields.Str(required=False, load_from="HashValue"),
    }


class PolicyBackendSetSchema(schema.ResponseSchema):
    """ PolicyBackendSet - 内容转发下rs详细信息
    """

    fields = {
        "Port": fields.Int(required=False, load_from="Port"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ObjectId": fields.Str(required=False, load_from="ObjectId"),
    }


class ULBBackendSetSchema(schema.ResponseSchema):
    """ ULBBackendSet - DescribeULB
    """

    fields = {
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Enabled": fields.Int(required=False, load_from="Enabled"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "Status": fields.Int(required=False, load_from="Status"),
        "BackendId": fields.Str(required=False, load_from="BackendId"),
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
        "SSLSet": fields.List(ULBSSLSetSchema()),
        "BackendSet": fields.List(ULBBackendSetSchema()),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
        "MonitorType": fields.Str(required=True, load_from="MonitorType"),
        "Path": fields.Str(required=True, load_from="Path"),
        "Method": fields.Str(required=False, load_from="Method"),
        "PersistenceInfo": fields.Str(required=False, load_from="PersistenceInfo"),
        "Domain": fields.Str(required=True, load_from="Domain"),
        "PersistenceType": fields.Str(required=False, load_from="PersistenceType"),
        "Status": fields.Int(required=False, load_from="Status"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "FrontendPort": fields.Int(required=False, load_from="FrontendPort"),
        "ClientTimeout": fields.Int(required=False, load_from="ClientTimeout"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "PolicySet": fields.List(ULBPolicySetSchema()),
    }


class ULBIPSetSchema(schema.ResponseSchema):
    """ ULBIPSet - DescribeULB
    """

    fields = {
        "EIP": fields.Str(required=False, load_from="EIP"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
    }


class ULBSetSchema(schema.ResponseSchema):
    """ ULBSet - DescribeULB
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VServerSet": fields.List(ULBVServerSetSchema()),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Resource": fields.List(fields.Str()),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBName": fields.Str(required=False, load_from="ULBName"),
        "Name": fields.Str(required=False, load_from="Name"),
        "IPSet": fields.List(ULBIPSetSchema()),
        "ULBType": fields.Str(required=False, load_from="ULBType"),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
    }
