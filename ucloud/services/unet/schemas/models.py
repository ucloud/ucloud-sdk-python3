from ucloud.core.typesystem import schema, fields


class EIPAddrSetSchema(schema.ResponseSchema):
    """ EIPAddrSet - DescribeShareBandwidth
    """

    fields = {
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "IP": fields.Str(required=False, load_from="IP"),
    }


class UnetBandwidthPackageSetSchema(schema.ResponseSchema):
    """ UnetBandwidthPackageSet - DescribeBandwidthPackage
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
        "BandwidthPackageId": fields.Str(
            required=False, load_from="BandwidthPackageId"
        ),
        "EnableTime": fields.Int(required=False, load_from="EnableTime"),
        "DisableTime": fields.Int(required=False, load_from="DisableTime"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
    }


class UnetBandwidthUsageEIPSetSchema(schema.ResponseSchema):
    """ UnetBandwidthUsageEIPSet - DescribeBandwidthUsage
    """

    fields = {
        "CurBandwidth": fields.Float(required=False, load_from="CurBandwidth"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
    }


class EIPPayModeSetSchema(schema.ResponseSchema):
    """ EIPPayModeSet - GetEIPPayModeEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPPayMode": fields.Str(required=False, load_from="EIPPayMode"),
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


class VIPDetailSetSchema(schema.ResponseSchema):
    """ VIPDetailSet - VIPDetailSet
    """

    fields = {
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "RealIp": fields.Str(required=False, load_from="RealIp"),
        "VIP": fields.Str(required=False, load_from="VIP"),
    }


class ResourceSetSchema(schema.ResponseSchema):
    """ ResourceSet - 资源信息
    """

    fields = {
        "Status": fields.Int(required=False, load_from="Status"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Zone": fields.Int(required=False, load_from="Zone"),
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceID": fields.Str(required=False, load_from="ResourceID"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
    }


class EIPPriceDetailSetSchema(schema.ResponseSchema):
    """ EIPPriceDetailSet - GetEIPPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
        "PurchaseValue": fields.Int(required=False, load_from="PurchaseValue"),
    }


class VIPSetSchema(schema.ResponseSchema):
    """ VIPSet - VIPSet
    """

    fields = {
        "VIP": fields.Str(required=False, load_from="VIP"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class UnetEIPResourceSetSchema(schema.ResponseSchema):
    """ UnetEIPResourceSet - DescribeEIP
    """

    fields = {
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
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


class UnetEIPSetSchema(schema.ResponseSchema):
    """ UnetEIPSet - DescribeEIP
    """

    fields = {
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Resource": UnetEIPResourceSetSchema,
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "PayMode": fields.Str(required=False, load_from="PayMode"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "Expire": fields.Bool(required=False, load_from="Expire"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Status": fields.Str(required=False, load_from="Status"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ShareBandwidthSet": ShareBandwidthSetSchema,
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
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Rule": fields.List(FirewallRuleSetSchema()),
        "FWId": fields.Str(required=True, load_from="FWId"),
        "GroupId": fields.Str(required=True, load_from="GroupId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceCount": fields.Int(required=False, load_from="ResourceCount"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class EIPSetDataSchema(schema.ResponseSchema):
    """ EIPSetData - describeShareBandwidth
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
    }


class UnetShareBandwidthSetSchema(schema.ResponseSchema):
    """ UnetShareBandwidthSet - DescribeShareBandwidth
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "ShareBandwidthId": fields.Str(required=False, load_from="ShareBandwidthId"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "BandwidthGuarantee": fields.Int(
            required=False, load_from="BandwidthGuarantee"
        ),
        "PostPayStartTime": fields.Int(required=False, load_from="PostPayStartTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ShareBandwidth": fields.Int(required=False, load_from="ShareBandwidth"),
        "EIPSet": fields.List(EIPSetDataSchema()),
    }
