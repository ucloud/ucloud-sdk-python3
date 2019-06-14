from ucloud.core.typesystem import schema, fields
from ucloud.services.vpc.schemas import models


""" VPC API Schema
"""


"""
API: DeleteVPCIntercom

删除VPC互通关系
"""


class DeleteVPCIntercomRequestSchema(schema.RequestSchema):
    """ DeleteVPCIntercom - 删除VPC互通关系
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "DstVPCId": fields.Str(required=True, dump_to="DstVPCId"),
        "DstRegion": fields.Str(required=False, dump_to="DstRegion"),
        "DstProjectId": fields.Str(required=False, dump_to="DstProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DeleteVPCIntercomResponseSchema(schema.ResponseSchema):
    """ DeleteVPCIntercom - 删除VPC互通关系
    """

    fields = {}


"""
API: ModifyRouteRule

路由策略增、删、改
"""


class ModifyRouteRuleRequestSchema(schema.RequestSchema):
    """ ModifyRouteRule - 路由策略增、删、改
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
        "RouteRule": fields.List(fields.Str()),
    }


class ModifyRouteRuleResponseSchema(schema.ResponseSchema):
    """ ModifyRouteRule - 路由策略增、删、改
    """

    fields = {}


"""
API: UpdateSubnetAttribute

更新子网信息
"""


class UpdateSubnetAttributeRequestSchema(schema.RequestSchema):
    """ UpdateSubnetAttribute - 更新子网信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class UpdateSubnetAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateSubnetAttribute - 更新子网信息
    """

    fields = {}


"""
API: CreateSubnet

创建子网
"""


class CreateSubnetRequestSchema(schema.RequestSchema):
    """ CreateSubnet - 创建子网
    """

    fields = {
        "Subnet": fields.Str(required=True, dump_to="Subnet"),
        "Netmask": fields.Int(required=False, dump_to="Netmask"),
        "SubnetName": fields.Str(required=False, dump_to="SubnetName"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class CreateSubnetResponseSchema(schema.ResponseSchema):
    """ CreateSubnet - 创建子网
    """

    fields = {"SubnetId": fields.Str(required=False, load_from="SubnetId")}


"""
API: CreateVPC

创建VPC
"""


class CreateVPCRequestSchema(schema.RequestSchema):
    """ CreateVPC - 创建VPC
    """

    fields = {
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Type": fields.Int(required=False, dump_to="Type"),
        "Network": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Name": fields.Str(required=True, dump_to="Name"),
    }


class CreateVPCResponseSchema(schema.ResponseSchema):
    """ CreateVPC - 创建VPC
    """

    fields = {"VPCId": fields.Str(required=False, load_from="VPCId")}


"""
API: DeleteSubnet

删除子网
"""


class DeleteSubnetRequestSchema(schema.RequestSchema):
    """ DeleteSubnet - 删除子网
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
    }


class DeleteSubnetResponseSchema(schema.ResponseSchema):
    """ DeleteSubnet - 删除子网
    """

    fields = {}


"""
API: DescribeSubnet

获取子网信息
"""


class DescribeSubnetRequestSchema(schema.RequestSchema):
    """ DescribeSubnet - 获取子网信息
    """

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "RouteTableId": fields.Str(required=False, dump_to="RouteTableId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "SubnetIds": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeSubnetResponseSchema(schema.ResponseSchema):
    """ DescribeSubnet - 获取子网信息
    """

    fields = {
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
        "DataSet": fields.List(
            models.SubnetInfoSchema(), required=True, load_from="DataSet"
        ),
    }


"""
API: UpdateRouteTableAttribute

更新路由表基本信息
"""


class UpdateRouteTableAttributeRequestSchema(schema.RequestSchema):
    """ UpdateRouteTableAttribute - 更新路由表基本信息
    """

    fields = {
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
        "Name": fields.Str(required=False, dump_to="Name"),
    }


class UpdateRouteTableAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateRouteTableAttribute - 更新路由表基本信息
    """

    fields = {}


"""
API: UpdateVPCNetwork

更新VPC网段
"""


class UpdateVPCNetworkRequestSchema(schema.RequestSchema):
    """ UpdateVPCNetwork - 更新VPC网段
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "Network": fields.List(fields.Str()),
    }


class UpdateVPCNetworkResponseSchema(schema.ResponseSchema):
    """ UpdateVPCNetwork - 更新VPC网段
    """

    fields = {"Message": fields.Str(required=True, load_from="Message")}


"""
API: CreateRouteTable

创建路由表
"""


class CreateRouteTableRequestSchema(schema.RequestSchema):
    """ CreateRouteTable - 创建路由表
    """

    fields = {
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class CreateRouteTableResponseSchema(schema.ResponseSchema):
    """ CreateRouteTable - 创建路由表
    """

    fields = {"RouteTableId": fields.Str(required=False, load_from="RouteTableId")}


"""
API: CreateVPCIntercom

新建VPC互通关系
"""


class CreateVPCIntercomRequestSchema(schema.RequestSchema):
    """ CreateVPCIntercom - 新建VPC互通关系
    """

    fields = {
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "DstVPCId": fields.Str(required=True, dump_to="DstVPCId"),
        "DstRegion": fields.Str(required=False, dump_to="DstRegion"),
        "DstProjectId": fields.Str(required=False, dump_to="DstProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class CreateVPCIntercomResponseSchema(schema.ResponseSchema):
    """ CreateVPCIntercom - 新建VPC互通关系
    """

    fields = {}


"""
API: DescribeRouteTable

获取路由表详细信息(包括路由策略)
"""


class DescribeRouteTableRequestSchema(schema.RequestSchema):
    """ DescribeRouteTable - 获取路由表详细信息(包括路由策略)
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "RouteTableId": fields.Str(required=False, dump_to="RouteTableId"),
        "OffSet": fields.Int(required=False, dump_to="OffSet"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
    }


class DescribeRouteTableResponseSchema(schema.ResponseSchema):
    """ DescribeRouteTable - 获取路由表详细信息(包括路由策略)
    """

    fields = {
        "RouteTables": fields.List(
            models.RouteTableInfoSchema(), required=False, load_from="RouteTables"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DeleteVPC

删除VPC
"""


class DeleteVPCRequestSchema(schema.RequestSchema):
    """ DeleteVPC - 删除VPC
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class DeleteVPCResponseSchema(schema.ResponseSchema):
    """ DeleteVPC - 删除VPC
    """

    fields = {}


"""
API: DescribeSubnetResource

展示子网资源
"""


class DescribeSubnetResourceRequestSchema(schema.RequestSchema):
    """ DescribeSubnetResource - 展示子网资源
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "ResourceType": fields.Str(required=False, dump_to="ResourceType"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
    }


class DescribeSubnetResourceResponseSchema(schema.ResponseSchema):
    """ DescribeSubnetResource - 展示子网资源
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSet": fields.List(
            models.SubnetResourceSchema(), required=False, load_from="DataSet"
        ),
    }


"""
API: DeleteRouteTable

删除自定义路由表
"""


class DeleteRouteTableRequestSchema(schema.RequestSchema):
    """ DeleteRouteTable - 删除自定义路由表
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
    }


class DeleteRouteTableResponseSchema(schema.ResponseSchema):
    """ DeleteRouteTable - 删除自定义路由表
    """

    fields = {}


"""
API: DescribeVPC

获取VPC信息
"""


class DescribeVPCRequestSchema(schema.RequestSchema):
    """ DescribeVPC - 获取VPC信息
    """

    fields = {
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "VPCIds": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class DescribeVPCResponseSchema(schema.ResponseSchema):
    """ DescribeVPC - 获取VPC信息
    """

    fields = {
        "DataSet": fields.List(
            models.VPCInfoSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: DescribeVPCIntercom

获取VPC互通信息
"""


class DescribeVPCIntercomRequestSchema(schema.RequestSchema):
    """ DescribeVPCIntercom - 获取VPC互通信息
    """

    fields = {
        "DstRegion": fields.Str(required=False, dump_to="DstRegion"),
        "DstProjectId": fields.Str(required=False, dump_to="DstProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class DescribeVPCIntercomResponseSchema(schema.ResponseSchema):
    """ DescribeVPCIntercom - 获取VPC互通信息
    """

    fields = {
        "DataSet": fields.List(
            models.VPCIntercomInfoSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: AddVPCNetwork

添加VPC网段
"""


class AddVPCNetworkRequestSchema(schema.RequestSchema):
    """ AddVPCNetwork - 添加VPC网段
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "Network": fields.List(fields.Str()),
    }


class AddVPCNetworkResponseSchema(schema.ResponseSchema):
    """ AddVPCNetwork - 添加VPC网段
    """

    fields = {}


"""
API: AssociateRouteTable

绑定子网的路由表
"""


class AssociateRouteTableRequestSchema(schema.RequestSchema):
    """ AssociateRouteTable - 绑定子网的路由表
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
    }


class AssociateRouteTableResponseSchema(schema.ResponseSchema):
    """ AssociateRouteTable - 绑定子网的路由表
    """

    fields = {}


"""
API: CloneRouteTable

根据一张现有路由表复制一张新的路由表
"""


class CloneRouteTableRequestSchema(schema.RequestSchema):
    """ CloneRouteTable - 根据一张现有路由表复制一张新的路由表
    """

    fields = {
        "Region": fields.Str(required=False, dump_to="Region"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
    }


class CloneRouteTableResponseSchema(schema.ResponseSchema):
    """ CloneRouteTable - 根据一张现有路由表复制一张新的路由表
    """

    fields = {}
