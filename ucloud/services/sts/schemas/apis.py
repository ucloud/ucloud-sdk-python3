""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.sts.schemas import models

""" STS API Schema
"""


"""
API: AssumeRole

获取扮演角色的临时身份凭证
"""


class AssumeRoleRequestSchema(schema.RequestSchema):
    """AssumeRole - 获取扮演角色的临时身份凭证"""

    fields = {
        "DurationSeconds": fields.Int(
            required=False, dump_to="DurationSeconds"
        ),
        "Policy": fields.Str(required=False, dump_to="Policy"),
        "RoleSessionName": fields.Str(required=True, dump_to="RoleSessionName"),
        "RoleUrn": fields.Str(required=True, dump_to="RoleUrn"),
    }


class AssumeRoleResponseSchema(schema.ResponseSchema):
    """AssumeRole - 获取扮演角色的临时身份凭证"""

    fields = {
        "Credentials": models.CredentialsSchema(),
    }
