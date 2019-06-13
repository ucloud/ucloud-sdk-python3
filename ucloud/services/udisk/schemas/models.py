from ucloud.core.typesystem import schema, fields


class UDiskDataSetSchema(schema.ResponseSchema):
    """ UDiskDataSet - DescribeUDisk
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "DiskType": fields.Str(required=False, load_from="DiskType"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UDataArkMode": fields.Str(required=False, load_from="UDataArkMode"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "UHostName": fields.Str(required=False, load_from="UHostName"),
        "SnapEnable": fields.Int(required=False, load_from="SnapEnable"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DeviceName": fields.Str(required=False, load_from="DeviceName"),
        "Version": fields.Str(required=False, load_from="Version"),
        "SnapshotCount": fields.Int(required=False, load_from="SnapshotCount"),
        "SnapshotLimit": fields.Int(required=False, load_from="SnapshotLimit"),
        "UHostIP": fields.Str(required=False, load_from="UHostIP"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "ArkSwitchEnable": fields.Int(required=False, load_from="ArkSwitchEnable"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "Status": fields.Str(required=False, load_from="Status"),
        "IsExpire": fields.Str(required=False, load_from="IsExpire"),
        "CloneEnable": fields.Int(required=False, load_from="CloneEnable"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
    }


class UDiskSnapshotSetSchema(schema.ResponseSchema):
    """ UDiskSnapshotSet - DescribeUDiskSnapshot
    """

    fields = {
        "UDiskName": fields.Str(required=True, load_from="UDiskName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "Status": fields.Str(required=True, load_from="Status"),
        "IsUDiskAvailable": fields.Bool(required=False, load_from="IsUDiskAvailable"),
        "Version": fields.Str(required=False, load_from="Version"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "DiskType": fields.Int(required=True, load_from="DiskType"),
        "Comment": fields.Str(required=False, load_from="Comment"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "SnapshotId": fields.Str(required=True, load_from="SnapshotId"),
        "Name": fields.Str(required=True, load_from="Name"),
        "UDiskId": fields.Str(required=True, load_from="UDiskId"),
        "Size": fields.Int(required=True, load_from="Size"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
    }


class UDiskPriceDataSetSchema(schema.ResponseSchema):
    """ UDiskPriceDataSet - DescribeUDiskPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
        "ChargeName": fields.Str(required=False, load_from="ChargeName"),
    }
