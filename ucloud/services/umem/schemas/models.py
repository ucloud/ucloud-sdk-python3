from ucloud.core.typesystem import schema, fields


class URedisPriceSetSchema(schema.ResponseSchema):
    """ URedisPriceSet - 主备Redis价格
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
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Size": fields.Int(required=False, load_from="Size"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "SpaceId": fields.Str(required=False, load_from="SpaceId"),
        "Address": fields.List(UMemSpaceAddressSetSchema()),
        "State": fields.Str(required=False, load_from="State"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class UMemcacheGroupSetSchema(schema.ResponseSchema):
    """ UMemcacheGroupSet - DescribeUMemcacheGroup
    """

    fields = {
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Size": fields.Int(required=False, load_from="Size"),
        "State": fields.Str(required=False, load_from="State"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Version": fields.Str(required=False, load_from="Version"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
    }


class UMemcachePriceSetSchema(schema.ResponseSchema):
    """ UMemcachePriceSet - DescribeUMemcachePrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class URedisGroupSetSchema(schema.ResponseSchema):
    """ URedisGroupSet - DescribeURedisGroup
    """

    fields = {
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "State": fields.Str(required=False, load_from="State"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Size": fields.Int(required=False, load_from="Size"),
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "Version": fields.Str(required=False, load_from="Version"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "Port": fields.Int(required=False, load_from="Port"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "HighAvailability": fields.Str(required=False, load_from="HighAvailability"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Name": fields.Str(required=False, load_from="Name"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
    }


class UMemPriceSetSchema(schema.ResponseSchema):
    """ UMemPriceSet - DescribeUMemPrice
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
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "State": fields.Str(required=False, load_from="State"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
    }
