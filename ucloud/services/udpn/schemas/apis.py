from ucloud.core.typesystem import schema, fields
from ucloud.services.udpn.schemas import models


""" UDPN API Schema
"""


"""
API: AllocateUDPN

分配一条 UDPN 专线
"""


class AllocateUDPNRequestSchema(schema.RequestSchema):
    """ AllocateUDPN - 分配一条 UDPN 专线
    """

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Peer1": fields.Str(required=True, dump_to="Peer1"),
        "Peer2": fields.Str(required=True, dump_to="Peer2"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
    }


class AllocateUDPNResponseSchema(schema.ResponseSchema):
    """ AllocateUDPN - 分配一条 UDPN 专线
    """

    fields = {"UDPNId": fields.Str(required=True, load_from="UDPNId")}


"""
API: DescribeUDPN

描述 UDPN
"""


class DescribeUDPNRequestSchema(schema.RequestSchema):
    """ DescribeUDPN - 描述 UDPN
    """

    fields = {
        "UDPNId": fields.Str(required=False, dump_to="UDPNId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUDPNResponseSchema(schema.ResponseSchema):
    """ DescribeUDPN - 描述 UDPN
    """

    fields = {
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
        "DataSet": fields.List(
            models.UDPNDataSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: GetUDPNLineList

获取当前支持的专线线路列表
"""


class GetUDPNLineListRequestSchema(schema.RequestSchema):
    """ GetUDPNLineList - 获取当前支持的专线线路列表
    """

    fields = {
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUDPNLineListResponseSchema(schema.ResponseSchema):
    """ GetUDPNLineList - 获取当前支持的专线线路列表
    """

    fields = {
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
        "DataSet": fields.List(
            models.UDPNLineSetSchema(), required=True, load_from="DataSet"
        ),
    }


"""
API: GetUDPNPrice

获取 UDPN 价格
"""


class GetUDPNPriceRequestSchema(schema.RequestSchema):
    """ GetUDPNPrice - 获取 UDPN 价格
    """

    fields = {
        "Peer1": fields.Str(required=True, dump_to="Peer1"),
        "Peer2": fields.Str(required=True, dump_to="Peer2"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=False, dump_to="Region"),
    }


class GetUDPNPriceResponseSchema(schema.ResponseSchema):
    """ GetUDPNPrice - 获取 UDPN 价格
    """

    fields = {
        "PurchaseValue": fields.Int(required=True, load_from="PurchaseValue"),
        "Price": fields.Float(required=True, load_from="Price"),
    }


"""
API: GetUDPNUpgradePrice

获取专线升级价格
"""


class GetUDPNUpgradePriceRequestSchema(schema.RequestSchema):
    """ GetUDPNUpgradePrice - 获取专线升级价格
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDPNId": fields.Str(required=True, dump_to="UDPNId"),
    }


class GetUDPNUpgradePriceResponseSchema(schema.ResponseSchema):
    """ GetUDPNUpgradePrice - 获取专线升级价格
    """

    fields = {"Price": fields.Float(required=True, load_from="Price")}


"""
API: ModifyUDPNBandwidth

修改带宽值
"""


class ModifyUDPNBandwidthRequestSchema(schema.RequestSchema):
    """ ModifyUDPNBandwidth - 修改带宽值
    """

    fields = {
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDPNId": fields.Str(required=True, dump_to="UDPNId"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
    }


class ModifyUDPNBandwidthResponseSchema(schema.ResponseSchema):
    """ ModifyUDPNBandwidth - 修改带宽值
    """

    fields = {}


"""
API: ReleaseUDPN

释放 UDPN
"""


class ReleaseUDPNRequestSchema(schema.RequestSchema):
    """ ReleaseUDPN - 释放 UDPN
    """

    fields = {
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UDPNId": fields.Str(required=True, dump_to="UDPNId"),
    }


class ReleaseUDPNResponseSchema(schema.ResponseSchema):
    """ ReleaseUDPN - 释放 UDPN
    """

    fields = {}
