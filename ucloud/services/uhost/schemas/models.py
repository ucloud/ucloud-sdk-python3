from ucloud.core.typesystem import schema, fields


class UHostDiskSetSchema(schema.ResponseSchema):
    """ UHostDiskSet - DescribeUHostInstance
    """

    fields = {
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "IsBoot": fields.Str(required=True, load_from="IsBoot"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "Encrypted": fields.Bool(required=False, load_from="Encrypted"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Drive": fields.Str(required=False, load_from="Drive"),
    }


class UHostIPSetSchema(schema.ResponseSchema):
    """ UHostIPSet - DescribeUHostInstance
    """

    fields = {
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IP": fields.Str(required=False, load_from="IP"),
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(required=False, load_from="Default"),
    }


class UHostInstanceSetSchema(schema.ResponseSchema):
    """ UHostInstanceSet - DescribeUHostInstance
    """

    fields = {
        "HostType": fields.Str(required=False, load_from="HostType"),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "UHostType": fields.Str(required=False, load_from="UHostType"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "IsolationGroup": fields.Str(required=False, load_from="IsolationGroup"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "SubnetType": fields.Str(required=False, load_from="SubnetType"),
        "LifeCycle": fields.Str(required=False, load_from="LifeCycle"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "BasicImageId": fields.Str(required=False, load_from="BasicImageId"),
        "BasicImageName": fields.Str(required=False, load_from="BasicImageName"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "NetworkState": fields.Str(required=False, load_from="NetworkState"),
        "TimemachineFeature": fields.Str(
            required=False, load_from="TimemachineFeature"
        ),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "TotalDiskSpace": fields.Int(required=False, load_from="TotalDiskSpace"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "DiskSet": fields.List(UHostDiskSetSchema()),
        "IPSet": fields.List(UHostIPSetSchema()),
        "NetCapability": fields.Str(required=False, load_from="NetCapability"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "MachineType": fields.Str(required=False, load_from="MachineType"),
        "StorageType": fields.Str(required=False, load_from="StorageType"),
        "State": fields.Str(required=False, load_from="State"),
        "Name": fields.Str(required=False, load_from="Name"),
        "HotplugFeature": fields.Bool(required=False, load_from="HotplugFeature"),
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


class UHostImageSetSchema(schema.ResponseSchema):
    """ UHostImageSet - DescribeImage
    """

    fields = {
        "Zone": fields.Str(required=False, load_from="Zone"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "State": fields.Str(required=False, load_from="State"),
        "MinimalCPU": fields.Str(required=False, load_from="MinimalCPU"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "FuncType": fields.Str(required=False, load_from="FuncType"),
        "IntegratedSoftware": fields.Str(
            required=False, load_from="IntegratedSoftware"
        ),
        "Vendor": fields.Str(required=False, load_from="Vendor"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ImageType": fields.Str(required=False, load_from="ImageType"),
        "Features": fields.List(fields.Str()),
        "Links": fields.Str(required=False, load_from="Links"),
        "ImageDescription": fields.Str(required=False, load_from="ImageDescription"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
    }
