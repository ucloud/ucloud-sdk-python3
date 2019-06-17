from ucloud.core.typesystem import schema, fields
from ucloud.services.uhost.schemas import models


""" UHost API Schema
"""


"""
API: ReinstallUHostInstance

重新安装指定UHost实例的操作系统
"""


class ReinstallUHostInstanceRequestSchema(schema.RequestSchema):
    """ ReinstallUHostInstance - 重新安装指定UHost实例的操作系统
    """

    fields = {
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
        "DNSServers": fields.List(fields.Str()),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Password": fields.Str(required=False, dump_to="Password"),
        "ReserveDisk": fields.Str(required=False, dump_to="ReserveDisk"),
        "ResourceType": fields.Int(required=False, dump_to="ResourceType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ReinstallUHostInstanceResponseSchema(schema.ResponseSchema):
    """ ReinstallUHostInstance - 重新安装指定UHost实例的操作系统
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: GetUHostUpgradePrice

获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
"""


class GetUHostUpgradePriceRequestSchema(schema.RequestSchema):
    """ GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {
        "HostType": fields.Str(required=False, dump_to="HostType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "TimemachineFeature": fields.Str(required=False, dump_to="TimemachineFeature"),
        "NetCapValue": fields.Int(required=False, dump_to="NetCapValue"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
    }


class GetUHostUpgradePriceResponseSchema(schema.ResponseSchema):
    """ GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: PoweroffUHostInstance

直接关闭UHost实例电源，无需等待实例正常关闭。
"""


class PoweroffUHostInstanceRequestSchema(schema.RequestSchema):
    """ PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
    }


class PoweroffUHostInstanceResponseSchema(schema.ResponseSchema):
    """ PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


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
        "UhostId": fields.Str(required=False, load_from="UhostId"),
        "VncIP": fields.Str(required=False, load_from="VncIP"),
        "VncPort": fields.Int(required=False, load_from="VncPort"),
        "VncPassword": fields.Str(required=False, load_from="VncPassword"),
    }


"""
API: ModifyUHostInstanceTag

修改指定UHost实例业务组标识。
"""


class ModifyUHostInstanceTagRequestSchema(schema.RequestSchema):
    """ ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class ModifyUHostInstanceTagResponseSchema(schema.ResponseSchema):
    """ ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
    }


class RebootUHostInstanceResponseSchema(schema.ResponseSchema):
    """ RebootUHostInstance - 重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: ResizeUHostInstance

修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
"""


class ResizeUHostInstanceRequestSchema(schema.RequestSchema):
    """ ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "NetCapValue": fields.Int(required=False, dump_to="NetCapValue"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
    }


class ResizeUHostInstanceResponseSchema(schema.ResponseSchema):
    """ ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考[[api:uhost-api:uhost_type|云主机机型说明]]。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: CreateCustomImage

从指定UHost实例，生成自定义镜像。
"""


class CreateCustomImageRequestSchema(schema.RequestSchema):
    """ CreateCustomImage - 从指定UHost实例，生成自定义镜像。
    """

    fields = {
        "ImageName": fields.Str(required=True, dump_to="ImageName"),
        "ImageDescription": fields.Str(required=False, dump_to="ImageDescription"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
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
        "Port": fields.Int(required=False, dump_to="Port"),
        "AreaCode": fields.Str(required=False, dump_to="AreaCode"),
        "Area": fields.Str(required=False, dump_to="Area"),
    }


class CreateUHostInstanceParamNetworkInterfaceEIPSchema(schema.RequestSchema):
    """ CreateUHostInstanceParamNetworkInterfaceEIP - CreateUHostInstance
    """

    fields = {
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ShareBandwidthId": fields.Str(required=False, dump_to="ShareBandwidthId"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "OperatorName": fields.Str(required=False, dump_to="OperatorName"),
        "GlobalSSH": CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSHSchema(
            required=False, dump_to="GlobalSSH"
        ),
        "Bandwidth": fields.Int(required=False, dump_to="Bandwidth"),
    }


class CreateUHostInstanceParamNetworkInterfaceSchema(schema.RequestSchema):
    """ CreateUHostInstanceParamNetworkInterface - CreateUHostInstance
    """

    fields = {
        "EIP": CreateUHostInstanceParamNetworkInterfaceEIPSchema(
            required=False, dump_to="EIP"
        )
    }


class CreateUHostInstanceParamDisksSchema(schema.RequestSchema):
    """ CreateUHostInstanceParamDisks - CreateUHostInstance
    """

    fields = {
        "Type": fields.Str(required=True, dump_to="Type"),
        "BackupType": fields.Str(required=False, dump_to="BackupType"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "KmsKeyId": fields.Str(required=False, dump_to="KmsKeyId"),
        "IsBoot": fields.Str(required=True, dump_to="IsBoot"),
        "Encrypted": fields.Bool(required=False, dump_to="Encrypted"),
    }


class CreateUHostInstanceRequestSchema(schema.RequestSchema):
    """ CreateUHostInstance - 创建UHost实例。
    """

    fields = {
        "GPU": fields.Int(required=False, dump_to="GPU"),
        "KeyPair": fields.Str(required=False, dump_to="KeyPair"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "MaxCount": fields.Int(required=False, dump_to="MaxCount"),
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
        "GpuType": fields.Str(required=False, dump_to="GpuType"),
        "LoginMode": fields.Str(required=True, dump_to="LoginMode"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "SecurityGroupId": fields.Str(required=False, dump_to="SecurityGroupId"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "CPU": fields.Int(required=False, dump_to="CPU"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "UHostType": fields.Str(required=False, dump_to="UHostType"),
        "UserDataScript": fields.Str(required=False, dump_to="UserDataScript"),
        "HostType": fields.Str(required=False, dump_to="HostType"),
        "IsolationGroup": fields.Str(required=False, dump_to="IsolationGroup"),
        "MinimalCpuPlatform": fields.Str(required=False, dump_to="MinimalCpuPlatform"),
        "MachineType": fields.Str(required=False, dump_to="MachineType"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "Disks": fields.List(CreateUHostInstanceParamDisksSchema()),
        "BootDiskSpace": fields.Int(required=False, dump_to="BootDiskSpace"),
        "NetworkId": fields.Str(required=False, dump_to="NetworkId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "NetCapability": fields.Str(required=False, dump_to="NetCapability"),
        "PrivateMac": fields.Str(required=False, dump_to="PrivateMac"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Memory": fields.Int(required=False, dump_to="Memory"),
        "InstallAgent": fields.Str(required=False, dump_to="InstallAgent"),
        "AlarmTemplateId": fields.Int(required=False, dump_to="AlarmTemplateId"),
        "SetId": fields.Int(required=False, dump_to="SetId"),
        "StorageType": fields.Str(required=False, dump_to="StorageType"),
        "TimemachineFeature": fields.Str(required=False, dump_to="TimemachineFeature"),
        "HotplugFeature": fields.Bool(required=False, dump_to="HotplugFeature"),
        "ResourceType": fields.Int(required=False, dump_to="ResourceType"),
        "NetworkInterface": fields.List(
            CreateUHostInstanceParamNetworkInterfaceSchema()
        ),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "PrivateIp": fields.List(fields.Str()),
    }


class CreateUHostInstanceResponseSchema(schema.ResponseSchema):
    """ CreateUHostInstance - 创建UHost实例。
    """

    fields = {
        "UHostIds": fields.List(fields.Str(), required=False, load_from="UHostIds"),
        "IPs": fields.List(fields.Str(), required=False, load_from="IPs"),
    }


"""
API: ModifyUHostInstanceName

修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。
"""


class ModifyUHostInstanceNameRequestSchema(schema.RequestSchema):
    """ ModifyUHostInstanceName - 修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Name": fields.Str(required=False, dump_to="Name"),
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
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class ModifyUHostInstanceRemarkResponseSchema(schema.ResponseSchema):
    """ ModifyUHostInstanceRemark - 修改指定UHost实例备注信息。
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
        "Password": fields.Str(required=True, dump_to="Password"),
    }


class ResetUHostInstancePasswordResponseSchema(schema.ResponseSchema):
    """ ResetUHostInstancePassword - 重置UHost实例的管理员密码。
    """

    fields = {"UhostId": fields.Str(required=False, load_from="UhostId")}


"""
API: TerminateUHostInstance

删除指定数据中心的UHost实例。
"""


class TerminateUHostInstanceRequestSchema(schema.RequestSchema):
    """ TerminateUHostInstance - 删除指定数据中心的UHost实例。
    """

    fields = {
        "ReleaseEIP": fields.Bool(required=False, dump_to="ReleaseEIP"),
        "ReleaseUDisk": fields.Bool(required=False, dump_to="ReleaseUDisk"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Destroy": fields.Int(required=False, dump_to="Destroy"),
    }


class TerminateUHostInstanceResponseSchema(schema.ResponseSchema):
    """ TerminateUHostInstance - 删除指定数据中心的UHost实例。
    """

    fields = {
        "InRecycle": fields.Str(required=True, load_from="InRecycle"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
    }


"""
API: UpgradeToArkUHostInstance

普通升级为方舟机型
"""


class UpgradeToArkUHostInstanceRequestSchema(schema.RequestSchema):
    """ UpgradeToArkUHostInstance - 普通升级为方舟机型
    """

    fields = {
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "UHostIds": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class UpgradeToArkUHostInstanceResponseSchema(schema.ResponseSchema):
    """ UpgradeToArkUHostInstance - 普通升级为方舟机型
    """

    fields = {
        "UHostSet": fields.List(fields.Str(), required=False, load_from="UHostSet")
    }


"""
API: DescribeImage

获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。
"""


class DescribeImageRequestSchema(schema.RequestSchema):
    """ DescribeImage - 获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageType": fields.Str(required=False, dump_to="ImageType"),
        "OsType": fields.Str(required=False, dump_to="OsType"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "PriceSet": fields.Int(required=False, dump_to="PriceSet"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
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
        "IsolationGroup": fields.Str(required=False, dump_to="IsolationGroup"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "UHostIds": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "LifeCycle": fields.Int(required=False, dump_to="LifeCycle"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUHostInstanceResponseSchema(schema.ResponseSchema):
    """ DescribeUHostInstance - 获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。
    """

    fields = {
        "UHostSet": fields.List(
            models.UHostInstanceSetSchema(), required=False, load_from="UHostSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: ImportCustomImage

把UFile的镜像文件导入到UHost，生成自定义镜像
"""


class ImportCustomImageRequestSchema(schema.RequestSchema):
    """ ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "OsType": fields.Str(required=True, dump_to="OsType"),
        "OsName": fields.Str(required=True, dump_to="OsName"),
        "Format": fields.Str(required=True, dump_to="Format"),
        "ImageDescription": fields.Str(required=False, dump_to="ImageDescription"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ImageName": fields.Str(required=True, dump_to="ImageName"),
        "UFileUrl": fields.Str(required=True, dump_to="UFileUrl"),
        "Auth": fields.Bool(required=True, dump_to="Auth"),
    }


class ImportCustomImageResponseSchema(schema.ResponseSchema):
    """ ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像
    """

    fields = {"ImageId": fields.Str(required=False, load_from="ImageId")}


"""
API: ResizeAttachedDisk

修改挂载的磁盘大小，包含系统盘和数据盘
"""


class ResizeAttachedDiskRequestSchema(schema.RequestSchema):
    """ ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘
    """

    fields = {
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "DiskSpace": fields.Int(required=True, dump_to="DiskSpace"),
        "DiskId": fields.Str(required=True, dump_to="DiskId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ResizeAttachedDiskResponseSchema(schema.ResponseSchema):
    """ ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘
    """

    fields = {"DiskId": fields.Str(required=False, load_from="DiskId")}


"""
API: StartUHostInstance

启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。
"""


class StartUHostInstanceRequestSchema(schema.RequestSchema):
    """ StartUHostInstance - 启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "DiskPassword": fields.Str(required=False, dump_to="DiskPassword"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
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
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
    }


class TerminateCustomImageResponseSchema(schema.ResponseSchema):
    """ TerminateCustomImage - 删除用户自定义镜像
    """

    fields = {"ImageId": fields.Str(required=False, load_from="ImageId")}


"""
API: CopyCustomImage

复制自制镜像
"""


class CopyCustomImageRequestSchema(schema.RequestSchema):
    """ CopyCustomImage - 复制自制镜像
    """

    fields = {
        "TargetImageDescription": fields.Str(
            required=False, dump_to="TargetImageDescription"
        ),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SourceImageId": fields.Str(required=True, dump_to="SourceImageId"),
        "TargetProjectId": fields.Str(required=True, dump_to="TargetProjectId"),
        "TargetRegion": fields.Str(required=False, dump_to="TargetRegion"),
        "TargetImageName": fields.Str(required=False, dump_to="TargetImageName"),
    }


class CopyCustomImageResponseSchema(schema.ResponseSchema):
    """ CopyCustomImage - 复制自制镜像
    """

    fields = {"TargetImageId": fields.Str(required=False, load_from="TargetImageId")}


"""
API: GetUHostInstancePrice

根据UHost实例配置，获取UHost实例的价格。
"""


class GetUHostInstancePriceParamDisksSchema(schema.RequestSchema):
    """ GetUHostInstancePriceParamDisks - GetUHostInstancePrice
    """

    fields = {
        "IsBoot": fields.Str(required=True, dump_to="IsBoot"),
        "BackupType": fields.Str(required=False, dump_to="BackupType"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Type": fields.Str(required=True, dump_to="Type"),
    }


class GetUHostInstancePriceRequestSchema(schema.RequestSchema):
    """ GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "StorageType": fields.Str(required=False, dump_to="StorageType"),
        "NetCapability": fields.Str(required=False, dump_to="NetCapability"),
        "LifeCycle": fields.Int(required=False, dump_to="LifeCycle"),
        "MachineType": fields.Str(required=False, dump_to="MachineType"),
        "GpuType": fields.Str(required=False, dump_to="GpuType"),
        "CPU": fields.Int(required=True, dump_to="CPU"),
        "GPU": fields.Int(required=False, dump_to="GPU"),
        "TimemachineFeature": fields.Str(required=False, dump_to="TimemachineFeature"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "Memory": fields.Int(required=True, dump_to="Memory"),
        "DiskSpace": fields.Int(required=False, dump_to="DiskSpace"),
        "UHostType": fields.Str(required=False, dump_to="UHostType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Disks": fields.List(GetUHostInstancePriceParamDisksSchema()),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "Count": fields.Int(required=True, dump_to="Count"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
    }


class GetUHostInstancePriceResponseSchema(schema.ResponseSchema):
    """ GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。
    """

    fields = {
        "PriceSet": fields.List(
            models.UHostPriceSetSchema(), required=False, load_from="PriceSet"
        )
    }
