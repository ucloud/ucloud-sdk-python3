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
        "RouteTableType": fields.Int(required=False, load_from="RouteTableType"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "RouteRules": fields.List(RouteRuleInfoSchema()),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "SubnetCount": fields.Str(required=False, load_from="SubnetCount"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Tag": fields.Str(required=False, load_from="Tag"),
    }


class SubnetInfoSchema(schema.ResponseSchema):
    """ SubnetInfo - 子网信息
    """

    fields = {
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Subnet": fields.Str(required=False, load_from="Subnet"),
        "HasNATGW": fields.Bool(required=False, load_from="HasNATGW"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SubnetType": fields.Int(required=False, load_from="SubnetType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Netmask": fields.Int(required=False, load_from="Netmask"),
    }


class SubnetResourceSchema(schema.ResponseSchema):
    """ SubnetResource - 子网下资源
    """

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "IPv6Address": fields.Str(required=False, load_from="IPv6Address"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubResourceName": fields.Str(required=False, load_from="SubResourceName"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceType": fields.Str(required=False, load_from="SubResourceType"),
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
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "Name": fields.Str(required=True, load_from="Name"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "NetworkInfo": fields.List(VPCNetworkInfoSchema()),
        "SubnetCount": fields.Int(required=True, load_from="SubnetCount"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
    }


class VPCIntercomInfoSchema(schema.ResponseSchema):
    """ VPCIntercomInfo - 
    """

    fields = {
        "Network": fields.List(fields.Str()),
        "DstRegion": fields.Str(required=False, load_from="DstRegion"),
        "Name": fields.Str(required=False, load_from="Name"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
    }
