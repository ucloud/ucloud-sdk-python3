from ucloud.core.typesystem import schema, fields


class UHostImageSetSchema(schema.ResponseSchema):
    """ UHostImageSet - DescribeImage
    """

    fields = {
        "OsName": fields.Str(required=False, load_from="OsName"),
        "Features": fields.List(fields.Str()),
        "Vendor": fields.Str(required=False, load_from="Vendor"),
        "MinimalCPU": fields.Str(required=False, load_from="MinimalCPU"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "ImageDescription": fields.Str(required=False, load_from="ImageDescription"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "IntegratedSoftware": fields.Str(
            required=False, load_from="IntegratedSoftware"
        ),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "ImageType": fields.Str(required=False, load_from="ImageType"),
        "FuncType": fields.Str(required=False, load_from="FuncType"),
        "Links": fields.Str(required=False, load_from="Links"),
        "State": fields.Str(required=False, load_from="State"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
    }


class UHostTagSetSchema(schema.ResponseSchema):
    """ UHostTagSet - DescribeUHostTags
    """

    fields = {
        "Zone": fields.Str(required=False, load_from="Zone"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


class UHostPriceSetSchema(schema.ResponseSchema):
    """ UHostPriceSet - 主机价格
    """

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "Price": fields.Float(required=True, load_from="Price"),
    }


class UHostIPSetSchema(schema.ResponseSchema):
    """ UHostIPSet - DescribeUHostInstance
    """

    fields = {
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IP": fields.Str(required=False, load_from="IP"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(required=False, load_from="Default"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class UHostDiskSetSchema(schema.ResponseSchema):
    """ UHostDiskSet - DescribeUHostInstance
    """

    fields = {
        "IsBoot": fields.Str(required=True, load_from="IsBoot"),
        "Name": fields.Str(required=False, load_from="Name"),
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "Type": fields.Str(required=False, load_from="Type"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "Size": fields.Int(required=False, load_from="Size"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "Encrypted": fields.Bool(required=False, load_from="Encrypted"),
    }


class UHostInstanceSetSchema(schema.ResponseSchema):
    """ UHostInstanceSet - DescribeUHostInstance
    """

    fields = {
        "DiskSet": fields.List(UHostDiskSetSchema()),
        "UHostType": fields.Str(required=False, load_from="UHostType"),
        "BasicImageName": fields.Str(required=False, load_from="BasicImageName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "HostType": fields.Str(required=False, load_from="HostType"),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "TimemachineFeature": fields.Str(
            required=False, load_from="TimemachineFeature"
        ),
        "IPSet": fields.List(UHostIPSetSchema()),
        "SubnetType": fields.Str(required=False, load_from="SubnetType"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "IsolationGroup": fields.Str(required=False, load_from="IsolationGroup"),
        "MachineType": fields.Str(required=False, load_from="MachineType"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "HotplugFeature": fields.Bool(required=False, load_from="HotplugFeature"),
        "LifeCycle": fields.Str(required=False, load_from="LifeCycle"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "BasicImageId": fields.Str(required=False, load_from="BasicImageId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "State": fields.Str(required=False, load_from="State"),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "StorageType": fields.Str(required=False, load_from="StorageType"),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "NetCapability": fields.Str(required=False, load_from="NetCapability"),
        "TotalDiskSpace": fields.Int(required=False, load_from="TotalDiskSpace"),
        "NetworkState": fields.Str(required=False, load_from="NetworkState"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
    }
