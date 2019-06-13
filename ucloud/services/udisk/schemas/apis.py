from ucloud.core.typesystem import schema, fields
from ucloud.services.udisk.schemas import models


""" UDisk API Schema
"""


"""
API: AttachUDisk

将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作
"""


class AttachUDiskRequestSchema(schema.RequestSchema):
    """ AttachUDisk - 将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作
    """

    fields = {
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "MultiAttach": fields.Str(required=False, dump_to="MultiAttach"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class AttachUDiskResponseSchema(schema.ResponseSchema):
    """ AttachUDisk - 将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作
    """

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
    }


"""
API: CloneUDisk

从UDisk创建UDisk克隆
"""


class CloneUDiskRequestSchema(schema.RequestSchema):
    """ CloneUDisk - 从UDisk创建UDisk克隆
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "Comment": fields.Str(required=False, dump_to="Comment"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "SourceId": fields.Str(required=True, dump_to="SourceId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
    }


class CloneUDiskResponseSchema(schema.ResponseSchema):
    """ CloneUDisk - 从UDisk创建UDisk克隆
    """

    fields = {"UDiskId": fields.List(fields.Str(), required=False, load_from="UDiskId")}


"""
API: CreateUDiskSnapshot

创建snapshot快照
"""


class CreateUDiskSnapshotRequestSchema(schema.RequestSchema):
    """ CreateUDiskSnapshot - 创建snapshot快照
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Comment": fields.Str(required=False, dump_to="Comment"),
    }


class CreateUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """ CreateUDiskSnapshot - 创建snapshot快照
    """

    fields = {
        "SnapshotId": fields.List(fields.Str(), required=True, load_from="SnapshotId")
    }


"""
API: DeleteUDiskSnapshot

删除Snapshot
"""


class DeleteUDiskSnapshotRequestSchema(schema.RequestSchema):
    """ DeleteUDiskSnapshot - 删除Snapshot
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SnapshotId": fields.Str(required=True, dump_to="SnapshotId"),
        "UDiskId": fields.Str(required=False, dump_to="UDiskId"),
    }


class DeleteUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """ DeleteUDiskSnapshot - 删除Snapshot
    """

    fields = {}


"""
API: DetachUDisk

卸载某个已经挂载在指定UHost实例上的UDisk
"""


class DetachUDiskRequestSchema(schema.RequestSchema):
    """ DetachUDisk - 卸载某个已经挂载在指定UHost实例上的UDisk
    """

    fields = {
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
    }


class DetachUDiskResponseSchema(schema.ResponseSchema):
    """ DetachUDisk - 卸载某个已经挂载在指定UHost实例上的UDisk
    """

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
    }


"""
API: CreateUDisk

创建UDisk磁盘
"""


class CreateUDiskRequestSchema(schema.RequestSchema):
    """ CreateUDisk - 创建UDisk磁盘
    """

    fields = {
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "CmkId": fields.Str(required=False, dump_to="CmkId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "UKmsMode": fields.Str(required=False, dump_to="UKmsMode"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
    }


class CreateUDiskResponseSchema(schema.ResponseSchema):
    """ CreateUDisk - 创建UDisk磁盘
    """

    fields = {"UDiskId": fields.List(fields.Str(), required=False, load_from="UDiskId")}


"""
API: ResizeUDisk

调整UDisk容量
"""


class ResizeUDiskRequestSchema(schema.RequestSchema):
    """ ResizeUDisk - 调整UDisk容量
    """

    fields = {
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Size": fields.Int(required=True, dump_to="Size"),
    }


class ResizeUDiskResponseSchema(schema.ResponseSchema):
    """ ResizeUDisk - 调整UDisk容量
    """

    fields = {}


"""
API: SetUDiskUDataArkMode

设置UDisk数据方舟的状态
"""


class SetUDiskUDataArkModeRequestSchema(schema.RequestSchema):
    """ SetUDiskUDataArkMode - 设置UDisk数据方舟的状态
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "UDataArkMode": fields.Str(required=True, dump_to="UDataArkMode"),
    }


class SetUDiskUDataArkModeResponseSchema(schema.ResponseSchema):
    """ SetUDiskUDataArkMode - 设置UDisk数据方舟的状态
    """

    fields = {}


"""
API: CloneUDiskSnapshot

从快照创建UDisk克隆
"""


class CloneUDiskSnapshotRequestSchema(schema.RequestSchema):
    """ CloneUDiskSnapshot - 从快照创建UDisk克隆
    """

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "SourceId": fields.Str(required=True, dump_to="SourceId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Comment": fields.Str(required=False, dump_to="Comment"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
    }


class CloneUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """ CloneUDiskSnapshot - 从快照创建UDisk克隆
    """

    fields = {"UDiskId": fields.List(fields.Str(), required=False, load_from="UDiskId")}


"""
API: DescribeUDisk

获取UDisk实例
"""


class DescribeUDiskRequestSchema(schema.RequestSchema):
    """ DescribeUDisk - 获取UDisk实例
    """

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDiskId": fields.Str(required=False, dump_to="UDiskId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
    }


class DescribeUDiskResponseSchema(schema.ResponseSchema):
    """ DescribeUDisk - 获取UDisk实例
    """

    fields = {
        "DataSet": fields.List(
            models.UDiskDataSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUDiskPrice

获取UDisk实例价格信息
"""


class DescribeUDiskPriceRequestSchema(schema.RequestSchema):
    """ DescribeUDiskPrice - 获取UDisk实例价格信息
    """

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Size": fields.Int(required=True, dump_to="Size"),
    }


class DescribeUDiskPriceResponseSchema(schema.ResponseSchema):
    """ DescribeUDiskPrice - 获取UDisk实例价格信息
    """

    fields = {
        "DataSet": fields.List(
            models.UDiskPriceDataSetSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: DescribeUDiskUpgradePrice

获取UDisk升级价格信息
"""


class DescribeUDiskUpgradePriceRequestSchema(schema.RequestSchema):
    """ DescribeUDiskUpgradePrice - 获取UDisk升级价格信息
    """

    fields = {
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SourceId": fields.Str(required=True, dump_to="SourceId"),
        "UDataArkMode": fields.Str(required=True, dump_to="UDataArkMode"),
    }


class DescribeUDiskUpgradePriceResponseSchema(schema.ResponseSchema):
    """ DescribeUDiskUpgradePrice - 获取UDisk升级价格信息
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: RenameUDisk

重命名UDisk
"""


class RenameUDiskRequestSchema(schema.RequestSchema):
    """ RenameUDisk - 重命名UDisk
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "UDiskName": fields.Str(required=True, dump_to="UDiskName"),
    }


class RenameUDiskResponseSchema(schema.ResponseSchema):
    """ RenameUDisk - 重命名UDisk
    """

    fields = {}


"""
API: DeleteUDisk

删除UDisk
"""


class DeleteUDiskRequestSchema(schema.RequestSchema):
    """ DeleteUDisk - 删除UDisk
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
    }


class DeleteUDiskResponseSchema(schema.ResponseSchema):
    """ DeleteUDisk - 删除UDisk
    """

    fields = {}


"""
API: DescribeUDiskSnapshot

获取UDisk快照
"""


class DescribeUDiskSnapshotRequestSchema(schema.RequestSchema):
    """ DescribeUDiskSnapshot - 获取UDisk快照
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "UDiskId": fields.Str(required=False, dump_to="UDiskId"),
        "SnapshotId": fields.Str(required=False, dump_to="SnapshotId"),
    }


class DescribeUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """ DescribeUDiskSnapshot - 获取UDisk快照
    """

    fields = {
        "DataSet": fields.List(
            models.UDiskSnapshotSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: RestoreUDisk

从备份恢复数据至UDisk
"""


class RestoreUDiskRequestSchema(schema.RequestSchema):
    """ RestoreUDisk - 从备份恢复数据至UDisk
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "SnapshotId": fields.Str(required=False, dump_to="SnapshotId"),
        "SnapshotTime": fields.Int(required=False, dump_to="SnapshotTime"),
    }


class RestoreUDiskResponseSchema(schema.ResponseSchema):
    """ RestoreUDisk - 从备份恢复数据至UDisk
    """

    fields = {}
