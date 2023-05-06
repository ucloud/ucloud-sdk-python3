""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class NodeListSchema(schema.ResponseSchema):
    """NodeList - 虚拟机资源id列表"""

    fields = {
        "NodeId": fields.Str(required=False, load_from="NodeId"),
    }


class RuleInfoSchema(schema.ResponseSchema):
    """RuleInfo - 防火墙规则"""

    fields = {
        "Action": fields.Str(required=True, load_from="Action"),
        "Port": fields.Str(required=True, load_from="Port"),
        "Priority": fields.Str(required=True, load_from="Priority"),
        "ProtocolType": fields.Str(required=True, load_from="ProtocolType"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "SrcIp": fields.Str(required=True, load_from="SrcIp"),
    }


class FirewallInfoSchema(schema.ResponseSchema):
    """FirewallInfo - 防火墙信息"""

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "FirewallId": fields.Str(required=True, load_from="FirewallId"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceCount": fields.Int(required=True, load_from="ResourceCount"),
        "Rule": fields.List(RuleInfoSchema()),
        "Type": fields.Str(required=True, load_from="Type"),
    }


class ResourceInfoSchema(schema.ResponseSchema):
    """ResourceInfo - 绑定防火墙的资源信息"""

    fields = {
        "Name": fields.Str(required=True, load_from="Name"),
        "PublicIpList": fields.List(fields.Str()),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "State": fields.Int(required=True, load_from="State"),
    }


class EnvListSchema(schema.ResponseSchema):
    """EnvList - 容器环境变量列表"""

    fields = {
        "Key": fields.Str(required=False, load_from="Key"),
        "Value": fields.Str(required=False, load_from="Value"),
    }


class CfgDictListSchema(schema.ResponseSchema):
    """CfgDictList - 容器配置字典列表"""

    fields = {
        "MountPath": fields.Str(required=False, load_from="MountPath"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
    }


class IpListSchema(schema.ResponseSchema):
    """IpList - 容器组外网ip列表"""

    fields = {
        "Ip": fields.Str(required=False, load_from="Ip"),
        "Isp": fields.Str(required=False, load_from="Isp"),
    }


class StorVolumeInfoSchema(schema.ResponseSchema):
    """StorVolumeInfo - 容器组存储卷信息"""

    fields = {
        "DiskSize": fields.Int(required=False, load_from="DiskSize"),
        "MountPoint": fields.Str(required=False, load_from="MountPoint"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
    }


class DockerInfoSchema(schema.ResponseSchema):
    """DockerInfo - 容器信息"""

    fields = {
        "Args": fields.Str(required=False, load_from="Args"),
        "CfgDictList": fields.List(CfgDictListSchema()),
        "Command": fields.Str(required=False, load_from="Command"),
        "CpuCores": fields.Float(required=False, load_from="CpuCores"),
        "EnvList": fields.List(EnvListSchema()),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "MemSize": fields.Float(required=False, load_from="MemSize"),
        "Name": fields.Str(required=False, load_from="Name"),
        "State": fields.Int(required=False, load_from="State"),
        "WorkDir": fields.Str(required=False, load_from="WorkDir"),
    }


class ImageListSchema(schema.ResponseSchema):
    """ImageList - 容器组镜像密钥列表"""

    fields = {
        "ImageKey": fields.Str(required=False, load_from="ImageKey"),
        "StoreAddr": fields.Str(required=False, load_from="StoreAddr"),
        "UserName": fields.Str(required=False, load_from="UserName"),
    }


class HolderListSchema(schema.ResponseSchema):
    """HolderList - 容器组信息"""

    fields = {
        "City": fields.Str(required=False, load_from="City"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DockerCount": fields.Int(required=False, load_from="DockerCount"),
        "DockerInfo": fields.List(DockerInfoSchema()),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "FirewallId": fields.Str(required=False, load_from="FirewallId"),
        "HolderName": fields.Str(required=False, load_from="HolderName"),
        "IdcId": fields.Str(required=False, load_from="IdcId"),
        "ImageList": fields.List(ImageListSchema()),
        "InnerIp": fields.Str(required=False, load_from="InnerIp"),
        "IpList": fields.List(IpListSchema()),
        "NetLimit": fields.Int(required=False, load_from="NetLimit"),
        "OcName": fields.Str(required=False, load_from="OcName"),
        "ProductType": fields.Str(required=False, load_from="ProductType"),
        "Province": fields.Str(required=False, load_from="Province"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "RestartStrategy": fields.Int(
            required=False, load_from="RestartStrategy"
        ),
        "State": fields.Int(required=False, load_from="State"),
        "StorVolumeCount": fields.Int(
            required=False, load_from="StorVolumeCount"
        ),
        "StorVolumeInfo": fields.List(StorVolumeInfoSchema()),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Int(required=False, load_from="Type"),
    }


class IdcInfoSchema(schema.ResponseSchema):
    """IdcInfo - 机房信息"""

    fields = {
        "City": fields.Str(required=False, load_from="City"),
        "IdcId": fields.Str(required=False, load_from="IdcId"),
        "Isp": fields.Str(required=False, load_from="Isp"),
        "MaxNodeCnt": fields.Int(required=False, load_from="MaxNodeCnt"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Province": fields.Str(required=False, load_from="Province"),
        "Type": fields.Int(required=False, load_from="Type"),
    }


class SubnetInfoSchema(schema.ResponseSchema):
    """SubnetInfo - 子网信息"""

    fields = {
        "AvailableIPCnt": fields.Int(required=True, load_from="AvailableIPCnt"),
        "CIDR": fields.Str(required=True, load_from="CIDR"),
        "Comment": fields.Str(required=True, load_from="Comment"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IdcId": fields.Str(required=True, load_from="IdcId"),
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
        "SubnetName": fields.Str(required=True, load_from="SubnetName"),
        "TotalIpCnt": fields.Int(required=True, load_from="TotalIpCnt"),
    }


class NodeIpListSchema(schema.ResponseSchema):
    """NodeIpList - 虚拟机外网ip列表"""

    fields = {
        "Ip": fields.Str(required=False, load_from="Ip"),
        "Isp": fields.Str(required=False, load_from="Isp"),
        "IspName": fields.Str(required=False, load_from="IspName"),
    }


class NodeInfoSchema(schema.ResponseSchema):
    """NodeInfo - 节点信息"""

    fields = {
        "ChargeType": fields.Int(required=False, load_from="ChargeType"),
        "City": fields.Str(required=False, load_from="City"),
        "CoreNum": fields.Int(required=False, load_from="CoreNum"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskSize": fields.Int(required=False, load_from="DiskSize"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "FirewallId": fields.Str(required=False, load_from="FirewallId"),
        "IdcId": fields.Str(required=False, load_from="IdcId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "InnerIps": fields.List(fields.Str()),
        "MemSize": fields.Int(required=False, load_from="MemSize"),
        "NetLimit": fields.Int(required=False, load_from="NetLimit"),
        "NodeId": fields.Str(required=False, load_from="NodeId"),
        "NodeIpList": fields.List(NodeIpListSchema()),
        "NodeName": fields.Str(required=False, load_from="NodeName"),
        "OcName": fields.Str(required=False, load_from="OcName"),
        "ProductType": fields.Str(required=False, load_from="ProductType"),
        "Province": fields.Str(required=False, load_from="Province"),
        "State": fields.Int(required=False, load_from="State"),
        "SysDiskSize": fields.Int(required=False, load_from="SysDiskSize"),
        "Type": fields.Int(required=False, load_from="Type"),
    }


class NodeIspListSchema(schema.ResponseSchema):
    """NodeIspList - 节点运营商列表"""

    fields = {
        "City": fields.Str(required=False, load_from="City"),
        "IdcName": fields.Str(required=False, load_from="IdcName"),
        "IspName": fields.Str(required=False, load_from="IspName"),
        "LineType": fields.Str(required=False, load_from="LineType"),
        "Province": fields.Str(required=False, load_from="Province"),
    }


class MonitorInfoSchema(schema.ResponseSchema):
    """MonitorInfo - 监控信息"""

    fields = {
        "TimeStamp": fields.Int(required=True, load_from="TimeStamp"),
        "Value": fields.Int(required=True, load_from="Value"),
    }


class MetricisDataSetSchema(schema.ResponseSchema):
    """MetricisDataSet - 监控数据"""

    fields = {
        "CPUUtilization": fields.List(MonitorInfoSchema()),
        "MemUtilization": fields.List(MonitorInfoSchema()),
        "NICIn": fields.List(MonitorInfoSchema()),
        "NICOut": fields.List(MonitorInfoSchema()),
        "NetPacketIn": fields.List(MonitorInfoSchema()),
        "NetPacketOut": fields.List(MonitorInfoSchema()),
    }


class ResourceSetSchema(schema.ResponseSchema):
    """ResourceSet - 受到影响的资源列表"""

    fields = {
        "NodeId": fields.Str(required=False, load_from="NodeId"),
        "OuterIps": fields.List(fields.Str()),
    }


class IDCCutInfoSchema(schema.ResponseSchema):
    """IDCCutInfo - 机房割接信息"""

    fields = {
        "City": fields.Str(required=False, load_from="City"),
        "CutType": fields.Str(required=False, load_from="CutType"),
        "EndTime": fields.Int(required=False, load_from="EndTime"),
        "IDCName": fields.Str(required=False, load_from="IDCName"),
        "Province": fields.Str(required=False, load_from="Province"),
        "ResourceSet": fields.List(ResourceSetSchema()),
        "StartTime": fields.Int(required=False, load_from="StartTime"),
    }


class DataSetSchema(schema.ResponseSchema):
    """DataSet - 监控信息集合"""

    fields = {
        "CPUUtilization": fields.List(MonitorInfoSchema()),
        "DiskReadOps": fields.List(MonitorInfoSchema()),
        "DiskWriteOps": fields.List(MonitorInfoSchema()),
        "IORead": fields.List(MonitorInfoSchema()),
        "IOWrite": fields.List(MonitorInfoSchema()),
        "MemUtilization": fields.List(MonitorInfoSchema()),
        "NICIn": fields.List(MonitorInfoSchema()),
        "NICOut": fields.List(MonitorInfoSchema()),
        "NetPacketIn": fields.List(MonitorInfoSchema()),
        "NetPacketOut": fields.List(MonitorInfoSchema()),
    }


class DeployImageInfoSchema(schema.ResponseSchema):
    """DeployImageInfo - 镜像部署信息"""

    fields = {
        "IdcId": fields.Str(required=False, load_from="IdcId"),
        "State": fields.Int(required=False, load_from="State"),
    }


class ImageInfoSchema(schema.ResponseSchema):
    """ImageInfo - 镜像详情"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DeployInfoList": fields.List(DeployImageInfoSchema()),
        "Gpu": fields.Int(required=False, load_from="Gpu"),
        "ImageDesc": fields.Str(required=False, load_from="ImageDesc"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
        "ImageType": fields.Int(required=False, load_from="ImageType"),
        "OcType": fields.Str(required=False, load_from="OcType"),
        "State": fields.Int(required=False, load_from="State"),
    }
