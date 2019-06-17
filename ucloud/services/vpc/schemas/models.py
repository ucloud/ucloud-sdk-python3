from ucloud.core.typesystem import schema, fields


class VPCNetworkInfoSchema(schema.ResponseSchema):
    """ VPCNetworkInfo - vpc地址空间信息
    """

    fields = {
        "Network": fields.Str(required=False, load_from="Network"),
        "SubnetCount": fields.Int(required=False, load_from="SubnetCount"),
    }


class VPCInfoSchema(schema.ResponseSchema):
    """ VPCInfo - VPC信息
    """

    fields = {
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Network": fields.List(fields.Str()),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "NetworkInfo": fields.List(VPCNetworkInfoSchema()),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "SubnetCount": fields.Int(required=True, load_from="SubnetCount"),
        "Tag": fields.Str(required=True, load_from="Tag"),
    }


class SubnetInfoSchema(schema.ResponseSchema):
    """ SubnetInfo - 子网信息
    """

    fields = {
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Subnet": fields.Str(required=False, load_from="Subnet"),
        "HasNATGW": fields.Bool(required=False, load_from="HasNATGW"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "SubnetType": fields.Int(required=False, load_from="SubnetType"),
        "Netmask": fields.Int(required=False, load_from="Netmask"),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
    }


class RouteRuleInfoSchema(schema.ResponseSchema):
    """ RouteRuleInfo - 路由规则信息
    """

    fields = {
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteRuleId": fields.Str(required=False, load_from="RouteRuleId"),
        "RuleType": fields.Int(required=False, load_from="RuleType"),
        "DstAddr": fields.Str(required=False, load_from="DstAddr"),
        "NexthopId": fields.Str(required=False, load_from="NexthopId"),
        "NexthopType": fields.Str(required=False, load_from="NexthopType"),
    }


class RouteTableInfoSchema(schema.ResponseSchema):
    """ RouteTableInfo - 路由表信息
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "RouteRules": fields.List(RouteRuleInfoSchema()),
        "RouteTableType": fields.Int(required=False, load_from="RouteTableType"),
        "SubnetCount": fields.Str(required=False, load_from="SubnetCount"),
    }


class SubnetResourceSchema(schema.ResponseSchema):
    """ SubnetResource - 子网下资源
    """

    fields = {
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "IP": fields.Str(required=False, load_from="IP"),
        "IPv6Address": fields.Str(required=False, load_from="IPv6Address"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
    }


class VPCIntercomInfoSchema(schema.ResponseSchema):
    """ VPCIntercomInfo - 
    """

    fields = {
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
        "Network": fields.List(fields.Str()),
        "DstRegion": fields.Str(required=False, load_from="DstRegion"),
        "Name": fields.Str(required=False, load_from="Name"),
    }
