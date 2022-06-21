""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class StatusInfoSchema(schema.ResponseSchema):
    """StatusInfo -"""

    fields = {
        "Message": fields.Str(required=False, load_from="Message"),
        "StatusCode": fields.Str(required=False, load_from="StatusCode"),
    }


class IpsInfoSchema(schema.ResponseSchema):
    """IpsInfo -"""

    fields = {
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "Ip": fields.Str(required=False, load_from="Ip"),
        "Mac": fields.Str(required=False, load_from="Mac"),
        "Mask": fields.Str(required=False, load_from="Mask"),
        "Status": StatusInfoSchema(),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class IpInfoSchema(schema.ResponseSchema):
    """IpInfo -"""

    fields = {
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "Ip": fields.Str(required=False, load_from="Ip"),
        "Mac": fields.Str(required=False, load_from="Mac"),
        "Mask": fields.Str(required=False, load_from="Mask"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class VIPSetSchema(schema.ResponseSchema):
    """VIPSet - VIPSet"""

    fields = {
        "VIP": fields.Str(required=False, load_from="VIP"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class AssociationInfoSchema(schema.ResponseSchema):
    """AssociationInfo - 绑定信息"""

    fields = {
        "AclId": fields.Str(required=True, load_from="AclId"),
        "AssociationId": fields.Str(required=True, load_from="AssociationId"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "SubnetworkId": fields.Str(required=True, load_from="SubnetworkId"),
    }


class NetworkInterfaceInfoSchema(schema.ResponseSchema):
    """NetworkInterfaceInfo - 虚拟网卡信息"""

    fields = {
        "AttachInstanceId": fields.Str(
            required=False, load_from="AttachInstanceId"
        ),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Default": fields.Bool(required=False, load_from="Default"),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "InterfaceId": fields.Str(required=True, load_from="InterfaceId"),
        "MacAddress": fields.Str(required=True, load_from="MacAddress"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Netmask": fields.Str(required=False, load_from="Netmask"),
        "PrivateIpSet": fields.List(fields.Str()),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Status": fields.Int(required=True, load_from="Status"),
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
    }


class InstanceNetworkInterfaceSchema(schema.ResponseSchema):
    """InstanceNetworkInterface - 实例绑定的虚拟网卡信息"""

    fields = {
        "AttachInstanceId": fields.Str(
            required=False, load_from="AttachInstanceId"
        ),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Default": fields.Bool(required=False, load_from="Default"),
        "EIPIdSet": fields.List(fields.Str()),
        "FirewallIdSet": fields.List(fields.Str()),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "InterfaceId": fields.Str(required=True, load_from="InterfaceId"),
        "MacAddress": fields.Str(required=True, load_from="MacAddress"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Netmask": fields.Str(required=False, load_from="Netmask"),
        "PrivateIpSet": fields.List(fields.Str()),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Status": fields.Int(required=True, load_from="Status"),
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
    }


class NatGWIPResInfoSchema(schema.ResponseSchema):
    """NatGWIPResInfo - IP信息"""

    fields = {
        "EIP": fields.Str(required=True, load_from="EIP"),
        "OperatorName": fields.Str(required=True, load_from="OperatorName"),
    }


class NatGatewayIPSetSchema(schema.ResponseSchema):
    """NatGatewayIPSet - IPSet信息"""

    fields = {
        "Bandwidth": fields.Int(required=True, load_from="Bandwidth"),
        "BandwidthType": fields.Str(required=True, load_from="BandwidthType"),
        "EIPId": fields.Str(required=True, load_from="EIPId"),
        "IPResInfo": fields.List(NatGWIPResInfoSchema()),
        "Weight": fields.Int(required=True, load_from="Weight"),
    }


class NatGatewaySubnetSetSchema(schema.ResponseSchema):
    """NatGatewaySubnetSet - natgw里面的子网信息"""

    fields = {
        "Subnet": fields.Str(required=True, load_from="Subnet"),
        "SubnetName": fields.Str(required=True, load_from="SubnetName"),
        "SubnetworkId": fields.Str(required=True, load_from="SubnetworkId"),
    }


class NatGatewayDataSetSchema(schema.ResponseSchema):
    """NatGatewayDataSet - natgw的信息"""

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "FirewallId": fields.Str(required=True, load_from="FirewallId"),
        "IPSet": fields.List(NatGatewayIPSetSchema()),
        "IsSnatpoolEnabled": fields.Str(
            required=True, load_from="IsSnatpoolEnabled"
        ),
        "NATGWId": fields.Str(required=True, load_from="NATGWId"),
        "NATGWName": fields.Str(required=True, load_from="NATGWName"),
        "PolicyId": fields.List(fields.Str()),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "SubnetSet": fields.List(NatGatewaySubnetSetSchema()),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
        "VPCName": fields.Str(required=True, load_from="VPCName"),
    }


class NATGWPolicyDataSetSchema(schema.ResponseSchema):
    """NATGWPolicyDataSet - DescribeNATGWPolicy"""

    fields = {
        "DstIP": fields.Str(required=True, load_from="DstIP"),
        "DstPort": fields.Str(required=True, load_from="DstPort"),
        "NATGWId": fields.Str(required=True, load_from="NATGWId"),
        "PolicyId": fields.Str(required=True, load_from="PolicyId"),
        "PolicyName": fields.Str(required=False, load_from="PolicyName"),
        "Protocol": fields.Str(required=True, load_from="Protocol"),
        "SrcEIP": fields.Str(required=True, load_from="SrcEIP"),
        "SrcEIPId": fields.Str(required=True, load_from="SrcEIPId"),
        "SrcPort": fields.Str(required=True, load_from="SrcPort"),
    }


class TargetResourceInfoSchema(schema.ResponseSchema):
    """TargetResourceInfo - ACL规则应用目标资源信息。"""

    fields = {
        "PrivateIp": fields.Str(required=True, load_from="PrivateIp"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "ResourceName": fields.Str(required=True, load_from="ResourceName"),
        "ResourceType": fields.Int(required=True, load_from="ResourceType"),
        "SubResourceId": fields.Str(required=True, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=True, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Int(
            required=True, load_from="SubResourceType"
        ),
        "SubnetworkId": fields.Str(required=True, load_from="SubnetworkId"),
    }


class AclEntryInfoSchema(schema.ResponseSchema):
    """AclEntryInfo - Entry的详细信息"""

    fields = {
        "CidrBlock": fields.Str(required=True, load_from="CidrBlock"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Direction": fields.Str(required=True, load_from="Direction"),
        "EntryAction": fields.Str(required=True, load_from="EntryAction"),
        "EntryId": fields.Str(required=True, load_from="EntryId"),
        "IpProtocol": fields.Str(required=True, load_from="IpProtocol"),
        "PortRange": fields.Str(required=True, load_from="PortRange"),
        "Priority": fields.Str(required=True, load_from="Priority"),
        "TargetResourceCount": fields.Int(
            required=False, load_from="TargetResourceCount"
        ),
        "TargetResourceList": fields.List(TargetResourceInfoSchema()),
        "TargetType": fields.Int(required=True, load_from="TargetType"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
    }


class AclInfoSchema(schema.ResponseSchema):
    """AclInfo - Acl的基础信息"""

    fields = {
        "AclId": fields.Str(required=True, load_from="AclId"),
        "AclName": fields.Str(required=True, load_from="AclName"),
        "Associations": fields.List(AssociationInfoSchema()),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Description": fields.Str(required=True, load_from="Description"),
        "Entries": fields.List(AclEntryInfoSchema()),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "VpcId": fields.Str(required=True, load_from="VpcId"),
    }


class UNIIpInfoSchema(schema.ResponseSchema):
    """UNIIpInfo - 虚拟网卡内网IP信息"""

    fields = {
        "IpAddr": fields.List(fields.Str()),
        "IpType": fields.Str(required=False, load_from="IpType"),
    }


class UNIQuotaInfoSchema(schema.ResponseSchema):
    """UNIQuotaInfo - 虚拟网卡内网IP配额使用情况"""

    fields = {
        "PrivateIpCount": fields.Int(
            required=False, load_from="PrivateIpCount"
        ),
        "PrivateIpQuota": fields.Int(
            required=False, load_from="PrivateIpQuota"
        ),
    }


class NetworkInterfaceSchema(schema.ResponseSchema):
    """NetworkInterface - 虚拟网卡信息"""

    fields = {
        "AttachInstanceId": fields.Str(
            required=False, load_from="AttachInstanceId"
        ),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Default": fields.Bool(required=False, load_from="Default"),
        "EIPIdSet": fields.List(fields.Str()),
        "FirewallIdSet": fields.List(fields.Str()),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "InterfaceId": fields.Str(required=True, load_from="InterfaceId"),
        "MacAddress": fields.Str(required=True, load_from="MacAddress"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Netmask": fields.Str(required=False, load_from="Netmask"),
        "PrivateIp": fields.List(UNIIpInfoSchema()),
        "PrivateIpLimit": UNIQuotaInfoSchema(),
        "PrivateIpSet": fields.List(fields.Str()),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Status": fields.Int(required=True, load_from="Status"),
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
    }


class RouteRuleInfoSchema(schema.ResponseSchema):
    """RouteRuleInfo - 路由规则信息"""

    fields = {
        "AccountId": fields.Int(required=False, load_from="AccountId"),
        "DstAddr": fields.Str(required=False, load_from="DstAddr"),
        "DstPort": fields.Int(required=False, load_from="DstPort"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "NexthopId": fields.Str(required=False, load_from="NexthopId"),
        "NexthopType": fields.Str(required=False, load_from="NexthopType"),
        "OriginAddr": fields.Str(required=False, load_from="OriginAddr"),
        "Priority": fields.Int(required=False, load_from="Priority"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteRuleId": fields.Str(required=False, load_from="RouteRuleId"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "RuleType": fields.Int(required=False, load_from="RuleType"),
        "SrcAddr": fields.Str(required=False, load_from="SrcAddr"),
        "SrcPort": fields.Int(required=False, load_from="SrcPort"),
        "VNetId": fields.Str(required=False, load_from="VNetId"),
    }


class RouteTableInfoSchema(schema.ResponseSchema):
    """RouteTableInfo - 路由表信息"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteRules": fields.List(RouteRuleInfoSchema()),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "RouteTableType": fields.Int(
            required=False, load_from="RouteTableType"
        ),
        "SubnetCount": fields.Int(required=False, load_from="SubnetCount"),
        "SubnetIds": fields.List(fields.Str()),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
    }


class SnatDnatRuleInfoSchema(schema.ResponseSchema):
    """SnatDnatRuleInfo -"""

    fields = {
        "EIP": fields.Str(required=False, load_from="EIP"),
        "NATGWId": fields.Str(required=False, load_from="NATGWId"),
        "PrivateIp": fields.Str(required=False, load_from="PrivateIp"),
    }


class NATGWSnatRuleSchema(schema.ResponseSchema):
    """NATGWSnatRule - Nat网关的Snat规则"""

    fields = {
        "Name": fields.Str(required=True, load_from="Name"),
        "SnatIp": fields.Str(required=True, load_from="SnatIp"),
        "SourceIp": fields.Str(required=True, load_from="SourceIp"),
        "SubnetworkId": fields.Str(required=True, load_from="SubnetworkId"),
    }


class SubnetInfoSchema(schema.ResponseSchema):
    """SubnetInfo - 子网信息"""

    fields = {
        "AvailableIPs": fields.Int(required=False, load_from="AvailableIPs"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "HasNATGW": fields.Bool(required=False, load_from="HasNATGW"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "Netmask": fields.Str(required=False, load_from="Netmask"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "Subnet": fields.Str(required=False, load_from="Subnet"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "SubnetType": fields.Int(required=False, load_from="SubnetType"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class SubnetResourceSchema(schema.ResponseSchema):
    """SubnetResource - 子网下资源"""

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "IPv6Address": fields.Str(
            required=False, load_from="IPv6Address"
        ),  # Deprecated, will be removed at 1.0
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubResourceId": fields.Str(
            required=False, load_from="SubResourceId"
        ),  # Deprecated, will be removed at 1.0
        "SubResourceName": fields.Str(
            required=False, load_from="SubResourceName"
        ),  # Deprecated, will be removed at 1.0
        "SubResourceType": fields.Str(
            required=False, load_from="SubResourceType"
        ),  # Deprecated, will be removed at 1.0
    }


class VIPDetailSetSchema(schema.ResponseSchema):
    """VIPDetailSet - VIPDetailSet"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "RealIp": fields.Str(required=False, load_from="RealIp"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VIP": fields.Str(required=False, load_from="VIP"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class VPCNetworkInfoSchema(schema.ResponseSchema):
    """VPCNetworkInfo - vpc地址空间信息"""

    fields = {
        "Network": fields.Str(required=False, load_from="Network"),
        "SubnetCount": fields.Int(required=False, load_from="SubnetCount"),
    }


class VPCInfoSchema(schema.ResponseSchema):
    """VPCInfo - VPC信息"""

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Network": fields.List(fields.Str()),
        "NetworkInfo": fields.List(VPCNetworkInfoSchema()),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "SubnetCount": fields.Int(required=True, load_from="SubnetCount"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class VPCIntercomInfoSchema(schema.ResponseSchema):
    """VPCIntercomInfo -"""

    fields = {
        "AccountId": fields.Int(required=True, load_from="AccountId"),
        "DstRegion": fields.Str(required=False, load_from="DstRegion"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Network": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCType": fields.Int(required=True, load_from="VPCType"),
    }


class DescribeWhiteListResourceObjectIPInfoSchema(schema.ResponseSchema):
    """DescribeWhiteListResourceObjectIPInfo - DescribeWhiteListResource"""

    fields = {
        "GwType": fields.Str(required=True, load_from="GwType"),
        "PrivateIP": fields.Str(required=True, load_from="PrivateIP"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "ResourceName": fields.Str(required=True, load_from="ResourceName"),
        "ResourceType": fields.Str(required=True, load_from="ResourceType"),
        "SubResourceId": fields.Str(required=True, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=True, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Str(
            required=True, load_from="SubResourceType"
        ),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class NatGWWhitelistDataSetSchema(schema.ResponseSchema):
    """NatGWWhitelistDataSet - nat网关白名单数据"""

    fields = {
        "IfOpen": fields.Int(required=True, load_from="IfOpen"),
        "NATGWId": fields.Str(required=True, load_from="NATGWId"),
        "ObjectIPInfo": fields.List(
            DescribeWhiteListResourceObjectIPInfoSchema()
        ),
    }


class GetAvailableResourceForPolicyDataSetSchema(schema.ResponseSchema):
    """GetAvailableResourceForPolicyDataSet - GetAvailableResourceForPolicy"""

    fields = {
        "PrivateIP": fields.Str(required=True, load_from="PrivateIP"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "ResourceType": fields.Str(required=True, load_from="ResourceType"),
    }


class GetAvailableResourceForSnatRuleDataSetSchema(schema.ResponseSchema):
    """GetAvailableResourceForSnatRuleDataSet -"""

    fields = {
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubnetworkId": fields.Str(required=False, load_from="SubnetworkId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class GetAvailableResourceForWhiteListDataSetSchema(schema.ResponseSchema):
    """GetAvailableResourceForWhiteListDataSet - GetAvailableResourceForWhiteList"""

    fields = {
        "PrivateIP": fields.Str(required=True, load_from="PrivateIP"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
        "ResourceName": fields.Str(required=True, load_from="ResourceName"),
        "ResourceType": fields.Str(required=True, load_from="ResourceType"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=True, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Str(
            required=False, load_from="SubResourceType"
        ),
        "SubnetworkId": fields.Str(required=True, load_from="SubnetworkId"),
        "VPCId": fields.Str(required=True, load_from="VPCId"),
    }


class NatgwSubnetDataSetSchema(schema.ResponseSchema):
    """NatgwSubnetDataSet - natgw可以绑定的子网"""

    fields = {
        "HasNATGW": fields.Bool(required=True, load_from="HasNATGW"),
        "Netmask": fields.Str(required=True, load_from="Netmask"),
        "Subnet": fields.Str(required=True, load_from="Subnet"),
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
        "SubnetName": fields.Str(required=True, load_from="SubnetName"),
    }
