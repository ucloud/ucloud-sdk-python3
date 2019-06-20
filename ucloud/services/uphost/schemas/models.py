from ucloud.core.typesystem import schema, fields


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
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
    }


class PHostPriceSetSchema(schema.ResponseSchema):
    """ PHostPriceSet - GetPHostPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
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


class PHostCPUSetSchema(schema.ResponseSchema):
    """ PHostCPUSet - DescribePHost
    """

    fields = {
        "CoreCount": fields.Int(required=False, load_from="CoreCount"),
        "Model": fields.Str(required=False, load_from="Model"),
        "Frequence": fields.Float(required=False, load_from="Frequence"),
        "Count": fields.Int(required=False, load_from="Count"),
    }


class PHostDiskSetSchema(schema.ResponseSchema):
    """ PHostDiskSet - GetPHostTypeInfo
    """

    fields = {
        "Type": fields.Str(required=False, load_from="Type"),
        "Name": fields.Str(required=False, load_from="Name"),
        "IOCap": fields.Int(required=False, load_from="IOCap"),
        "Space": fields.Int(required=False, load_from="Space"),
        "Count": fields.Int(required=False, load_from="Count"),
    }


class PHostSetSchema(schema.ResponseSchema):
    """ PHostSet - DescribePHost
    """

    fields = {
        "Name": fields.Str(required=False, load_from="Name"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "OSname": fields.Str(required=False, load_from="OSname"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "RaidSupported": fields.Str(required=False, load_from="RaidSupported"),
        "PMStatus": fields.Str(required=False, load_from="PMStatus"),
        "SN": fields.Str(required=False, load_from="SN"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "PHostType": fields.Str(required=False, load_from="PHostType"),
        "CPUSet": fields.List(PHostCPUSetSchema()),
        "IPSet": fields.List(PHostIPSetSchema()),
        "PHostId": fields.Str(required=False, load_from="PHostId"),
        "IsSupportKVM": fields.Str(required=False, load_from="IsSupportKVM"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "PowerState": fields.Str(required=False, load_from="PowerState"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "DiskSet": fields.List(PHostDiskSetSchema()),
        "Cluster": fields.Str(required=False, load_from="Cluster"),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "OSType": fields.Str(required=False, load_from="OSType"),
        "Components": fields.Str(required=False, load_from="Components"),
        "Remark": fields.Str(required=False, load_from="Remark"),
    }
