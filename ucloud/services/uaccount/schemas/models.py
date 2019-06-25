from ucloud.core.typesystem import schema, fields


class ProjectListInfoSchema(schema.ResponseSchema):
    """ ProjectListInfo - 项目信息
    """

    fields = {
        "ParentId": fields.Str(required=True, load_from="ParentId"),
        "ParentName": fields.Str(required=True, load_from="ParentName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "ResourceCount": fields.Int(required=True, load_from="ResourceCount"),
        "MemberCount": fields.Int(required=True, load_from="MemberCount"),
        "ProjectId": fields.Str(required=True, load_from="ProjectId"),
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
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
        "UserType": fields.Int(required=True, load_from="UserType"),
        "City": fields.Str(required=True, load_from="City"),
        "UserVersion": fields.Int(required=True, load_from="UserVersion"),
        "AuthState": fields.Str(required=True, load_from="AuthState"),
        "UserEmail": fields.Str(required=True, load_from="UserEmail"),
        "UserPhone": fields.Str(required=True, load_from="UserPhone"),
        "PhonePrefix": fields.Str(required=True, load_from="PhonePrefix"),
        "UserName": fields.Str(required=True, load_from="UserName"),
        "CompanyName": fields.Str(required=True, load_from="CompanyName"),
        "Admin": fields.Int(required=True, load_from="Admin"),
        "Administrator": fields.Str(required=True, load_from="Administrator"),
        "UserId": fields.Int(required=True, load_from="UserId"),
        "IndustryType": fields.Int(required=True, load_from="IndustryType"),
        "Province": fields.Str(required=True, load_from="Province"),
        "UserAddress": fields.Str(required=True, load_from="UserAddress"),
        "Finance": fields.Int(required=True, load_from="Finance"),
    }
