""" Code is generated by ucloud-model, DO NOT EDIT IT. """




from ucloud.core.typesystem import schema, fields
from ucloud.services.ipsecvpn.schemas import models

""" IPSecVPN API Schema
"""















"""
API: CreateRemoteVPNGateway

创建客户VPN网关
"""





class CreateRemoteVPNGatewayRequestSchema(schema.RequestSchema):
    """ CreateRemoteVPNGateway - 创建客户VPN网关
    """
    fields = {
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'Remark': fields.Str(required=False, dump_to='Remark'), 
    
        'RemoteVPNGatewayAddr': fields.Str(required=True, dump_to='RemoteVPNGatewayAddr'), 
    
        'RemoteVPNGatewayName': fields.Str(required=True, dump_to='RemoteVPNGatewayName'), 
    
        'Tag': fields.Str(required=False, dump_to='Tag'), 
    
    }


class CreateRemoteVPNGatewayResponseSchema(schema.ResponseSchema):
    """ CreateRemoteVPNGateway - 创建客户VPN网关
    """
    fields = {
    
        'RemoteVPNGatewayId': fields.Str(required=False, load_from='RemoteVPNGatewayId'), 
    
    }


"""
API: CreateVPNGateway

创建VPN网关
"""





class CreateVPNGatewayRequestSchema(schema.RequestSchema):
    """ CreateVPNGateway - 创建VPN网关
    """
    fields = {
    
        'BusinessId': fields.Str(required=False, dump_to='BusinessId'), 
    
        'ChargeType': fields.Str(required=False, dump_to='ChargeType'), 
    
        'CouponId': fields.Str(required=False, dump_to='CouponId'), 
    
        'EIPId': fields.Str(required=False, dump_to='EIPId'), 
    
        'Grade': fields.Str(required=True, dump_to='Grade'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Quantity': fields.Int(required=False, dump_to='Quantity'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'Remark': fields.Str(required=False, dump_to='Remark'), 
    
        'Tag': fields.Str(required=False, dump_to='Tag'), 
    
        'VPCId': fields.Str(required=True, dump_to='VPCId'), 
    
        'VPNGatewayName': fields.Str(required=True, dump_to='VPNGatewayName'), 
    
    }


class CreateVPNGatewayResponseSchema(schema.ResponseSchema):
    """ CreateVPNGateway - 创建VPN网关
    """
    fields = {
    
        'VPNGatewayId': fields.Str(required=False, load_from='VPNGatewayId'), 
    
    }


"""
API: CreateVPNTunnel

创建VPN隧道
"""





class CreateVPNTunnelRequestSchema(schema.RequestSchema):
    """ CreateVPNTunnel - 创建VPN隧道
    """
    fields = {
    
        'IKEAuthenticationAlgorithm': fields.Str(required=False, dump_to='IKEAuthenticationAlgorithm'), 
    
        'IKEDhGroup': fields.Str(required=False, dump_to='IKEDhGroup'), 
    
        'IKEEncryptionAlgorithm': fields.Str(required=False, dump_to='IKEEncryptionAlgorithm'), 
    
        'IKEExchangeMode': fields.Str(required=False, dump_to='IKEExchangeMode'), 
    
        'IKELocalId': fields.Str(required=False, dump_to='IKELocalId'), 
    
        'IKEPreSharedKey': fields.Str(required=True, dump_to='IKEPreSharedKey'), 
    
        'IKERemoteId': fields.Str(required=False, dump_to='IKERemoteId'), 
    
        'IKESALifetime': fields.Str(required=False, dump_to='IKESALifetime'), 
    
        'IKEVersion': fields.Str(required=True, dump_to='IKEVersion'), 
    
        'IPSecAuthenticationAlgorithm': fields.Str(required=False, dump_to='IPSecAuthenticationAlgorithm'), 
    
        'IPSecCloseAction': fields.Str(required=False, dump_to='IPSecCloseAction'), 
    
        'IPSecEncryptionAlgorithm': fields.Str(required=False, dump_to='IPSecEncryptionAlgorithm'), 
    
        'IPSecLocalSubnetIds': fields.List(fields.Str()), 
    
        'IPSecPFSDhGroup': fields.Str(required=False, dump_to='IPSecPFSDhGroup'), 
    
        'IPSecProtocol': fields.Str(required=False, dump_to='IPSecProtocol'), 
    
        'IPSecRemoteSubnets': fields.List(fields.Str()), 
    
        'IPSecSALifetime': fields.Str(required=False, dump_to='IPSecSALifetime'), 
    
        'IPSecSALifetimeBytes': fields.Str(required=False, dump_to='IPSecSALifetimeBytes'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'Remark': fields.Str(required=False, dump_to='Remark'), 
    
        'RemoteVPNGatewayId': fields.Str(required=True, dump_to='RemoteVPNGatewayId'), 
    
        'Tag': fields.Str(required=False, dump_to='Tag'), 
    
        'VPCId': fields.Str(required=True, dump_to='VPCId'), 
    
        'VPNGatewayId': fields.Str(required=True, dump_to='VPNGatewayId'), 
    
        'VPNTunnelName': fields.Str(required=True, dump_to='VPNTunnelName'), 
    
    }


class CreateVPNTunnelResponseSchema(schema.ResponseSchema):
    """ CreateVPNTunnel - 创建VPN隧道
    """
    fields = {
    
        'VPNTunnelId': fields.Str(required=False, load_from='VPNTunnelId'), 
    
    }


"""
API: DeleteRemoteVPNGateway

删除客户VPN网关
"""





class DeleteRemoteVPNGatewayRequestSchema(schema.RequestSchema):
    """ DeleteRemoteVPNGateway - 删除客户VPN网关
    """
    fields = {
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'RemoteVPNGatewayId': fields.Str(required=True, dump_to='RemoteVPNGatewayId'), 
    
    }


class DeleteRemoteVPNGatewayResponseSchema(schema.ResponseSchema):
    """ DeleteRemoteVPNGateway - 删除客户VPN网关
    """
    fields = {
    
    }


"""
API: DeleteVPNGateway

删除VPN网关
"""





class DeleteVPNGatewayRequestSchema(schema.RequestSchema):
    """ DeleteVPNGateway - 删除VPN网关
    """
    fields = {
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'ReleaseEip': fields.Bool(required=False, dump_to='ReleaseEip'), 
    
        'VPNGatewayId': fields.Str(required=True, dump_to='VPNGatewayId'), 
    
    }


class DeleteVPNGatewayResponseSchema(schema.ResponseSchema):
    """ DeleteVPNGateway - 删除VPN网关
    """
    fields = {
    
    }


"""
API: DeleteVPNTunnel

删除VPN隧道
"""





class DeleteVPNTunnelRequestSchema(schema.RequestSchema):
    """ DeleteVPNTunnel - 删除VPN隧道
    """
    fields = {
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'VPNTunnelId': fields.Str(required=True, dump_to='VPNTunnelId'), 
    
    }


class DeleteVPNTunnelResponseSchema(schema.ResponseSchema):
    """ DeleteVPNTunnel - 删除VPN隧道
    """
    fields = {
    
    }


"""
API: DescribeRemoteVPNGateway

获取客户VPN网关信息
"""





class DescribeRemoteVPNGatewayRequestSchema(schema.RequestSchema):
    """ DescribeRemoteVPNGateway - 获取客户VPN网关信息
    """
    fields = {
    
        'Limit': fields.Int(required=False, dump_to='Limit'), 
    
        'Offset': fields.Int(required=False, dump_to='Offset'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'RemoteVPNGatewayIds': fields.List(fields.Str()), 
    
        'Tag': fields.Str(required=False, dump_to='Tag'), 
    
    }


class DescribeRemoteVPNGatewayResponseSchema(schema.ResponseSchema):
    """ DescribeRemoteVPNGateway - 获取客户VPN网关信息
    """
    fields = {
    
        'DataSet': fields.List(models.RemoteVPNGatewayDataSetSchema(), required=False, load_from='DataSet'), 
    
        'TotalCount': fields.Int(required=False, load_from='TotalCount'), 
    
    }


"""
API: DescribeVPNGateway

获取VPN网关信息
"""





class DescribeVPNGatewayRequestSchema(schema.RequestSchema):
    """ DescribeVPNGateway - 获取VPN网关信息
    """
    fields = {
    
        'Limit': fields.Int(required=False, dump_to='Limit'), 
    
        'Offset': fields.Int(required=False, dump_to='Offset'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'Tag': fields.Str(required=False, dump_to='Tag'), 
    
        'VPCId': fields.Str(required=False, dump_to='VPCId'), 
    
        'VPNGatewayIds': fields.List(fields.Str()), 
    
    }


class DescribeVPNGatewayResponseSchema(schema.ResponseSchema):
    """ DescribeVPNGateway - 获取VPN网关信息
    """
    fields = {
    
        'DataSet': fields.List(models.VPNGatewayDataSetSchema(), required=False, load_from='DataSet'), 
    
        'TotalCount': fields.Int(required=False, load_from='TotalCount'), 
    
    }


"""
API: DescribeVPNTunnel

获取VPN隧道信息
"""





class DescribeVPNTunnelRequestSchema(schema.RequestSchema):
    """ DescribeVPNTunnel - 获取VPN隧道信息
    """
    fields = {
    
        'Limit': fields.Int(required=False, dump_to='Limit'), 
    
        'Offset': fields.Int(required=False, dump_to='Offset'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'Tag': fields.Str(required=False, dump_to='Tag'), 
    
        'VPNTunnelIds': fields.List(fields.Str()), 
    
    }


class DescribeVPNTunnelResponseSchema(schema.ResponseSchema):
    """ DescribeVPNTunnel - 获取VPN隧道信息
    """
    fields = {
    
        'DataSet': fields.List(models.VPNTunnelDataSetSchema(), required=False, load_from='DataSet'), 
    
        'TotalCount': fields.Int(required=False, load_from='TotalCount'), 
    
    }


"""
API: GetVPNGatewayPrice

获取VPN价格
"""





class GetVPNGatewayPriceRequestSchema(schema.RequestSchema):
    """ GetVPNGatewayPrice - 获取VPN价格
    """
    fields = {
    
        'ChargeType': fields.Str(required=False, dump_to='ChargeType'), 
    
        'Grade': fields.Str(required=True, dump_to='Grade'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Quantity': fields.Int(required=False, dump_to='Quantity'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
    }


class GetVPNGatewayPriceResponseSchema(schema.ResponseSchema):
    """ GetVPNGatewayPrice - 获取VPN价格
    """
    fields = {
    
        'PriceSet': fields.List(models.VPNGatewayPriceSetSchema(), required=False, load_from='PriceSet'), 
    
    }


"""
API: GetVPNGatewayUpgradePrice

获取VPN网关规格改动价格
"""





class GetVPNGatewayUpgradePriceRequestSchema(schema.RequestSchema):
    """ GetVPNGatewayUpgradePrice - 获取VPN网关规格改动价格
    """
    fields = {
    
        'Grade': fields.Str(required=True, dump_to='Grade'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'VPNGatewayId': fields.Str(required=True, dump_to='VPNGatewayId'), 
    
    }


class GetVPNGatewayUpgradePriceResponseSchema(schema.ResponseSchema):
    """ GetVPNGatewayUpgradePrice - 获取VPN网关规格改动价格
    """
    fields = {
    
        'Price': fields.Float(required=False, load_from='Price'), 
    
    }


"""
API: UpdateVPNGateway

更改VPN网关规格
"""





class UpdateVPNGatewayRequestSchema(schema.RequestSchema):
    """ UpdateVPNGateway - 更改VPN网关规格
    """
    fields = {
    
        'Grade': fields.Str(required=True, dump_to='Grade'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'VPNGatewayId': fields.Str(required=True, dump_to='VPNGatewayId'), 
    
    }


class UpdateVPNGatewayResponseSchema(schema.ResponseSchema):
    """ UpdateVPNGateway - 更改VPN网关规格
    """
    fields = {
    
    }


"""
API: UpdateVPNTunnelAttribute

更新VPN隧道属性
"""





class UpdateVPNTunnelAttributeRequestSchema(schema.RequestSchema):
    """ UpdateVPNTunnelAttribute - 更新VPN隧道属性
    """
    fields = {
    
        'IKEAuthenticationAlgorithm': fields.Str(required=False, dump_to='IKEAuthenticationAlgorithm'), 
    
        'IKEDhGroup': fields.Str(required=False, dump_to='IKEDhGroup'), 
    
        'IKEEncryptionAlgorithm': fields.Str(required=False, dump_to='IKEEncryptionAlgorithm'), 
    
        'IKEExchangeMode': fields.Str(required=False, dump_to='IKEExchangeMode'), 
    
        'IKELocalId': fields.Str(required=False, dump_to='IKELocalId'), 
    
        'IKEPreSharedKey': fields.Str(required=False, dump_to='IKEPreSharedKey'), 
    
        'IKERemoteId': fields.Str(required=False, dump_to='IKERemoteId'), 
    
        'IKESALifetime': fields.Str(required=False, dump_to='IKESALifetime'), 
    
        'IKEVersion': fields.Str(required=False, dump_to='IKEVersion'), 
    
        'IPSecAuthenticationAlgorithm': fields.Str(required=False, dump_to='IPSecAuthenticationAlgorithm'), 
    
        'IPSecCloseAction': fields.Str(required=False, dump_to='IPSecCloseAction'), 
    
        'IPSecEncryptionAlgorithm': fields.Str(required=False, dump_to='IPSecEncryptionAlgorithm'), 
    
        'IPSecLocalSubnetIds': fields.List(fields.Str()), 
    
        'IPSecPFSDhGroup': fields.Str(required=False, dump_to='IPSecPFSDhGroup'), 
    
        'IPSecProtocol': fields.Str(required=False, dump_to='IPSecProtocol'), 
    
        'IPSecRemoteSubnets': fields.List(fields.Str()), 
    
        'IPSecSALifetime': fields.Str(required=False, dump_to='IPSecSALifetime'), 
    
        'IPSecSALifetimeBytes': fields.Str(required=False, dump_to='IPSecSALifetimeBytes'), 
    
        'ProjectId': fields.Str(required=True, dump_to='ProjectId'), 
    
        'Region': fields.Str(required=True, dump_to='Region'), 
    
        'VPNTunnelId': fields.Str(required=True, dump_to='VPNTunnelId'), 
    
    }


class UpdateVPNTunnelAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateVPNTunnelAttribute - 更新VPN隧道属性
    """
    fields = {
    
    }

