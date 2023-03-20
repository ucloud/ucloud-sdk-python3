""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.uslk.schemas import models

""" USLK API Schema
"""


"""
API: BatchCreateUSLKShortLink

批量创建短链接【免审】
"""


class BatchCreateUSLKShortLinkRequestSchema(schema.RequestSchema):
    """BatchCreateUSLKShortLink - 批量创建短链接【免审】"""

    fields = {
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "LongLinks": fields.List(fields.Str()),
        "Proto": fields.Str(required=True, dump_to="Proto"),
        "ScenarioID": fields.Int(required=True, dump_to="ScenarioID"),
        "ShortLinkDomain": fields.Str(required=True, dump_to="ShortLinkDomain"),
        "StartTime": fields.Int(required=True, dump_to="StartTime"),
    }


class BatchCreateUSLKShortLinkResponseSchema(schema.ResponseSchema):
    """BatchCreateUSLKShortLink - 批量创建短链接【免审】"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
        "ShortLinks": fields.List(
            fields.Str(), required=True, load_from="ShortLinks"
        ),
    }


"""
API: CreateUSLKLongLink

报备长链接
"""


class CreateUSLKLongLinkRequestSchema(schema.RequestSchema):
    """CreateUSLKLongLink - 报备长链接"""

    fields = {
        "LongLink": fields.Str(required=True, dump_to="LongLink"),
        "ScenarioID": fields.Int(required=True, dump_to="ScenarioID"),
    }


class CreateUSLKLongLinkResponseSchema(schema.ResponseSchema):
    """CreateUSLKLongLink - 报备长链接"""

    fields = {
        "LongLinkID": fields.Int(required=False, load_from="LongLinkID"),
        "Message": fields.Str(required=True, load_from="Message"),
        "ReqUuid": fields.Str(required=False, load_from="ReqUuid"),
    }


"""
API: CreateUSLKScenario

长链接报备场景创建
"""


class CreateUSLKScenarioRequestSchema(schema.RequestSchema):
    """CreateUSLKScenario - 长链接报备场景创建"""

    fields = {
        "Scenario": fields.Str(required=True, dump_to="Scenario"),
        "ScenarioDesc": fields.Str(required=True, dump_to="ScenarioDesc"),
    }


class CreateUSLKScenarioResponseSchema(schema.ResponseSchema):
    """CreateUSLKScenario - 长链接报备场景创建"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
        "ReqUuid": fields.Str(required=False, load_from="ReqUuid"),
        "ScenarioID": fields.Int(required=False, load_from="ScenarioID"),
    }


"""
API: CreateUSLKShortLink

创建短链接
"""


class CreateUSLKShortLinkRequestSchema(schema.RequestSchema):
    """CreateUSLKShortLink - 创建短链接"""

    fields = {
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "LongLinkID": fields.Int(required=True, dump_to="LongLinkID"),
        "Proto": fields.Str(required=True, dump_to="Proto"),
        "ShortLinkDomain": fields.Str(
            required=False, dump_to="ShortLinkDomain"
        ),
        "StartTime": fields.Int(required=True, dump_to="StartTime"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class CreateUSLKShortLinkResponseSchema(schema.ResponseSchema):
    """CreateUSLKShortLink - 创建短链接"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
        "ShortLink": fields.Str(required=False, load_from="ShortLink"),
    }


"""
API: DescribeUSLKRedirectRecords

查询短链接访问明细列表
"""


class DescribeUSLKRedirectRecordsRequestSchema(schema.RequestSchema):
    """DescribeUSLKRedirectRecords - 查询短链接访问明细列表"""

    fields = {
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "FuzzySearch": fields.Str(required=False, dump_to="FuzzySearch"),
        "NumPerPage": fields.Int(required=False, dump_to="NumPerPage"),
        "OrderBy": fields.Str(required=False, dump_to="OrderBy"),
        "OrderType": fields.Str(required=False, dump_to="OrderType"),
        "Page": fields.Int(required=False, dump_to="Page"),
        "ShortLink": fields.Str(required=True, dump_to="ShortLink"),
        "StartTime": fields.Int(required=True, dump_to="StartTime"),
    }


class DescribeUSLKRedirectRecordsResponseSchema(schema.ResponseSchema):
    """DescribeUSLKRedirectRecords - 查询短链接访问明细列表"""

    fields = {
        "Data": fields.List(
            models.RedirectRecordsSchema(), required=False, load_from="Data"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
        "Total": fields.Int(required=False, load_from="Total"),
    }


"""
API: DescribeUSLKShortLinkList

查询短链接列表
"""


class DescribeUSLKShortLinkListRequestSchema(schema.RequestSchema):
    """DescribeUSLKShortLinkList - 查询短链接列表"""

    fields = {
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "FuzzySearch": fields.Str(required=False, dump_to="FuzzySearch"),
        "LongLinkID": fields.Int(required=False, dump_to="LongLinkID"),
        "NumPerPage": fields.Int(required=False, dump_to="NumPerPage"),
        "OrderBy": fields.Str(required=False, dump_to="OrderBy"),
        "OrderType": fields.Str(required=False, dump_to="OrderType"),
        "Page": fields.Int(required=False, dump_to="Page"),
        "ScenarioID": fields.Int(required=False, dump_to="ScenarioID"),
        "ShortLink": fields.Str(required=False, dump_to="ShortLink"),
        "StartTime": fields.Int(required=False, dump_to="StartTime"),
        "Status": fields.Int(required=False, dump_to="Status"),
    }


class DescribeUSLKShortLinkListResponseSchema(schema.ResponseSchema):
    """DescribeUSLKShortLinkList - 查询短链接列表"""

    fields = {
        "Data": fields.List(
            models.ShortLinkSchema(), required=False, load_from="Data"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }