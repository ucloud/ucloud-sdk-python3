""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.uec.schemas import models

""" UEC API Schema
"""


"""
API: BindUEcFirewall

绑定防火墙，应用防火墙规则
"""


class BindUEcFirewallRequestSchema(schema.RequestSchema):
    """BindUEcFirewall - 绑定防火墙，应用防火墙规则"""

    fields = {
        "FirewallId": fields.Str(required=True, dump_to="FirewallId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
    }


class BindUEcFirewallResponseSchema(schema.ResponseSchema):
    """BindUEcFirewall - 绑定防火墙，应用防火墙规则"""

    fields = {}


"""
API: CreateUEcFirewall

创建外网防火墙
"""


class CreateUEcFirewallParamRuleSchema(schema.RequestSchema):
    """CreateUEcFirewallParamRule -"""

    fields = {
        "Action": fields.Str(required=True, dump_to="Action"),
        "Port": fields.Str(required=True, dump_to="Port"),
        "Priority": fields.Str(required=True, dump_to="Priority"),
        "ProtocolType": fields.Str(required=True, dump_to="ProtocolType"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "SrcIp": fields.Str(required=True, dump_to="SrcIp"),
    }


class CreateUEcFirewallRequestSchema(schema.RequestSchema):
    """CreateUEcFirewall - 创建外网防火墙"""

    fields = {
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Rule": fields.List(CreateUEcFirewallParamRuleSchema()),
    }


class CreateUEcFirewallResponseSchema(schema.ResponseSchema):
    """CreateUEcFirewall - 创建外网防火墙"""

    fields = {
        "FirewallId": fields.Str(required=True, load_from="FirewallId"),
    }


"""
API: CreateUEcHolder

创建容器组
"""


class CreateUEcHolderParamImageSchema(schema.RequestSchema):
    """CreateUEcHolderParamImage -"""

    fields = {
        "Message": fields.Str(required=False, dump_to="Message"),
        "StoreAddress": fields.Str(required=False, dump_to="StoreAddress"),
    }


class CreateUEcHolderParamPackSchema(schema.RequestSchema):
    """CreateUEcHolderParamPack -"""

    fields = {
        "Args": fields.Str(required=False, dump_to="Args"),
        "Cmd": fields.Str(required=False, dump_to="Cmd"),
        "ConfigDict": fields.Str(required=False, dump_to="ConfigDict"),
        "CpuCore": fields.Float(required=False, dump_to="CpuCore"),
        "Environment": fields.Str(required=False, dump_to="Environment"),
        "ImageName": fields.Str(required=False, dump_to="ImageName"),
        "MemSize": fields.Int(required=False, dump_to="MemSize"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "WorkDir": fields.Str(required=False, dump_to="WorkDir"),
    }


class CreateUEcHolderParamStorageSchema(schema.RequestSchema):
    """CreateUEcHolderParamStorage -"""

    fields = {
        "Path": fields.Str(required=False, dump_to="Path"),
        "ResourceId": fields.Str(required=False, dump_to="ResourceId"),
    }


class CreateUEcHolderRequestSchema(schema.RequestSchema):
    """CreateUEcHolder - 创建容器组"""

    fields = {
        "Bandwidth": fields.Int(required=False, dump_to="Bandwidth"),
        "ChargeQuantity": fields.Int(required=False, dump_to="ChargeQuantity"),
        "ChargeType": fields.Int(required=False, dump_to="ChargeType"),
        "CpuCore": fields.Float(required=True, dump_to="CpuCore"),
        "ElasticIp": fields.Str(required=False, dump_to="ElasticIp"),
        "FirewallId": fields.Str(required=False, dump_to="FirewallId"),
        "IdcId": fields.Str(required=True, dump_to="IdcId"),
        "Image": fields.List(CreateUEcHolderParamImageSchema()),
        "MemSize": fields.Int(required=True, dump_to="MemSize"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Pack": fields.List(CreateUEcHolderParamPackSchema()),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "RestartStrategy": fields.Int(
            required=False, dump_to="RestartStrategy"
        ),
        "Storage": fields.List(CreateUEcHolderParamStorageSchema()),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
    }


class CreateUEcHolderResponseSchema(schema.ResponseSchema):
    """CreateUEcHolder - 创建容器组"""

    fields = {
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
    }


"""
API: CreateUEcSubnet

创建子网
"""


class CreateUEcSubnetRequestSchema(schema.RequestSchema):
    """CreateUEcSubnet - 创建子网"""

    fields = {
        "CIDR": fields.Str(required=True, dump_to="CIDR"),
        "Comment": fields.Str(required=False, dump_to="Comment"),
        "IdcId": fields.Str(required=True, dump_to="IdcId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetName": fields.Str(required=False, dump_to="SubnetName"),
    }


class CreateUEcSubnetResponseSchema(schema.ResponseSchema):
    """CreateUEcSubnet - 创建子网"""

    fields = {
        "SubnetId": fields.Str(required=True, load_from="SubnetId"),
    }


"""
API: CreateUEcVHost

创建虚拟机v2.0
"""


class CreateUEcVHostRequestSchema(schema.RequestSchema):
    """CreateUEcVHost - 创建虚拟机v2.0"""

    fields = {
        "AccountName": fields.Str(required=False, dump_to="AccountName"),
        "ChargeQuantity": fields.Int(required=False, dump_to="ChargeQuantity"),
        "ChargeType": fields.Int(required=False, dump_to="ChargeType"),
        "CpuCore": fields.Int(required=True, dump_to="CpuCore"),
        "DiskSize": fields.Int(required=True, dump_to="DiskSize"),
        "FirewallId": fields.Str(required=False, dump_to="FirewallId"),
        "IdcId": fields.Str(required=True, dump_to="IdcId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "IsNeedOuterIp": fields.Str(required=False, dump_to="IsNeedOuterIp"),
        "Isp": fields.List(fields.Int()),
        "MemSize": fields.Int(required=True, dump_to="MemSize"),
        "NetLimit": fields.Int(required=True, dump_to="NetLimit"),
        "NodeCount": fields.Int(required=False, dump_to="NodeCount"),
        "NodeName": fields.Str(required=False, dump_to="NodeName"),
        "PassWord": fields.Str(required=False, dump_to="PassWord"),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "SysDiskSize": fields.Int(required=False, dump_to="SysDiskSize"),
    }


class CreateUEcVHostResponseSchema(schema.ResponseSchema):
    """CreateUEcVHost - 创建虚拟机v2.0"""

    fields = {
        "NodeList": fields.List(
            models.NodeListSchema(), required=True, load_from="NodeList"
        ),
    }


"""
API: DeleteUEcCustomImage

删除UEDN客户自定义镜像
"""


class DeleteUEcCustomImageRequestSchema(schema.RequestSchema):
    """DeleteUEcCustomImage - 删除UEDN客户自定义镜像"""

    fields = {
        "IdcId": fields.Str(required=False, dump_to="IdcId"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DeleteUEcCustomImageResponseSchema(schema.ResponseSchema):
    """DeleteUEcCustomImage - 删除UEDN客户自定义镜像"""

    fields = {
        "ImageId": fields.Int(required=True, load_from="ImageId"),
    }


"""
API: DeleteUEcHolder

删除容器组
"""


class DeleteUEcHolderRequestSchema(schema.RequestSchema):
    """DeleteUEcHolder - 删除容器组"""

    fields = {
        "HolderId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DeleteUEcHolderResponseSchema(schema.ResponseSchema):
    """DeleteUEcHolder - 删除容器组"""

    fields = {}


"""
API: DeleteUEcSubnet

删除子网
"""


class DeleteUEcSubnetRequestSchema(schema.RequestSchema):
    """DeleteUEcSubnet - 删除子网"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
    }


class DeleteUEcSubnetResponseSchema(schema.ResponseSchema):
    """DeleteUEcSubnet - 删除子网"""

    fields = {}


"""
API: DeleteUEcVHost

删除vhost虚拟机 v2.0
"""


class DeleteUEcVHostRequestSchema(schema.RequestSchema):
    """DeleteUEcVHost - 删除vhost虚拟机 v2.0"""

    fields = {
        "NodeId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DeleteUEcVHostResponseSchema(schema.ResponseSchema):
    """DeleteUEcVHost - 删除vhost虚拟机 v2.0"""

    fields = {}


"""
API: DescribeUEcFirewall

获取防火墙信息
"""


class DescribeUEcFirewallRequestSchema(schema.RequestSchema):
    """DescribeUEcFirewall - 获取防火墙信息"""

    fields = {
        "FirewallId": fields.Str(required=False, dump_to="FirewallId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.Str(required=False, dump_to="ResourceId"),
    }


class DescribeUEcFirewallResponseSchema(schema.ResponseSchema):
    """DescribeUEcFirewall - 获取防火墙信息"""

    fields = {
        "FirewallSet": fields.List(
            models.FirewallInfoSchema(), required=False, load_from="FirewallSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUEcFirewallResource

防火墙绑定的资源列表
"""


class DescribeUEcFirewallResourceRequestSchema(schema.RequestSchema):
    """DescribeUEcFirewallResource - 防火墙绑定的资源列表"""

    fields = {
        "FirewallId": fields.Str(required=True, dump_to="FirewallId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUEcFirewallResourceResponseSchema(schema.ResponseSchema):
    """DescribeUEcFirewallResource - 防火墙绑定的资源列表"""

    fields = {
        "ResourceSet": fields.List(
            models.ResourceInfoSchema(), required=True, load_from="ResourceSet"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeUEcHolder

获得容器组信息
"""


class DescribeUEcHolderRequestSchema(schema.RequestSchema):
    """DescribeUEcHolder - 获得容器组信息"""

    fields = {
        "HolderId": fields.List(fields.Str()),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUEcHolderResponseSchema(schema.ResponseSchema):
    """DescribeUEcHolder - 获得容器组信息"""

    fields = {
        "HolderList": fields.List(
            models.HolderListSchema(), required=True, load_from="HolderList"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeUEcHolderIDC

获取容器组机房信息
"""


class DescribeUEcHolderIDCRequestSchema(schema.RequestSchema):
    """DescribeUEcHolderIDC - 获取容器组机房信息"""

    fields = {
        "Cpu": fields.Float(required=True, dump_to="Cpu"),
        "IdcId": fields.List(fields.Str()),
        "Memory": fields.Int(required=True, dump_to="Memory"),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class DescribeUEcHolderIDCResponseSchema(schema.ResponseSchema):
    """DescribeUEcHolderIDC - 获取容器组机房信息"""

    fields = {
        "IdcList": fields.List(
            models.IdcInfoSchema(), required=True, load_from="IdcList"
        ),
    }


"""
API: DescribeUEcIDC

获取IDC机房列表
"""


class DescribeUEcIDCRequestSchema(schema.RequestSchema):
    """DescribeUEcIDC - 获取IDC机房列表"""

    fields = {
        "Cpu": fields.Int(required=True, dump_to="Cpu"),
        "IdcId": fields.List(fields.Str()),
        "Memory": fields.Int(required=True, dump_to="Memory"),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class DescribeUEcIDCResponseSchema(schema.ResponseSchema):
    """DescribeUEcIDC - 获取IDC机房列表"""

    fields = {
        "Action": fields.Str(required=True, load_from="Action"),
        "IdcList": fields.List(
            models.IdcInfoSchema(), required=False, load_from="IdcList"
        ),
        "RetCode": fields.Int(required=True, load_from="RetCode"),
    }


"""
API: DescribeUEcSubnet

获取子网列表
"""


class DescribeUEcSubnetRequestSchema(schema.RequestSchema):
    """DescribeUEcSubnet - 获取子网列表"""

    fields = {
        "IdcId": fields.Str(required=False, dump_to="IdcId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
    }


class DescribeUEcSubnetResponseSchema(schema.ResponseSchema):
    """DescribeUEcSubnet - 获取子网列表"""

    fields = {
        "SubnetList": fields.List(
            models.SubnetInfoSchema(), required=False, load_from="SubnetList"
        ),
    }


"""
API: DescribeUEcVHost

获取虚拟机列表 2.0
"""


class DescribeUEcVHostRequestSchema(schema.RequestSchema):
    """DescribeUEcVHost - 获取虚拟机列表 2.0"""

    fields = {
        "IdcId": fields.List(fields.Str()),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "NodeId": fields.List(fields.Str()),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DescribeUEcVHostResponseSchema(schema.ResponseSchema):
    """DescribeUEcVHost - 获取虚拟机列表 2.0"""

    fields = {
        "NodeList": fields.List(
            models.NodeInfoSchema(), required=False, load_from="NodeList"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUEcVHostISP

获取虚拟机运营商信息
"""


class DescribeUEcVHostISPRequestSchema(schema.RequestSchema):
    """DescribeUEcVHostISP - 获取虚拟机运营商信息"""

    fields = {
        "City": fields.Str(required=False, dump_to="City"),
        "IspName": fields.Str(required=False, dump_to="IspName"),
        "Province": fields.Str(required=False, dump_to="Province"),
    }


class DescribeUEcVHostISPResponseSchema(schema.ResponseSchema):
    """DescribeUEcVHostISP - 获取虚拟机运营商信息"""

    fields = {
        "NodeIspList": fields.List(
            models.NodeIspListSchema(), required=True, load_from="NodeIspList"
        ),
    }


"""
API: GetUEcHolderLog

获取单个容器日志
"""


class GetUEcHolderLogRequestSchema(schema.RequestSchema):
    """GetUEcHolderLog - 获取单个容器日志"""

    fields = {
        "PackName": fields.Str(required=True, dump_to="PackName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
    }


class GetUEcHolderLogResponseSchema(schema.ResponseSchema):
    """GetUEcHolderLog - 获取单个容器日志"""

    fields = {
        "Data": fields.Str(required=False, load_from="Data"),
    }


"""
API: GetUEcHolderMetrics

获取容器（CPU利用率，带宽，内存）数据
"""


class GetUEcHolderMetricsRequestSchema(schema.RequestSchema):
    """GetUEcHolderMetrics - 获取容器（CPU利用率，带宽，内存）数据"""

    fields = {
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "PackName": fields.Str(required=True, dump_to="PackName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
        "StartTime": fields.Int(required=False, dump_to="StartTime"),
        "Type": fields.List(fields.Str()),
    }


class GetUEcHolderMetricsResponseSchema(schema.ResponseSchema):
    """GetUEcHolderMetrics - 获取容器（CPU利用率，带宽，内存）数据"""

    fields = {
        "DataSets": models.MetricisDataSetSchema(),
    }


"""
API: GetUEcIDCCutInfo

获取机房割接信息
"""


class GetUEcIDCCutInfoRequestSchema(schema.RequestSchema):
    """GetUEcIDCCutInfo - 获取机房割接信息"""

    fields = {}


class GetUEcIDCCutInfoResponseSchema(schema.ResponseSchema):
    """GetUEcIDCCutInfo - 获取机房割接信息"""

    fields = {
        "IDCCutInfo": fields.List(
            models.IDCCutInfoSchema(), required=True, load_from="IDCCutInfo"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetUEcIDCVHostData

获取机房虚拟机监控数据
"""


class GetUEcIDCVHostDataRequestSchema(schema.RequestSchema):
    """GetUEcIDCVHostData - 获取机房虚拟机监控数据"""

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "NodeId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.List(fields.Str()),
    }


class GetUEcIDCVHostDataResponseSchema(schema.ResponseSchema):
    """GetUEcIDCVHostData - 获取机房虚拟机监控数据"""

    fields = {
        "DataSets": models.DataSetSchema(),
    }


"""
API: GetUEcImage

uec2.0
"""


class GetUEcImageRequestSchema(schema.RequestSchema):
    """GetUEcImage - uec2.0"""

    fields = {
        "ImageType": fields.Str(required=False, dump_to="ImageType"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUEcImageResponseSchema(schema.ResponseSchema):
    """GetUEcImage - uec2.0"""

    fields = {
        "ImageList": fields.List(
            models.ImageInfoSchema(), required=False, load_from="ImageList"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetUEcPodPrice

获得容器组价格
"""


class GetUEcPodPriceRequestSchema(schema.RequestSchema):
    """GetUEcPodPrice - 获得容器组价格"""

    fields = {
        "Bandwidth": fields.Int(required=False, dump_to="Bandwidth"),
        "ChargeQuantity": fields.Int(required=False, dump_to="ChargeQuantity"),
        "ChargeType": fields.Int(required=False, dump_to="ChargeType"),
        "CpuCore": fields.Float(required=False, dump_to="CpuCore"),
        "ElasticIp": fields.Str(required=False, dump_to="ElasticIp"),
        "IdcId": fields.Str(required=True, dump_to="IdcId"),
        "MemSize": fields.Int(required=False, dump_to="MemSize"),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
    }


class GetUEcPodPriceResponseSchema(schema.ResponseSchema):
    """GetUEcPodPrice - 获得容器组价格"""

    fields = {
        "HolderPrice": fields.Float(required=True, load_from="HolderPrice"),
        "IpPrice": fields.Float(required=True, load_from="IpPrice"),
    }


"""
API: GetUEcUpgradePrice

获取虚拟机调整差价
"""


class GetUEcUpgradePriceRequestSchema(schema.RequestSchema):
    """GetUEcUpgradePrice - 获取虚拟机调整差价"""

    fields = {
        "CpuCore": fields.Int(required=False, dump_to="CpuCore"),
        "DiskSize": fields.Int(required=False, dump_to="DiskSize"),
        "MemSize": fields.Int(required=False, dump_to="MemSize"),
        "NetLimit": fields.Int(required=False, dump_to="NetLimit"),
        "NodeId": fields.Str(required=True, dump_to="NodeId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SysDiskSize": fields.Int(required=False, dump_to="SysDiskSize"),
    }


class GetUEcUpgradePriceResponseSchema(schema.ResponseSchema):
    """GetUEcUpgradePrice - 获取虚拟机调整差价"""

    fields = {
        "Price": fields.Int(required=False, load_from="Price"),
    }


"""
API: GetUEcVHostData

获取虚拟机监控数据
"""


class GetUEcVHostDataRequestSchema(schema.RequestSchema):
    """GetUEcVHostData - 获取虚拟机监控数据"""

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "NodeId": fields.Str(required=True, dump_to="NodeId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.List(fields.Int()),
    }


class GetUEcVHostDataResponseSchema(schema.ResponseSchema):
    """GetUEcVHostData - 获取虚拟机监控数据"""

    fields = {
        "Action": fields.Str(required=True, load_from="Action"),
        "DataSets": models.DataSetSchema(),
        "RetCode": fields.Int(required=True, load_from="RetCode"),
    }


"""
API: GetUEcVHostPrice

获取虚拟机价格
"""


class GetUEcVHostPriceRequestSchema(schema.RequestSchema):
    """GetUEcVHostPrice - 获取虚拟机价格"""

    fields = {
        "ChargeQuantity": fields.Int(required=False, dump_to="ChargeQuantity"),
        "ChargeType": fields.Int(required=False, dump_to="ChargeType"),
        "CpuCore": fields.Int(required=False, dump_to="CpuCore"),
        "DiskSize": fields.Int(required=False, dump_to="DiskSize"),
        "IdcId": fields.Str(required=True, dump_to="IdcId"),
        "IpCount": fields.Int(required=False, dump_to="IpCount"),
        "MemSize": fields.Int(required=False, dump_to="MemSize"),
        "NetLimit": fields.Int(required=False, dump_to="NetLimit"),
        "NodeCount": fields.Int(required=False, dump_to="NodeCount"),
        "ProductType": fields.Str(required=False, dump_to="ProductType"),
        "SysDiskSize": fields.Int(required=False, dump_to="SysDiskSize"),
    }


class GetUEcVHostPriceResponseSchema(schema.ResponseSchema):
    """GetUEcVHostPrice - 获取虚拟机价格"""

    fields = {
        "IpPrice": fields.Float(required=False, load_from="IpPrice"),
        "NodePrice": fields.Float(required=False, load_from="NodePrice"),
    }


"""
API: ImportUEcCustomImage

导入自定义镜像
"""


class ImportUEcCustomImageRequestSchema(schema.RequestSchema):
    """ImportUEcCustomImage - 导入自定义镜像"""

    fields = {
        "Format": fields.Str(required=False, dump_to="Format"),
        "IdcId": fields.List(fields.Str()),
        "ImageDesc": fields.Str(required=False, dump_to="ImageDesc"),
        "ImageId": fields.Str(required=False, dump_to="ImageId"),
        "ImageName": fields.Str(required=False, dump_to="ImageName"),
        "OsType": fields.Str(required=False, dump_to="OsType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UFileUrl": fields.Str(required=False, dump_to="UFileUrl"),
    }


class ImportUEcCustomImageResponseSchema(schema.ResponseSchema):
    """ImportUEcCustomImage - 导入自定义镜像"""

    fields = {
        "ImageId": fields.Str(required=True, load_from="ImageId"),
    }


"""
API: LoginUEcDocker

登录容器
"""


class LoginUEcDockerRequestSchema(schema.RequestSchema):
    """LoginUEcDocker - 登录容器"""

    fields = {
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
    }


class LoginUEcDockerResponseSchema(schema.ResponseSchema):
    """LoginUEcDocker - 登录容器"""

    fields = {
        "Link": fields.Str(required=False, load_from="Link"),
        "LinkPort": fields.Int(required=False, load_from="LinkPort"),
        "SessionId": fields.Str(required=True, load_from="SessionId"),
    }


"""
API: ModifyUEcBandwidth

修改节点带宽限制
"""


class ModifyUEcBandwidthRequestSchema(schema.RequestSchema):
    """ModifyUEcBandwidth - 修改节点带宽限制"""

    fields = {
        "NetLimit": fields.Str(required=True, dump_to="NetLimit"),
        "NodeId": fields.Str(required=True, dump_to="NodeId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ModifyUEcBandwidthResponseSchema(schema.ResponseSchema):
    """ModifyUEcBandwidth - 修改节点带宽限制"""

    fields = {}


"""
API: ModifyUEcHolderName

修改容器组名称
"""


class ModifyUEcHolderNameRequestSchema(schema.RequestSchema):
    """ModifyUEcHolderName - 修改容器组名称"""

    fields = {
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
    }


class ModifyUEcHolderNameResponseSchema(schema.ResponseSchema):
    """ModifyUEcHolderName - 修改容器组名称"""

    fields = {}


"""
API: ModifyUEcImageName

修改镜像名称
"""


class ModifyUEcImageNameRequestSchema(schema.RequestSchema):
    """ModifyUEcImageName - 修改镜像名称"""

    fields = {
        "ImageDesc": fields.Str(required=False, dump_to="ImageDesc"),
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "ImageName": fields.Str(required=True, dump_to="ImageName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ModifyUEcImageNameResponseSchema(schema.ResponseSchema):
    """ModifyUEcImageName - 修改镜像名称"""

    fields = {}


"""
API: PoweroffUEcVHost

虚拟机断电
"""


class PoweroffUEcVHostRequestSchema(schema.RequestSchema):
    """PoweroffUEcVHost - 虚拟机断电"""

    fields = {
        "NodeId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class PoweroffUEcVHostResponseSchema(schema.ResponseSchema):
    """PoweroffUEcVHost - 虚拟机断电"""

    fields = {}


"""
API: ReinstallUEcVHost

虚拟机重装系统
"""


class ReinstallUEcVHostRequestSchema(schema.RequestSchema):
    """ReinstallUEcVHost - 虚拟机重装系统"""

    fields = {
        "ImageId": fields.Str(required=True, dump_to="ImageId"),
        "KeepData": fields.Int(required=False, dump_to="KeepData"),
        "NodeId": fields.Str(required=True, dump_to="NodeId"),
        "Password": fields.Str(required=False, dump_to="Password"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SysDiskSize": fields.Int(required=False, dump_to="SysDiskSize"),
    }


class ReinstallUEcVHostResponseSchema(schema.ResponseSchema):
    """ReinstallUEcVHost - 虚拟机重装系统"""

    fields = {}


"""
API: RestartUEcHolder

重启容器组
"""


class RestartUEcHolderRequestSchema(schema.RequestSchema):
    """RestartUEcHolder - 重启容器组"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.List(fields.Str()),
    }


class RestartUEcHolderResponseSchema(schema.ResponseSchema):
    """RestartUEcHolder - 重启容器组"""

    fields = {}


"""
API: RestartUEcVHost

重启虚拟机v2.0
"""


class RestartUEcVHostRequestSchema(schema.RequestSchema):
    """RestartUEcVHost - 重启虚拟机v2.0"""

    fields = {
        "NodeId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class RestartUEcVHostResponseSchema(schema.ResponseSchema):
    """RestartUEcVHost - 重启虚拟机v2.0"""

    fields = {}


"""
API: StartUEcVHost

启动UEC虚拟机
"""


class StartUEcVHostRequestSchema(schema.RequestSchema):
    """StartUEcVHost - 启动UEC虚拟机"""

    fields = {
        "NodeId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class StartUEcVHostResponseSchema(schema.ResponseSchema):
    """StartUEcVHost - 启动UEC虚拟机"""

    fields = {}


"""
API: StopUEcVHost

停止UEC虚拟机
"""


class StopUEcVHostRequestSchema(schema.RequestSchema):
    """StopUEcVHost - 停止UEC虚拟机"""

    fields = {
        "NodeId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class StopUEcVHostResponseSchema(schema.ResponseSchema):
    """StopUEcVHost - 停止UEC虚拟机"""

    fields = {}


"""
API: UnBindUEcFirewall

解绑防火墙
"""


class UnBindUEcFirewallRequestSchema(schema.RequestSchema):
    """UnBindUEcFirewall - 解绑防火墙"""

    fields = {
        "FirewallId": fields.Str(required=True, dump_to="FirewallId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
    }


class UnBindUEcFirewallResponseSchema(schema.ResponseSchema):
    """UnBindUEcFirewall - 解绑防火墙"""

    fields = {}


"""
API: UpdateUEcFirewall

更新防火墙信息，新增和删除规则
"""


class UpdateUEcFirewallParamRuleSchema(schema.RequestSchema):
    """UpdateUEcFirewallParamRule -"""

    fields = {
        "Action": fields.Str(required=True, dump_to="Action"),
        "Port": fields.Str(required=True, dump_to="Port"),
        "Priority": fields.Str(required=True, dump_to="Priority"),
        "ProtocolType": fields.Str(required=True, dump_to="ProtocolType"),
        "Remark": fields.Str(required=True, dump_to="Remark"),
        "SrcIp": fields.Str(required=True, dump_to="SrcIp"),
    }


class UpdateUEcFirewallRequestSchema(schema.RequestSchema):
    """UpdateUEcFirewall - 更新防火墙信息，新增和删除规则"""

    fields = {
        "FirewallId": fields.Str(required=True, dump_to="FirewallId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Rule": fields.List(UpdateUEcFirewallParamRuleSchema()),
    }


class UpdateUEcFirewallResponseSchema(schema.ResponseSchema):
    """UpdateUEcFirewall - 更新防火墙信息，新增和删除规则"""

    fields = {}


"""
API: UpdateUEcFirewallAttribute

更新防火墙名称及描述
"""


class UpdateUEcFirewallAttributeRequestSchema(schema.RequestSchema):
    """UpdateUEcFirewallAttribute - 更新防火墙名称及描述"""

    fields = {
        "FirewallId": fields.Str(required=True, dump_to="FirewallId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
    }


class UpdateUEcFirewallAttributeResponseSchema(schema.ResponseSchema):
    """UpdateUEcFirewallAttribute - 更新防火墙名称及描述"""

    fields = {}


"""
API: UpdateUEcSubnet

更新子网信息
"""


class UpdateUEcSubnetRequestSchema(schema.RequestSchema):
    """UpdateUEcSubnet - 更新子网信息"""

    fields = {
        "Comment": fields.Str(required=False, dump_to="Comment"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "SubnetName": fields.Str(required=False, dump_to="SubnetName"),
    }


class UpdateUEcSubnetResponseSchema(schema.ResponseSchema):
    """UpdateUEcSubnet - 更新子网信息"""

    fields = {}
