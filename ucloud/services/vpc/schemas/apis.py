""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.vpc.schemas import models


""" VPC API Schema
"""


"""
API: AddVPCNetwork

添加VPC网段
"""


class AddVPCNetworkRequestSchema(schema.RequestSchema):
    """AddVPCNetwork - 添加VPC网段"""

    fields = {
        "Network": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class AddVPCNetworkResponseSchema(schema.ResponseSchema):
    """AddVPCNetwork - 添加VPC网段"""

    fields = {}


"""
API: AssociateRouteTable

绑定子网的路由表
"""


class AssociateRouteTableRequestSchema(schema.RequestSchema):
    """AssociateRouteTable - 绑定子网的路由表"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
    }


class AssociateRouteTableResponseSchema(schema.ResponseSchema):
    """AssociateRouteTable - 绑定子网的路由表"""

    fields = {}


"""
API: CloneRouteTable

根据一张现有路由表复制一张新的路由表
"""


class CloneRouteTableRequestSchema(schema.RequestSchema):
    """CloneRouteTable - 根据一张现有路由表复制一张新的路由表"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
    }


class CloneRouteTableResponseSchema(schema.ResponseSchema):
    """CloneRouteTable - 根据一张现有路由表复制一张新的路由表"""

    fields = {}


"""
API: CreateRouteTable

创建路由表
"""


class CreateRouteTableRequestSchema(schema.RequestSchema):
    """CreateRouteTable - 创建路由表"""

    fields = {
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class CreateRouteTableResponseSchema(schema.ResponseSchema):
    """CreateRouteTable - 创建路由表"""

    fields = {
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId")
    }


"""
API: CreateSubnet

创建子网
"""


class CreateSubnetRequestSchema(schema.RequestSchema):
    """CreateSubnet - 创建子网"""

    fields = {
        "Netmask": fields.Int(required=False, dump_to="Netmask"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Subnet": fields.Str(required=True, dump_to="Subnet"),
        "SubnetName": fields.Str(required=False, dump_to="SubnetName"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class CreateSubnetResponseSchema(schema.ResponseSchema):
    """CreateSubnet - 创建子网"""

    fields = {"SubnetId": fields.Str(required=False, load_from="SubnetId")}


"""
API: CreateVPC

创建VPC
"""


class CreateVPCRequestSchema(schema.RequestSchema):
    """CreateVPC - 创建VPC"""

    fields = {
        "Name": fields.Str(required=True, dump_to="Name"),
        "Network": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class CreateVPCResponseSchema(schema.ResponseSchema):
    """CreateVPC - 创建VPC"""

    fields = {"VPCId": fields.Str(required=False, load_from="VPCId")}


"""
API: CreateVPCIntercom

新建VPC互通关系
"""


class CreateVPCIntercomRequestSchema(schema.RequestSchema):
    """CreateVPCIntercom - 新建VPC互通关系"""

    fields = {
        "DstProjectId": fields.Str(required=False, dump_to="DstProjectId"),
        "DstRegion": fields.Str(required=False, dump_to="DstRegion"),
        "DstVPCId": fields.Str(required=True, dump_to="DstVPCId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class CreateVPCIntercomResponseSchema(schema.ResponseSchema):
    """CreateVPCIntercom - 新建VPC互通关系"""

    fields = {}


"""
API: DeleteRouteTable

删除自定义路由表
"""


class DeleteRouteTableRequestSchema(schema.RequestSchema):
    """DeleteRouteTable - 删除自定义路由表"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
    }


class DeleteRouteTableResponseSchema(schema.ResponseSchema):
    """DeleteRouteTable - 删除自定义路由表"""

    fields = {}


"""
API: DeleteSubnet

删除子网
"""


class DeleteSubnetRequestSchema(schema.RequestSchema):
    """DeleteSubnet - 删除子网"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
    }


class DeleteSubnetResponseSchema(schema.ResponseSchema):
    """DeleteSubnet - 删除子网"""

    fields = {}


"""
API: DeleteVPC

删除VPC
"""


class DeleteVPCRequestSchema(schema.RequestSchema):
    """DeleteVPC - 删除VPC"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class DeleteVPCResponseSchema(schema.ResponseSchema):
    """DeleteVPC - 删除VPC"""

    fields = {}


"""
API: DeleteVPCIntercom

删除VPC互通关系
"""


class DeleteVPCIntercomRequestSchema(schema.RequestSchema):
    """DeleteVPCIntercom - 删除VPC互通关系"""

    fields = {
        "DstProjectId": fields.Str(required=False, dump_to="DstProjectId"),
        "DstRegion": fields.Str(required=False, dump_to="DstRegion"),
        "DstVPCId": fields.Str(required=True, dump_to="DstVPCId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class DeleteVPCIntercomResponseSchema(schema.ResponseSchema):
    """DeleteVPCIntercom - 删除VPC互通关系"""

    fields = {}


"""
API: DescribeRouteTable

获取路由表详细信息(包括路由策略)
"""


class DescribeRouteTableRequestSchema(schema.RequestSchema):
    """DescribeRouteTable - 获取路由表详细信息(包括路由策略)"""

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "OffSet": fields.Int(required=False, dump_to="OffSet"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RouteTableId": fields.Str(required=False, dump_to="RouteTableId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class DescribeRouteTableResponseSchema(schema.ResponseSchema):
    """DescribeRouteTable - 获取路由表详细信息(包括路由策略)"""

    fields = {
        "RouteTables": fields.List(
            models.RouteTableInfoSchema(),
            required=False,
            load_from="RouteTables",
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeSubnet

获取子网信息
"""


class DescribeSubnetRequestSchema(schema.RequestSchema):
    """DescribeSubnet - 获取子网信息"""

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RouteTableId": fields.Str(required=False, dump_to="RouteTableId"),
        "ShowAvailableIPs": fields.Bool(
            required=False, dump_to="ShowAvailableIPs"
        ),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "SubnetIds": fields.List(fields.Str()),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
    }


class DescribeSubnetResponseSchema(schema.ResponseSchema):
    """DescribeSubnet - 获取子网信息"""

    fields = {
        "DataSet": fields.List(
            models.SubnetInfoSchema(), required=True, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeSubnetResource

展示子网资源
"""


class DescribeSubnetResourceRequestSchema(schema.RequestSchema):
    """DescribeSubnetResource - 展示子网资源"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceType": fields.Str(required=False, dump_to="ResourceType"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
    }


class DescribeSubnetResourceResponseSchema(schema.ResponseSchema):
    """DescribeSubnetResource - 展示子网资源"""

    fields = {
        "DataSet": fields.List(
            models.SubnetResourceSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeVPC

获取VPC信息
"""


class DescribeVPCRequestSchema(schema.RequestSchema):
    """DescribeVPC - 获取VPC信息"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCIds": fields.List(fields.Str()),
    }


class DescribeVPCResponseSchema(schema.ResponseSchema):
    """DescribeVPC - 获取VPC信息"""

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
    """DescribeVPCIntercom - 获取VPC互通信息"""

    fields = {
        "DstProjectId": fields.Str(required=False, dump_to="DstProjectId"),
        "DstRegion": fields.Str(required=False, dump_to="DstRegion"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class DescribeVPCIntercomResponseSchema(schema.ResponseSchema):
    """DescribeVPCIntercom - 获取VPC互通信息"""

    fields = {
        "DataSet": fields.List(
            models.VPCIntercomInfoSchema(), required=False, load_from="DataSet"
        )
    }


"""
API: ModifyRouteRule

路由策略增、删、改
"""


class ModifyRouteRuleRequestSchema(schema.RequestSchema):
    """ModifyRouteRule - 路由策略增、删、改"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "RouteRule": fields.List(fields.Str()),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
    }


class ModifyRouteRuleResponseSchema(schema.ResponseSchema):
    """ModifyRouteRule - 路由策略增、删、改"""

    fields = {}


"""
API: UpdateRouteTableAttribute

更新路由表基本信息
"""


class UpdateRouteTableAttributeRequestSchema(schema.RequestSchema):
    """UpdateRouteTableAttribute - 更新路由表基本信息"""

    fields = {
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "RouteTableId": fields.Str(required=True, dump_to="RouteTableId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class UpdateRouteTableAttributeResponseSchema(schema.ResponseSchema):
    """UpdateRouteTableAttribute - 更新路由表基本信息"""

    fields = {}


"""
API: UpdateSubnetAttribute

更新子网信息
"""


class UpdateSubnetAttributeRequestSchema(schema.RequestSchema):
    """UpdateSubnetAttribute - 更新子网信息"""

    fields = {
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class UpdateSubnetAttributeResponseSchema(schema.ResponseSchema):
    """UpdateSubnetAttribute - 更新子网信息"""

    fields = {}


"""
API: UpdateVPCNetwork

更新VPC网段
"""


class UpdateVPCNetworkRequestSchema(schema.RequestSchema):
    """UpdateVPCNetwork - 更新VPC网段"""

    fields = {
        "Network": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class UpdateVPCNetworkResponseSchema(schema.ResponseSchema):
    """UpdateVPCNetwork - 更新VPC网段"""

    fields = {"Message": fields.Str(required=True, load_from="Message")}
