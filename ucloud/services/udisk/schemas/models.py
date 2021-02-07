""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class RecycleUDiskSetSchema(schema.ResponseSchema):
    """RecycleUDiskSet - 回收站列表"""

    fields = {
        "CountdownTime": fields.Int(required=True, load_from="CountdownTime"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ExpiredTime": fields.Int(required=True, load_from="ExpiredTime"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Size": fields.Int(required=True, load_from="Size"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UDiskId": fields.Str(required=True, load_from="UDiskId"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class UDiskDataSetSchema(schema.ResponseSchema):
    """UDiskDataSet - DescribeUDisk"""

    fields = {
        "ArkSwitchEnable": fields.Int(
            required=False, load_from="ArkSwitchEnable"
        ),
        "BackupMode": fields.Str(required=False, load_from="BackupMode"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CloneEnable": fields.Int(required=False, load_from="CloneEnable"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "DeviceName": fields.Str(required=False, load_from="DeviceName"),
        "DiskType": fields.Str(required=False, load_from="DiskType"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "HostIP": fields.Str(required=False, load_from="HostIP"),
        "HostId": fields.Str(required=False, load_from="HostId"),
        "HostName": fields.Str(required=False, load_from="HostName"),
        "IsBoot": fields.Str(required=False, load_from="IsBoot"),
        "IsExpire": fields.Str(required=False, load_from="IsExpire"),
        "Name": fields.Str(required=False, load_from="Name"),
        "RdmaClusterId": fields.Str(required=False, load_from="RdmaClusterId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "SnapEnable": fields.Int(required=False, load_from="SnapEnable"),
        "SnapshotCount": fields.Int(required=False, load_from="SnapshotCount"),
        "SnapshotLimit": fields.Int(required=False, load_from="SnapshotLimit"),
        "Status": fields.Str(required=False, load_from="Status"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UDataArkMode": fields.Str(required=False, load_from="UDataArkMode"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "UHostIP": fields.Str(required=False, load_from="UHostIP"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UHostName": fields.Str(required=False, load_from="UHostName"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "Version": fields.Str(required=False, load_from="Version"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDiskPriceDataSetSchema(schema.ResponseSchema):
    """UDiskPriceDataSet - DescribeUDiskPrice"""

    fields = {
        "ChargeName": fields.Str(required=False, load_from="ChargeName"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ListPrice": fields.Int(required=False, load_from="ListPrice"),
        "OriginalPrice": fields.Int(required=False, load_from="OriginalPrice"),
        "Price": fields.Int(required=False, load_from="Price"),
    }


class UDiskSnapshotSetSchema(schema.ResponseSchema):
    """UDiskSnapshotSet - DescribeUDiskSnapshot"""

    fields = {
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "Comment": fields.Str(required=False, load_from="Comment"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "DiskType": fields.Int(required=True, load_from="DiskType"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "IsUDiskAvailable": fields.Bool(
            required=False, load_from="IsUDiskAvailable"
        ),
        "Name": fields.Str(required=True, load_from="Name"),
        "Size": fields.Int(required=True, load_from="Size"),
        "SnapshotId": fields.Str(required=True, load_from="SnapshotId"),
        "Status": fields.Str(required=True, load_from="Status"),
        "UDiskId": fields.Str(required=True, load_from="UDiskId"),
        "UDiskName": fields.Str(required=True, load_from="UDiskName"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "Version": fields.Str(required=False, load_from="Version"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }
