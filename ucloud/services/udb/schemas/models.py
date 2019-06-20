from ucloud.core.typesystem import schema, fields


class UDBBackupSetSchema(schema.ResponseSchema):
    """ UDBBackupSet - DescribeUDBBackup
    """

    fields = {
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "BackupEndTime": fields.Int(required=False, load_from="BackupEndTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "State": fields.Str(required=False, load_from="State"),
        "ErrorInfo": fields.Str(required=False, load_from="ErrorInfo"),
    }


class UDBSlaveInstanceSetSchema(schema.ResponseSchema):
    """ UDBSlaveInstanceSet - DescribeUDBSlaveInstance
    """

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "State": fields.Str(required=False, load_from="State"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "ClusterRole": fields.Str(required=False, load_from="ClusterRole"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "Port": fields.Int(required=False, load_from="Port"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Role": fields.Str(required=False, load_from="Role"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class UDBInstanceSetSchema(schema.ResponseSchema):
    """ UDBInstanceSet - DescribeUDBInstance
    """

    fields = {
        "DataSet": fields.List(UDBSlaveInstanceSetSchema()),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "State": fields.Str(required=False, load_from="State"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "CluserRole": fields.Str(required=False, load_from="CluserRole"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Role": fields.Str(required=False, load_from="Role"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "Name": fields.Str(required=False, load_from="Name"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
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


class LogPackageDataSetSchema(schema.ResponseSchema):
    """ LogPackageDataSet - DescribeUDBLogPackage
    """

    fields = {
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "State": fields.Str(required=False, load_from="State"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDBInstancePriceSetSchema(schema.ResponseSchema):
    """ UDBInstancePriceSet - DescribeUDBInstancePrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


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
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RegionFlag": fields.Bool(required=False, load_from="RegionFlag"),
        "GroupId": fields.Int(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Description": fields.Str(required=False, load_from="Description"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "ParamMember": fields.List(UDBParamMemberSetSchema()),
    }
