""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.uhost.schemas import models

""" UHost API Schema
"""


"""
API: CopyCustomImage

复制自制镜像
"""


class CopyCustomImageRequestSchema(schema.RequestSchema):
    """CopyCustomImage - 复制自制镜像"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SourceImageId": fields.Str(required=True, dump_to="SourceImageId"),
        "TargetImageDescription": fields.Str(
            required=False, dump_to="TargetImageDescription"
        ),
        "TargetImageName": fields.Str(
            required=False, dump_to="TargetImageName"
        ),
        "TargetProjectId": fields.Str(required=True, dump_to="TargetProjectId"),
        "TargetRegion": fields.Str(required=False, dump_to="TargetRegion"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class CopyCustomImageResponseSchema(schema.ResponseSchema):
    """CopyCustomImage - 复制自制镜像"""

    fields = {
        "TargetImageId": fields.Str(required=False, load_from="TargetImageId"),
    }


"""
API: CreateCustomImage

从指定UHost实例，生成自定义镜像。
"""


class CreateCustomImageRequestSchema(schema.RequestSchema):
    """CreateCustomImage - 从指定UHost实例，生成自定义镜像。"""

    fields = {
        "ImageDescription": fields.Str(
            required=False, dump_to="ImageDescription"
        ),
        "ImageName": fields.Str(required=True, dump_to="ImageName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class CreateCustomImageResponseSchema(schema.ResponseSchema):
    """CreateCustomImage - 从指定UHost实例，生成自定义镜像。"""

    fields = {
        "ImageId": fields.Str(required=False, load_from="ImageId"),
    }


"""
API: CreateIsolationGroup

创建硬件隔离组，组内机器严格隔离在不同宿主机上。
"""


class CreateIsolationGroupRequestSchema(schema.RequestSchema):
    """CreateIsolationGroup - 创建硬件隔离组，组内机器严格隔离在不同宿主机上。"""

    fields = {
        "GroupName": fields.Str(required=True, dump_to="GroupName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
    }


class CreateIsolationGroupResponseSchema(schema.ResponseSchema):
    """CreateIsolationGroup - 创建硬件隔离组，组内机器严格隔离在不同宿主机上。"""

    fields = {
        "GroupId": fields.Str(required=True, load_from="GroupId"),
    }


"""
API: CreateUHostInstance

创建UHost实例。
"""


class CreateUHostInstanceParamDisksSchema(schema.RequestSchema):
    """CreateUHostInstanceParamDisks -"""

    fields = {
        "BackupType": fields.Str(required=False, dump_to="BackupType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Encrypted": fields.Bool(required=False, dump_to="Encrypted"),
        "IsBoot": fields.Str(required=True, dump_to="IsBoot"),
        "KmsKeyId": fields.Str(required=False, dump_to="KmsKeyId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=True, dump_to="Type"),
    }


class CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSHSchema(
    schema.RequestSchema
):
    """CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSH -"""

    fields = {
        "Area": fields.Str(required=False, dump_to="Area"),
        "AreaCode": fields.Str(required=False, dump_to="AreaCode"),
        "Port": fields.Int(required=False, dump_to="Port"),
    }


class CreateUHostInstanceParamNetworkInterfaceEIPSchema(schema.RequestSchema):
    """CreateUHostInstanceParamNetworkInterfaceEIP -"""

    fields = {
        "Bandwidth": fields.Int(required=False, dump_to="Bandwidth"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "GlobalSSH": CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSHSchema(
            required=False, dump_to="GlobalSSH"
        ),
        "OperatorName": fields.Str(required=False, dump_to="OperatorName"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "ShareBandwidthId": fields.Str(
            required=False, dump_to="ShareBandwidthId"
        ),
    }


class CreateUHostInstanceParamNetworkInterfaceIPv6Schema(schema.RequestSchema):
    """CreateUHostInstanceParamNetworkInterfaceIPv6 -"""

    fields = {
        "Adress": fields.Str(
            required=False, dump_to="Adress"
        ),  # Deprecated, will be removed at 1.0
        "ShareBandwidthId": fields.Str(
            required=False, dump_to="ShareBandwidthId"
        ),  # Deprecated, will be removed at 1.0
    }


class CreateUHostInstanceParamNetworkInterfaceSchema(schema.RequestSchema):
    """CreateUHostInstanceParamNetworkInterface -"""

    fields = {
        "CreateCernetIp": fields.Bool(required=False, dump_to="CreateCernetIp"),
        "EIP": CreateUHostInstanceParamNetworkInterfaceEIPSchema(
            required=False, dump_to="EIP"
        ),
        "IPv6": CreateUHostInstanceParamNetworkInterfaceIPv6Schema(
            required=False, dump_to="IPv6"
        ),  # Deprecated, will be removed at 1.0
    }


class CreateUHostInstanceParamVirtualGpuGPUVirtualGpuSchema(
    schema.RequestSchema
):
    """CreateUHostInstanceParamVirtualGpuGPUVirtualGpu -"""

    fields = {}


class CreateUHostInstanceParamVolumesSchema(schema.RequestSchema):
    """CreateUHostInstanceParamVolumes -"""

    fields = {}


class CreateUHostInstanceParamVirtualGpuSchema(schema.RequestSchema):
    """CreateUHostInstanceParamVirtualGpu -"""

    fields = {}


class CreateUHostInstanceRequestSchema(schema.RequestSchema):
    """CreateUHostInstance - 创建UHost实例。"""

    fields = {
        "AlarmTemplateId": fields.Int(
            required=False, dump_to="AlarmTemplateId"
        ),
        "AutoDataDiskInit": fields.Str(
            required=False, dump_to="AutoDataDiskInit"
        ),
        "BootDiskSpace": fields.Int(
            required=False, dump_to="BootDiskSpace"
        ),  # Deprecated, will be removed at 1.0
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "DiskPassword": fields.Str(
            required=False, dump_to="DiskPassword"
        ),  # Deprecated, will be removed at 1.0
        "DiskSpace": fields.Int(
            required=False, dump_to="DiskSpace"
        ),  # Deprecated, will be removed at 1.0
        "Disks": fields.List(CreateUHostInstanceParamDisksSchema()),
        "GPU": fields.Int(required=False, dump_to="GPU"),
        "GpuType": fields.Str(required=False, dump_to="GpuType"),
        "HostIp": fields.Str(
            required=False, dump_to="HostIp"
        ),  # Deprecated, will be removed at 1.0
        "HostType": fields.Str(
            required=False, dump_to="HostType"
        ),  # Deprecated, will be removed at 1.0
        "HotplugFeature": fields.Bool(required=False, dump_to="HotplugFeature"),
        "HpcEnhanced": fields.Bool(required=False, dump_to="HpcEnhanced"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "InstallAgent": fields.Str(
            required=False, dump_to="InstallAgent"
        ),  # Deprecated, will be removed at 1.0
        "IsolationGroup": fields.Str(required=False, dump_to="IsolationGroup"),
        "KeyPair": fields.Str(
            required=False, dump_to="KeyPair"
        ),  # Deprecated, will be removed at 1.0
        "LoginMode": fields.Str(required=True, dump_to="LoginMode"),
        "MachineType": fields.Str(required=False, dump_to="MachineType"),
        "MaxCount": fields.Int(required=False, dump_to="MaxCount"),
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "MinimalCpuPlatform": fields.Str(
            required=False, dump_to="MinimalCpuPlatform"
        ),
        "Name": fields.Str(required=False, dump_to="Name"),
        "NetCapability": fields.Str(required=False, dump_to="NetCapability"),
        "NetworkId": fields.Str(
            required=False, dump_to="NetworkId"
        ),  # Deprecated, will be removed at 1.0
        "NetworkInterface": fields.List(
            CreateUHostInstanceParamNetworkInterfaceSchema()
        ),
        "Password": fields.Base64(required=True, dump_to="Password"),
        "PrivateIp": fields.List(fields.Str()),
        "PrivateMac": fields.Str(
            required=False, dump_to="PrivateMac"
        ),  # Deprecated, will be removed at 1.0
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceType": fields.Str(
            required=False, dump_to="ResourceType"
        ),  # Deprecated, will be removed at 1.0
        "RestrictMode": fields.Str(required=False, dump_to="RestrictMode"),
        "SecurityGroupId": fields.Str(
            required=False, dump_to="SecurityGroupId"
        ),
        "SetId": fields.Int(
            required=False, dump_to="SetId"
        ),  # Deprecated, will be removed at 1.0
        "StorageType": fields.Str(
            required=False, dump_to="StorageType"
        ),  # Deprecated, will be removed at 1.0
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "TimemachineFeature": fields.Str(
            required=False, dump_to="TimemachineFeature"
        ),  # Deprecated, will be removed at 1.0
        "UHostType": fields.Str(required=False, dump_to="UHostType"),
        "UserData": fields.Str(required=False, dump_to="UserData"),
        "UserDataScript": fields.Str(
            required=False, dump_to="UserDataScript"
        ),  # Deprecated, will be removed at 1.0
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUHostInstanceResponseSchema(schema.ResponseSchema):
    """CreateUHostInstance - 创建UHost实例。"""

    fields = {
        "IPs": fields.List(fields.Str(), required=False, load_from="IPs"),
        "UHostIds": fields.List(
            fields.Str(), required=False, load_from="UHostIds"
        ),
    }


"""
API: DeleteIsolationGroup

删除硬件隔离组。
"""


class DeleteIsolationGroupRequestSchema(schema.RequestSchema):
    """DeleteIsolationGroup - 删除硬件隔离组。"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DeleteIsolationGroupResponseSchema(schema.ResponseSchema):
    """DeleteIsolationGroup - 删除硬件隔离组。"""

    fields = {
        "GroupId": fields.Str(required=True, load_from="GroupId"),
    }


"""
API: DescribeImage

获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。
"""


class DescribeImageRequestSchema(schema.RequestSchema):
    """DescribeImage - 获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。"""

    fields = {
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "ImageType": fields.Str(required=False, dump_to="ImageType"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "OsType": fields.Str(required=False, dump_to="OsType"),
        "PriceSet": fields.Int(required=False, dump_to="PriceSet"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeImageResponseSchema(schema.ResponseSchema):
    """DescribeImage - 获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。"""

    fields = {
        "Action": fields.Str(required=True, load_from="Action"),
        "ImageSet": fields.List(
            models.UHostImageSetSchema(), required=False, load_from="ImageSet"
        ),
        "RetCode": fields.Int(required=True, load_from="RetCode"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeIsolationGroup

查询硬件隔离组列表。
"""


class DescribeIsolationGroupRequestSchema(schema.RequestSchema):
    """DescribeIsolationGroup - 查询硬件隔离组列表。"""

    fields = {
        "GroupId": fields.Str(required=False, dump_to="GroupId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeIsolationGroupResponseSchema(schema.ResponseSchema):
    """DescribeIsolationGroup - 查询硬件隔离组列表。"""

    fields = {
        "IsolationGroupSet": fields.List(
            models.IsolationGroupSchema(),
            required=False,
            load_from="IsolationGroupSet",
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUHostInstance

获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。
"""


class DescribeUHostInstanceRequestSchema(schema.RequestSchema):
    """DescribeUHostInstance - 获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。"""

    fields = {
        "IsolationGroup": fields.Str(required=False, dump_to="IsolationGroup"),
        "LifeCycle": fields.Int(
            required=False, dump_to="LifeCycle"
        ),  # Deprecated, will be removed at 1.0
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "UDiskIdForAttachment": fields.Str(
            required=False, dump_to="UDiskIdForAttachment"
        ),
        "UHostIds": fields.List(fields.Str()),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUHostInstanceResponseSchema(schema.ResponseSchema):
    """DescribeUHostInstance - 获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。"""

    fields = {
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
        "UHostSet": fields.List(
            models.UHostInstanceSetSchema(), required=True, load_from="UHostSet"
        ),
    }


"""
API: DescribeUHostInstanceSnapshot


"""


class DescribeUHostInstanceSnapshotRequestSchema(schema.RequestSchema):
    """DescribeUHostInstanceSnapshot -"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUHostInstanceSnapshotResponseSchema(schema.ResponseSchema):
    """DescribeUHostInstanceSnapshot -"""

    fields = {
        "SnapshotSet": fields.List(
            models.UHostSnapshotSetSchema(),
            required=False,
            load_from="SnapshotSet",
        ),
        "UhostId": fields.Str(required=False, load_from="UhostId"),
    }


"""
API: DescribeUHostTags

获取指定数据中心的业务组列表。
"""


class DescribeUHostTagsRequestSchema(schema.RequestSchema):
    """DescribeUHostTags - 获取指定数据中心的业务组列表。"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUHostTagsResponseSchema(schema.ResponseSchema):
    """DescribeUHostTags - 获取指定数据中心的业务组列表。"""

    fields = {
        "TagSet": fields.List(
            models.UHostTagSetSchema(), required=False, load_from="TagSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetAttachedDiskUpgradePrice

获取挂载磁盘的升级价格
"""


class GetAttachedDiskUpgradePriceRequestSchema(schema.RequestSchema):
    """GetAttachedDiskUpgradePrice - 获取挂载磁盘的升级价格"""

    fields = {
        "BackupMode": fields.Str(required=False, dump_to="BackupMode"),
        "DiskId": fields.Str(required=True, dump_to="DiskId"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetAttachedDiskUpgradePriceResponseSchema(schema.ResponseSchema):
    """GetAttachedDiskUpgradePrice - 获取挂载磁盘的升级价格"""

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
    }


"""
API: GetUHostInstancePrice

根据UHost实例配置，获取UHost实例的价格。
"""


class GetUHostInstancePriceParamDisksSchema(schema.RequestSchema):
    """GetUHostInstancePriceParamDisks -"""

    fields = {
        "BackupType": fields.Str(required=False, dump_to="BackupType"),
        "IsBoot": fields.Str(required=True, dump_to="IsBoot"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=True, dump_to="Type"),
    }


class GetUHostInstancePriceParamVolumesSchema(schema.RequestSchema):
    """GetUHostInstancePriceParamVolumes -"""

    fields = {}


class GetUHostInstancePriceRequestSchema(schema.RequestSchema):
    """GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。"""

    fields = {
        "CPU": fields.Int(required=True, dump_to="CPU"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Count": fields.Int(required=True, dump_to="Count"),
        "CpuPlatform": fields.Str(required=False, dump_to="CpuPlatform"),
        "DiskSpace": fields.Int(
            required=False, dump_to="DiskSpace"
        ),  # Deprecated, will be removed at 1.0
        "Disks": fields.List(GetUHostInstancePriceParamDisksSchema()),
        "GPU": fields.Int(required=False, dump_to="GPU"),
        "GpuType": fields.Str(required=False, dump_to="GpuType"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "LifeCycle": fields.Int(
            required=False, dump_to="LifeCycle"
        ),  # Deprecated, will be removed at 1.0
        "MachineType": fields.Str(required=False, dump_to="MachineType"),
        "Memory": fields.Int(required=True, dump_to="Memory"),
        "NetCapability": fields.Str(required=False, dump_to="NetCapability"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "StorageType": fields.Str(
            required=False, dump_to="StorageType"
        ),  # Deprecated, will be removed at 1.0
        "TimemachineFeature": fields.Str(
            required=False, dump_to="TimemachineFeature"
        ),  # Deprecated, will be removed at 1.0
        "UHostType": fields.Str(required=False, dump_to="UHostType"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetUHostInstancePriceResponseSchema(schema.ResponseSchema):
    """GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。"""

    fields = {
        "PriceSet": fields.List(
            models.UHostPriceSetSchema(), required=False, load_from="PriceSet"
        ),
    }


"""
API: GetUHostInstanceVncInfo

获取指定UHost实例的管理VNC配置详细信息。
"""


class GetUHostInstanceVncInfoRequestSchema(schema.RequestSchema):
    """GetUHostInstanceVncInfo - 获取指定UHost实例的管理VNC配置详细信息。"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetUHostInstanceVncInfoResponseSchema(schema.ResponseSchema):
    """GetUHostInstanceVncInfo - 获取指定UHost实例的管理VNC配置详细信息。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
        "VncIP": fields.Str(required=False, load_from="VncIP"),
        "VncPassword": fields.Str(required=False, load_from="VncPassword"),
        "VncPort": fields.Int(required=False, load_from="VncPort"),
    }


"""
API: GetUHostUpgradePrice

获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
"""


class GetUHostUpgradePriceRequestSchema(schema.RequestSchema):
    """GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。"""

    fields = {
        "BootDiskSpace": fields.Int(
            required=False, dump_to="BootDiskSpace"
        ),  # Deprecated, will be removed at 1.0
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "DiskSpace": fields.Int(
            required=False, dump_to="DiskSpace"
        ),  # Deprecated, will be removed at 1.0
        "HostType": fields.Str(
            required=False, dump_to="HostType"
        ),  # Deprecated, will be removed at 1.0
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "NetCapValue": fields.Int(required=False, dump_to="NetCapValue"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "TimemachineFeature": fields.Str(
            required=False, dump_to="TimemachineFeature"
        ),  # Deprecated, will be removed at 1.0
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetUHostUpgradePriceResponseSchema(schema.ResponseSchema):
    """GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。"""

    fields = {
        "OriginalPrice": fields.Float(
            required=False, load_from="OriginalPrice"
        ),
        "Price": fields.Float(required=False, load_from="Price"),
    }


"""
API: ImportCustomImage

把UFile的镜像文件导入到UHost，生成自定义镜像
"""


class ImportCustomImageRequestSchema(schema.RequestSchema):
    """ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像"""

    fields = {
        "Auth": fields.Bool(required=True, dump_to="Auth"),
        "Format": fields.Str(required=True, dump_to="Format"),
        "ImageDescription": fields.Str(
            required=False, dump_to="ImageDescription"
        ),
        "ImageName": fields.Str(required=True, dump_to="ImageName"),
        "OsName": fields.Str(required=True, dump_to="OsName"),
        "OsType": fields.Str(required=True, dump_to="OsType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UFileUrl": fields.Str(required=True, dump_to="UFileUrl"),
    }


class ImportCustomImageResponseSchema(schema.ResponseSchema):
    """ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像"""

    fields = {
        "ImageId": fields.Str(required=False, load_from="ImageId"),
    }


"""
API: LeaveIsolationGroup

移除硬件隔离组中的主机
"""


class LeaveIsolationGroupRequestSchema(schema.RequestSchema):
    """LeaveIsolationGroup - 移除硬件隔离组中的主机"""

    fields = {
        "GroupId": fields.Str(required=True, dump_to="GroupId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class LeaveIsolationGroupResponseSchema(schema.ResponseSchema):
    """LeaveIsolationGroup - 移除硬件隔离组中的主机"""

    fields = {
        "UHostId": fields.Str(required=True, load_from="UHostId"),
    }


"""
API: ModifyUHostIP

修改云主机内网 IP 地址
"""


class ModifyUHostIPRequestSchema(schema.RequestSchema):
    """ModifyUHostIP - 修改云主机内网 IP 地址"""

    fields = {
        "PresentIpAddress": fields.Str(
            required=True, dump_to="PresentIpAddress"
        ),
        "PreviousIpAddress": fields.Str(
            required=False, dump_to="PreviousIpAddress"
        ),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ModifyUHostIPResponseSchema(schema.ResponseSchema):
    """ModifyUHostIP - 修改云主机内网 IP 地址"""

    fields = {
        "Message": fields.Str(required=False, load_from="Message"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
    }


"""
API: ModifyUHostInstanceName

修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。
"""


class ModifyUHostInstanceNameRequestSchema(schema.RequestSchema):
    """ModifyUHostInstanceName - 修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。"""

    fields = {
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ModifyUHostInstanceNameResponseSchema(schema.ResponseSchema):
    """ModifyUHostInstanceName - 修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: ModifyUHostInstanceRemark

修改指定UHost实例备注信息。
"""


class ModifyUHostInstanceRemarkRequestSchema(schema.RequestSchema):
    """ModifyUHostInstanceRemark - 修改指定UHost实例备注信息。"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ModifyUHostInstanceRemarkResponseSchema(schema.ResponseSchema):
    """ModifyUHostInstanceRemark - 修改指定UHost实例备注信息。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: ModifyUHostInstanceTag

修改指定UHost实例业务组标识。
"""


class ModifyUHostInstanceTagRequestSchema(schema.RequestSchema):
    """ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ModifyUHostInstanceTagResponseSchema(schema.ResponseSchema):
    """ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: PoweroffUHostInstance

直接关闭UHost实例电源，无需等待实例正常关闭。
"""


class PoweroffUHostInstanceRequestSchema(schema.RequestSchema):
    """PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class PoweroffUHostInstanceResponseSchema(schema.ResponseSchema):
    """PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: RebootUHostInstance

重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。
"""


class RebootUHostInstanceRequestSchema(schema.RequestSchema):
    """RebootUHostInstance - 重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。"""

    fields = {
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class RebootUHostInstanceResponseSchema(schema.ResponseSchema):
    """RebootUHostInstance - 重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: ReinstallUHostInstance

重新安装指定UHost实例的操作系统
"""


class ReinstallUHostInstanceRequestSchema(schema.RequestSchema):
    """ReinstallUHostInstance - 重新安装指定UHost实例的操作系统"""

    fields = {
        "AutoDataDiskInit": fields.Str(
            required=False, dump_to="AutoDataDiskInit"
        ),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
        "DNSServers": fields.List(
            fields.Str()
        ),  # Deprecated, will be removed at 1.0
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "Password": fields.Base64(required=False, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ReserveDisk": fields.Str(required=False, dump_to="ReserveDisk"),
        "ResourceType": fields.Int(
            required=False, dump_to="ResourceType"
        ),  # Deprecated, will be removed at 1.0
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "UserData": fields.Str(required=False, dump_to="UserData"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ReinstallUHostInstanceResponseSchema(schema.ResponseSchema):
    """ReinstallUHostInstance - 重新安装指定UHost实例的操作系统"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: ResetUHostInstancePassword

重置UHost实例的管理员密码。
"""


class ResetUHostInstancePasswordRequestSchema(schema.RequestSchema):
    """ResetUHostInstancePassword - 重置UHost实例的管理员密码。"""

    fields = {
        "Password": fields.Base64(required=True, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ResetUHostInstancePasswordResponseSchema(schema.ResponseSchema):
    """ResetUHostInstancePassword - 重置UHost实例的管理员密码。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: ResizeAttachedDisk

修改挂载的磁盘大小，包含系统盘和数据盘
"""


class ResizeAttachedDiskRequestSchema(schema.RequestSchema):
    """ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘"""

    fields = {
        "DiskId": fields.Str(required=True, dump_to="DiskId"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "DryRun": fields.Bool(required=False, dump_to="DryRun"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ResizeAttachedDiskResponseSchema(schema.ResponseSchema):
    """ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘"""

    fields = {
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "NeedRestart": fields.Bool(required=False, load_from="NeedRestart"),
    }


"""
API: ResizeUHostInstance

修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
"""


class ResizeUHostInstanceRequestSchema(schema.RequestSchema):
    """ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。"""

    fields = {
        "BootDiskSpace": fields.Int(
            required=False, dump_to="BootDiskSpace"
        ),  # Deprecated, will be removed at 1.0
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "DiskSpace": fields.Int(
            required=False, dump_to="DiskSpace"
        ),  # Deprecated, will be removed at 1.0
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "NetCapValue": fields.Int(required=False, dump_to="NetCapValue"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ResizeUHostInstanceResponseSchema(schema.ResponseSchema):
    """ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: StartUHostInstance

启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。
"""


class StartUHostInstanceRequestSchema(schema.RequestSchema):
    """StartUHostInstance - 启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。"""

    fields = {
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class StartUHostInstanceResponseSchema(schema.ResponseSchema):
    """StartUHostInstance - 启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: StopUHostInstance

指停止处于运行状态的UHost实例，需指定数据中心及UhostID。
"""


class StopUHostInstanceRequestSchema(schema.RequestSchema):
    """StopUHostInstance - 指停止处于运行状态的UHost实例，需指定数据中心及UhostID。"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class StopUHostInstanceResponseSchema(schema.ResponseSchema):
    """StopUHostInstance - 指停止处于运行状态的UHost实例，需指定数据中心及UhostID。"""

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UhostId": fields.Str(
            required=False, load_from="UhostId"
        ),  # Deprecated, will be removed at 1.0
    }


"""
API: TerminateCustomImage

删除用户自定义镜像
"""


class TerminateCustomImageRequestSchema(schema.RequestSchema):
    """TerminateCustomImage - 删除用户自定义镜像"""

    fields = {
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(
            required=False, dump_to="Zone"
        ),  # Deprecated, will be removed at 1.0
    }


class TerminateCustomImageResponseSchema(schema.ResponseSchema):
    """TerminateCustomImage - 删除用户自定义镜像"""

    fields = {
        "ImageId": fields.Str(required=False, load_from="ImageId"),
    }


"""
API: TerminateUHostInstance

删除指定数据中心的UHost实例。
"""


class TerminateUHostInstanceRequestSchema(schema.RequestSchema):
    """TerminateUHostInstance - 删除指定数据中心的UHost实例。"""

    fields = {
        "Destroy": fields.Int(
            required=False, dump_to="Destroy"
        ),  # Deprecated, will be removed at 1.0
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ReleaseEIP": fields.Bool(required=False, dump_to="ReleaseEIP"),
        "ReleaseUDisk": fields.Bool(required=False, dump_to="ReleaseUDisk"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class TerminateUHostInstanceResponseSchema(schema.ResponseSchema):
    """TerminateUHostInstance - 删除指定数据中心的UHost实例。"""

    fields = {
        "InRecycle": fields.Str(required=True, load_from="InRecycle"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
    }


"""
API: UpgradeToArkUHostInstance

普通升级为方舟机型
"""


class UpgradeToArkUHostInstanceRequestSchema(schema.RequestSchema):
    """UpgradeToArkUHostInstance - 普通升级为方舟机型"""

    fields = {
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UHostIds": fields.List(fields.Str()),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class UpgradeToArkUHostInstanceResponseSchema(schema.ResponseSchema):
    """UpgradeToArkUHostInstance - 普通升级为方舟机型"""

    fields = {
        "UHostSet": fields.List(
            fields.Str(), required=False, load_from="UHostSet"
        ),
    }
