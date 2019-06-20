from ucloud.core.typesystem import schema, fields


class VIPSetSchema(schema.ResponseSchema):
    """ VIPSet - VIPSet
    """

    fields = {
        "VIP": fields.Str(required=False, load_from="VIP"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class ResourceSetSchema(schema.ResponseSchema):
    """ ResourceSet - 资源信息
    """

    fields = {
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "Status": fields.Int(required=False, load_from="Status"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Zone": fields.Int(required=False, load_from="Zone"),
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceID": fields.Str(required=False, load_from="ResourceID"),
    }


class EIPAddrSetSchema(schema.ResponseSchema):
    """ EIPAddrSet - DescribeShareBandwidth
    """

    fields = {
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "IP": fields.Str(required=False, load_from="IP"),
    }


class EIPSetDataSchema(schema.ResponseSchema):
    """ EIPSetData - describeShareBandwidth
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
    }


class UnetShareBandwidthSetSchema(schema.ResponseSchema):
    """ UnetShareBandwidthSet - DescribeShareBandwidth
    """

    fields = {
        "ShareBandwidthId": fields.Str(required=False, load_from="ShareBandwidthId"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "EIPSet": fields.List(EIPSetDataSchema()),
        "BandwidthGuarantee": fields.Int(
            required=False, load_from="BandwidthGuarantee"
        ),
        "Name": fields.Str(required=False, load_from="Name"),
        "ShareBandwidth": fields.Int(required=False, load_from="ShareBandwidth"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "PostPayStartTime": fields.Int(required=False, load_from="PostPayStartTime"),
    }


class VIPDetailSetSchema(schema.ResponseSchema):
    """ VIPDetailSet - VIPDetailSet
    """

    fields = {
        "RealIp": fields.Str(required=False, load_from="RealIp"),
        "VIP": fields.Str(required=False, load_from="VIP"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
    }


class FirewallRuleSetSchema(schema.ResponseSchema):
    """ FirewallRuleSet - DescribeFirewall
    """

    fields = {
        "DstPort": fields.Str(required=False, load_from="DstPort"),
        "RuleAction": fields.Str(required=False, load_from="RuleAction"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SrcIP": fields.Str(required=False, load_from="SrcIP"),
        "Priority": fields.Str(required=False, load_from="Priority"),
        "ProtocolType": fields.Str(required=False, load_from="ProtocolType"),
    }


class FirewallDataSetSchema(schema.ResponseSchema):
    """ FirewallDataSet - DescribeFirewall
    """

    fields = {
        "ResourceCount": fields.Int(required=False, load_from="ResourceCount"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Rule": fields.List(FirewallRuleSetSchema()),
        "FWId": fields.Str(required=True, load_from="FWId"),
        "GroupId": fields.Str(required=True, load_from="GroupId"),
    }


class EIPPayModeSetSchema(schema.ResponseSchema):
    """ EIPPayModeSet - GetEIPPayModeEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPPayMode": fields.Str(required=False, load_from="EIPPayMode"),
    }


class UnetBandwidthPackageSetSchema(schema.ResponseSchema):
    """ UnetBandwidthPackageSet - DescribeBandwidthPackage
    """

    fields = {
        "BandwidthPackageId": fields.Str(
            required=False, load_from="BandwidthPackageId"
        ),
        "EnableTime": fields.Int(required=False, load_from="EnableTime"),
        "DisableTime": fields.Int(required=False, load_from="DisableTime"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
    }


class UnetBandwidthUsageEIPSetSchema(schema.ResponseSchema):
    """ UnetBandwidthUsageEIPSet - DescribeBandwidthUsage
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "CurBandwidth": fields.Float(required=False, load_from="CurBandwidth"),
    }


class UnetEIPAddrSetSchema(schema.ResponseSchema):
    """ UnetEIPAddrSet - DescribeEIP
    """

    fields = {
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "IP": fields.Str(required=False, load_from="IP"),
    }


class UnetAllocateEIPSetSchema(schema.ResponseSchema):
    """ UnetAllocateEIPSet - AllocateEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
    }


class ShareBandwidthSetSchema(schema.ResponseSchema):
    """ ShareBandwidthSet - DescribeEIP
    """

    fields = {
        "ShareBandwidth": fields.Int(required=False, load_from="ShareBandwidth"),
        "ShareBandwidthName": fields.Str(
            required=False, load_from="ShareBandwidthName"
        ),
        "ShareBandwidthId": fields.Str(required=False, load_from="ShareBandwidthId"),
    }


class UnetEIPResourceSetSchema(schema.ResponseSchema):
    """ UnetEIPResourceSet - DescribeEIP
    """

    fields = {
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
    }


class UnetEIPSetSchema(schema.ResponseSchema):
    """ UnetEIPSet - DescribeEIP
    """

    fields = {
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "ShareBandwidthSet": ShareBandwidthSetSchema,
        "Expire": fields.Bool(required=False, load_from="Expire"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "Status": fields.Str(required=False, load_from="Status"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Resource": UnetEIPResourceSetSchema,
        "PayMode": fields.Str(required=False, load_from="PayMode"),
    }


class EIPPriceDetailSetSchema(schema.ResponseSchema):
    """ EIPPriceDetailSet - GetEIPPrice
    """

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
        "PurchaseValue": fields.Int(required=False, load_from="PurchaseValue"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
    }
