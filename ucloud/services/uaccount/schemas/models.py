from ucloud.core.typesystem import schema, fields


class UserInfoSchema(schema.ResponseSchema):
    """ UserInfo - 用户信息
    """

    fields = {
        "UserId": fields.Int(required=True, load_from="UserId"),
        "UserType": fields.Int(required=True, load_from="UserType"),
        "City": fields.Str(required=True, load_from="City"),
        "UserVersion": fields.Int(required=True, load_from="UserVersion"),
        "AuthState": fields.Str(required=True, load_from="AuthState"),
        "UserEmail": fields.Str(required=True, load_from="UserEmail"),
        "CompanyName": fields.Str(required=True, load_from="CompanyName"),
        "IndustryType": fields.Int(required=True, load_from="IndustryType"),
        "Admin": fields.Int(required=True, load_from="Admin"),
        "Administrator": fields.Str(required=True, load_from="Administrator"),
        "UserPhone": fields.Str(required=True, load_from="UserPhone"),
        "PhonePrefix": fields.Str(required=True, load_from="PhonePrefix"),
        "UserAddress": fields.Str(required=True, load_from="UserAddress"),
        "UserName": fields.Str(required=True, load_from="UserName"),
        "Province": fields.Str(required=True, load_from="Province"),
        "Finance": fields.Int(required=True, load_from="Finance"),
    }


class ProjectListInfoSchema(schema.ResponseSchema):
    """ ProjectListInfo - 项目信息
    """

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "ResourceCount": fields.Int(required=True, load_from="ResourceCount"),
        "MemberCount": fields.Int(required=True, load_from="MemberCount"),
        "ProjectId": fields.Str(required=True, load_from="ProjectId"),
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
        "ParentId": fields.Str(required=True, load_from="ParentId"),
        "ParentName": fields.Str(required=True, load_from="ParentName"),
    }


class RegionInfoSchema(schema.ResponseSchema):
    """ RegionInfo - 数据中心信息
    """

    fields = {
        "RegionId": fields.Int(required=True, load_from="RegionId"),
        "RegionName": fields.Str(required=True, load_from="RegionName"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "BitMaps": fields.Str(required=True, load_from="BitMaps"),
        "Region": fields.Str(required=True, load_from="Region"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }
