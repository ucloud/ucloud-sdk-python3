from ucloud.core.typesystem import schema, fields


class ProjectListInfoSchema(schema.ResponseSchema):
    """ ProjectListInfo - 项目信息
    """

    fields = {
        "ProjectId": fields.Str(required=True, load_from="ProjectId"),
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
        "ParentId": fields.Str(required=True, load_from="ParentId"),
        "ParentName": fields.Str(required=True, load_from="ParentName"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "ResourceCount": fields.Int(required=True, load_from="ResourceCount"),
        "MemberCount": fields.Int(required=True, load_from="MemberCount"),
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
        "Finance": fields.Int(required=True, load_from="Finance"),
        "UserType": fields.Int(required=True, load_from="UserType"),
        "UserName": fields.Str(required=True, load_from="UserName"),
        "UserVersion": fields.Int(required=True, load_from="UserVersion"),
        "UserId": fields.Int(required=True, load_from="UserId"),
        "UserPhone": fields.Str(required=True, load_from="UserPhone"),
        "City": fields.Str(required=True, load_from="City"),
        "IndustryType": fields.Int(required=True, load_from="IndustryType"),
        "Province": fields.Str(required=True, load_from="Province"),
        "UserAddress": fields.Str(required=True, load_from="UserAddress"),
        "Administrator": fields.Str(required=True, load_from="Administrator"),
        "AuthState": fields.Str(required=True, load_from="AuthState"),
        "UserEmail": fields.Str(required=True, load_from="UserEmail"),
        "PhonePrefix": fields.Str(required=True, load_from="PhonePrefix"),
        "CompanyName": fields.Str(required=True, load_from="CompanyName"),
        "Admin": fields.Int(required=True, load_from="Admin"),
    }
