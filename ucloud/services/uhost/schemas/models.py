from ucloud.core.typesystem import schema, fields


class UHostImageSetSchema(schema.ResponseSchema):
    """ UHostImageSet - DescribeImage
    """

    fields = {
        "ImageType": fields.Str(required=False, load_from="ImageType"),
        "State": fields.Str(required=False, load_from="State"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
        "MinimalCPU": fields.Str(required=False, load_from="MinimalCPU"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "Features": fields.List(fields.Str()),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageDescription": fields.Str(required=False, load_from="ImageDescription"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "IntegratedSoftware": fields.Str(
            required=False, load_from="IntegratedSoftware"
        ),
        "Vendor": fields.Str(required=False, load_from="Vendor"),
        "Links": fields.Str(required=False, load_from="Links"),
        "FuncType": fields.Str(required=False, load_from="FuncType"),
    }


class UHostDiskSetSchema(schema.ResponseSchema):
    """ UHostDiskSet - DescribeUHostInstance
    """

    fields = {
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "IsBoot": fields.Str(required=True, load_from="IsBoot"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Encrypted": fields.Bool(required=False, load_from="Encrypted"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "Size": fields.Int(required=False, load_from="Size"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
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
        "BasicImageId": fields.Str(required=False, load_from="BasicImageId"),
        "NetworkState": fields.Str(required=False, load_from="NetworkState"),
        "LifeCycle": fields.Str(required=False, load_from="LifeCycle"),
        "IsolationGroup": fields.Str(required=False, load_from="IsolationGroup"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "NetCapability": fields.Str(required=False, load_from="NetCapability"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "State": fields.Str(required=False, load_from="State"),
        "TimemachineFeature": fields.Str(
            required=False, load_from="TimemachineFeature"
        ),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "StorageType": fields.Str(required=False, load_from="StorageType"),
        "DiskSet": fields.List(UHostDiskSetSchema()),
        "TotalDiskSpace": fields.Int(required=False, load_from="TotalDiskSpace"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "MachineType": fields.Str(required=False, load_from="MachineType"),
        "BasicImageName": fields.Str(required=False, load_from="BasicImageName"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "HotplugFeature": fields.Bool(required=False, load_from="HotplugFeature"),
        "SubnetType": fields.Str(required=False, load_from="SubnetType"),
        "UHostType": fields.Str(required=False, load_from="UHostType"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "IPSet": fields.List(UHostIPSetSchema()),
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
