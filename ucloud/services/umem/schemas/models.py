from ucloud.core.typesystem import schema, fields


class UMemcacheGroupSetSchema(schema.ResponseSchema):
    """ UMemcacheGroupSet - DescribeUMemcacheGroup
    """

    fields = {
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "State": fields.Str(required=False, load_from="State"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Version": fields.Str(required=False, load_from="Version"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Port": fields.Int(required=False, load_from="Port"),
    }


class URedisGroupSetSchema(schema.ResponseSchema):
    """ URedisGroupSet - DescribeURedisGroup
    """

    fields = {
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Port": fields.Int(required=False, load_from="Port"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "Size": fields.Int(required=False, load_from="Size"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "Version": fields.Str(required=False, load_from="Version"),
        "State": fields.Str(required=False, load_from="State"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "Type": fields.Str(required=False, load_from="Type"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "HighAvailability": fields.Str(required=False, load_from="HighAvailability"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class URedisPriceSetSchema(schema.ResponseSchema):
    """ URedisPriceSet - 主备Redis价格
    """

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
    }


class UMemcachePriceSetSchema(schema.ResponseSchema):
    """ UMemcachePriceSet - DescribeUMemcachePrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class UMemPriceSetSchema(schema.ResponseSchema):
    """ UMemPriceSet - DescribeUMemPrice
    """

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
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
        "Name": fields.Str(required=False, load_from="Name"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "SpaceId": fields.Str(required=False, load_from="SpaceId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Address": fields.List(UMemSpaceAddressSetSchema()),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "Type": fields.Str(required=False, load_from="Type"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "State": fields.Str(required=False, load_from="State"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
    }


class URedisBackupSetSchema(schema.ResponseSchema):
    """ URedisBackupSet - DescribeURedisBackup
    """

    fields = {
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
        "State": fields.Str(required=False, load_from="State"),
        "BackupId": fields.Str(required=False, load_from="BackupId"),
    }
