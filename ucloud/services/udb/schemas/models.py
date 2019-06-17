from ucloud.core.typesystem import schema, fields


class UDBSlaveInstanceSetSchema(schema.ResponseSchema):
    """ UDBSlaveInstanceSet - DescribeUDBSlaveInstance
    """

    fields = {
        "Role": fields.Str(required=False, load_from="Role"),
        "ClusterRole": fields.Str(required=False, load_from="ClusterRole"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "State": fields.Str(required=False, load_from="State"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "Name": fields.Str(required=False, load_from="Name"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
    }


class UDBInstanceSetSchema(schema.ResponseSchema):
    """ UDBInstanceSet - DescribeUDBInstance
    """

    fields = {
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "CluserRole": fields.Str(required=False, load_from="CluserRole"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "State": fields.Str(required=False, load_from="State"),
        "Role": fields.Str(required=False, load_from="Role"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "DataSet": fields.List(UDBSlaveInstanceSetSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
    }


class UDBTypeSetSchema(schema.ResponseSchema):
    """ UDBTypeSet - DescribeUDBType
    """

    fields = {"DBTypeId": fields.Str(required=False, load_from="DBTypeId")}


class UDBBackupSetSchema(schema.ResponseSchema):
    """ UDBBackupSet - DescribeUDBBackup
    """

    fields = {
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "State": fields.Str(required=False, load_from="State"),
        "ErrorInfo": fields.Str(required=False, load_from="ErrorInfo"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "BackupEndTime": fields.Int(required=False, load_from="BackupEndTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
    }


class UDBParamMemberSetSchema(schema.ResponseSchema):
    """ UDBParamMemberSet - DescribeUDBParamGroup
    """

    fields = {
        "ValueType": fields.Int(required=False, load_from="ValueType"),
        "AllowedVal": fields.Str(required=False, load_from="AllowedVal"),
        "ApplyType": fields.Int(required=False, load_from="ApplyType"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "FormatType": fields.Int(required=False, load_from="FormatType"),
        "Key": fields.Str(required=False, load_from="Key"),
        "Value": fields.Str(required=False, load_from="Value"),
    }


class UDBParamGroupSetSchema(schema.ResponseSchema):
    """ UDBParamGroupSet - DescribeUDBParamGroup
    """

    fields = {
        "GroupId": fields.Int(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Description": fields.Str(required=False, load_from="Description"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "ParamMember": fields.List(UDBParamMemberSetSchema()),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RegionFlag": fields.Bool(required=False, load_from="RegionFlag"),
    }


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
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "State": fields.Str(required=False, load_from="State"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBName": fields.Str(required=False, load_from="DBName"),
    }


class UDBInstanceBinlogSetSchema(schema.ResponseSchema):
    """ UDBInstanceBinlogSet - DescribeUDBInstanceBinlog
    """

    fields = {
        "BeginTime": fields.Int(required=False, load_from="BeginTime"),
        "EndTime": fields.Int(required=False, load_from="EndTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
    }
