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


class PHostIPSetSchema(schema.ResponseSchema):
    """ PHostIPSet - DescribePHost
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IPAddr": fields.Str(required=False, load_from="IPAddr"),
        "MACAddr": fields.Str(required=False, load_from="MACAddr"),
    }


class PHostCPUSetSchema(schema.ResponseSchema):
    """ PHostCPUSet - DescribePHost
    """

    fields = {
        "Model": fields.Str(required=False, load_from="Model"),
        "Frequence": fields.Float(required=False, load_from="Frequence"),
        "Count": fields.Int(required=False, load_from="Count"),
        "CoreCount": fields.Int(required=False, load_from="CoreCount"),
    }


class PHostSetSchema(schema.ResponseSchema):
    """ PHostSet - DescribePHost
    """

    fields = {
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "PowerState": fields.Str(required=False, load_from="PowerState"),
        "DiskSet": fields.List(PHostDiskSetSchema()),
        "IsSupportKVM": fields.Str(required=False, load_from="IsSupportKVM"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "OSname": fields.Str(required=False, load_from="OSname"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "PHostType": fields.Str(required=False, load_from="PHostType"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "CPUSet": fields.List(PHostCPUSetSchema()),
        "Cluster": fields.Str(required=False, load_from="Cluster"),
        "Components": fields.Str(required=False, load_from="Components"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "RaidSupported": fields.Str(required=False, load_from="RaidSupported"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "IPSet": fields.List(PHostIPSetSchema()),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "OSType": fields.Str(required=False, load_from="OSType"),
        "PMStatus": fields.Str(required=False, load_from="PMStatus"),
        "SN": fields.Str(required=False, load_from="SN"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "PHostId": fields.Str(required=False, load_from="PHostId"),
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
