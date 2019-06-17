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
        "DisableTime": fields.Int(required=False, load_from="DisableTime"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
        "BandwidthPackageId": fields.Str(
            required=False, load_from="BandwidthPackageId"
        ),
        "EnableTime": fields.Int(required=False, load_from="EnableTime"),
    }


class EIPPriceDetailSetSchema(schema.ResponseSchema):
    """ EIPPriceDetailSet - GetEIPPrice
    """

    fields = {
        "PurchaseValue": fields.Int(required=False, load_from="PurchaseValue"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class UnetEIPAddrSetSchema(schema.ResponseSchema):
    """ UnetEIPAddrSet - DescribeEIP
    """

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
    }


class UnetAllocateEIPSetSchema(schema.ResponseSchema):
    """ UnetAllocateEIPSet - AllocateEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
    }


class UnetBandwidthUsageEIPSetSchema(schema.ResponseSchema):
    """ UnetBandwidthUsageEIPSet - DescribeBandwidthUsage
    """

    fields = {
        "CurBandwidth": fields.Float(required=False, load_from="CurBandwidth"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
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
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
    }


class UnetEIPSetSchema(schema.ResponseSchema):
    """ UnetEIPSet - DescribeEIP
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Status": fields.Str(required=False, load_from="Status"),
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Resource": UnetEIPResourceSetSchema,
        "PayMode": fields.Str(required=False, load_from="PayMode"),
        "ShareBandwidthSet": ShareBandwidthSetSchema,
        "Expire": fields.Bool(required=False, load_from="Expire"),
        "Weight": fields.Int(required=False, load_from="Weight"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
    }


class EIPPayModeSetSchema(schema.ResponseSchema):
    """ EIPPayModeSet - GetEIPPayModeEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPPayMode": fields.Str(required=False, load_from="EIPPayMode"),
    }


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
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceID": fields.Str(required=False, load_from="ResourceID"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "Status": fields.Int(required=False, load_from="Status"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Zone": fields.Int(required=False, load_from="Zone"),
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
    }


class VIPDetailSetSchema(schema.ResponseSchema):
    """ VIPDetailSet - VIPDetailSet
    """

    fields = {
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "RealIp": fields.Str(required=False, load_from="RealIp"),
        "VIP": fields.Str(required=False, load_from="VIP"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Name": fields.Str(required=False, load_from="Name"),
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
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Rule": fields.List(FirewallRuleSetSchema()),
        "FWId": fields.Str(required=True, load_from="FWId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "GroupId": fields.Str(required=True, load_from="GroupId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceCount": fields.Int(required=False, load_from="ResourceCount"),
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
        "ShareBandwidth": fields.Int(required=False, load_from="ShareBandwidth"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "EIPSet": fields.List(EIPSetDataSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
        "ShareBandwidthId": fields.Str(required=False, load_from="ShareBandwidthId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "BandwidthGuarantee": fields.Int(
            required=False, load_from="BandwidthGuarantee"
        ),
        "PostPayStartTime": fields.Int(required=False, load_from="PostPayStartTime"),
    }
