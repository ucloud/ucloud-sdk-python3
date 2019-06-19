from ucloud.core.typesystem import schema, fields


class UDiskSnapshotSetSchema(schema.ResponseSchema):
    """ UDiskSnapshotSet - DescribeUDiskSnapshot
    """

    fields = {
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "UDiskId": fields.Str(required=True, load_from="UDiskId"),
        "DiskType": fields.Int(required=True, load_from="DiskType"),
        "Comment": fields.Str(required=False, load_from="Comment"),
        "SnapshotId": fields.Str(required=True, load_from="SnapshotId"),
        "Name": fields.Str(required=True, load_from="Name"),
        "IsUDiskAvailable": fields.Bool(required=False, load_from="IsUDiskAvailable"),
        "Status": fields.Str(required=True, load_from="Status"),
        "Version": fields.Str(required=False, load_from="Version"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "UDiskName": fields.Str(required=True, load_from="UDiskName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Size": fields.Int(required=True, load_from="Size"),
    }


class UDiskPriceDataSetSchema(schema.ResponseSchema):
    """ UDiskPriceDataSet - DescribeUDiskPrice
    """

    fields = {
        "ChargeName": fields.Str(required=False, load_from="ChargeName"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class UDiskDataSetSchema(schema.ResponseSchema):
    """ UDiskDataSet - DescribeUDisk
    """

    fields = {
        "IsExpire": fields.Str(required=False, load_from="IsExpire"),
        "Size": fields.Int(required=False, load_from="Size"),
        "SnapshotCount": fields.Int(required=False, load_from="SnapshotCount"),
        "SnapshotLimit": fields.Int(required=False, load_from="SnapshotLimit"),
        "CmkIdAlias": fields.Str(required=False, load_from="CmkIdAlias"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "UDataArkMode": fields.Str(required=False, load_from="UDataArkMode"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
        "UHostIP": fields.Str(required=False, load_from="UHostIP"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Version": fields.Str(required=False, load_from="Version"),
        "ArkSwitchEnable": fields.Int(required=False, load_from="ArkSwitchEnable"),
        "CmkIdStatus": fields.Str(required=False, load_from="CmkIdStatus"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "DiskType": fields.Str(required=False, load_from="DiskType"),
        "SnapEnable": fields.Int(required=False, load_from="SnapEnable"),
        "DataKey": fields.Str(required=False, load_from="DataKey"),
        "Status": fields.Str(required=False, load_from="Status"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "UHostName": fields.Str(required=False, load_from="UHostName"),
        "DeviceName": fields.Str(required=False, load_from="DeviceName"),
        "UKmsMode": fields.Str(required=False, load_from="UKmsMode"),
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "CloneEnable": fields.Int(required=False, load_from="CloneEnable"),
        "CmkId": fields.Str(required=False, load_from="CmkId"),
    }
