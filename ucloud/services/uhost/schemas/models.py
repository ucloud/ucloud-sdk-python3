from ucloud.core.typesystem import schema, fields


class UHostImageSetSchema(schema.ResponseSchema):
    """ UHostImageSet - DescribeImage
    """

    fields = {
        "FuncType": fields.Str(required=False, load_from="FuncType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "Features": fields.List(fields.Str()),
        "State": fields.Str(required=False, load_from="State"),
        "MinimalCPU": fields.Str(required=False, load_from="MinimalCPU"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "Links": fields.Str(required=False, load_from="Links"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "IntegratedSoftware": fields.Str(
            required=False, load_from="IntegratedSoftware"
        ),
        "Vendor": fields.Str(required=False, load_from="Vendor"),
        "ImageDescription": fields.Str(required=False, load_from="ImageDescription"),
        "ImageType": fields.Str(required=False, load_from="ImageType"),
    }


class UHostIPSetSchema(schema.ResponseSchema):
    """ UHostIPSet - DescribeUHostInstance
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(required=False, load_from="Default"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IP": fields.Str(required=False, load_from="IP"),
    }


class UHostDiskSetSchema(schema.ResponseSchema):
    """ UHostDiskSet - DescribeUHostInstance
    """

    fields = {
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "IsBoot": fields.Str(required=True, load_from="IsBoot"),
        "Encrypted": fields.Bool(required=False, load_from="Encrypted"),
    }


class UHostInstanceSetSchema(schema.ResponseSchema):
    """ UHostInstanceSet - DescribeUHostInstance
    """

    fields = {
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "HotplugFeature": fields.Bool(required=False, load_from="HotplugFeature"),
        "LifeCycle": fields.Str(required=False, load_from="LifeCycle"),
        "IsolationGroup": fields.Str(required=False, load_from="IsolationGroup"),
        "MachineType": fields.Str(required=False, load_from="MachineType"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "TimemachineFeature": fields.Str(
            required=False, load_from="TimemachineFeature"
        ),
        "SubnetType": fields.Str(required=False, load_from="SubnetType"),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BasicImageName": fields.Str(required=False, load_from="BasicImageName"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "State": fields.Str(required=False, load_from="State"),
        "IPSet": fields.List(UHostIPSetSchema()),
        "NetworkState": fields.Str(required=False, load_from="NetworkState"),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "StorageType": fields.Str(required=False, load_from="StorageType"),
        "BasicImageId": fields.Str(required=False, load_from="BasicImageId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "DiskSet": fields.List(UHostDiskSetSchema()),
        "TotalDiskSpace": fields.Int(required=False, load_from="TotalDiskSpace"),
        "UHostType": fields.Str(required=False, load_from="UHostType"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "NetCapability": fields.Str(required=False, load_from="NetCapability"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "HostType": fields.Str(required=False, load_from="HostType"),
    }


class UHostTagSetSchema(schema.ResponseSchema):
    """ UHostTagSet - DescribeUHostTags
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UHostPriceSetSchema(schema.ResponseSchema):
    """ UHostPriceSet - 主机价格
    """

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "Price": fields.Float(required=True, load_from="Price"),
    }
