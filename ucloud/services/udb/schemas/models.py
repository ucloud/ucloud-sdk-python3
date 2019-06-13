from ucloud.core.typesystem import schema, fields


class UDBParamMemberSetSchema(schema.ResponseSchema):
    """ UDBParamMemberSet - DescribeUDBParamGroup
    """

    fields = {
        "ApplyType": fields.Int(required=False, load_from="ApplyType"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "FormatType": fields.Int(required=False, load_from="FormatType"),
        "Key": fields.Str(required=False, load_from="Key"),
        "Value": fields.Str(required=False, load_from="Value"),
        "ValueType": fields.Int(required=False, load_from="ValueType"),
        "AllowedVal": fields.Str(required=False, load_from="AllowedVal"),
    }


class UDBParamGroupSetSchema(schema.ResponseSchema):
    """ UDBParamGroupSet - DescribeUDBParamGroup
    """

    fields = {
        "ParamMember": fields.List(UDBParamMemberSetSchema()),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RegionFlag": fields.Bool(required=False, load_from="RegionFlag"),
        "GroupId": fields.Int(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Description": fields.Str(required=False, load_from="Description"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
    }


class UDBBackupSetSchema(schema.ResponseSchema):
    """ UDBBackupSet - DescribeUDBBackup
    """

    fields = {
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "State": fields.Str(required=False, load_from="State"),
        "ErrorInfo": fields.Str(required=False, load_from="ErrorInfo"),
        "BackupEndTime": fields.Int(required=False, load_from="BackupEndTime"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
    }


class UDBSlaveInstanceSetSchema(schema.ResponseSchema):
    """ UDBSlaveInstanceSet - DescribeUDBSlaveInstance
    """

    fields = {
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "State": fields.Str(required=False, load_from="State"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "Port": fields.Int(required=False, load_from="Port"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "Role": fields.Str(required=False, load_from="Role"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "ClusterRole": fields.Str(required=False, load_from="ClusterRole"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
    }


class UDBInstanceSetSchema(schema.ResponseSchema):
    """ UDBInstanceSet - DescribeUDBInstance
    """

    fields = {
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "DataSet": fields.List(UDBSlaveInstanceSetSchema()),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "Role": fields.Str(required=False, load_from="Role"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "Port": fields.Int(required=False, load_from="Port"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "State": fields.Str(required=False, load_from="State"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "CluserRole": fields.Str(required=False, load_from="CluserRole"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
    }


class UDBInstanceBinlogSetSchema(schema.ResponseSchema):
    """ UDBInstanceBinlogSet - DescribeUDBInstanceBinlog
    """

    fields = {
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
        "BeginTime": fields.Int(required=False, load_from="BeginTime"),
        "EndTime": fields.Int(required=False, load_from="EndTime"),
    }


class UDBTypeSetSchema(schema.ResponseSchema):
    """ UDBTypeSet - DescribeUDBType
    """

    fields = {"DBTypeId": fields.Str(required=False, load_from="DBTypeId")}


class UDBInstancePriceSetSchema(schema.ResponseSchema):
    """ UDBInstancePriceSet - DescribeUDBInstancePrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class LogPackageDataSetSchema(schema.ResponseSchema):
    """ LogPackageDataSet - DescribeUDBLogPackage
    """

    fields = {
        "DBName": fields.Str(required=False, load_from="DBName"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "State": fields.Str(required=False, load_from="State"),
        "DBId": fields.Str(required=False, load_from="DBId"),
    }
