""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class UPhoneInstanceSchema(schema.ResponseSchema):
    """UPhoneInstance -"""

    fields = {
        "ADB": fields.Str(required=False, load_from="ADB"),
        "CPU": fields.Float(required=True, load_from="CPU"),
        "Callback": fields.Str(required=True, load_from="Callback"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CityId": fields.Str(required=True, load_from="CityId"),
        "CityName": fields.Str(required=True, load_from="CityName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DiskSize": fields.Int(required=True, load_from="DiskSize"),
        "EipId": fields.Str(required=False, load_from="EipId"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "ImageId": fields.Str(required=True, load_from="ImageId"),
        "Ip": fields.Str(required=False, load_from="Ip"),
        "IpRegion": fields.Str(required=False, load_from="IpRegion"),
        "Memory": fields.Int(required=True, load_from="Memory"),
        "OsType": fields.Str(required=True, load_from="OsType"),
        "Refresh": fields.Int(required=True, load_from="Refresh"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Resolution": fields.Str(required=True, load_from="Resolution"),
        "ServerId": fields.Str(required=True, load_from="ServerId"),
        "ShareBandwidthId": fields.Str(
            required=False, load_from="ShareBandwidthId"
        ),
        "ShareBandwidthName": fields.Str(
            required=False, load_from="ShareBandwidthName"
        ),
        "SplashScreen": fields.Str(required=True, load_from="SplashScreen"),
        "State": fields.Str(required=True, load_from="State"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "UPhoneId": fields.Str(required=True, load_from="UPhoneId"),
        "UPhoneModelName": fields.Str(
            required=True, load_from="UPhoneModelName"
        ),
        "UPhoneName": fields.Str(required=True, load_from="UPhoneName"),
    }


class AppInstanceSchema(schema.ResponseSchema):
    """AppInstance -"""

    fields = {
        "AppId": fields.Str(required=True, load_from="AppId"),
        "AppName": fields.Str(required=True, load_from="AppName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Description": fields.Str(required=False, load_from="Description"),
        "ModifyTime": fields.Int(required=True, load_from="ModifyTime"),
    }


class AppVersionInstanceSchema(schema.ResponseSchema):
    """AppVersionInstance -"""

    fields = {
        "AppId": fields.Str(required=True, load_from="AppId"),
        "AppVersionId": fields.Str(required=True, load_from="AppVersionId"),
        "AppVersionName": fields.Str(required=True, load_from="AppVersionName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Description": fields.Str(required=False, load_from="Description"),
        "ModifyTime": fields.Int(required=True, load_from="ModifyTime"),
        "PackageName": fields.Str(required=True, load_from="PackageName"),
        "URL": fields.Str(required=True, load_from="URL"),
    }


class CityInstanceSchema(schema.ResponseSchema):
    """CityInstance -"""

    fields = {
        "CityAlias": fields.Str(required=False, load_from="CityAlias"),
        "CityId": fields.Str(required=False, load_from="CityId"),
        "CityName": fields.Str(required=False, load_from="CityName"),
        "CityType": fields.Str(required=False, load_from="CityType"),
        "IsSoldOut": fields.Bool(required=False, load_from="IsSoldOut"),
    }


class UPhoneDetailInstanceSchema(schema.ResponseSchema):
    """UPhoneDetailInstance -"""

    fields = {
        "AppVersion": AppVersionInstanceSchema(),
        "CPU": fields.Int(required=False, load_from="CPU"),
        "CityId": fields.Str(required=False, load_from="CityId"),
        "CityName": fields.Str(required=False, load_from="CityName"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskSize": fields.Int(required=False, load_from="DiskSize"),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "Refresh": fields.Int(required=False, load_from="Refresh"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Resolution": fields.Str(required=False, load_from="Resolution"),
        "ServerId": fields.Str(required=False, load_from="ServerId"),
        "State": fields.Str(required=False, load_from="State"),
        "UPhoneId": fields.Str(required=False, load_from="UPhoneId"),
        "UPhoneModelName": fields.Str(
            required=False, load_from="UPhoneModelName"
        ),
        "UPhoneName": fields.Str(required=False, load_from="UPhoneName"),
    }


class EipInfoSchema(schema.ResponseSchema):
    """EipInfo - EIP信息"""

    fields = {
        "BindCount": fields.Int(required=False, load_from="BindCount"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EipId": fields.Str(required=True, load_from="EipId"),
        "EipIp": fields.Str(required=True, load_from="EipIp"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Proportion": fields.Int(required=False, load_from="Proportion"),
        "Region": fields.Str(required=True, load_from="Region"),
        "RemainCount": fields.Int(required=False, load_from="RemainCount"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "UPhoneIds": fields.List(fields.Str()),
    }


class UPhoneImageInstanceSchema(schema.ResponseSchema):
    """UPhoneImageInstance -"""

    fields = {
        "AppVersions": fields.List(AppVersionInstanceSchema()),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Description": fields.Str(required=False, load_from="Description"),
        "ImageId": fields.Str(required=True, load_from="ImageId"),
        "ImageName": fields.Str(required=True, load_from="ImageName"),
        "ImageState": fields.Str(required=True, load_from="ImageState"),
        "ImageType": fields.Str(required=True, load_from="ImageType"),
        "ModifyTime": fields.Int(required=True, load_from="ModifyTime"),
        "OsType": fields.Str(required=True, load_from="OsType"),
        "UPhoneId": fields.Str(required=False, load_from="UPhoneId"),
    }


class IpRegionSchema(schema.ResponseSchema):
    """IpRegion - 独立IP地域信息"""

    fields = {
        "Id": fields.Str(required=True, load_from="Id"),
        "StockStatus": fields.Str(required=True, load_from="StockStatus"),
    }


class TaskSchema(schema.ResponseSchema):
    """Task -"""

    fields = {
        "AppVersionId": fields.Str(required=False, load_from="AppVersionId"),
        "BeginTime": fields.Int(required=True, load_from="BeginTime"),
        "EndTime": fields.Int(required=True, load_from="EndTime"),
        "ErrorMsg": fields.Str(required=True, load_from="ErrorMsg"),
        "ExecuteMsg": fields.Str(required=False, load_from="ExecuteMsg"),
        "State": fields.Str(required=True, load_from="State"),
        "TaskId": fields.Str(required=True, load_from="TaskId"),
        "UPhoneId": fields.Str(required=False, load_from="UPhoneId"),
    }


class JobSchema(schema.ResponseSchema):
    """Job -"""

    fields = {
        "AppVersionId": fields.Str(required=False, load_from="AppVersionId"),
        "BeginTime": fields.Int(required=False, load_from="BeginTime"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EndTime": fields.Int(required=False, load_from="EndTime"),
        "JobId": fields.Str(required=False, load_from="JobId"),
        "JobType": fields.Str(required=False, load_from="JobType"),
        "State": fields.Str(required=False, load_from="State"),
        "Tasks": fields.List(TaskSchema()),
        "UPhoneIds": fields.List(fields.Str()),
    }


class UPhoneModelInstanceSchema(schema.ResponseSchema):
    """UPhoneModelInstance -"""

    fields = {
        "CPU": fields.Int(required=True, load_from="CPU"),
        "Description": fields.Str(required=False, load_from="Description"),
        "DiskSize": fields.Int(required=True, load_from="DiskSize"),
        "Dpi": fields.Int(required=False, load_from="Dpi"),
        "Memory": fields.Int(required=True, load_from="Memory"),
        "Refresh": fields.Int(required=True, load_from="Refresh"),
        "Resolution": fields.Str(required=True, load_from="Resolution"),
        "UPhoneModelName": fields.Str(
            required=True, load_from="UPhoneModelName"
        ),
    }


class ServerDiskSetSchema(schema.ResponseSchema):
    """ServerDiskSet -"""

    fields = {
        "DiskType": fields.Str(required=True, load_from="DiskType"),
        "IsBoot": fields.Bool(required=True, load_from="IsBoot"),
        "Size": fields.Int(required=True, load_from="Size"),
    }


class UPhoneSpecSchema(schema.ResponseSchema):
    """UPhoneSpec -"""

    fields = {
        "UPhoneCount": fields.Int(required=False, load_from="UPhoneCount"),
        "UPhoneModelName": fields.Str(
            required=False, load_from="UPhoneModelName"
        ),
    }


class IpSetSchema(schema.ResponseSchema):
    """IpSet -"""

    fields = {
        "Ip": fields.Str(required=False, load_from="Ip"),
        "IpMode": fields.Str(required=False, load_from="IpMode"),
        "IpType": fields.Str(required=False, load_from="IpType"),
        "Isp": fields.Str(required=False, load_from="Isp"),
    }


class ServerModelInstanceSchema(schema.ResponseSchema):
    """ServerModelInstance -"""

    fields = {
        "CPU": fields.Int(required=False, load_from="CPU"),
        "DiskSet": fields.List(ServerDiskSetSchema()),
        "GPU": fields.Int(required=False, load_from="GPU"),
        "GPUType": fields.Str(required=False, load_from="GPUType"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "ServerModelName": fields.Str(
            required=False, load_from="ServerModelName"
        ),
        "ServerModelState": fields.Str(
            required=False, load_from="ServerModelState"
        ),
        "UPhoneSpecs": fields.List(UPhoneSpecSchema()),
    }


class ServerInstanceSchema(schema.ResponseSchema):
    """ServerInstance -"""

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "CityId": fields.Str(required=True, load_from="CityId"),
        "CityName": fields.Str(required=True, load_from="CityName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "IpSet": fields.List(IpSetSchema()),
        "ModifyTime": fields.Int(required=True, load_from="ModifyTime"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ServerId": fields.Str(required=True, load_from="ServerId"),
        "ServerModel": ServerModelInstanceSchema(),
        "ServerName": fields.Str(required=True, load_from="ServerName"),
        "State": fields.Str(required=False, load_from="State"),
        "UPhoneCount": fields.Int(required=False, load_from="UPhoneCount"),
        "UPhoneModelName": fields.Str(
            required=True, load_from="UPhoneModelName"
        ),
    }


class StockInfoSchema(schema.ResponseSchema):
    """StockInfo - model的可用量信息"""

    fields = {
        "ModelName": fields.Str(required=False, load_from="ModelName"),
        "StockCount": fields.Int(required=False, load_from="StockCount"),
    }


class ShareBandwidthInfoSchema(schema.ResponseSchema):
    """ShareBandwidthInfo - 共享带宽信息"""

    fields = {
        "Bandwidth": fields.Int(required=True, load_from="Bandwidth"),
        "BindCount": fields.Int(required=False, load_from="BindCount"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Id": fields.Str(required=True, load_from="Id"),
        "IpCount": fields.Int(required=False, load_from="IpCount"),
        "IpProportion": fields.Int(required=True, load_from="IpProportion"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Region": fields.Str(required=True, load_from="Region"),
        "RemainCount": fields.Int(required=False, load_from="RemainCount"),
        "Remark": fields.Str(required=False, load_from="Remark"),
    }


class UPhoneAllowanceSchema(schema.ResponseSchema):
    """UPhoneAllowance - 云手机余量结构体"""

    fields = {
        "Allowance": fields.Int(required=True, load_from="Allowance"),
        "ModelName": fields.Str(required=True, load_from="ModelName"),
    }


class UPhonePriceSetSchema(schema.ResponseSchema):
    """UPhonePriceSet - 云手机价格列表"""

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "ListPrice": fields.Float(required=False, load_from="ListPrice"),
        "OriginalPrice": fields.Float(required=True, load_from="OriginalPrice"),
        "Price": fields.Float(required=True, load_from="Price"),
    }


class UPhoneServerPriceSetSchema(schema.ResponseSchema):
    """UPhoneServerPriceSet - 价格列表"""

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "ListPrice": fields.Float(required=False, load_from="ListPrice"),
        "OriginalPrice": fields.Float(required=True, load_from="OriginalPrice"),
        "Price": fields.Float(required=True, load_from="Price"),
    }


class UPhoneCommandResultSchema(schema.ResponseSchema):
    """UPhoneCommandResult -"""

    fields = {
        "ExecuteMsg": fields.Str(required=False, load_from="ExecuteMsg"),
        "UPhoneId": fields.Str(required=False, load_from="UPhoneId"),
    }


class ResultsSchema(schema.ResponseSchema):
    """Results -"""

    fields = {
        "ExecuteMsg": fields.Str(required=False, load_from="ExecuteMsg"),
        "UPhoneId": fields.Str(required=False, load_from="UPhoneId"),
    }
