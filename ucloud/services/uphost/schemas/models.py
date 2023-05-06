""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class PHostComponentSetSchema(schema.ResponseSchema):
    """PHostComponentSet - GetPHostTypeInfo"""

    fields = {
        "Count": fields.Int(required=False, load_from="Count"),
        "Name": fields.Str(required=False, load_from="Name"),
    }


class PHostClusterSetSchema(schema.ResponseSchema):
    """PHostClusterSet - 物理云主机集群库存信息"""

    fields = {
        "Name": fields.Str(required=False, load_from="Name"),
        "StockStatus": fields.Str(required=False, load_from="StockStatus"),
    }


class PHostCPUSetSchema(schema.ResponseSchema):
    """PHostCPUSet - DescribePHost"""

    fields = {
        "CoreCount": fields.Int(required=False, load_from="CoreCount"),
        "Count": fields.Int(required=False, load_from="Count"),
        "Frequence": fields.Float(required=False, load_from="Frequence"),
        "Model": fields.Str(required=False, load_from="Model"),
    }


class PHostCloudMachineTypeSetSchema(schema.ResponseSchema):
    """PHostCloudMachineTypeSet - 裸金属云盘的MachineTypeSet"""

    fields = {
        "CPU": PHostCPUSetSchema(),
        "Clusters": fields.List(PHostClusterSetSchema()),
        "Components": PHostComponentSetSchema(),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "Type": fields.Str(required=True, load_from="Type"),
    }


class PHostIPSetSchema(schema.ResponseSchema):
    """PHostIPSet - DescribePHost"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "IPAddr": fields.Str(required=False, load_from="IPAddr"),
        "IPId": fields.Str(required=False, load_from="IPId"),
        "MACAddr": fields.Str(required=False, load_from="MACAddr"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class PHostDescDiskSetSchema(schema.ResponseSchema):
    """PHostDescDiskSet - DescribePHost（包括传统和裸金属1、裸金属2）"""

    fields = {
        "Count": fields.Int(required=False, load_from="Count"),
        "DiskId": fields.Str(required=False, load_from="DiskId"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "IOCap": fields.Int(required=False, load_from="IOCap"),
        "IsBoot": fields.Str(required=False, load_from="IsBoot"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Space": fields.Int(required=False, load_from="Space"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class PHostSetSchema(schema.ResponseSchema):
    """PHostSet - DescribePHost"""

    fields = {
        "AutoRenew": fields.Str(required=False, load_from="AutoRenew"),
        "BootDiskState": fields.Str(required=False, load_from="BootDiskState"),
        "CPUSet": PHostCPUSetSchema(),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Cluster": fields.Str(required=False, load_from="Cluster"),
        "Components": fields.Str(required=False, load_from="Components"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskSet": fields.List(PHostDescDiskSetSchema()),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "IPSet": fields.List(PHostIPSetSchema()),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "IsSupportKVM": fields.Str(required=False, load_from="IsSupportKVM"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "Name": fields.Str(required=False, load_from="Name"),
        "OSType": fields.Str(required=False, load_from="OSType"),
        "OSname": fields.Str(required=False, load_from="OSname"),
        "PHostId": fields.Str(required=False, load_from="PHostId"),
        "PHostType": fields.Str(required=False, load_from="PHostType"),
        "PMStatus": fields.Str(required=False, load_from="PMStatus"),
        "PhostClass": fields.Str(required=False, load_from="PhostClass"),
        "PowerState": fields.Str(required=False, load_from="PowerState"),
        "RaidSupported": fields.Str(required=False, load_from="RaidSupported"),
        "RdmaClusterId": fields.Str(required=False, load_from="RdmaClusterId"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SN": fields.Str(required=False, load_from="SN"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class PHostImageSetSchema(schema.ResponseSchema):
    """PHostImageSet - DescribePHostImage"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ImageDescription": fields.Str(
            required=False, load_from="ImageDescription"
        ),
        "ImageId": fields.Str(required=False, load_from="ImageId"),
        "ImageName": fields.Str(required=False, load_from="ImageName"),
        "ImageSize": fields.Int(required=False, load_from="ImageSize"),
        "ImageType": fields.Str(required=False, load_from="ImageType"),
        "OsName": fields.Str(required=False, load_from="OsName"),
        "OsType": fields.Str(required=False, load_from="OsType"),
        "State": fields.Str(required=False, load_from="State"),
        "Support": fields.List(fields.Str()),
        "Version": fields.Str(required=False, load_from="Version"),
    }


class PHostDiskSetSchema(schema.ResponseSchema):
    """PHostDiskSet - GetPHostTypeInfo"""

    fields = {
        "Count": fields.Int(required=False, load_from="Count"),
        "IOCap": fields.Int(required=False, load_from="IOCap"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Space": fields.Int(required=False, load_from="Space"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class PHostMachineTypeSetSchema(schema.ResponseSchema):
    """PHostMachineTypeSet - 物理云主机机型列表"""

    fields = {
        "CPU": PHostCPUSetSchema(),
        "Clusters": fields.List(PHostClusterSetSchema()),
        "Components": PHostComponentSetSchema(),
        "Disks": fields.List(PHostDiskSetSchema()),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "RaidSupported": fields.Str(required=False, load_from="RaidSupported"),
        "Type": fields.Str(required=True, load_from="Type"),
    }


class PHostTagSetSchema(schema.ResponseSchema):
    """PHostTagSet - DescribePHostTags"""

    fields = {
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


class PHostPriceSetSchema(schema.ResponseSchema):
    """PHostPriceSet - GetPHostPrice"""

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "OriginalPrice": fields.Float(
            required=False, load_from="OriginalPrice"
        ),
        "Price": fields.Float(required=False, load_from="Price"),
        "Product": fields.Str(required=False, load_from="Product"),
    }
