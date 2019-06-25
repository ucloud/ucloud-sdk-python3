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
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "SpaceId": fields.Str(required=False, load_from="SpaceId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Size": fields.Int(required=False, load_from="Size"),
        "State": fields.Str(required=False, load_from="State"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Address": fields.List(UMemSpaceAddressSetSchema()),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
    }


class UMemcacheGroupSetSchema(schema.ResponseSchema):
    """ UMemcacheGroupSet - DescribeUMemcacheGroup
    """

    fields = {
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Version": fields.Str(required=False, load_from="Version"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Size": fields.Int(required=False, load_from="Size"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "State": fields.Str(required=False, load_from="State"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
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
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "State": fields.Str(required=False, load_from="State"),
        "BackupId": fields.Str(required=False, load_from="BackupId"),
    }


class URedisGroupSetSchema(schema.ResponseSchema):
    """ URedisGroupSet - DescribeURedisGroup
    """

    fields = {
        "HighAvailability": fields.Str(required=False, load_from="HighAvailability"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Type": fields.Str(required=False, load_from="Type"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "Port": fields.Int(required=False, load_from="Port"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Version": fields.Str(required=False, load_from="Version"),
        "State": fields.Str(required=False, load_from="State"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
    }


class URedisPriceSetSchema(schema.ResponseSchema):
    """ URedisPriceSet - 主备Redis价格
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }
