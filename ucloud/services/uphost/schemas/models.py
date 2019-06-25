from ucloud.core.typesystem import schema, fields


class PHostCPUSetSchema(schema.ResponseSchema):
    """ PHostCPUSet - DescribePHost
    """

    fields = {
        "Frequence": fields.Float(required=False, load_from="Frequence"),
        "Count": fields.Int(required=False, load_from="Count"),
        "CoreCount": fields.Int(required=False, load_from="CoreCount"),
        "Model": fields.Str(required=False, load_from="Model"),
    }


class PHostIPSetSchema(schema.ResponseSchema):
    """ PHostIPSet - DescribePHost
    """

    fields = {
        "MACAddr": fields.Str(required=False, load_from="MACAddr"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IPAddr": fields.Str(required=False, load_from="IPAddr"),
    }


class PHostDiskSetSchema(schema.ResponseSchema):
    """ PHostDiskSet - GetPHostTypeInfo
    """

    fields = {
        "Name": fields.Str(required=False, load_from="Name"),
        "IOCap": fields.Int(required=False, load_from="IOCap"),
        "Space": fields.Int(required=False, load_from="Space"),
        "Count": fields.Int(required=False, load_from="Count"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class PHostSetSchema(schema.ResponseSchema):
    """ PHostSet - DescribePHost
    """

    fields = {
        "DiskSet": fields.List(PHostDiskSetSchema()),
        "IPSet": fields.List(PHostIPSetSchema()),
        "IsSupportKVM": fields.Str(required=False, load_from="IsSupportKVM"),
        "RaidSupported": fields.Str(required=False, load_from="RaidSupported"),
        "PowerState": fields.Str(required=False, load_from="PowerState"),
        "PHostId": fields.Str(required=False, load_from="PHostId"),
        "PMStatus": fields.Str(required=False, load_from="PMStatus"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "OSname": fields.Str(required=False, load_from="OSname"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "PHostType": fields.Str(required=False, load_from="PHostType"),
        "Components": fields.Str(required=False, load_from="Components"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "CPUSet": fields.List(PHostCPUSetSchema()),
        "SN": fields.Str(required=False, load_from="SN"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "Cluster": fields.Str(required=False, load_from="Cluster"),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "OSType": fields.Str(required=False, load_from="OSType"),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class PHostImageSetSchema(schema.ResponseSchema):
    """ PHostImageSet - DescribePHostImage
    """

    fields = {
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
    }


class PHostTagSetSchema(schema.ResponseSchema):
    """ PHostTagSet - DescribePHostTags
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


class PHostPriceSetSchema(schema.ResponseSchema):
    """ PHostPriceSet - GetPHostPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }
