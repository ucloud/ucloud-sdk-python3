from ucloud.core.typesystem import schema, fields


class ProjectListInfoSchema(schema.ResponseSchema):
    """ ProjectListInfo - 项目信息
    """

    fields = {
        "ResourceCount": fields.Int(required=True, load_from="ResourceCount"),
        "MemberCount": fields.Int(required=True, load_from="MemberCount"),
        "ProjectId": fields.Str(required=True, load_from="ProjectId"),
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
        "ParentId": fields.Str(required=True, load_from="ParentId"),
        "ParentName": fields.Str(required=True, load_from="ParentName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
    }


class RegionInfoSchema(schema.ResponseSchema):
    """ RegionInfo - 数据中心信息
    """

    fields = {
        "RegionName": fields.Str(required=True, load_from="RegionName"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "BitMaps": fields.Str(required=True, load_from="BitMaps"),
        "Region": fields.Str(required=True, load_from="Region"),
        "Zone": fields.Str(required=True, load_from="Zone"),
        "RegionId": fields.Int(required=True, load_from="RegionId"),
    }


class UserInfoSchema(schema.ResponseSchema):
    """ UserInfo - 用户信息
    """

    fields = {
        "UserAddress": fields.Str(required=True, load_from="UserAddress"),
        "Admin": fields.Int(required=True, load_from="Admin"),
        "Finance": fields.Int(required=True, load_from="Finance"),
        "City": fields.Str(required=True, load_from="City"),
        "UserVersion": fields.Int(required=True, load_from="UserVersion"),
        "Administrator": fields.Str(required=True, load_from="Administrator"),
        "UserName": fields.Str(required=True, load_from="UserName"),
        "UserEmail": fields.Str(required=True, load_from="UserEmail"),
        "PhonePrefix": fields.Str(required=True, load_from="PhonePrefix"),
        "IndustryType": fields.Int(required=True, load_from="IndustryType"),
        "Province": fields.Str(required=True, load_from="Province"),
        "AuthState": fields.Str(required=True, load_from="AuthState"),
        "UserId": fields.Int(required=True, load_from="UserId"),
        "UserType": fields.Int(required=True, load_from="UserType"),
        "CompanyName": fields.Str(required=True, load_from="CompanyName"),
        "UserPhone": fields.Str(required=True, load_from="UserPhone"),
    }
