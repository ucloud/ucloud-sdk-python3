from ucloud.core.typesystem import schema, fields


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


class PHostCPUSetSchema(schema.ResponseSchema):
    """ PHostCPUSet - DescribePHost
    """

    fields = {
        "Model": fields.Str(required=False, load_from="Model"),
        "Frequence": fields.Float(required=False, load_from="Frequence"),
        "Count": fields.Int(required=False, load_from="Count"),
        "CoreCount": fields.Int(required=False, load_from="CoreCount"),
    }


class PHostDiskSetSchema(schema.ResponseSchema):
    """ PHostDiskSet - GetPHostTypeInfo
    """

    fields = {
        "IOCap": fields.Int(required=False, load_from="IOCap"),
        "Space": fields.Int(required=False, load_from="Space"),
        "Count": fields.Int(required=False, load_from="Count"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class PHostSetSchema(schema.ResponseSchema):
    """ PHostSet - DescribePHost
    """

    fields = {
        "Components": fields.Str(required=False, load_from="Components"),
        "Name": fields.Str(required=False, load_from="Name"),
        "OSname": fields.Str(required=False, load_from="OSname"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "DiskSet": fields.List(PHostDiskSetSchema()),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "PHostType": fields.Str(required=False, load_from="PHostType"),
        "Cluster": fields.Str(required=False, load_from="Cluster"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "CPUSet": fields.List(PHostCPUSetSchema()),
        "IPSet": fields.List(PHostIPSetSchema()),
        "IsSupportKVM": fields.Str(required=False, load_from="IsSupportKVM"),
        "SN": fields.Str(required=False, load_from="SN"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "OSType": fields.Str(required=False, load_from="OSType"),
        "RaidSupported": fields.Str(required=False, load_from="RaidSupported"),
        "PHostId": fields.Str(required=False, load_from="PHostId"),
        "PMStatus": fields.Str(required=False, load_from="PMStatus"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "PowerState": fields.Str(required=False, load_from="PowerState"),
    }


class PHostPriceSetSchema(schema.ResponseSchema):
    """ PHostPriceSet - GetPHostPrice
    """

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
    }


class PHostTagSetSchema(schema.ResponseSchema):
    """ PHostTagSet - DescribePHostTags
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
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
