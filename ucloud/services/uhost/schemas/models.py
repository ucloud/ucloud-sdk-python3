""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class UHostImageSetSchema(schema.ResponseSchema):
    """UHostImageSet - DescribeImage"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Features": fields.List(fields.Str()),
        "FuncType": fields.Str(required=False, load_from="FuncType"),
        "ImageDescription": fields.Str(
            required=False, load_from="ImageDescription"
        ),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
        "ImageType": fields.Str(required=False, load_from="ImageType"),
        "IntegratedSoftware": fields.Str(
            required=False, load_from="IntegratedSoftware"
        ),
        "Links": fields.Str(required=False, load_from="Links"),
        "MinimalCPU": fields.Str(required=False, load_from="MinimalCPU"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "State": fields.Str(required=False, load_from="State"),
        "Vendor": fields.Str(required=False, load_from="Vendor"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class SpreadInfoSchema(schema.ResponseSchema):
    """SpreadInfo - 每个可用区中硬件隔离组信息"""

    fields = {
        "UHostCount": fields.Int(required=False, load_from="UHostCount"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class IsolationGroupSchema(schema.ResponseSchema):
    """IsolationGroup - 硬件隔离组信息"""

    fields = {
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SpreadInfoSet": fields.List(SpreadInfoSchema()),
    }


class UHostDiskSetSchema(schema.ResponseSchema):
    """UHostDiskSet - DescribeUHostInstance"""

    fields = {
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "Encrypted": fields.Str(required=False, load_from="Encrypted"),
        "IsBoot": fields.Str(required=True, load_from="IsBoot"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class UHostIPSetSchema(schema.ResponseSchema):
    """UHostIPSet - DescribeUHostInstance"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(required=False, load_from="Default"),
        "IP": fields.Str(required=False, load_from="IP"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "IPMode": fields.Str(required=True, load_from="IPMode"),
        "Mac": fields.Str(required=False, load_from="Mac"),
        "NetworkInterfaceId": fields.Str(
            required=False, load_from="NetworkInterfaceId"
        ),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Weight": fields.Int(required=False, load_from="Weight"),
    }


class UHostInstanceSetSchema(schema.ResponseSchema):
    """UHostInstanceSet - DescribeUHostInstance"""

    fields = {
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "BasicImageId": fields.Str(required=False, load_from="BasicImageId"),
        "BasicImageName": fields.Str(
            required=False, load_from="BasicImageName"
        ),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CloudInitFeature": fields.Bool(
            required=False, load_from="CloudInitFeature"
        ),
        "CpuPlatform": fields.Str(required=False, load_from="CpuPlatform"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskSet": fields.List(UHostDiskSetSchema()),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "HostType": fields.Str(required=False, load_from="HostType"),
        "HotplugFeature": fields.Bool(
            required=False, load_from="HotplugFeature"
        ),
        "IPSet": fields.List(UHostIPSetSchema()),
        "IPv6Feature": fields.Bool(required=False, load_from="IPv6Feature"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "IsolationGroup": fields.Str(
            required=False, load_from="IsolationGroup"
        ),
        "LifeCycle": fields.Str(required=False, load_from="LifeCycle"),
        "MachineType": fields.Str(required=False, load_from="MachineType"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "Name": fields.Str(required=False, load_from="Name"),
        "NetCapability": fields.Str(required=False, load_from="NetCapability"),
        "NetworkState": fields.Str(required=False, load_from="NetworkState"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "RdmaClusterId": fields.Str(required=False, load_from="RdmaClusterId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RestrictMode": fields.Str(required=False, load_from="RestrictMode"),
        "State": fields.Str(required=False, load_from="State"),
        "StorageType": fields.Str(required=False, load_from="StorageType"),
        "SubnetType": fields.Str(required=False, load_from="SubnetType"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TimemachineFeature": fields.Str(
            required=False, load_from="TimemachineFeature"
        ),
        "TotalDiskSpace": fields.Int(
            required=False, load_from="TotalDiskSpace"
        ),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UHostType": fields.Str(required=False, load_from="UHostType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UHostSnapshotSetSchema(schema.ResponseSchema):
    """UHostSnapshotSet -"""

    fields = {
        "SnapshotName": fields.Str(required=False, load_from="SnapshotName"),
        "SnapshotState": fields.Str(required=False, load_from="SnapshotState"),
        "SnapshotTime": fields.Str(required=False, load_from="SnapshotTime"),
    }


class UHostTagSetSchema(schema.ResponseSchema):
    """UHostTagSet - DescribeUHostTags"""

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UHostPriceSetSchema(schema.ResponseSchema):
    """UHostPriceSet - 主机价格"""

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "ListPrice": fields.Float(required=False, load_from="ListPrice"),
        "OriginalPrice": fields.Float(required=True, load_from="OriginalPrice"),
        "Price": fields.Float(required=True, load_from="Price"),
    }
