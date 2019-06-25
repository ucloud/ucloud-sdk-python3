from ucloud.core.typesystem import schema, fields


class UDBBackupSetSchema(schema.ResponseSchema):
    """ UDBBackupSet - DescribeUDBBackup
    """

    fields = {
        "State": fields.Str(required=False, load_from="State"),
        "ErrorInfo": fields.Str(required=False, load_from="ErrorInfo"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "BackupEndTime": fields.Int(required=False, load_from="BackupEndTime"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
    }


class UDBSlaveInstanceSetSchema(schema.ResponseSchema):
    """ UDBSlaveInstanceSet - DescribeUDBSlaveInstance
    """

    fields = {
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "Role": fields.Str(required=False, load_from="Role"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "State": fields.Str(required=False, load_from="State"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "ClusterRole": fields.Str(required=False, load_from="ClusterRole"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Port": fields.Int(required=False, load_from="Port"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
    }


class UDBInstanceSetSchema(schema.ResponseSchema):
    """ UDBInstanceSet - DescribeUDBInstance
    """

    fields = {
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "DataSet": fields.List(UDBSlaveInstanceSetSchema()),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "Role": fields.Str(required=False, load_from="Role"),
        "SystemFileSize": fields.Float(required=False, load_from="SystemFileSize"),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "BackupBlacklist": fields.Str(required=False, load_from="BackupBlacklist"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "BackupBeginTime": fields.Int(required=False, load_from="BackupBeginTime"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "BackupDuration": fields.Int(required=False, load_from="BackupDuration"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "CluserRole": fields.Str(required=False, load_from="CluserRole"),
        "InstanceTypeId": fields.Int(required=False, load_from="InstanceTypeId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "State": fields.Str(required=False, load_from="State"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
    }


class UDBInstanceBinlogSetSchema(schema.ResponseSchema):
    """ UDBInstanceBinlogSet - DescribeUDBInstanceBinlog
    """

    fields = {
        "Size": fields.Int(required=False, load_from="Size"),
        "BeginTime": fields.Int(required=False, load_from="BeginTime"),
        "EndTime": fields.Int(required=False, load_from="EndTime"),
        "Name": fields.Str(required=False, load_from="Name"),
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
        "DBId": fields.Str(required=False, load_from="DBId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "State": fields.Str(required=False, load_from="State"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
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
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "ParamMember": fields.List(UDBParamMemberSetSchema()),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "RegionFlag": fields.Bool(required=False, load_from="RegionFlag"),
        "GroupId": fields.Int(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Description": fields.Str(required=False, load_from="Description"),
    }


class UDBTypeSetSchema(schema.ResponseSchema):
    """ UDBTypeSet - DescribeUDBType
    """

    fields = {"DBTypeId": fields.Str(required=False, load_from="DBTypeId")}
