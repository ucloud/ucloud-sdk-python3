""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class AccessKeySchema(schema.ResponseSchema):
    """AccessKey - 密钥信息实例"""

    fields = {
        "AccessKeyID": fields.Str(required=False, load_from="AccessKeyID"),
        "AccessKeySecret": fields.Str(
            required=False, load_from="AccessKeySecret"
        ),
        "CreatedAt": fields.Int(required=False, load_from="CreatedAt"),
        "DeletedAt": fields.Int(required=False, load_from="DeletedAt"),
        "Description": fields.Str(required=False, load_from="Description"),
        "ExpiredAt": fields.Int(required=False, load_from="ExpiredAt"),
        "Status": fields.Str(required=False, load_from="Status"),
        "UpdatedAt": fields.Int(required=False, load_from="UpdatedAt"),
        "UserId": fields.Int(required=False, load_from="UserId"),
    }


class GroupSchema(schema.ResponseSchema):
    """Group - 用户组模型"""

    fields = {
        "CreatedAt": fields.Int(required=False, load_from="CreatedAt"),
        "Description": fields.Str(required=True, load_from="Description"),
        "GroupName": fields.Str(required=True, load_from="GroupName"),
    }


class IAMPolicySchema(schema.ResponseSchema):
    """IAMPolicy - 获取IAM权限策略详情"""

    fields = {
        "CreatedAt": fields.Int(required=False, load_from="CreatedAt"),
        "Description": fields.Str(required=False, load_from="Description"),
        "Document": fields.Str(required=False, load_from="Document"),
        "PolicyName": fields.Str(required=False, load_from="PolicyName"),
        "PolicyURN": fields.Str(required=False, load_from="PolicyURN"),
        "ScopeType": fields.Str(required=False, load_from="ScopeType"),
        "UpdatedAt": fields.Int(required=False, load_from="UpdatedAt"),
    }


class LoginProfileSchema(schema.ResponseSchema):
    """LoginProfile - 登录资料"""

    fields = {
        "MFABindRequired": fields.Bool(
            required=True, load_from="MFABindRequired"
        ),
        "MaxPasswordAge": fields.Int(required=True, load_from="MaxPasswordAge"),
        "Status": fields.Str(required=True, load_from="Status"),
    }


class UserSchema(schema.ResponseSchema):
    """User - 用户模型"""

    fields = {
        "CreatedAt": fields.Int(required=False, load_from="CreatedAt"),
        "DisplayName": fields.Str(required=False, load_from="DisplayName"),
        "Email": fields.Str(required=True, load_from="Email"),
        "Status": fields.Str(required=False, load_from="Status"),
        "UserName": fields.Str(required=True, load_from="UserName"),
    }


class EntitySchema(schema.ResponseSchema):
    """Entity - 权限策略的实体"""

    fields = {
        "AttachedAt": fields.Int(required=True, load_from="AttachedAt"),
        "EntityKind": fields.Str(required=True, load_from="EntityKind"),
        "EntityName": fields.Str(required=True, load_from="EntityName"),
    }


class PolicySchema(schema.ResponseSchema):
    """Policy - 权限策略"""

    fields = {
        "AttachedAt": fields.Int(required=False, load_from="AttachedAt"),
        "CreatedAt": fields.Int(required=False, load_from="CreatedAt"),
        "Description": fields.Str(required=False, load_from="Description"),
        "PolicyName": fields.Str(required=True, load_from="PolicyName"),
        "PolicyURN": fields.Str(required=True, load_from="PolicyURN"),
        "ProjectID": fields.Str(required=False, load_from="ProjectID"),
        "Scope": fields.Str(required=False, load_from="Scope"),
    }


class ProjectSchema(schema.ResponseSchema):
    """Project - 项目模型"""

    fields = {
        "CreatedAt": fields.Int(required=True, load_from="CreatedAt"),
        "ProjectID": fields.Str(required=True, load_from="ProjectID"),
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
        "UserCount": fields.Int(required=True, load_from="UserCount"),
    }


class UsersSchema(schema.ResponseSchema):
    """Users - 用户模型"""

    fields = {
        "CreatedAt": fields.Int(required=False, load_from="CreatedAt"),
        "DisplayName": fields.Str(required=False, load_from="DisplayName"),
        "Email": fields.Str(required=True, load_from="Email"),
        "Status": fields.Str(required=False, load_from="Status"),
        "UserName": fields.Str(required=True, load_from="UserName"),
    }


class UserForGroupSchema(schema.ResponseSchema):
    """UserForGroup - 用户模型"""

    fields = {
        "DisplayName": fields.Str(required=False, load_from="DisplayName"),
        "Email": fields.Str(required=True, load_from="Email"),
        "JoinedAt": fields.Int(required=False, load_from="JoinedAt"),
        "UserName": fields.Str(required=True, load_from="UserName"),
    }
