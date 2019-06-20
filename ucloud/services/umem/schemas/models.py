from ucloud.core.typesystem import schema, fields


class URedisBackupSetSchema(schema.ResponseSchema):
    """ URedisBackupSet - DescribeURedisBackup
    """

    fields = {
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupId": fields.Str(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "State": fields.Str(required=False, load_from="State"),
    }


class URedisGroupSetSchema(schema.ResponseSchema):
    """ URedisGroupSet - DescribeURedisGroup
    """

    fields = {
        "HighAvailability": fields.Str(required=False, load_from="HighAvailability"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "Type": fields.Str(required=False, load_from="Type"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "State": fields.Str(required=False, load_from="State"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "Port": fields.Int(required=False, load_from="Port"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Version": fields.Str(required=False, load_from="Version"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
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
        "SpaceId": fields.Str(required=False, load_from="SpaceId"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Address": fields.List(UMemSpaceAddressSetSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "State": fields.Str(required=False, load_from="State"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class UMemPriceSetSchema(schema.ResponseSchema):
    """ UMemPriceSet - DescribeUMemPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class UMemcacheGroupSetSchema(schema.ResponseSchema):
    """ UMemcacheGroupSet - DescribeUMemcacheGroup
    """

    fields = {
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Version": fields.Str(required=False, load_from="Version"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "State": fields.Str(required=False, load_from="State"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Port": fields.Int(required=False, load_from="Port"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class UMemcachePriceSetSchema(schema.ResponseSchema):
    """ UMemcachePriceSet - DescribeUMemcachePrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class URedisPriceSetSchema(schema.ResponseSchema):
    """ URedisPriceSet - 主备Redis价格
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }
