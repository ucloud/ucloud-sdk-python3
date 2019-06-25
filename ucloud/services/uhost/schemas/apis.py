from ucloud.core.typesystem import schema, fields
from ucloud.services.uhost.schemas import models


""" UHost API Schema
"""


"""
API: CopyCustomImage

复制自制镜像
"""


class CopyCustomImageRequestSchema(schema.RequestSchema):
    """ CopyCustomImage - 复制自制镜像
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SourceImageId": fields.Str(required=True, dump_to="SourceImageId"),
        "TargetProjectId": fields.Str(required=True, dump_to="TargetProjectId"),
        "TargetRegion": fields.Str(required=False, dump_to="TargetRegion"),
        "TargetImageName": fields.Str(required=False, dump_to="TargetImageName"),
        "TargetImageDescription": fields.Str(
            required=False, dump_to="TargetImageDescription"
        ),
    }


class CopyCustomImageResponseSchema(schema.ResponseSchema):
    """ CopyCustomImage - 复制自制镜像
    """

    fields = {"TargetImageId": fields.Str(required=False, load_from="TargetImageId")}


"""
API: CreateCustomImage

从指定UHost实例，生成自定义镜像。
"""


class CreateCustomImageRequestSchema(schema.RequestSchema):
    """ CreateCustomImage - 从指定UHost实例，生成自定义镜像。
    """

    fields = {
        "ImageDescription": fields.Str(required=False, dump_to="ImageDescription"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "ImageName": fields.Str(required=True, dump_to="ImageName"),
    }


class CreateCustomImageResponseSchema(schema.ResponseSchema):
    """ CreateCustomImage - 从指定UHost实例，生成自定义镜像。
    """

    fields = {"ImageId": fields.Str(required=False, load_from="ImageId")}


"""
API: CreateUHostInstance

创建UHost实例。
"""


class CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSHSchema(schema.RequestSchema):
    """ CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSH - CreateUHostInstance
    """

    fields = {
        "AreaCode": fields.Str(required=False, dump_to="AreaCode"),
        "Port": fields.Int(required=False, dump_to="Port"),
        "Area": fields.Str(required=False, dump_to="Area"),
    }


class CreateUHostInstanceParamNetworkInterfaceEIPSchema(schema.RequestSchema):
    """ CreateUHostInstanceParamNetworkInterfaceEIP - CreateUHostInstance
    """

    fields = {
        "Bandwidth": fields.Int(required=False, dump_to="Bandwidth"),
        "ShareBandwidthId": fields.Str(required=False, dump_to="ShareBandwidthId"),
        "OperatorName": fields.Str(required=False, dump_to="OperatorName"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "GlobalSSH": CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSHSchema(
            required=False, dump_to="GlobalSSH"
        ),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
    }


class CreateUHostInstanceParamDisksSchema(schema.RequestSchema):
    """ CreateUHostInstanceParamDisks - CreateUHostInstance
    """

    fields = {
        "IsBoot": fields.Str(required=True, dump_to="IsBoot"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "BackupType": fields.Str(required=False, dump_to="BackupType"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Encrypted": fields.Bool(required=False, dump_to="Encrypted"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "KmsKeyId": fields.Str(required=False, dump_to="KmsKeyId"),
    }


class CreateUHostInstanceParamNetworkInterfaceSchema(schema.RequestSchema):
    """ CreateUHostInstanceParamNetworkInterface - CreateUHostInstance
    """

    fields = {
        "EIP": CreateUHostInstanceParamNetworkInterfaceEIPSchema(
            required=False, dump_to="EIP"
        )
    }


class CreateUHostInstanceRequestSchema(schema.RequestSchema):
    """ CreateUHostInstance - 创建UHost实例。
    """

    fields = {
        "PrivateIp": fields.List(fields.Str()),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "InstallAgent": fields.Str(required=False, dump_to="InstallAgent"),
        "StorageType": fields.Str(required=False, dump_to="StorageType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "KeyPair": fields.Str(required=False, dump_to="KeyPair"),
        "NetCapability": fields.Str(required=False, dump_to="NetCapability"),
        "HostType": fields.Str(required=False, dump_to="HostType"),
        "SetId": fields.Int(required=False, dump_to="SetId"),
        "MachineType": fields.Str(required=False, dump_to="MachineType"),
        "NetworkInterface": fields.List(
            CreateUHostInstanceParamNetworkInterfaceSchema()
        ),
        "Password": fields.Base64(required=True, dump_to="Password"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "NetworkId": fields.Str(required=False, dump_to="NetworkId"),
        "GpuType": fields.Str(required=False, dump_to="GpuType"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "TimemachineFeature": fields.Str(required=False, dump_to="TimemachineFeature"),
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "GPU": fields.Int(required=False, dump_to="GPU"),
        "IsolationGroup": fields.Str(required=False, dump_to="IsolationGroup"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Disks": fields.List(CreateUHostInstanceParamDisksSchema()),
        "LoginMode": fields.Str(required=True, dump_to="LoginMode"),
        "MinimalCpuPlatform": fields.Str(required=False, dump_to="MinimalCpuPlatform"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostType": fields.Str(required=False, dump_to="UHostType"),
        "AlarmTemplateId": fields.Int(required=False, dump_to="AlarmTemplateId"),
        "UserDataScript": fields.Str(required=False, dump_to="UserDataScript"),
        "ResourceType": fields.Int(required=False, dump_to="ResourceType"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "HotplugFeature": fields.Bool(required=False, dump_to="HotplugFeature"),
        "PrivateMac": fields.Str(required=False, dump_to="PrivateMac"),
        "SecurityGroupId": fields.Str(required=False, dump_to="SecurityGroupId"),
        "MaxCount": fields.Int(required=False, dump_to="MaxCount"),
    }


class CreateUHostInstanceResponseSchema(schema.ResponseSchema):
    """ CreateUHostInstance - 创建UHost实例。
    """

    fields = {
        "UHostIds": fields.List(fields.Str(), required=False, load_from="UHostIds"),
        "IPs": fields.List(fields.Str(), required=False, load_from="IPs"),
    }


"""
API: DescribeImage

获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。
"""


class DescribeImageRequestSchema(schema.RequestSchema):
    """ DescribeImage - 获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageType": fields.Str(required=False, dump_to="ImageType"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "PriceSet": fields.Int(required=False, dump_to="PriceSet"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "OsType": fields.Str(required=False, dump_to="OsType"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
    }


class DescribeImageResponseSchema(schema.ResponseSchema):
    """ DescribeImage - 获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "ImageSet": fields.List(
            models.UHostImageSetSchema(), required=False, load_from="ImageSet"
        ),
    }


"""
API: DescribeUHostInstance

获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。
"""


class DescribeUHostInstanceRequestSchema(schema.RequestSchema):
    """ DescribeUHostInstance - 获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "LifeCycle": fields.Int(required=False, dump_to="LifeCycle"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "IsolationGroup": fields.Str(required=False, dump_to="IsolationGroup"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "UHostIds": fields.List(fields.Str()),
    }


class DescribeUHostInstanceResponseSchema(schema.ResponseSchema):
    """ DescribeUHostInstance - 获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "UHostSet": fields.List(
            models.UHostInstanceSetSchema(), required=False, load_from="UHostSet"
        ),
    }


"""
API: DescribeUHostTags

获取指定数据中心的业务组列表。
"""


class DescribeUHostTagsRequestSchema(schema.RequestSchema):
    """ DescribeUHostTags - 获取指定数据中心的业务组列表。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUHostTagsResponseSchema(schema.ResponseSchema):
    """ DescribeUHostTags - 获取指定数据中心的业务组列表。
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "TagSet": fields.List(
            models.UHostTagSetSchema(), required=False, load_from="TagSet"
        ),
    }


"""
API: GetUHostInstancePrice

根据UHost实例配置，获取UHost实例的价格。
"""


class GetUHostInstancePriceParamDisksSchema(schema.RequestSchema):
    """ GetUHostInstancePriceParamDisks - GetUHostInstancePrice
    """

    fields = {
        "BackupType": fields.Str(required=False, dump_to="BackupType"),
        "IsBoot": fields.Str(required=True, dump_to="IsBoot"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "Size": fields.Int(required=True, dump_to="Size"),
    }


class GetUHostInstancePriceRequestSchema(schema.RequestSchema):
    """ GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。
    """

    fields = {
        "NetCapability": fields.Str(required=False, dump_to="NetCapability"),
        "LifeCycle": fields.Int(required=False, dump_to="LifeCycle"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "CPU": fields.Int(required=True, dump_to="CPU"),
        "Memory": fields.Int(required=True, dump_to="Memory"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "TimemachineFeature": fields.Str(required=False, dump_to="TimemachineFeature"),
        "MachineType": fields.Str(required=False, dump_to="MachineType"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "StorageType": fields.Str(required=False, dump_to="StorageType"),
        "Disks": fields.List(GetUHostInstancePriceParamDisksSchema()),
        "UHostType": fields.Str(required=False, dump_to="UHostType"),
        "GpuType": fields.Str(required=False, dump_to="GpuType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Count": fields.Int(required=True, dump_to="Count"),
        "GPU": fields.Int(required=False, dump_to="GPU"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
    }


class GetUHostInstancePriceResponseSchema(schema.ResponseSchema):
    """ GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。
    """

    fields = {
        "PriceSet": fields.List(
            models.UHostPriceSetSchema(), required=False, load_from="PriceSet"
        )
    }


"""
API: GetUHostInstanceVncInfo

获取指定UHost实例的管理VNC配置详细信息。
"""


class GetUHostInstanceVncInfoRequestSchema(schema.RequestSchema):
    """ GetUHostInstanceVncInfo - 获取指定UHost实例的管理VNC配置详细信息。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
    }


class GetUHostInstanceVncInfoResponseSchema(schema.ResponseSchema):
    """ GetUHostInstanceVncInfo - 获取指定UHost实例的管理VNC配置详细信息。
    """

    fields = {
        "VncIP": fields.Str(required=False, load_from="VncIP"),
        "VncPort": fields.Int(required=False, load_from="VncPort"),
        "VncPassword": fields.Str(required=False, load_from="VncPassword"),
        "UhostId": fields.Str(required=False, load_from="UhostId"),
    }


"""
API: GetUHostUpgradePrice

获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
"""


class GetUHostUpgradePriceRequestSchema(schema.RequestSchema):
    """ GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {
        "HostType": fields.Str(required=False, dump_to="HostType"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "TimemachineFeature": fields.Str(required=False, dump_to="TimemachineFeature"),
        "NetCapValue": fields.Int(required=False, dump_to="NetCapValue"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Memory": fields.Int(required=False, dump_to="Memory"),
    }


class GetUHostUpgradePriceResponseSchema(schema.ResponseSchema):
    """ GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: ImportCustomImage

把UFile的镜像文件导入到UHost，生成自定义镜像
"""


class ImportCustomImageRequestSchema(schema.RequestSchema):
    """ ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Format": fields.Str(required=True, dump_to="Format"),
        "Auth": fields.Bool(required=True, dump_to="Auth"),
        "ImageDescription": fields.Str(required=False, dump_to="ImageDescription"),
        "OsName": fields.Str(required=True, dump_to="OsName"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ImageName": fields.Str(required=True, dump_to="ImageName"),
        "UFileUrl": fields.Str(required=True, dump_to="UFileUrl"),
        "OsType": fields.Str(required=True, dump_to="OsType"),
    }


class ImportCustomImageResponseSchema(schema.ResponseSchema):
    """ ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像
    """

    fields = {"ImageId": fields.Str(required=False, load_from="ImageId")}


"""
API: ModifyUHostInstanceName

修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。
"""


class ModifyUHostInstanceNameRequestSchema(schema.RequestSchema):
    """ ModifyUHostInstanceName - 修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。
    """

    fields = {
        "Name": fields.Str(required=False, dump_to="Name"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
    }


class ModifyUHostInstanceNameResponseSchema(schema.ResponseSchema):
    """ ModifyUHostInstanceName - 修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: ModifyUHostInstanceRemark

修改指定UHost实例备注信息。
"""


class ModifyUHostInstanceRemarkRequestSchema(schema.RequestSchema):
    """ ModifyUHostInstanceRemark - 修改指定UHost实例备注信息。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
    }


class ModifyUHostInstanceRemarkResponseSchema(schema.ResponseSchema):
    """ ModifyUHostInstanceRemark - 修改指定UHost实例备注信息。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: ModifyUHostInstanceTag

修改指定UHost实例业务组标识。
"""


class ModifyUHostInstanceTagRequestSchema(schema.RequestSchema):
    """ ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。
    """

    fields = {
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class ModifyUHostInstanceTagResponseSchema(schema.ResponseSchema):
    """ ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: PoweroffUHostInstance

直接关闭UHost实例电源，无需等待实例正常关闭。
"""


class PoweroffUHostInstanceRequestSchema(schema.RequestSchema):
    """ PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class PoweroffUHostInstanceResponseSchema(schema.ResponseSchema):
    """ PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: RebootUHostInstance

重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。
"""


class RebootUHostInstanceRequestSchema(schema.RequestSchema):
    """ RebootUHostInstance - 重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。
    """

    fields = {
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class RebootUHostInstanceResponseSchema(schema.ResponseSchema):
    """ RebootUHostInstance - 重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: ReinstallUHostInstance

重新安装指定UHost实例的操作系统
"""


class ReinstallUHostInstanceRequestSchema(schema.RequestSchema):
    """ ReinstallUHostInstance - 重新安装指定UHost实例的操作系统
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Password": fields.Base64(required=False, dump_to="Password"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "ReserveDisk": fields.Str(required=False, dump_to="ReserveDisk"),
        "ResourceType": fields.Int(required=False, dump_to="ResourceType"),
        "DNSServers": fields.List(fields.Str()),
    }


class ReinstallUHostInstanceResponseSchema(schema.ResponseSchema):
    """ ReinstallUHostInstance - 重新安装指定UHost实例的操作系统
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: ResetUHostInstancePassword

重置UHost实例的管理员密码。
"""


class ResetUHostInstancePasswordRequestSchema(schema.RequestSchema):
    """ ResetUHostInstancePassword - 重置UHost实例的管理员密码。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Password": fields.Base64(required=True, dump_to="Password"),
    }


class ResetUHostInstancePasswordResponseSchema(schema.ResponseSchema):
    """ ResetUHostInstancePassword - 重置UHost实例的管理员密码。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: ResizeAttachedDisk

修改挂载的磁盘大小，包含系统盘和数据盘
"""


class ResizeAttachedDiskRequestSchema(schema.RequestSchema):
    """ ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘
    """

    fields = {
        "DiskId": fields.Str(required=True, dump_to="DiskId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
    }


class ResizeAttachedDiskResponseSchema(schema.ResponseSchema):
    """ ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘
    """

    fields = {"DiskId": fields.Str(required=False, load_from="DiskId")}


"""
API: ResizeUHostInstance

修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
"""


class ResizeUHostInstanceRequestSchema(schema.RequestSchema):
    """ ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
        "NetCapValue": fields.Int(required=False, dump_to="NetCapValue"),
    }


class ResizeUHostInstanceResponseSchema(schema.ResponseSchema):
    """ ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: StartUHostInstance

启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。
"""


class StartUHostInstanceRequestSchema(schema.RequestSchema):
    """ StartUHostInstance - 启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
    }


class StartUHostInstanceResponseSchema(schema.ResponseSchema):
    """ StartUHostInstance - 启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: StopUHostInstance

指停止处于运行状态的UHost实例，需指定数据中心及UhostID。
"""


class StopUHostInstanceRequestSchema(schema.RequestSchema):
    """ StopUHostInstance - 指停止处于运行状态的UHost实例，需指定数据中心及UhostID。
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class StopUHostInstanceResponseSchema(schema.ResponseSchema):
    """ StopUHostInstance - 指停止处于运行状态的UHost实例，需指定数据中心及UhostID。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: TerminateCustomImage

删除用户自定义镜像
"""


class TerminateCustomImageRequestSchema(schema.RequestSchema):
    """ TerminateCustomImage - 删除用户自定义镜像
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class TerminateCustomImageResponseSchema(schema.ResponseSchema):
    """ TerminateCustomImage - 删除用户自定义镜像
    """

    fields = {"ImageId": fields.Str(required=False, load_from="ImageId")}


"""
API: TerminateUHostInstance

删除指定数据中心的UHost实例。
"""


class TerminateUHostInstanceRequestSchema(schema.RequestSchema):
    """ TerminateUHostInstance - 删除指定数据中心的UHost实例。
    """

    fields = {
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Destroy": fields.Int(required=False, dump_to="Destroy"),
        "ReleaseEIP": fields.Bool(required=False, dump_to="ReleaseEIP"),
        "ReleaseUDisk": fields.Bool(required=False, dump_to="ReleaseUDisk"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class TerminateUHostInstanceResponseSchema(schema.ResponseSchema):
    """ TerminateUHostInstance - 删除指定数据中心的UHost实例。
    """

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "InRecycle": fields.Str(required=True, load_from="InRecycle"),
    }


"""
API: UpgradeToArkUHostInstance

普通升级为方舟机型
"""


class UpgradeToArkUHostInstanceRequestSchema(schema.RequestSchema):
    """ UpgradeToArkUHostInstance - 普通升级为方舟机型
    """

    fields = {
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "UHostIds": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UpgradeToArkUHostInstanceResponseSchema(schema.ResponseSchema):
    """ UpgradeToArkUHostInstance - 普通升级为方舟机型
    """

    fields = {
        "UHostSet": fields.List(fields.Str(), required=False, load_from="UHostSet")
    }
