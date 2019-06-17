from ucloud.core.typesystem import schema, fields


class PHostDiskSetSchema(schema.ResponseSchema):
    """ PHostDiskSet - GetPHostTypeInfo
    """

    fields = {
        "Space": fields.Int(required=False, load_from="Space"),
        "Count": fields.Int(required=False, load_from="Count"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Name": fields.Str(required=False, load_from="Name"),
        "IOCap": fields.Int(required=False, load_from="IOCap"),
    }


class PHostCPUSetSchema(schema.ResponseSchema):
    """ PHostCPUSet - DescribePHost
    """

    fields = {
        "CoreCount": fields.Int(required=False, load_from="CoreCount"),
        "Model": fields.Str(required=False, load_from="Model"),
        "Frequence": fields.Float(required=False, load_from="Frequence"),
        "Count": fields.Int(required=False, load_from="Count"),
    }


class PHostIPSetSchema(schema.ResponseSchema):
    """ PHostIPSet - DescribePHost
    """

    fields = {
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IPAddr": fields.Str(required=False, load_from="IPAddr"),
        "MACAddr": fields.Str(required=False, load_from="MACAddr"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
    }


class PHostSetSchema(schema.ResponseSchema):
    """ PHostSet - DescribePHost
    """

    fields = {
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Cluster": fields.Str(required=False, load_from="Cluster"),
        "IsSupportKVM": fields.Str(required=False, load_from="IsSupportKVM"),
        "OSType": fields.Str(required=False, load_from="OSType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "SN": fields.Str(required=False, load_from="SN"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "CPUSet": fields.List(PHostCPUSetSchema()),
        "DiskSet": fields.List(PHostDiskSetSchema()),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "PHostId": fields.Str(required=False, load_from="PHostId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "OSname": fields.Str(required=False, load_from="OSname"),
        "PowerState": fields.Str(required=False, load_from="PowerState"),
        "IPSet": fields.List(PHostIPSetSchema()),
        "Components": fields.Str(required=False, load_from="Components"),
        "RaidSupported": fields.Str(required=False, load_from="RaidSupported"),
        "PMStatus": fields.Str(required=False, load_from="PMStatus"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "PHostType": fields.Str(required=False, load_from="PHostType"),
        "Memory": fields.Int(required=False, load_from="Memory"),
    }


class PHostImageSetSchema(schema.ResponseSchema):
    """ PHostImageSet - DescribePHostImage
    """

    fields = {
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
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
