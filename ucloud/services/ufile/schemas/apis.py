""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.ufile.schemas import models

""" UFile API Schema
"""


"""
API: CreateBucket

创建Bucket
"""


class CreateBucketRequestSchema(schema.RequestSchema):
    """CreateBucket - 创建Bucket"""

    fields = {
        "BucketName": fields.Str(required=True, dump_to="BucketName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Type": fields.Str(required=False, dump_to="Type"),
    }


class CreateBucketResponseSchema(schema.ResponseSchema):
    """CreateBucket - 创建Bucket"""

    fields = {
        "BucketId": fields.Str(required=False, load_from="BucketId"),
        "BucketName": fields.Str(required=False, load_from="BucketName"),
    }


"""
API: CreateUFileToken

创建US3令牌
"""


class CreateUFileTokenRequestSchema(schema.RequestSchema):
    """CreateUFileToken - 创建US3令牌"""

    fields = {
        "AllowedBuckets": fields.List(fields.Str()),
        "AllowedOps": fields.List(fields.Str()),
        "AllowedPrefixes": fields.List(fields.Str()),
        "ExpireTime": fields.Int(required=False, dump_to="ExpireTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "TokenName": fields.Str(required=True, dump_to="TokenName"),
    }


class CreateUFileTokenResponseSchema(schema.ResponseSchema):
    """CreateUFileToken - 创建US3令牌"""

    fields = {
        "TokenId": fields.Str(required=False, load_from="TokenId"),
    }


"""
API: DeleteBucket

删除Bucket
"""


class DeleteBucketRequestSchema(schema.RequestSchema):
    """DeleteBucket - 删除Bucket"""

    fields = {
        "BucketName": fields.Str(required=True, dump_to="BucketName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DeleteBucketResponseSchema(schema.ResponseSchema):
    """DeleteBucket - 删除Bucket"""

    fields = {
        "BucketId": fields.Str(required=False, load_from="BucketId"),
        "BucketName": fields.Str(required=False, load_from="BucketName"),
    }


"""
API: DeleteUFileToken

删除令牌
"""


class DeleteUFileTokenRequestSchema(schema.RequestSchema):
    """DeleteUFileToken - 删除令牌"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "TokenId": fields.Str(required=True, dump_to="TokenId"),
    }


class DeleteUFileTokenResponseSchema(schema.ResponseSchema):
    """DeleteUFileToken - 删除令牌"""

    fields = {}


"""
API: DescribeBucket

获取Bucket的描述信息
"""


class DescribeBucketRequestSchema(schema.RequestSchema):
    """DescribeBucket - 获取Bucket的描述信息"""

    fields = {
        "BucketName": fields.Str(required=False, dump_to="BucketName"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
    }


class DescribeBucketResponseSchema(schema.ResponseSchema):
    """DescribeBucket - 获取Bucket的描述信息"""

    fields = {
        "DataSet": fields.List(
            models.UFileBucketSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DescribeUFileToken

获取令牌信息
"""


class DescribeUFileTokenRequestSchema(schema.RequestSchema):
    """DescribeUFileToken - 获取令牌信息"""

    fields = {
        "Display": fields.Int(required=False, dump_to="Display"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "TokenId": fields.Str(required=False, dump_to="TokenId"),
        "TokenName": fields.Str(required=False, dump_to="TokenName"),
    }


class DescribeUFileTokenResponseSchema(schema.ResponseSchema):
    """DescribeUFileToken - 获取令牌信息"""

    fields = {
        "DataSet": fields.List(
            models.UFileTokenSetSchema(), required=True, load_from="DataSet"
        ),
    }


"""
API: GetUFileQuota

查看配额状态
"""


class GetUFileQuotaRequestSchema(schema.RequestSchema):
    """GetUFileQuota - 查看配额状态"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "QuotaType": fields.Str(required=True, dump_to="QuotaType"),
    }


class GetUFileQuotaResponseSchema(schema.ResponseSchema):
    """GetUFileQuota - 查看配额状态"""

    fields = {
        "LeftQuota": fields.Float(required=False, load_from="LeftQuota"),
    }


"""
API: GetUFileQuotaInfo

获取配额信息
"""


class GetUFileQuotaInfoRequestSchema(schema.RequestSchema):
    """GetUFileQuotaInfo - 获取配额信息"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "QuotaType": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class GetUFileQuotaInfoResponseSchema(schema.ResponseSchema):
    """GetUFileQuotaInfo - 获取配额信息"""

    fields = {
        "DataSet": fields.List(
            models.UFileQuotaDataSetItemSchema(),
            required=False,
            load_from="DataSet",
        ),
    }


"""
API: GetUFileQuotaPrice

根据US3的购买配额，查询需要支付的价格。
"""


class GetUFileQuotaPriceRequestSchema(schema.RequestSchema):
    """GetUFileQuotaPrice - 根据US3的购买配额，查询需要支付的价格。"""

    fields = {
        "DownloadTraffic": fields.Int(
            required=False, dump_to="DownloadTraffic"
        ),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RequestCount": fields.Int(required=False, dump_to="RequestCount"),
        "StorageVolume": fields.Int(required=False, dump_to="StorageVolume"),
    }


class GetUFileQuotaPriceResponseSchema(schema.ResponseSchema):
    """GetUFileQuotaPrice - 根据US3的购买配额，查询需要支付的价格。"""

    fields = {
        "Price": fields.Float(required=False, load_from="Price"),
    }


"""
API: GetUFileReport

查看配额使用报表
"""


class GetUFileReportRequestSchema(schema.RequestSchema):
    """GetUFileReport - 查看配额使用报表"""

    fields = {
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "StartTime": fields.Int(required=True, dump_to="StartTime"),
    }


class GetUFileReportResponseSchema(schema.ResponseSchema):
    """GetUFileReport - 查看配额使用报表"""

    fields = {
        "DataSet": fields.List(
            models.UFileReportSetSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: SetUFileReferer

设置对象存储防盗链
"""


class SetUFileRefererRequestSchema(schema.RequestSchema):
    """SetUFileReferer - 设置对象存储防盗链"""

    fields = {
        "BucketName": fields.Str(required=True, dump_to="BucketName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "RefererAllowNull": fields.Bool(
            required=False, dump_to="RefererAllowNull"
        ),
        "RefererStatus": fields.Str(required=True, dump_to="RefererStatus"),
        "RefererType": fields.Int(required=False, dump_to="RefererType"),
        "Referers": fields.List(fields.Str()),
        "Region": fields.Str(required=False, dump_to="Region"),
    }


class SetUFileRefererResponseSchema(schema.ResponseSchema):
    """SetUFileReferer - 设置对象存储防盗链"""

    fields = {}


"""
API: UpdateBucket

更改Bucket的属性
"""


class UpdateBucketRequestSchema(schema.RequestSchema):
    """UpdateBucket - 更改Bucket的属性"""

    fields = {
        "BucketName": fields.Str(required=True, dump_to="BucketName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Str(required=True, dump_to="Type"),
    }


class UpdateBucketResponseSchema(schema.ResponseSchema):
    """UpdateBucket - 更改Bucket的属性"""

    fields = {
        "BucketId": fields.Str(required=False, load_from="BucketId"),
        "BucketName": fields.Str(required=False, load_from="BucketName"),
    }


"""
API: UpdateUFileToken

更新令牌的操作权限，可操作key的前缀，可操作bucket和令牌超时时间点
"""


class UpdateUFileTokenRequestSchema(schema.RequestSchema):
    """UpdateUFileToken - 更新令牌的操作权限，可操作key的前缀，可操作bucket和令牌超时时间点"""

    fields = {
        "AllowedBuckets": fields.List(fields.Str()),
        "AllowedOps": fields.List(fields.Str()),
        "AllowedPrefixes": fields.List(fields.Str()),
        "ExpireTime": fields.Int(required=False, dump_to="ExpireTime"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "TokenId": fields.Str(required=True, dump_to="TokenId"),
        "TokenName": fields.Str(required=False, dump_to="TokenName"),
    }


class UpdateUFileTokenResponseSchema(schema.ResponseSchema):
    """UpdateUFileToken - 更新令牌的操作权限，可操作key的前缀，可操作bucket和令牌超时时间点"""

    fields = {}
