from ucloud.core.typesystem import schema, fields


class ProjectListInfoSchema(schema.ResponseSchema):
    """ ProjectListInfo - 项目信息
    """

    fields = {
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
        "ParentId": fields.Str(required=True, load_from="ParentId"),
        "ParentName": fields.Str(required=True, load_from="ParentName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "ResourceCount": fields.Int(required=True, load_from="ResourceCount"),
        "MemberCount": fields.Int(required=True, load_from="MemberCount"),
        "ProjectId": fields.Str(required=True, load_from="ProjectId"),
    }


class RegionInfoSchema(schema.ResponseSchema):
    """ RegionInfo - 数据中心信息
    """

    fields = {
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "BitMaps": fields.Str(required=True, load_from="BitMaps"),
        "Region": fields.Str(required=True, load_from="Region"),
        "Zone": fields.Str(required=True, load_from="Zone"),
        "RegionId": fields.Int(required=True, load_from="RegionId"),
        "RegionName": fields.Str(required=True, load_from="RegionName"),
    }


class UserInfoSchema(schema.ResponseSchema):
    """ UserInfo - 用户信息
    """

    fields = {
        "IndustryType": fields.Int(required=True, load_from="IndustryType"),
        "Province": fields.Str(required=True, load_from="Province"),
        "AuthState": fields.Str(required=True, load_from="AuthState"),
        "UserId": fields.Int(required=True, load_from="UserId"),
        "UserEmail": fields.Str(required=True, load_from="UserEmail"),
        "UserPhone": fields.Str(required=True, load_from="UserPhone"),
        "PhonePrefix": fields.Str(required=True, load_from="PhonePrefix"),
        "CompanyName": fields.Str(required=True, load_from="CompanyName"),
        "UserAddress": fields.Str(required=True, load_from="UserAddress"),
        "Finance": fields.Int(required=True, load_from="Finance"),
        "UserType": fields.Int(required=True, load_from="UserType"),
        "City": fields.Str(required=True, load_from="City"),
        "UserName": fields.Str(required=True, load_from="UserName"),
        "Admin": fields.Int(required=True, load_from="Admin"),
        "UserVersion": fields.Int(required=True, load_from="UserVersion"),
        "Administrator": fields.Str(required=True, load_from="Administrator"),
    }
