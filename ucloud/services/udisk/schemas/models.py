from ucloud.core.typesystem import schema, fields


class UDiskDataSetSchema(schema.ResponseSchema):
    """ UDiskDataSet - DescribeUDisk
    """

    fields = {
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "UDataArkMode": fields.Str(required=False, load_from="UDataArkMode"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "UHostName": fields.Str(required=False, load_from="UHostName"),
        "Version": fields.Str(required=False, load_from="Version"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "DeviceName": fields.Str(required=False, load_from="DeviceName"),
        "CloneEnable": fields.Int(required=False, load_from="CloneEnable"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Size": fields.Int(required=False, load_from="Size"),
        "UHostIP": fields.Str(required=False, load_from="UHostIP"),
        "SnapshotCount": fields.Int(required=False, load_from="SnapshotCount"),
        "ArkSwitchEnable": fields.Int(required=False, load_from="ArkSwitchEnable"),
        "Status": fields.Str(required=False, load_from="Status"),
        "IsExpire": fields.Str(required=False, load_from="IsExpire"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Name": fields.Str(required=False, load_from="Name"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "SnapshotLimit": fields.Int(required=False, load_from="SnapshotLimit"),
        "DiskType": fields.Str(required=False, load_from="DiskType"),
        "SnapEnable": fields.Int(required=False, load_from="SnapEnable"),
    }


class UDiskPriceDataSetSchema(schema.ResponseSchema):
    """ UDiskPriceDataSet - DescribeUDiskPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
        "ChargeName": fields.Str(required=False, load_from="ChargeName"),
    }


class UDiskSnapshotSetSchema(schema.ResponseSchema):
    """ UDiskSnapshotSet - DescribeUDiskSnapshot
    """

    fields = {
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "Name": fields.Str(required=True, load_from="Name"),
        "UDiskId": fields.Str(required=True, load_from="UDiskId"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "IsUDiskAvailable": fields.Bool(required=False, load_from="IsUDiskAvailable"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "UDiskName": fields.Str(required=True, load_from="UDiskName"),
        "Comment": fields.Str(required=False, load_from="Comment"),
        "Version": fields.Str(required=False, load_from="Version"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "SnapshotId": fields.Str(required=True, load_from="SnapshotId"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Size": fields.Int(required=True, load_from="Size"),
        "Status": fields.Str(required=True, load_from="Status"),
        "DiskType": fields.Int(required=True, load_from="DiskType"),
    }
