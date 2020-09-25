""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class TagSetSchema(schema.ResponseSchema):
    """TagSet - Tag详细信息"""

    fields = {
        "TagName": fields.Str(required=True, load_from="TagName"),
        "UpdateTime": fields.Str(required=True, load_from="UpdateTime"),
    }


class RepoSetSchema(schema.ResponseSchema):
    """RepoSet - 镜像仓库"""

    fields = {
        "CreateTime": fields.Str(required=True, load_from="CreateTime"),
        "Description": fields.Str(required=True, load_from="Description"),
        "IsOutSide": fields.Str(required=True, load_from="IsOutSide"),
        "IsShared": fields.Str(required=True, load_from="IsShared"),
        "RepoName": fields.Str(required=True, load_from="RepoName"),
        "UpdateTime": fields.Str(required=True, load_from="UpdateTime"),
    }


class ImageSetSchema(schema.ResponseSchema):
    """ImageSet - 镜像信息"""

    fields = {
        "CreateTime": fields.Str(required=True, load_from="CreateTime"),
        "ImageName": fields.Str(required=True, load_from="ImageName"),
        "LatestTag": fields.Str(required=True, load_from="LatestTag"),
        "PullCount": fields.Int(required=True, load_from="PullCount"),
        "RepoName": fields.Str(required=True, load_from="RepoName"),
        "UpdateTime": fields.Str(required=True, load_from="UpdateTime"),
    }
