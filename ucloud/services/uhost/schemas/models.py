from ucloud.core.typesystem import schema, fields


class UHostImageSetSchema(schema.ResponseSchema):
    """ UHostImageSet - DescribeImage
    """

    fields = {
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "Features": fields.List(fields.Str()),
        "Links": fields.Str(required=False, load_from="Links"),
        "ImageDescription": fields.Str(required=False, load_from="ImageDescription"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "Vendor": fields.Str(required=False, load_from="Vendor"),
        "MinimalCPU": fields.Str(required=False, load_from="MinimalCPU"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "IntegratedSoftware": fields.Str(
            required=False, load_from="IntegratedSoftware"
        ),
        "State": fields.Str(required=False, load_from="State"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "ImageType": fields.Str(required=False, load_from="ImageType"),
        "FuncType": fields.Str(required=False, load_from="FuncType"),
    }


class UHostDiskSetSchema(schema.ResponseSchema):
    """ UHostDiskSet - DescribeUHostInstance
    """

    fields = {
        "Type": fields.Str(required=False, load_from="Type"),
        "Size": fields.Int(required=False, load_from="Size"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "IsBoot": fields.Str(required=True, load_from="IsBoot"),
        "Encrypted": fields.Bool(required=False, load_from="Encrypted"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Drive": fields.Str(required=False, load_from="Drive"),
    }


class UHostIPSetSchema(schema.ResponseSchema):
    """ UHostIPSet - DescribeUHostInstance
    """

    fields = {
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IP": fields.Str(required=False, load_from="IP"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(required=False, load_from="Default"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class UHostInstanceSetSchema(schema.ResponseSchema):
    """ UHostInstanceSet - DescribeUHostInstance
    """

    fields = {
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "TotalDiskSpace": fields.Int(required=False, load_from="TotalDiskSpace"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UHostType": fields.Str(required=False, load_from="UHostType"),
        "BasicImageName": fields.Str(required=False, load_from="BasicImageName"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "NetCapability": fields.Str(required=False, load_from="NetCapability"),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "SubnetType": fields.Str(required=False, load_from="SubnetType"),
        "LifeCycle": fields.Str(required=False, load_from="LifeCycle"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "BasicImageId": fields.Str(required=False, load_from="BasicImageId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "IPSet": fields.List(UHostIPSetSchema()),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "HostType": fields.Str(required=False, load_from="HostType"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskSet": fields.List(UHostDiskSetSchema()),
        "NetworkState": fields.Str(required=False, load_from="NetworkState"),
        "TimemachineFeature": fields.Str(
            required=False, load_from="TimemachineFeature"
        ),
        "HotplugFeature": fields.Bool(required=False, load_from="HotplugFeature"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "MachineType": fields.Str(required=False, load_from="MachineType"),
        "StorageType": fields.Str(required=False, load_from="StorageType"),
        "State": fields.Str(required=False, load_from="State"),
        "IsolationGroup": fields.Str(required=False, load_from="IsolationGroup"),
    }


class UHostPriceSetSchema(schema.ResponseSchema):
    """ UHostPriceSet - 主机价格
    """

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "Price": fields.Float(required=True, load_from="Price"),
    }


class UHostTagSetSchema(schema.ResponseSchema):
    """ UHostTagSet - DescribeUHostTags
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }
