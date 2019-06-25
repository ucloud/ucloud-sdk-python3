from ucloud.core.typesystem import schema, fields


class UDiskDataSetSchema(schema.ResponseSchema):
    """ UDiskDataSet - DescribeUDisk
    """

    fields = {
        "SnapshotLimit": fields.Int(required=False, load_from="SnapshotLimit"),
        "ArkSwitchEnable": fields.Int(required=False, load_from="ArkSwitchEnable"),
        "Status": fields.Str(required=False, load_from="Status"),
        "UHostIP": fields.Str(required=False, load_from="UHostIP"),
        "SnapshotCount": fields.Int(required=False, load_from="SnapshotCount"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "DiskType": fields.Str(required=False, load_from="DiskType"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UDataArkMode": fields.Str(required=False, load_from="UDataArkMode"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "SnapEnable": fields.Int(required=False, load_from="SnapEnable"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "IsExpire": fields.Str(required=False, load_from="IsExpire"),
        "Version": fields.Str(required=False, load_from="Version"),
        "CloneEnable": fields.Int(required=False, load_from="CloneEnable"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "UHostName": fields.Str(required=False, load_from="UHostName"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "DeviceName": fields.Str(required=False, load_from="DeviceName"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
    }


class UDiskPriceDataSetSchema(schema.ResponseSchema):
    """ UDiskPriceDataSet - DescribeUDiskPrice
    """

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
        "ChargeName": fields.Str(required=False, load_from="ChargeName"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
    }


class UDiskSnapshotSetSchema(schema.ResponseSchema):
    """ UDiskSnapshotSet - DescribeUDiskSnapshot
    """

    fields = {
        "UDiskId": fields.Str(required=True, load_from="UDiskId"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Status": fields.Str(required=True, load_from="Status"),
        "Comment": fields.Str(required=False, load_from="Comment"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "UDiskName": fields.Str(required=True, load_from="UDiskName"),
        "DiskType": fields.Int(required=True, load_from="DiskType"),
        "IsUDiskAvailable": fields.Bool(required=False, load_from="IsUDiskAvailable"),
        "Version": fields.Str(required=False, load_from="Version"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "SnapshotId": fields.Str(required=True, load_from="SnapshotId"),
        "Size": fields.Int(required=True, load_from="Size"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
    }
