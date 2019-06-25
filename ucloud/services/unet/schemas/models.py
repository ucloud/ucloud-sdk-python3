from ucloud.core.typesystem import schema, fields


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


class VIPSetSchema(schema.ResponseSchema):
    """ VIPSet - VIPSet
    """

    fields = {
        "VIP": fields.Str(required=False, load_from="VIP"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


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
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
        "BandwidthPackageId": fields.Str(
            required=False, load_from="BandwidthPackageId"
        ),
        "EnableTime": fields.Int(required=False, load_from="EnableTime"),
        "DisableTime": fields.Int(required=False, load_from="DisableTime"),
    }


class UnetBandwidthUsageEIPSetSchema(schema.ResponseSchema):
    """ UnetBandwidthUsageEIPSet - DescribeBandwidthUsage
    """

    fields = {
        "CurBandwidth": fields.Float(required=False, load_from="CurBandwidth"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
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
        "ShareBandwidthId": fields.Str(required=False, load_from="ShareBandwidthId"),
        "ShareBandwidth": fields.Int(required=False, load_from="ShareBandwidth"),
        "ShareBandwidthName": fields.Str(
            required=False, load_from="ShareBandwidthName"
        ),
    }


class UnetEIPSetSchema(schema.ResponseSchema):
    """ UnetEIPSet - DescribeEIP
    """

    fields = {
        "Resource": UnetEIPResourceSetSchema,
        "PayMode": fields.Str(required=False, load_from="PayMode"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Status": fields.Str(required=False, load_from="Status"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Expire": fields.Bool(required=False, load_from="Expire"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "ShareBandwidthSet": ShareBandwidthSetSchema,
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
    }


class FirewallRuleSetSchema(schema.ResponseSchema):
    """ FirewallRuleSet - DescribeFirewall
    """

    fields = {
        "SrcIP": fields.Str(required=False, load_from="SrcIP"),
        "Priority": fields.Str(required=False, load_from="Priority"),
        "ProtocolType": fields.Str(required=False, load_from="ProtocolType"),
        "DstPort": fields.Str(required=False, load_from="DstPort"),
        "RuleAction": fields.Str(required=False, load_from="RuleAction"),
        "Remark": fields.Str(required=False, load_from="Remark"),
    }


class FirewallDataSetSchema(schema.ResponseSchema):
    """ FirewallDataSet - DescribeFirewall
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ResourceCount": fields.Int(required=False, load_from="ResourceCount"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Rule": fields.List(FirewallRuleSetSchema()),
        "FWId": fields.Str(required=True, load_from="FWId"),
        "GroupId": fields.Str(required=True, load_from="GroupId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
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
        "ShareBandwidthId": fields.Str(required=False, load_from="ShareBandwidthId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "ShareBandwidth": fields.Int(required=False, load_from="ShareBandwidth"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "EIPSet": fields.List(EIPSetDataSchema()),
        "BandwidthGuarantee": fields.Int(
            required=False, load_from="BandwidthGuarantee"
        ),
        "PostPayStartTime": fields.Int(required=False, load_from="PostPayStartTime"),
        "Name": fields.Str(required=False, load_from="Name"),
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


class EIPPayModeSetSchema(schema.ResponseSchema):
    """ EIPPayModeSet - GetEIPPayModeEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPPayMode": fields.Str(required=False, load_from="EIPPayMode"),
    }


class EIPPriceDetailSetSchema(schema.ResponseSchema):
    """ EIPPriceDetailSet - GetEIPPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
        "PurchaseValue": fields.Int(required=False, load_from="PurchaseValue"),
    }
