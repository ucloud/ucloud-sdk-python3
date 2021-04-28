""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class ReceiptPerPhoneSchema(schema.ResponseSchema):
    """ReceiptPerPhone - 每个目的手机号的发送回执信息"""

    fields = {
        "Phone": fields.Str(required=True, load_from="Phone"),
        "ReceiptCode": fields.Str(required=True, load_from="ReceiptCode"),
        "ReceiptDesc": fields.Str(required=True, load_from="ReceiptDesc"),
        "ReceiptResult": fields.Str(required=True, load_from="ReceiptResult"),
        "ReceiptTime": fields.Int(required=True, load_from="ReceiptTime"),
        "SessionId": fields.Str(required=True, load_from="SessionId"),
    }


class ReceiptPerTaskSchema(schema.ResponseSchema):
    """ReceiptPerTask - 每个提交任务的视频短信的回执结果集合"""

    fields = {
        "ReceiptSet": fields.List(ReceiptPerPhoneSchema()),
        "TaskId": fields.Str(required=True, load_from="TaskId"),
    }