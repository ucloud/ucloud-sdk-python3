from ucloud.core.typesystem import schema, fields


class UDiskPriceDataSetSchema(schema.ResponseSchema):
    """ UDiskPriceDataSet - DescribeUDiskPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
        "ChargeName": fields.Str(required=False, load_from="ChargeName"),
    }


class UDiskDataSetSchema(schema.ResponseSchema):
    """ UDiskDataSet - DescribeUDisk
    """

    fields = {
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UHostIP": fields.Str(required=False, load_from="UHostIP"),
        "DeviceName": fields.Str(required=False, load_from="DeviceName"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Status": fields.Str(required=False, load_from="Status"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "ArkSwitchEnable": fields.Int(required=False, load_from="ArkSwitchEnable"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "SnapshotLimit": fields.Int(required=False, load_from="SnapshotLimit"),
        "SnapEnable": fields.Int(required=False, load_from="SnapEnable"),
        "SnapshotCount": fields.Int(required=False, load_from="SnapshotCount"),
        "CloneEnable": fields.Int(required=False, load_from="CloneEnable"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "Size": fields.Int(required=False, load_from="Size"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UDataArkMode": fields.Str(required=False, load_from="UDataArkMode"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "IsExpire": fields.Str(required=False, load_from="IsExpire"),
        "DiskType": fields.Str(required=False, load_from="DiskType"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "UHostName": fields.Str(required=False, load_from="UHostName"),
        "Version": fields.Str(required=False, load_from="Version"),
    }


class UDiskSnapshotSetSchema(schema.ResponseSchema):
    """ UDiskSnapshotSet - DescribeUDiskSnapshot
    """

    fields = {
        "UDiskName": fields.Str(required=True, load_from="UDiskName"),
        "Size": fields.Int(required=True, load_from="Size"),
        "Status": fields.Str(required=True, load_from="Status"),
        "Version": fields.Str(required=False, load_from="Version"),
        "SnapshotId": fields.Str(required=True, load_from="SnapshotId"),
        "UDiskId": fields.Str(required=True, load_from="UDiskId"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "Comment": fields.Str(required=False, load_from="Comment"),
        "IsUDiskAvailable": fields.Bool(required=False, load_from="IsUDiskAvailable"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "Name": fields.Str(required=True, load_from="Name"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DiskType": fields.Int(required=True, load_from="DiskType"),
    }
