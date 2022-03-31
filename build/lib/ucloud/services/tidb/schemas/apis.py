""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.tidb.schemas import models

""" TiDB API Schema
"""


"""
API: CreateTiDBService

创建TiDB服务
"""


class CreateTiDBServiceRequestSchema(schema.RequestSchema):
    """CreateTiDBService - 创建TiDB服务"""

    fields = {
        "DTType": fields.Str(required=False, dump_to="DTType"),
        "Ip": fields.Str(required=False, dump_to="Ip"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Password": fields.Str(required=True, dump_to="Password"),
        "Port": fields.Str(required=False, dump_to="Port"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "TikvMemoryHardTh": fields.Str(
            required=False, dump_to="TikvMemoryHardTh"
        ),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class CreateTiDBServiceResponseSchema(schema.ResponseSchema):
    """CreateTiDBService - 创建TiDB服务"""

    fields = {
        "Data": models.ServiceIDSchema(),
        "Message": fields.Str(required=False, load_from="Message"),
        "ServiceId": fields.Str(required=False, load_from="ServiceId"),
    }


"""
API: DeleteTiDBService

删除一个服务
"""


class DeleteTiDBServiceRequestSchema(schema.RequestSchema):
    """DeleteTiDBService - 删除一个服务"""

    fields = {
        "Id": fields.Str(required=True, dump_to="Id"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DeleteTiDBServiceResponseSchema(schema.ResponseSchema):
    """DeleteTiDBService - 删除一个服务"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
        "ServiceId": fields.Str(required=False, load_from="ServiceId"),
    }


"""
API: SetTiDBConfig

设置TiDB服务实例参数
"""


class SetTiDBConfigParamConfigsSchema(schema.RequestSchema):
    """SetTiDBConfigParamConfigs -"""

    fields = {
        "Name": fields.Str(required=True, dump_to="Name"),
        "Value": fields.Str(required=True, dump_to="Value"),
    }


class SetTiDBConfigRequestSchema(schema.RequestSchema):
    """SetTiDBConfig - 设置TiDB服务实例参数"""

    fields = {
        "Configs": fields.List(SetTiDBConfigParamConfigsSchema()),
        "Id": fields.Str(required=True, dump_to="Id"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class SetTiDBConfigResponseSchema(schema.ResponseSchema):
    """SetTiDBConfig - 设置TiDB服务实例参数"""

    fields = {
        "ServiceId": fields.Str(required=False, load_from="ServiceId"),
    }
