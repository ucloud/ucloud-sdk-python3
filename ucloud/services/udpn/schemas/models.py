from ucloud.core.typesystem import schema, fields


class UDPNDataSchema(schema.ResponseSchema):
    """ UDPNData - UDPN 详细信息
    """

    fields = {
        "UDPNId": fields.Str(required=True, load_from="UDPNId"),
        "Peer1": fields.Str(required=True, load_from="Peer1"),
        "Peer2": fields.Str(required=True, load_from="Peer2"),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "Bandwidth": fields.Int(required=True, load_from="Bandwidth"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
    }


class UDPNLineSetSchema(schema.ResponseSchema):
    """ UDPNLineSet - GetUDPNLineList
    """

    fields = {
        "BandwidthUpperLimit": fields.Int(
            required=True, load_from="BandwidthUpperLimit"
        ),
        "LocalRegion": fields.Str(required=True, load_from="LocalRegion"),
        "RemoteRegion": fields.Str(required=True, load_from="RemoteRegion"),
    }
