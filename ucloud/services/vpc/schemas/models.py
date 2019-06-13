from ucloud.core.typesystem import schema, fields


class SubnetInfoSchema(schema.ResponseSchema):
    """ SubnetInfo - 子网信息
    """

    fields = {
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Subnet": fields.Str(required=False, load_from="Subnet"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "HasNATGW": fields.Bool(required=False, load_from="HasNATGW"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "SubnetType": fields.Int(required=False, load_from="SubnetType"),
        "Netmask": fields.Int(required=False, load_from="Netmask"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
    }


class VPCIntercomInfoSchema(schema.ResponseSchema):
    """ VPCIntercomInfo - 
    """

    fields = {
        "DstRegion": fields.Str(required=False, load_from="DstRegion"),
        "Name": fields.Str(required=False, load_from="Name"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
        "Network": fields.List(fields.Str()),
    }


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
        "Remark": fields.Str(required=False, load_from="Remark"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "RouteRules": fields.List(RouteRuleInfoSchema()),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "RouteTableType": fields.Int(required=False, load_from="RouteTableType"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Tag": fields.Str(required=False, load_from="Tag"),
    }


class SubnetResourceSchema(schema.ResponseSchema):
    """ SubnetResource - 子网下资源
    """

    fields = {
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
        "IP": fields.Str(required=False, load_from="IP"),
        "IPv6Address": fields.Str(required=False, load_from="IPv6Address"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
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
        "NetworkInfo": fields.List(VPCNetworkInfoSchema()),
        "SubnetCount": fields.Int(required=True, load_from="SubnetCount"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "Name": fields.Str(required=True, load_from="Name"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Network": fields.List(fields.Str()),
    }
