""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class UDRedisProxyInfoSchema(schema.ResponseSchema):
    """UDRedisProxyInfo - udredis代理信息"""

    fields = {
        "ProxyId": fields.Str(required=True, load_from="ProxyId"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "State": fields.Str(required=True, load_from="State"),
        "Vip": fields.Str(required=True, load_from="Vip"),
    }


class UDRedisSlowlogSetSchema(schema.ResponseSchema):
    """UDRedisSlowlogSet - DescribeUDRedisSlowlog"""

    fields = {
        "BlockId": fields.Str(required=False, load_from="BlockId"),
        "Command": fields.Str(required=False, load_from="Command"),
        "SpendTime": fields.Int(required=False, load_from="SpendTime"),
        "StartTime": fields.Int(required=False, load_from="StartTime"),
    }


class UMemSlaveDataSetSchema(schema.ResponseSchema):
    """UMemSlaveDataSet - DescribeUMem"""

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "MasterGroupId": fields.Str(required=False, load_from="MasterGroupId"),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Port": fields.Int(required=False, load_from="Port"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "RewriteTime": fields.Int(required=False, load_from="RewriteTime"),
        "Role": fields.Str(required=False, load_from="Role"),
        "Size": fields.Int(required=False, load_from="Size"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "Version": fields.Str(required=False, load_from="Version"),
        "VirtualIP": fields.Str(required=True, load_from="VirtualIP"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UMemSpaceAddressSetSchema(schema.ResponseSchema):
    """UMemSpaceAddressSet - DescribeUMemSpace"""

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "Port": fields.Int(required=False, load_from="Port"),
    }


class UMemDataSetSchema(schema.ResponseSchema):
    """UMemDataSet - DescribeUMem"""

    fields = {
        "Address": fields.List(UMemSpaceAddressSetSchema()),
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DataSet": fields.List(UMemSlaveDataSetSchema()),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "HighAvailability": fields.Str(
            required=False, load_from="HighAvailability"
        ),
        "Name": fields.Str(required=False, load_from="Name"),
        "OwnSlave": fields.Str(required=True, load_from="OwnSlave"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "RewriteTime": fields.Int(required=False, load_from="RewriteTime"),
        "Role": fields.Str(required=False, load_from="Role"),
        "Size": fields.Int(required=False, load_from="Size"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Type": fields.Str(required=False, load_from="Type"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Version": fields.Str(required=False, load_from="Version"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UMemBackupSetSchema(schema.ResponseSchema):
    """UMemBackupSet - DescribeUMemBackup"""

    fields = {
        "BackupId": fields.Str(required=True, load_from="BackupId"),
        "BackupName": fields.Str(required=True, load_from="BackupName"),
        "BackupType": fields.Str(required=True, load_from="BackupType"),
        "BlockCount": fields.Int(required=True, load_from="BlockCount"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "State": fields.Str(required=True, load_from="State"),
    }


class UMemBlockInfoSchema(schema.ResponseSchema):
    """UMemBlockInfo - 分布式redis 分片信息"""

    fields = {
        "BlockId": fields.Str(required=True, load_from="BlockId"),
        "BlockName": fields.Str(required=False, load_from="BlockName"),
        "BlockPort": fields.Int(required=True, load_from="BlockPort"),
        "BlockReadWeight": fields.Int(
            required=False, load_from="BlockReadWeight"
        ),
        "BlockSize": fields.Int(required=True, load_from="BlockSize"),
        "BlockSlotBegin": fields.Int(required=True, load_from="BlockSlotBegin"),
        "BlockSlotEnd": fields.Int(required=True, load_from="BlockSlotEnd"),
        "BlockState": fields.Str(required=True, load_from="BlockState"),
        "BlockType": fields.Str(required=False, load_from="BlockType"),
        "BlockUsedSize": fields.Int(required=False, load_from="BlockUsedSize"),
        "BlockVip": fields.Str(required=False, load_from="BlockVip"),
    }


class UMemPriceSetSchema(schema.ResponseSchema):
    """UMemPriceSet - DescribeUMemPrice"""

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ListPrice": fields.Int(
            required=False, load_from="ListPrice"
        ),  # Deprecated, will be removed at 1.0
        "OriginalPrice": fields.Int(required=False, load_from="OriginalPrice"),
        "Price": fields.Int(required=False, load_from="Price"),
    }


class UMemSpaceSetSchema(schema.ResponseSchema):
    """UMemSpaceSet - DescribeUMemSpace"""

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


class PriceDataSetSchema(schema.ResponseSchema):
    """PriceDataSet -"""

    fields = {
        "CustomPrice": fields.Int(required=False, load_from="CustomPrice"),
        "PurchaseValue": fields.Int(required=False, load_from="PurchaseValue"),
        "TotalPrice": fields.Int(required=False, load_from="TotalPrice"),
    }


class UMemcacheGroupSetSchema(schema.ResponseSchema):
    """UMemcacheGroupSet - DescribeUMemcacheGroup"""

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
    """UMemcachePriceSet - DescribeUMemcachePrice"""

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ListPrice": fields.Int(required=False, load_from="ListPrice"),
        "OriginalPrice": fields.Int(required=False, load_from="OriginalPrice"),
        "Price": fields.Int(required=False, load_from="Price"),
    }


class URedisBackupSetSchema(schema.ResponseSchema):
    """URedisBackupSet - DescribeURedisBackup"""

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


class URedisConfigSetSchema(schema.ResponseSchema):
    """URedisConfigSet - 主备Redis配置文件信息"""

    fields = {
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Description": fields.Str(required=False, load_from="Description"),
        "IsModify": fields.Str(required=False, load_from="IsModify"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "RegionFlag": fields.Bool(required=False, load_from="RegionFlag"),
        "State": fields.Str(required=False, load_from="State"),
        "Version": fields.Str(required=False, load_from="Version"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class URedisGroupSetSchema(schema.ResponseSchema):
    """URedisGroupSet - DescribeURedisGroup"""

    fields = {
        "AutoBackup": fields.Str(required=False, load_from="AutoBackup"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ConfigId": fields.Str(required=False, load_from="ConfigId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "GroupId": fields.Str(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "HighAvailability": fields.Str(
            required=False, load_from="HighAvailability"
        ),
        "MemorySize": fields.Int(required=False, load_from="MemorySize"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "RewriteTime": fields.Int(required=True, load_from="RewriteTime"),
        "Role": fields.Str(required=True, load_from="Role"),
        "Size": fields.Int(required=False, load_from="Size"),
        "SlaveZone": fields.Str(required=False, load_from="SlaveZone"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Type": fields.Str(required=False, load_from="Type"),
        "UsedSize": fields.Int(required=False, load_from="UsedSize"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Version": fields.Str(required=False, load_from="Version"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class URedisPriceSetSchema(schema.ResponseSchema):
    """URedisPriceSet - 主备Redis价格"""

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ListPrice": fields.Int(required=False, load_from="ListPrice"),
        "OriginalPrice": fields.Int(required=True, load_from="OriginalPrice"),
        "Price": fields.Int(required=False, load_from="Price"),
    }


class URedisSlowlogSetSchema(schema.ResponseSchema):
    """URedisSlowlogSet - DescribeURedisSlowlog"""

    fields = {
        "Command": fields.Str(required=False, load_from="Command"),
        "SpendTime": fields.Int(required=False, load_from="SpendTime"),
        "StartTime": fields.Int(required=False, load_from="StartTime"),
    }


class URedisVersionSetSchema(schema.ResponseSchema):
    """URedisVersionSet - DescribeURedisVersion"""

    fields = {
        "Version": fields.Str(required=False, load_from="Version"),
    }
