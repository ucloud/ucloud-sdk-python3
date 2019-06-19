from ucloud.core.typesystem import schema, fields


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
        "State": fields.Str(required=False, load_from="State"),
        "BackupId": fields.Str(required=False, load_from="BackupId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupType": fields.Str(required=False, load_from="BackupType"),
    }


class UMemPriceSetSchema(schema.ResponseSchema):
    """ UMemPriceSet - DescribeUMemPrice
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
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Port": fields.Int(required=False, load_from="Port"),
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "HighAvailability": fields.Str(required=False, load_from="HighAvailability"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "State": fields.Str(required=False, load_from="State"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Version": fields.Str(required=False, load_from="Version"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
    }


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
        "Port": fields.Int(required=False, load_from="Port"),
        "IP": fields.Str(required=False, load_from="IP"),
    }


class UMemSpaceSetSchema(schema.ResponseSchema):
    """ UMemSpaceSet - DescribeUMemSpace
    """

    fields = {
        "State": fields.Str(required=False, load_from="State"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "Type": fields.Str(required=False, load_from="Type"),
        "SpaceId": fields.Str(required=False, load_from="SpaceId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Address": fields.List(UMemSpaceAddressSetSchema()),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
    }


class UMemcacheGroupSetSchema(schema.ResponseSchema):
    """ UMemcacheGroupSet - DescribeUMemcacheGroup
    """

    fields = {
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "Version": fields.Str(required=False, load_from="Version"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Port": fields.Int(required=False, load_from="Port"),
        "State": fields.Str(required=False, load_from="State"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Size": fields.Int(required=False, load_from="Size"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
    }
