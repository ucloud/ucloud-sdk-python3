""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class AccountInfoSchema(schema.ResponseSchema):
    """AccountInfo - 账户信息"""

    fields = {
        "Amount": fields.Str(required=False, load_from="Amount"),
        "AmountAvailable": fields.Str(
            required=False, load_from="AmountAvailable"
        ),
        "AmountCredit": fields.Str(required=False, load_from="AmountCredit"),
        "AmountFree": fields.Str(required=False, load_from="AmountFree"),
        "AmountFreeze": fields.Str(required=False, load_from="AmountFreeze"),
    }


class ItemDetailSchema(schema.ResponseSchema):
    """ItemDetail - 产品配置"""

    fields = {
        "ProductName": fields.Str(required=True, load_from="ProductName"),
        "Value": fields.Str(required=True, load_from="Value"),
    }


class ResourceExtendInfoSchema(schema.ResponseSchema):
    """ResourceExtendInfo - 资源标识"""

    fields = {
        "KeyId": fields.Str(required=True, load_from="KeyId"),
        "Value": fields.Str(required=True, load_from="Value"),
    }


class BillDetailItemSchema(schema.ResponseSchema):
    """BillDetailItem - 账单详情数据"""

    fields = {
        "Admin": fields.Int(required=True, load_from="Admin"),
        "Amount": fields.Str(required=True, load_from="Amount"),
        "AmountCoupon": fields.Str(required=True, load_from="AmountCoupon"),
        "AmountFree": fields.Str(required=True, load_from="AmountFree"),
        "AmountReal": fields.Str(required=True, load_from="AmountReal"),
        "AzGroupCName": fields.Str(required=True, load_from="AzGroupCName"),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "EndTime": fields.Int(required=True, load_from="EndTime"),
        "ItemDetails": fields.List(ItemDetailSchema()),
        "OrderNo": fields.Str(required=True, load_from="OrderNo"),
        "OrderType": fields.Str(required=True, load_from="OrderType"),
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
        "ResourceExtendInfo": fields.List(ResourceExtendInfoSchema()),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "ResourceType": fields.Str(required=True, load_from="ResourceType"),
        "ResourceTypeCode": fields.Int(
            required=True, load_from="ResourceTypeCode"
        ),
        "ShowHover": fields.Int(required=True, load_from="ShowHover"),
        "StartTime": fields.Int(required=True, load_from="StartTime"),
        "UserDisplayName": fields.Str(
            required=True, load_from="UserDisplayName"
        ),
        "UserEmail": fields.Str(required=True, load_from="UserEmail"),
        "UserName": fields.Str(required=True, load_from="UserName"),
    }


class BillOverviewItemSchema(schema.ResponseSchema):
    """BillOverviewItem - 账单总览数组内单个结构体数据"""

    fields = {
        "Admin": fields.Int(required=False, load_from="Admin"),
        "Amount": fields.Str(required=True, load_from="Amount"),
        "AmountCoupon": fields.Str(required=False, load_from="AmountCoupon"),
        "AmountFree": fields.Str(required=False, load_from="AmountFree"),
        "AmountReal": fields.Str(required=False, load_from="AmountReal"),
        "Dimension": fields.Str(required=True, load_from="Dimension"),
        "ProductCategory": fields.Str(
            required=False, load_from="ProductCategory"
        ),
        "ProjectName": fields.Str(required=False, load_from="ProjectName"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "ResourceTypeCode": fields.Int(
            required=False, load_from="ResourceTypeCode"
        ),
        "UserDisplayName": fields.Str(
            required=False, load_from="UserDisplayName"
        ),
        "UserEmail": fields.Str(required=False, load_from="UserEmail"),
        "UserName": fields.Str(required=False, load_from="UserName"),
    }


class ResultSetSchema(schema.ResponseSchema):
    """ResultSet - 结果集"""

    fields = {
        "Message": fields.Str(required=False, load_from="Message"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "RetCode": fields.Int(required=False, load_from="RetCode"),
    }
