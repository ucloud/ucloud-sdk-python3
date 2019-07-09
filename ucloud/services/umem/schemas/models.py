""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class UMemPriceSetSchema(schema.ResponseSchema):
    """ UMemPriceSet - DescribeUMemPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class UMemSpaceAddressSetSchema(schema.ResponseSchema):
    """ UMemSpaceAddressSet - DescribeUMemSpace
    """

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "Port": fields.Int(required=False, load_from="Port"),
    }


class UMemSpaceSetSchema(schema.ResponseSchema):
    """ UMemSpaceSet - DescribeUMemSpace
    """

    fields = {
        "Address": fields.List(UMemSpaceAddressSetSchema()),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "Size": fields.Int(required=False, load_from="Size"),
        "SpaceId": fields.Str(required=False, load_from="SpaceId"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "Type": fields.Str(required=False, load_from="Type"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UMemcacheGroupSetSchema(schema.ResponseSchema):
    """ UMemcacheGroupSet - DescribeUMemcacheGroup
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Size": fields.Int(required=False, load_from="Size"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Version": fields.Str(required=False, load_from="Version"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
    }


class UMemcachePriceSetSchema(schema.ResponseSchema):
    """ UMemcachePriceSet - DescribeUMemcachePrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class URedisBackupSetSchema(schema.ResponseSchema):
    """ URedisBackupSet - DescribeURedisBackup
    """

    fields = {
        "BackupId": fields.Str(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "State": fields.Str(required=False, load_from="State"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class URedisGroupSetSchema(schema.ResponseSchema):
    """ URedisGroupSet - DescribeURedisGroup
    """

    fields = {
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "HighAvailability": fields.Str(required=False, load_from="HighAvailability"),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "Size": fields.Int(required=False, load_from="Size"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Type": fields.Str(required=False, load_from="Type"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "Version": fields.Str(required=False, load_from="Version"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class URedisPriceSetSchema(schema.ResponseSchema):
    """ URedisPriceSet - 主备Redis价格
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }
