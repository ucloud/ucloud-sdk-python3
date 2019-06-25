from ucloud.core.typesystem import schema, fields


class RouteRuleInfoSchema(schema.ResponseSchema):
    """ RouteRuleInfo - 路由规则信息
    """

    fields = {
        "DstAddr": fields.Str(required=False, load_from="DstAddr"),
        "NexthopId": fields.Str(required=False, load_from="NexthopId"),
        "NexthopType": fields.Str(required=False, load_from="NexthopType"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteRuleId": fields.Str(required=False, load_from="RouteRuleId"),
        "RuleType": fields.Int(required=False, load_from="RuleType"),
    }


class RouteTableInfoSchema(schema.ResponseSchema):
    """ RouteTableInfo - 路由表信息
    """

    fields = {
        "SubnetCount": fields.Str(required=False, load_from="SubnetCount"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "RouteRules": fields.List(RouteRuleInfoSchema()),
        "RouteTableType": fields.Int(required=False, load_from="RouteTableType"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
    }


class SubnetInfoSchema(schema.ResponseSchema):
    """ SubnetInfo - 子网信息
    """

    fields = {
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "SubnetType": fields.Int(required=False, load_from="SubnetType"),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "HasNATGW": fields.Bool(required=False, load_from="HasNATGW"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Subnet": fields.Str(required=False, load_from="Subnet"),
        "Netmask": fields.Int(required=False, load_from="Netmask"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
    }


class SubnetResourceSchema(schema.ResponseSchema):
    """ SubnetResource - 子网下资源
    """

    fields = {
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "IP": fields.Str(required=False, load_from="IP"),
        "IPv6Address": fields.Str(required=False, load_from="IPv6Address"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
    }


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
        "Network": fields.List(fields.Str()),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "SubnetCount": fields.Int(required=True, load_from="SubnetCount"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "NetworkInfo": fields.List(VPCNetworkInfoSchema()),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "Name": fields.Str(required=True, load_from="Name"),
    }


class VPCIntercomInfoSchema(schema.ResponseSchema):
    """ VPCIntercomInfo - 
    """

    fields = {
        "Name": fields.Str(required=False, load_from="Name"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
        "Network": fields.List(fields.Str()),
        "DstRegion": fields.Str(required=False, load_from="DstRegion"),
    }
