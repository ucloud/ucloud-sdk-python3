from ucloud.core.typesystem import schema, fields


class UDBInstanceBinlogSetSchema(schema.ResponseSchema):
    """ UDBInstanceBinlogSet - DescribeUDBInstanceBinlog
    """

    fields = {
        "BeginTime": fields.Int(required=False, load_from="BeginTime"),
        "EndTime": fields.Int(required=False, load_from="EndTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
    }


class UDBInstancePriceSetSchema(schema.ResponseSchema):
    """ UDBInstancePriceSet - DescribeUDBInstancePrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
    }


class UDBBackupSetSchema(schema.ResponseSchema):
    """ UDBBackupSet - DescribeUDBBackup
    """

    fields = {
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "State": fields.Str(required=False, load_from="State"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "BackupEndTime": fields.Int(required=False, load_from="BackupEndTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "ErrorInfo": fields.Str(required=False, load_from="ErrorInfo"),
        "DBId": fields.Str(required=False, load_from="DBId"),
    }


class UDBSlaveInstanceSetSchema(schema.ResponseSchema):
    """ UDBSlaveInstanceSet - DescribeUDBSlaveInstance
    """

    fields = {
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "State": fields.Str(required=False, load_from="State"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "ClusterRole": fields.Str(required=False, load_from="ClusterRole"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "Role": fields.Str(required=False, load_from="Role"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "Tag": fields.Str(required=False, load_from="Tag"),
    }


class UDBInstanceSetSchema(schema.ResponseSchema):
    """ UDBInstanceSet - DescribeUDBInstance
    """

    fields = {
        "State": fields.Str(required=False, load_from="State"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "Role": fields.Str(required=False, load_from="Role"),
        "DataSet": fields.List(UDBSlaveInstanceSetSchema()),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "CluserRole": fields.Str(required=False, load_from="CluserRole"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
    }


class UDBTypeSetSchema(schema.ResponseSchema):
    """ UDBTypeSet - DescribeUDBType
    """

    fields = {"DBTypeId": fields.Str(required=False, load_from="DBTypeId")}


class LogPackageDataSetSchema(schema.ResponseSchema):
    """ LogPackageDataSet - DescribeUDBLogPackage
    """

    fields = {
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "State": fields.Str(required=False, load_from="State"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDBParamMemberSetSchema(schema.ResponseSchema):
    """ UDBParamMemberSet - DescribeUDBParamGroup
    """

    fields = {
        "AllowedVal": fields.Str(required=False, load_from="AllowedVal"),
        "ApplyType": fields.Int(required=False, load_from="ApplyType"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "FormatType": fields.Int(required=False, load_from="FormatType"),
        "Key": fields.Str(required=False, load_from="Key"),
        "Value": fields.Str(required=False, load_from="Value"),
        "ValueType": fields.Int(required=False, load_from="ValueType"),
    }


class UDBParamGroupSetSchema(schema.ResponseSchema):
    """ UDBParamGroupSet - DescribeUDBParamGroup
    """

    fields = {
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Description": fields.Str(required=False, load_from="Description"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "ParamMember": fields.List(UDBParamMemberSetSchema()),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RegionFlag": fields.Bool(required=False, load_from="RegionFlag"),
        "GroupId": fields.Int(required=False, load_from="GroupId"),
    }
