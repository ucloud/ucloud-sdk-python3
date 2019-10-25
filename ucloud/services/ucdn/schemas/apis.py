""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.ucdn.schemas import models


""" UCDN API Schema
"""


"""
API: DescribeNewUcdnPrefetchCacheTask

获取预取任务状态
"""


class DescribeNewUcdnPrefetchCacheTaskRequestSchema(schema.RequestSchema):
    """ DescribeNewUcdnPrefetchCacheTask - 获取预取任务状态
    """

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Status": fields.Str(required=False, dump_to="Status"),
        "TaskId": fields.List(fields.Str()),
    }


class DescribeNewUcdnPrefetchCacheTaskResponseSchema(schema.ResponseSchema):
    """ DescribeNewUcdnPrefetchCacheTask - 获取预取任务状态
    """

    fields = {
        "TaskList": fields.List(
            models.TaskInfoSchema(), required=False, load_from="TaskList"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeNewUcdnRefreshCacheTask

获取域名刷新任务状态
"""


class DescribeNewUcdnRefreshCacheTaskRequestSchema(schema.RequestSchema):
    """ DescribeNewUcdnRefreshCacheTask - 获取域名刷新任务状态
    """

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Status": fields.Str(required=False, dump_to="Status"),
        "TaskId": fields.List(fields.Str()),
    }


class DescribeNewUcdnRefreshCacheTaskResponseSchema(schema.ResponseSchema):
    """ DescribeNewUcdnRefreshCacheTask - 获取域名刷新任务状态
    """

    fields = {
        "TaskList": fields.List(
            models.TaskInfoSchema(), required=False, load_from="TaskList"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetNewUcdnDomainBandwidth

获取域名带宽数据
"""


class GetNewUcdnDomainBandwidthRequestSchema(schema.RequestSchema):
    """ GetNewUcdnDomainBandwidth - 获取域名带宽数据
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainBandwidthResponseSchema(schema.ResponseSchema):
    """ GetNewUcdnDomainBandwidth - 获取域名带宽数据
    """

    fields = {
        "BandwidthList": fields.List(
            models.BandwidthInfoSchema(),
            required=False,
            load_from="BandwidthList",
        ),
        "Traffic": fields.Str(required=False, load_from="Traffic"),
    }


"""
API: GetNewUcdnDomainHitRate

获取域名命中率
"""


class GetNewUcdnDomainHitRateRequestSchema(schema.RequestSchema):
    """ GetNewUcdnDomainHitRate - 获取域名命中率
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainHitRateResponseSchema(schema.ResponseSchema):
    """ GetNewUcdnDomainHitRate - 获取域名命中率
    """

    fields = {
        "HitRateList": fields.List(
            models.HitRateInfoSchema(), required=False, load_from="HitRateList"
        )
    }


"""
API: GetNewUcdnDomainHttpCode

获取域名状态码监控
"""


class GetNewUcdnDomainHttpCodeRequestSchema(schema.RequestSchema):
    """ GetNewUcdnDomainHttpCode - 获取域名状态码监控
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainHttpCodeResponseSchema(schema.ResponseSchema):
    """ GetNewUcdnDomainHttpCode - 获取域名状态码监控
    """

    fields = {
        "HttpCodeDetail": fields.List(
            models.HttpCodeInfoSchema(),
            required=False,
            load_from="HttpCodeDetail",
        )
    }


"""
API: GetNewUcdnDomainHttpCodeV2

获取域名详细状态码监控
"""


class GetNewUcdnDomainHttpCodeV2RequestSchema(schema.RequestSchema):
    """ GetNewUcdnDomainHttpCodeV2 - 获取域名详细状态码监控
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainHttpCodeV2ResponseSchema(schema.ResponseSchema):
    """ GetNewUcdnDomainHttpCodeV2 - 获取域名详细状态码监控
    """

    fields = {
        "HttpCodeV2Detail": fields.List(
            models.HttpCodeV2DetailSchema(),
            required=False,
            load_from="HttpCodeV2Detail",
        )
    }


"""
API: GetNewUcdnDomainRequestNum

获取域名请求数
"""


class GetNewUcdnDomainRequestNumRequestSchema(schema.RequestSchema):
    """ GetNewUcdnDomainRequestNum - 获取域名请求数
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainRequestNumResponseSchema(schema.ResponseSchema):
    """ GetNewUcdnDomainRequestNum - 获取域名请求数
    """

    fields = {
        "RequestList": fields.List(
            models.RequestInfoSchema(), required=False, load_from="RequestList"
        )
    }


"""
API: GetUcdnDomainLog

获取加速域名原始日志
"""


class GetUcdnDomainLogRequestSchema(schema.RequestSchema):
    """ GetUcdnDomainLog - 获取加速域名原始日志
    """

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class GetUcdnDomainLogResponseSchema(schema.ResponseSchema):
    """ GetUcdnDomainLog - 获取加速域名原始日志
    """

    fields = {
        "LogSet": fields.List(
            models.LogSetListSchema(), required=False, load_from="LogSet"
        )
    }


"""
API: GetUcdnDomainPrefetchEnable

获取域名预取开启状态
"""


class GetUcdnDomainPrefetchEnableRequestSchema(schema.RequestSchema):
    """ GetUcdnDomainPrefetchEnable - 获取域名预取开启状态
    """

    fields = {
        "DomainId": fields.Str(required=True, dump_to="DomainId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomainPrefetchEnableResponseSchema(schema.ResponseSchema):
    """ GetUcdnDomainPrefetchEnable - 获取域名预取开启状态
    """

    fields = {"Enable": fields.Int(required=False, load_from="Enable")}


"""
API: GetUcdnDomainRequestNumV2

获取域名请求数
"""


class GetUcdnDomainRequestNumV2RequestSchema(schema.RequestSchema):
    """ GetUcdnDomainRequestNumV2 - 获取域名请求数
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainRequestNumV2ResponseSchema(schema.ResponseSchema):
    """ GetUcdnDomainRequestNumV2 - 获取域名请求数
    """

    fields = {
        "RequestList": fields.List(
            models.RequestInfoSchema(), required=False, load_from="RequestList"
        )
    }


"""
API: GetUcdnDomainTraffic

获取加速域名流量使用信息
"""


class GetUcdnDomainTrafficRequestSchema(schema.RequestSchema):
    """ GetUcdnDomainTraffic - 获取加速域名流量使用信息
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomainTrafficResponseSchema(schema.ResponseSchema):
    """ GetUcdnDomainTraffic - 获取加速域名流量使用信息
    """

    fields = {
        "TrafficSet": fields.List(
            models.UcdnDomainTrafficSetSchema(),
            required=False,
            load_from="TrafficSet",
        )
    }


"""
API: GetUcdnPassBandwidth

获取回源带宽数据（cdn回客户源站部分）
"""


class GetUcdnPassBandwidthRequestSchema(schema.RequestSchema):
    """ GetUcdnPassBandwidth - 获取回源带宽数据（cdn回客户源站部分）
    """

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnPassBandwidthResponseSchema(schema.ResponseSchema):
    """ GetUcdnPassBandwidth - 获取回源带宽数据（cdn回客户源站部分）
    """

    fields = {
        "BandwidthDetail": fields.List(
            models.BandwidthInfoDetailSchema(),
            required=False,
            load_from="BandwidthDetail",
        )
    }


"""
API: GetUcdnTraffic

获取流量信息
"""


class GetUcdnTrafficRequestSchema(schema.RequestSchema):
    """ GetUcdnTraffic - 获取流量信息
    """

    fields = {"ProjectId": fields.Str(required=False, dump_to="ProjectId")}


class GetUcdnTrafficResponseSchema(schema.ResponseSchema):
    """ GetUcdnTraffic - 获取流量信息
    """

    fields = {
        "TrafficSet": fields.List(
            models.TrafficSetSchema(), required=False, load_from="TrafficSet"
        )
    }


"""
API: PrefetchNewUcdnDomainCache

提交预取任务
"""


class PrefetchNewUcdnDomainCacheRequestSchema(schema.RequestSchema):
    """ PrefetchNewUcdnDomainCache - 提交预取任务
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UrlList": fields.List(fields.Str()),
    }


class PrefetchNewUcdnDomainCacheResponseSchema(schema.ResponseSchema):
    """ PrefetchNewUcdnDomainCache - 提交预取任务
    """

    fields = {"TaskId": fields.Str(required=False, load_from="TaskId")}


"""
API: RefreshNewUcdnDomainCache

刷新缓存
"""


class RefreshNewUcdnDomainCacheRequestSchema(schema.RequestSchema):
    """ RefreshNewUcdnDomainCache - 刷新缓存
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "UrlList": fields.List(fields.Str()),
    }


class RefreshNewUcdnDomainCacheResponseSchema(schema.ResponseSchema):
    """ RefreshNewUcdnDomainCache - 刷新缓存
    """

    fields = {"TaskId": fields.Str(required=False, load_from="TaskId")}


"""
API: SwitchUcdnChargeType

切换账号计费方式
"""


class SwitchUcdnChargeTypeRequestSchema(schema.RequestSchema):
    """ SwitchUcdnChargeType - 切换账号计费方式
    """

    fields = {
        "ChargeType": fields.Str(required=True, dump_to="ChargeType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class SwitchUcdnChargeTypeResponseSchema(schema.ResponseSchema):
    """ SwitchUcdnChargeType - 切换账号计费方式
    """

    fields = {}
