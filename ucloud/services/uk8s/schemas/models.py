""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class IPSetSchema(schema.ResponseSchema):
    """IPSet - 节点的IP信息"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(required=False, load_from="Default"),
        "IP": fields.Str(required=False, load_from="IP"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class DiskSetSchema(schema.ResponseSchema):
    """DiskSet - 节点磁盘信息"""

    fields = {
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "DiskType": fields.Str(required=False, load_from="DiskType"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "Encrypted": fields.Str(required=False, load_from="Encrypted"),
        "IOPS": fields.Int(required=False, load_from="IOPS"),
        "IsBoot": fields.Str(required=False, load_from="IsBoot"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class UhostInfoSchema(schema.ResponseSchema):
    """UhostInfo - 机器信息"""

    fields = {
        "CPU": fields.Int(required=True, load_from="CPU"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DiskSet": fields.List(DiskSetSchema()),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "IPSet": fields.List(IPSetSchema()),
        "Memory": fields.Int(required=True, load_from="Memory"),
        "Name": fields.Str(required=True, load_from="Name"),
        "NodeId": fields.Str(required=True, load_from="NodeId"),
        "NodeType": fields.Str(required=True, load_from="NodeType"),
        "OsName": fields.Str(required=True, load_from="OsName"),
        "State": fields.Str(required=True, load_from="State"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class ImageInfoSchema(schema.ResponseSchema):
    """ImageInfo - UK8S 可用镜像信息"""

    fields = {
        "ImageId": fields.Str(required=True, load_from="ImageId"),
        "ImageName": fields.Str(required=True, load_from="ImageName"),
        "NotSupportGPU": fields.Bool(required=True, load_from="NotSupportGPU"),
        "ZoneId": fields.Int(required=True, load_from="ZoneId"),
    }


class K8SNodeConditionSchema(schema.ResponseSchema):
    """K8SNodeCondition - Kubernetes Node Condition"""

    fields = {
        "LastProbeTime": fields.Str(required=False, load_from="LastProbeTime"),
        "LastTransitionTime": fields.Str(
            required=False, load_from="LastTransitionTime"
        ),
        "Message": fields.Str(required=False, load_from="Message"),
        "Reason": fields.Str(required=False, load_from="Reason"),
        "Status": fields.Str(required=False, load_from="Status"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class KubeProxySchema(schema.ResponseSchema):
    """KubeProxy - KubeProxy信息"""

    fields = {
        "Mode": fields.Str(required=False, load_from="Mode"),
    }


class UHostIPSetSchema(schema.ResponseSchema):
    """UHostIPSet - 云主机IP信息"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "Default": fields.Str(
            required=False, load_from="Default"
        ),  # Deprecated, will be removed at 1.0
        "IP": fields.Str(required=False, load_from="IP"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "Mac": fields.Str(required=False, load_from="Mac"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class NodeInfoV2Schema(schema.ResponseSchema):
    """NodeInfoV2 - UK8S 节点信息"""

    fields = {
        "AsgId": fields.Str(required=True, load_from="AsgId"),
        "CPU": fields.Int(required=True, load_from="CPU"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "IPSet": fields.List(UHostIPSetSchema()),
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "InstanceName": fields.Str(required=True, load_from="InstanceName"),
        "InstanceType": fields.Str(required=True, load_from="InstanceType"),
        "KubeProxy": KubeProxySchema(),
        "MachineType": fields.Str(required=True, load_from="MachineType"),
        "Memory": fields.Int(required=True, load_from="Memory"),
        "NodeId": fields.Str(required=True, load_from="NodeId"),
        "NodeLogInfo": fields.Str(required=True, load_from="NodeLogInfo"),
        "NodeRole": fields.Str(required=True, load_from="NodeRole"),
        "NodeStatus": fields.Str(required=True, load_from="NodeStatus"),
        "OsName": fields.Str(required=True, load_from="OsName"),
        "OsType": fields.Str(required=True, load_from="OsType"),
        "Unschedulable": fields.Bool(required=True, load_from="Unschedulable"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class ClusterSetSchema(schema.ResponseSchema):
    """ClusterSet - 集群信息"""

    fields = {
        "ApiServer": fields.Str(required=True, load_from="ApiServer"),
        "ClusterId": fields.Str(required=True, load_from="ClusterId"),
        "ClusterLogInfo": fields.Str(
            required=False, load_from="ClusterLogInfo"
        ),
        "ClusterName": fields.Str(required=True, load_from="ClusterName"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExternalApiServer": fields.Str(
            required=False, load_from="ExternalApiServer"
        ),
        "K8sVersion": fields.Str(required=True, load_from="K8sVersion"),
        "MasterCount": fields.Int(required=True, load_from="MasterCount"),
        "NodeCount": fields.Int(required=False, load_from="NodeCount"),
        "PodCIDR": fields.Str(required=True, load_from="PodCIDR"),
        "ServiceCIDR": fields.Str(required=True, load_from="ServiceCIDR"),
        "Status": fields.Str(required=False, load_from="Status"),
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
    }
