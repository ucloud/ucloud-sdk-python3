""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class GlobalSSHAreaSchema(schema.ResponseSchema):
    """GlobalSSHArea -"""

    fields = {
        "Area": fields.Str(required=True, load_from="Area"),
        "AreaCode": fields.Str(required=True, load_from="AreaCode"),
        "RegionSet": fields.List(fields.Str()),
    }


class GlobalSSHInfoSchema(schema.ResponseSchema):
    """GlobalSSHInfo - GlobalSSH实例信息"""

    fields = {
        "AcceleratingDomain": fields.Str(
            required=True, load_from="AcceleratingDomain"
        ),
        "Area": fields.Str(required=True, load_from="Area"),
        "BandwidthPackage": fields.Int(
            required=False, load_from="BandwidthPackage"
        ),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DomainStatus": fields.Str(),
        "Expire": fields.Bool(required=True, load_from="Expire"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "ExtraDomain": fields.List(fields.Str()),
        "ForwardRegion": fields.Str(required=False, load_from="ForwardRegion"),
        "GlobalSSHPort": fields.Int(required=True, load_from="GlobalSSHPort"),
        "IPV6Access": fields.Bool(required=False, load_from="IPV6Access"),
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "InstanceType": fields.Str(required=True, load_from="InstanceType"),
        "Port": fields.Int(required=True, load_from="Port"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "TargetIP": fields.Str(required=True, load_from="TargetIP"),
    }


class LineDetailSchema(schema.ResponseSchema):
    """LineDetail - 子线路"""

    fields = {
        "LineFrom": fields.Str(required=True, load_from="LineFrom"),
        "LineFromName": fields.Str(required=True, load_from="LineFromName"),
        "LineId": fields.Str(required=False, load_from="LineId"),
        "LineTo": fields.Str(required=True, load_from="LineTo"),
        "LineToName": fields.Str(required=True, load_from="LineToName"),
    }


class UGAALineSchema(schema.ResponseSchema):
    """UGAALine - PathX线路参数"""

    fields = {
        "FlagUnicodeFrom": fields.Str(
            required=True, load_from="FlagUnicodeFrom"
        ),
        "FlagUnicodeTo": fields.Str(required=True, load_from="FlagUnicodeTo"),
        "GuaranteedBandwidthProportion": fields.Int(
            required=True, load_from="GuaranteedBandwidthProportion"
        ),
        "LineDetail": fields.List(LineDetailSchema()),
        "LineFrom": fields.Str(required=True, load_from="LineFrom"),
        "LineFromName": fields.Str(required=True, load_from="LineFromName"),
        "LineId": fields.Str(required=True, load_from="LineId"),
        "LineTo": fields.Str(required=True, load_from="LineTo"),
        "LineToName": fields.Str(required=True, load_from="LineToName"),
        "MaxBandwidth": fields.Int(required=True, load_from="MaxBandwidth"),
        "PostPaidMaxBandwidth": fields.Int(
            required=True, load_from="PostPaidMaxBandwidth"
        ),
        "RegionCategoryFrom": fields.Str(
            required=True, load_from="RegionCategoryFrom"
        ),
        "RegionCategoryTo": fields.Str(
            required=True, load_from="RegionCategoryTo"
        ),
        "SupportPublicNetwork": fields.Bool(
            required=True, load_from="SupportPublicNetwork"
        ),
    }


class SSLBindedTargetSetSchema(schema.ResponseSchema):
    """SSLBindedTargetSet - Describle SSL Bind UAG Info"""

    fields = {
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
    }


class PathXSSLSetSchema(schema.ResponseSchema):
    """PathXSSLSet - Describle PathX SSL"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "SSLBindedTargetSet": fields.List(SSLBindedTargetSetSchema()),
        "SSLContent": fields.Str(required=False, load_from="SSLContent"),
        "SSLId": fields.Str(required=False, load_from="SSLId"),
        "SSLMD5": fields.Str(required=False, load_from="SSLMD5"),
        "SSLName": fields.Str(required=False, load_from="SSLName"),
        "SourceType": fields.Int(required=False, load_from="SourceType"),
        "SubjectName": fields.Str(required=False, load_from="SubjectName"),
    }


class ForwardAreaSchema(schema.ResponseSchema):
    """ForwardArea -"""

    fields = {
        "Area": fields.Str(required=True, load_from="Area"),
        "AreaCode": fields.Str(required=True, load_from="AreaCode"),
        "ContinentCode": fields.Str(required=True, load_from="ContinentCode"),
        "CountryCode": fields.Str(required=True, load_from="CountryCode"),
        "FlagEmoji": fields.Str(required=True, load_from="FlagEmoji"),
        "FlagUnicode": fields.Str(required=True, load_from="FlagUnicode"),
    }


class SrcAreaInfoSchema(schema.ResponseSchema):
    """SrcAreaInfo -"""

    fields = {
        "Area": fields.Str(required=True, load_from="Area"),
        "AreaCode": fields.Str(required=True, load_from="AreaCode"),
        "FlagEmoji": fields.Str(required=True, load_from="FlagEmoji"),
        "FlagUnicode": fields.Str(required=True, load_from="FlagUnicode"),
    }


class OutPublicIpInfoSchema(schema.ResponseSchema):
    """OutPublicIpInfo - 线路回源IP信息"""

    fields = {
        "Area": fields.Str(required=False, load_from="Area"),
        "IP": fields.Str(required=False, load_from="IP"),
    }


class AccelerationAreaInfosSchema(schema.ResponseSchema):
    """AccelerationAreaInfos -"""

    fields = {
        "AccelerationArea": fields.Str(
            required=True, load_from="AccelerationArea"
        ),
        "AccelerationNodes": fields.List(SrcAreaInfoSchema()),
    }


class ForwardTaskSchema(schema.ResponseSchema):
    """ForwardTask -"""

    fields = {
        "Port": fields.Int(required=True, load_from="Port"),
        "Protocol": fields.Str(required=True, load_from="Protocol"),
        "RSPort": fields.Int(required=True, load_from="RSPort"),
    }


class ForwardInfoSchema(schema.ResponseSchema):
    """ForwardInfo -"""

    fields = {
        "AccelerationArea": fields.Str(
            required=True, load_from="AccelerationArea"
        ),
        "AccelerationAreaInfos": fields.List(AccelerationAreaInfosSchema()),
        "AccelerationAreaName": fields.Str(
            required=True, load_from="AccelerationAreaName"
        ),
        "Bandwidth": fields.Int(required=True, load_from="Bandwidth"),
        "CName": fields.Str(required=True, load_from="CName"),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Domain": fields.Str(required=False, load_from="Domain"),
        "EgressIpList": fields.List(OutPublicIpInfoSchema()),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "IPList": fields.List(fields.Str()),
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "Name": fields.Str(required=True, load_from="Name"),
        "OriginArea": fields.Str(required=True, load_from="OriginArea"),
        "OriginAreaCode": fields.Str(required=True, load_from="OriginAreaCode"),
        "PortSets": fields.List(ForwardTaskSchema()),
        "Remark": fields.Str(required=False, load_from="Remark"),
    }


class NodeDelaysSchema(schema.ResponseSchema):
    """NodeDelays -"""

    fields = {
        "Area": fields.Str(required=True, load_from="Area"),
        "AreaCode": fields.Str(required=True, load_from="AreaCode"),
        "CountryCode": fields.Str(required=True, load_from="CountryCode"),
        "FlagEmoji": fields.Str(required=True, load_from="FlagEmoji"),
        "FlagUnicode": fields.Str(required=True, load_from="FlagUnicode"),
        "Latency": fields.Float(required=True, load_from="Latency"),
        "LatencyInternet": fields.Float(
            required=True, load_from="LatencyInternet"
        ),
        "LatencyOptimization": fields.Float(
            required=True, load_from="LatencyOptimization"
        ),
        "Loss": fields.Float(required=True, load_from="Loss"),
        "LossInternet": fields.Float(required=True, load_from="LossInternet"),
        "LossOptimization": fields.Float(
            required=True, load_from="LossOptimization"
        ),
    }


class AccelerationInfoSchema(schema.ResponseSchema):
    """AccelerationInfo -"""

    fields = {
        "AccelerationArea": fields.Str(
            required=True, load_from="AccelerationArea"
        ),
        "AccelerationName": fields.Str(
            required=True, load_from="AccelerationName"
        ),
        "NodeInfo": fields.List(NodeDelaysSchema()),
    }


class UPathSetSchema(schema.ResponseSchema):
    """UPathSet - uga关联的upath信息"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "LineFrom": fields.Str(required=False, load_from="LineFrom"),
        "LineFromName": fields.Str(required=False, load_from="LineFromName"),
        "LineId": fields.Str(required=False, load_from="LineId"),
        "LineTo": fields.Str(required=False, load_from="LineTo"),
        "LineToName": fields.Str(required=False, load_from="LineToName"),
        "UPathId": fields.Str(required=False, load_from="UPathId"),
        "UPathName": fields.Str(required=False, load_from="UPathName"),
    }


class UGAATaskSchema(schema.ResponseSchema):
    """UGAATask - 用户在UGAA实例下配置的多端口任务"""

    fields = {
        "Port": fields.Int(required=True, load_from="Port"),
        "Protocol": fields.Str(required=True, load_from="Protocol"),
    }


class UGAL7ForwarderSchema(schema.ResponseSchema):
    """UGAL7Forwarder - UGA实例 7层转发器信息"""

    fields = {
        "Port": fields.Int(required=True, load_from="Port"),
        "Protocol": fields.Str(required=True, load_from="Protocol"),
        "RSPort": fields.Int(required=True, load_from="RSPort"),
        "SSLId": fields.Str(required=False, load_from="SSLId"),
        "SSLName": fields.Str(required=False, load_from="SSLName"),
    }


class UGAL4ForwarderSchema(schema.ResponseSchema):
    """UGAL4Forwarder - UGA实例 4层转发器信息"""

    fields = {
        "Port": fields.Int(required=True, load_from="Port"),
        "Protocol": fields.Str(required=True, load_from="Protocol"),
        "RSPort": fields.Int(required=True, load_from="RSPort"),
    }


class UGAAInfoSchema(schema.ResponseSchema):
    """UGAAInfo - 全球加速实例信息"""

    fields = {
        "CName": fields.Str(required=True, load_from="CName"),
        "Domain": fields.Str(required=False, load_from="Domain"),
        "IPList": fields.List(fields.Str()),
        "L4ForwarderSet": fields.List(UGAL4ForwarderSchema()),
        "L7ForwarderSet": fields.List(UGAL7ForwarderSchema()),
        "Location": fields.Str(required=False, load_from="Location"),
        "OutPublicIpList": fields.List(OutPublicIpInfoSchema()),
        "TaskSet": fields.List(UGAATaskSchema()),
        "UGAId": fields.Str(required=True, load_from="UGAId"),
        "UGAName": fields.Str(required=True, load_from="UGAName"),
        "UPathSet": fields.List(UPathSetSchema()),
    }


class PathXUGAInfoSchema(schema.ResponseSchema):
    """PathXUGAInfo - 加速实例配置信息"""

    fields = {
        "Domain": fields.Str(required=False, load_from="Domain"),
        "IPList": fields.List(fields.Str()),
        "UGAId": fields.Str(required=False, load_from="UGAId"),
    }


class UPathInfoSchema(schema.ResponseSchema):
    """UPathInfo - 加速线路信息"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "LineFromName": fields.Str(required=False, load_from="LineFromName"),
        "LineId": fields.Str(required=False, load_from="LineId"),
        "LineToName": fields.Str(required=False, load_from="LineToName"),
        "Name": fields.Str(required=False, load_from="Name"),
        "OutPublicIpList": fields.List(OutPublicIpInfoSchema()),
        "PostPaid": fields.Bool(required=False, load_from="PostPaid"),
        "UGAList": fields.List(PathXUGAInfoSchema()),
        "UPathId": fields.Str(required=False, load_from="UPathId"),
    }


class AlarmRulerSchema(schema.ResponseSchema):
    """AlarmRuler - 告警详情"""

    fields = {
        "AlarmFrequency": fields.Int(required=True, load_from="AlarmFrequency"),
        "AlarmStrategy": fields.Str(required=True, load_from="AlarmStrategy"),
        "AlarmTemplateRuleId": fields.Int(
            required=True, load_from="AlarmTemplateRuleId"
        ),
        "Compare": fields.Str(required=True, load_from="Compare"),
        "ContactGroupId": fields.Int(required=True, load_from="ContactGroupId"),
        "MetricName": fields.Str(required=True, load_from="MetricName"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "Threshold": fields.Int(required=True, load_from="Threshold"),
        "TriggerCount": fields.Int(required=True, load_from="TriggerCount"),
    }


class TrafficDailyRecentlySchema(schema.ResponseSchema):
    """TrafficDailyRecently - 最近3个月日流量统计"""

    fields = {
        "Day": fields.Str(required=False, load_from="Day"),
        "TrafficUnitGB": fields.Str(required=False, load_from="TrafficUnitGB"),
        "TrafficUnitMB": fields.Str(required=False, load_from="TrafficUnitMB"),
    }


class TrafficDailySchema(schema.ResponseSchema):
    """TrafficDaily -"""

    fields = {
        "BillingState": fields.Str(required=True, load_from="BillingState"),
        "Date": fields.Int(required=True, load_from="Date"),
        "Traffic": fields.Int(required=True, load_from="Traffic"),
    }


class MatricPointSchema(schema.ResponseSchema):
    """MatricPoint -"""

    fields = {
        "Timestamp": fields.Int(required=False, load_from="Timestamp"),
        "Value": fields.Int(required=False, load_from="Value"),
    }


class MetricPeriodSchema(schema.ResponseSchema):
    """MetricPeriod - 一段时间内的监控数据"""

    fields = {
        "NetworkIn": fields.List(MatricPointSchema()),
        "NetworkInUsage": fields.List(MatricPointSchema()),
        "NetworkOut": fields.List(MatricPointSchema()),
        "NetworkOutUsage": fields.List(MatricPointSchema()),
    }


class UGA3MetricSchema(schema.ResponseSchema):
    """UGA3Metric -"""

    fields = {
        "ConnectCount": fields.List(MatricPointSchema()),
        "ConnectCountSubline": fields.List(MatricPointSchema()),
        "Delay": fields.List(MatricPointSchema()),
        "DelayPromote": fields.List(MatricPointSchema()),
        "DelayPromoteSubline": fields.List(MatricPointSchema()),
        "DelaySubline": fields.List(MatricPointSchema()),
        "NetworkIn": fields.List(MatricPointSchema()),
        "NetworkInSubline": fields.List(MatricPointSchema()),
        "NetworkInUsage": fields.List(MatricPointSchema()),
        "NetworkOut": fields.List(MatricPointSchema()),
        "NetworkOutSubline": fields.List(MatricPointSchema()),
        "NetworkOutUsage": fields.List(MatricPointSchema()),
    }


class UGA3PriceSchema(schema.ResponseSchema):
    """UGA3Price -"""

    fields = {
        "AccelerationArea": fields.Str(
            required=True, load_from="AccelerationArea"
        ),
        "AccelerationAreaName": fields.Str(
            required=True, load_from="AccelerationAreaName"
        ),
        "AccelerationBandwidthPrice": fields.Float(
            required=True, load_from="AccelerationBandwidthPrice"
        ),
        "AccelerationForwarderPrice": fields.Float(
            required=True, load_from="AccelerationForwarderPrice"
        ),
    }
