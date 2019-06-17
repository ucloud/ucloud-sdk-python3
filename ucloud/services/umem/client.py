import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.umem.schemas import apis


class UMemClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(UMemClient, self).__init__(config, transport)

    def delete_umem_space(self, req: dict = None) -> dict:
        """ DeleteUMemSpace - 删除UMem内存空间

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SpaceId: (Required) UMem内存空间ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUMemSpaceRequestSchema().dumps(d)
        resp = self.invoke("DeleteUMemSpace", d)
        return apis.DeleteUMemSpaceResponseSchema().loads(resp)

    def delete_uredis_group(self, req: dict = None) -> dict:
        """ DeleteURedisGroup - 删除主备redis

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 组ID
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteURedisGroupRequestSchema().dumps(d)
        resp = self.invoke("DeleteURedisGroup", d)
        return apis.DeleteURedisGroupResponseSchema().loads(resp)

    def describe_umem_cache_group(self, req: dict = None) -> dict:
        """ DescribeUMemcacheGroup - 显示Memcache

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Optional) 组的ID,如果指定则获取描述，否则为列表操 作,需指定Offset/Limit
        :param Limit: (Optional) 分页显示的条目数, 默认值为20
        :param Offset: (Optional) 分页显示的起始偏移, 默认值为0
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemcacheGroupRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemcacheGroup", d)
        return apis.DescribeUMemcacheGroupResponseSchema().loads(resp)

    def describe_umem_cache_price(self, req: dict = None) -> dict:
        """ DescribeUMemcachePrice - 获取umemcache组价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 容量大小,单位:GB 取值范围[1-32]
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) 计费模式，Year， Month， Dynamic，默认: Dynamic 默认: 获取所有计费模式的价格
        :param Quantity: (Optional) 购买umemcache的时长，默认值为1
        :param Type: (Optional) 空间类型:single(无热备),double(热备)(默认: double)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemcachePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemcachePrice", d)
        return apis.DescribeUMemcachePriceResponseSchema().loads(resp)

    def describe_uredis_backup_url(self, req: dict = None) -> dict:
        """ DescribeURedisBackupURL - 获取主备Redis备份下载链接

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param BackupId: (Required) 备份ID
        :param GroupId: (Required) 
        :param RegionFlag: (Optional) 是否是跨机房URedis(默认false)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisBackupURLRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisBackupURL", d)
        return apis.DescribeURedisBackupURLResponseSchema().loads(resp)

    def resize_uredis_group(self, req: dict = None) -> dict:
        """ ResizeURedisGroup - 调整主备redis容量

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 组ID
        :param Size: (Required) 内存大小, 单位:GB (需要大于原size,且小于等于32) 目前仅支持1/2/4/8/16/32 G 六种容量规格
        :param ChargeType: (Optional) 
        :param CouponId: (Optional) 代金券ID 请参考DescribeCoupon接口
        :param Type: (Optional) 空间类型:single(无热备),double(热备)(默认: double)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeURedisGroupRequestSchema().dumps(d)
        resp = self.invoke("ResizeURedisGroup", d)
        return apis.ResizeURedisGroupResponseSchema().loads(resp)

    def create_umem_space(self, req: dict = None) -> dict:
        """ CreateUMemSpace - 创建UMem内存空间

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 空间名称,长度(6<=size<=63)
        :param Size: (Required) 内存大小, 单位:GB, 范围[1~1024]
        :param ChargeType: (Optional) Year , Month, Dynamic, Trial 默认: Month
        :param CouponId: (Optional) 使用的代金券id
        :param Password: (Optional) URedis密码。请遵照[[api:uhost-api:specification|字段规范]]设定密码。密码需使用base64进行编码，举例如下：# echo -n Password1 | base64UGFzc3dvcmQx。
        :param Protocol: (Optional) 协议:memcache, redis (默认redis).注意:redis无single类型
        :param Quantity: (Optional) 购买时长 默认: 1
        :param SubnetId: (Optional) 
        :param Tag: (Optional) 
        :param Type: (Optional) 空间类型:single(无热备),double(热备)(默认: double)
        :param VPCId: (Optional) 
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUMemSpaceRequestSchema().dumps(d)
        resp = self.invoke("CreateUMemSpace", d)
        return apis.CreateUMemSpaceResponseSchema().loads(resp)

    def create_umem_cache_group(self, req: dict = None) -> dict:
        """ CreateUMemcacheGroup - 创建单机Memcache

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 请求创建组的名称 范围[6-60]
        :param ChargeType: (Optional) 计费模式，Year , Month, Dynamic 默认: Month
        :param ConfigId: (Optional) 配置ID,目前仅支持默认配置id 默认配置id:"9a891891-c245-4b66-bce8-67e59430d67c"
        :param CouponId: (Optional) 代金券ID
        :param Protocol: (Optional) 
        :param Quantity: (Optional) 购买时长，默认为1
        :param Size: (Optional) 每个节点的内存大小,单位GB,默认1GB 目前仅支持1/2/4/8/16/32这几档
        :param SubnetId: (Optional) 
        :param Tag: (Optional) 业务组 默认：Default
        :param VPCId: (Optional) 
        :param Version: (Optional) Memcache版本信息,默认为1.4.31
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUMemcacheGroupRequestSchema().dumps(d)
        resp = self.invoke("CreateUMemcacheGroup", d)
        return apis.CreateUMemcacheGroupResponseSchema().loads(resp)

    def modify_uredis_group_name(self, req: dict = None) -> dict:
        """ ModifyURedisGroupName - 修改主备redis名称

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 组的ID
        :param Name: (Required) Redis组名称 (范围[6-63],只能包含英文、数字以及符号-和_)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyURedisGroupNameRequestSchema().dumps(d)
        resp = self.invoke("ModifyURedisGroupName", d)
        return apis.ModifyURedisGroupNameResponseSchema().loads(resp)

    def resize_umem_space(self, req: dict = None) -> dict:
        """ ResizeUMemSpace - 调整内存空间容量

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 内存大小, 单位:GB (需要大于原size,<= 1024)
        :param SpaceId: (Required) UMem 内存空间Id
        :param ChargeType: (Optional) 
        :param CouponId: (Optional) 使用的代金券Id
        :param Type: (Optional) 空间类型:single(无热备),double(热备)(默认: double)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUMemSpaceRequestSchema().dumps(d)
        resp = self.invoke("ResizeUMemSpace", d)
        return apis.ResizeUMemSpaceResponseSchema().loads(resp)

    def restart_umem_cache_group(self, req: dict = None) -> dict:
        """ RestartUMemcacheGroup - 重启单机Memcache

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 组的ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RestartUMemcacheGroupRequestSchema().dumps(d)
        resp = self.invoke("RestartUMemcacheGroup", d)
        return apis.RestartUMemcacheGroupResponseSchema().loads(resp)

    def describe_uredis_price(self, req: dict = None) -> dict:
        """ DescribeURedisPrice - 取uredis价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 量大小,单位:GB  取值范围[1-32]
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) 计费模式，Year， Month， Dynamic；如果不指定，则一次性获取三种计费
        :param ProductType: (Optional) 产品类型：MS_Redis（标准主备版），S_Redis（从库），默认为MS_Redis
        :param Quantity: (Optional) 计费模式为Dynamic时，购买的时长, 默认为1
        :param RegionFlag: (Optional) 是否是跨机房URedis(默认false)
        :param Type: (Optional) 
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisPriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisPrice", d)
        return apis.DescribeURedisPriceResponseSchema().loads(resp)

    def get_umem_space_state(self, req: dict = None) -> dict:
        """ GetUMemSpaceState - 获取UMem内存空间列表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param SpaceId: (Required) 内存空间ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUMemSpaceStateRequestSchema().dumps(d)
        resp = self.invoke("GetUMemSpaceState", d)
        return apis.GetUMemSpaceStateResponseSchema().loads(resp)

    def describe_umem_upgrade_price(self, req: dict = None) -> dict:
        """ DescribeUMemUpgradePrice - 获取UMem升级价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 购买UMem大小,单位:GB
        :param SpaceId: (Required) 需要升级的空间的SpaceId
        :param Type: (Required) 空间类型:single(无热备),double(热备)(默认: double)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemUpgradePrice", d)
        return apis.DescribeUMemUpgradePriceResponseSchema().loads(resp)

    def describe_uredis_backup(self, req: dict = None) -> dict:
        """ DescribeURedisBackup - 查询主备redis备份

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Optional) 组的ID
        :param Limit: (Optional) 分页显示的条目数, 默认值为10
        :param Offset: (Optional) 分页显示的起始偏移, 默认值为0
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisBackupRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisBackup", d)
        return apis.DescribeURedisBackupResponseSchema().loads(resp)

    def modify_umem_space_name(self, req: dict = None) -> dict:
        """ ModifyUMemSpaceName - 修改UMem内存空间名称

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Name: (Required) 新的名称,长度(6<=size<=63)
        :param SpaceId: (Required) UMem内存空间ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUMemSpaceNameRequestSchema().dumps(d)
        resp = self.invoke("ModifyUMemSpaceName", d)
        return apis.ModifyUMemSpaceNameResponseSchema().loads(resp)

    def describe_umem_price(self, req: dict = None) -> dict:
        """ DescribeUMemPrice - 获取UMem实例价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 购买umem大小,单位:GB,范围[1~1024]
        :param Type: (Required) 空间类型:single(无热备),double(热备)(默认: double)
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param ChargeType: (Optional) Year， Month， Dynamic，Trial 如果不指定，则一次性获取三种计费
        :param Quantity: (Optional) 购买UMem的时长，默认值为1
        :param RegionFlag: (Optional) 
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemPriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemPrice", d)
        return apis.DescribeUMemPriceResponseSchema().loads(resp)

    def describe_umem_space(self, req: dict = None) -> dict:
        """ DescribeUMemSpace - 获取UMem内存空间列表

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Limit: (Optional) 返回数据长度, 默认为20
        :param Offset: (Optional) 数据偏移量, 默认为0
        :param SpaceId: (Optional) 内存空间ID (无ID，则获取所有)
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemSpaceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemSpace", d)
        return apis.DescribeUMemSpaceResponseSchema().loads(resp)

    def describe_umem_cache_upgrade_price(self, req: dict = None) -> dict:
        """ DescribeUMemcacheUpgradePrice - 获取umemcache升级价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 需要升级的空间的GroupId,请参考DescribeUMemcacheGroup接口
        :param Size: (Required) 购买umemcache大小,单位:GB
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemcacheUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemcacheUpgradePrice", d)
        return apis.DescribeUMemcacheUpgradePriceResponseSchema().loads(resp)

    def describe_uredis_group(self, req: dict = None) -> dict:
        """ DescribeURedisGroup - 查询主备Redis

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Optional) 组的ID,如果指定则获取描述，否则为列表操 作,需指定Offset/Limit
        :param Limit: (Optional) 分页显示的条目数, 默认值为20
        :param Offset: (Optional) 分页显示的起始偏移, 默认值为0
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisGroupRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisGroup", d)
        return apis.DescribeURedisGroupResponseSchema().loads(resp)

    def describe_uredis_upgrade_price(self, req: dict = None) -> dict:
        """ DescribeURedisUpgradePrice - 获取uredis升级价格信息

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 要升级的空间的GroupId,请参考DescribeURedisGroup接口
        :param Size: (Required) 购买uredis大小,单位:GB,范围是[1-32]
        :param Type: (Optional) 
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisUpgradePrice", d)
        return apis.DescribeURedisUpgradePriceResponseSchema().loads(resp)

    def resize_udredis_space(self, req: dict = None) -> dict:
        """ ResizeUDredisSpace - 调整内存空间容量

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param Size: (Required) 内存大小, 单位:GB (需要大于原size,<= 1024)
        :param SpaceId: (Required) 高性能UMem 内存空间Id
        :param CouponId: (Optional) 使用的代金券Id
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUDredisSpaceRequestSchema().dumps(d)
        resp = self.invoke("ResizeUDredisSpace", d)
        return apis.ResizeUDredisSpaceResponseSchema().loads(resp)

    def create_uredis_group(self, req: dict = None) -> dict:
        """ CreateURedisGroup - 创建主备redis

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param HighAvailability: (Required) 是否开启高可用,enable或disable
        :param Name: (Required) 请求创建组的名称 (范围[6-63],只能包含英文、数字以及符号-和_)
        :param Zone: (Required) 可用区。参见 [可用区列表](../summary/regionlist.html)
        :param AutoBackup: (Optional) 是否自动备份,enable或disable，默认disable
        :param BackupId: (Optional) 有此项代表从备份中创建，无代表正常创建
        :param BackupTime: (Optional) 自动备份开始时间,范围[0-23],默认3点
        :param ChargeType: (Optional) 计费模式，Year , Month, Dynamic 默认: Month
        :param ConfigId: (Optional) 配置ID,目前仅支持默认配置id 默认配置id:"03f58ca9-b64d-4bdd-abc7-c6b9a46fd801"，如果从备份创建，为必填项。
        :param CouponId: (Optional) 代金券ID
        :param MasterGroupId: (Optional) Master Redis Group的ID，创建只读Slave时，必须填写
        :param Password: (Optional) 初始化密码,需要 base64 编码
        :param Quantity: (Optional) 购买时长，默认为1
        :param Size: (Optional) 每个节点的内存大小,单位GB,默认1GB,目前仅支持1/2/4/8/16/32,六种
        :param SlaveZone: (Optional) 跨机房URedis，slave所在可用区（必须和Zone在同一Region，且不可相同）
        :param SubnetId: (Optional) 
        :param Tag: (Optional) 业务组名称
        :param VPCId: (Optional) 
        :param Version: (Optional) Redis版本信息(详见DescribeURedisVersion返回结果),默认版本3.0
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateURedisGroupRequestSchema().dumps(d)
        resp = self.invoke("CreateURedisGroup", d)
        return apis.CreateURedisGroupResponseSchema().loads(resp)

    def delete_umem_cache_group(self, req: dict = None) -> dict:
        """ DeleteUMemcacheGroup - 删除单机Memcache

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param Region: (Config) 地域。 参见 [地域和可用区列表](../summary/regionlist.html)
        :param GroupId: (Required) 组ID
        :param Zone: (Optional) 可用区。参见 [可用区列表](../summary/regionlist.html)
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUMemcacheGroupRequestSchema().dumps(d)
        resp = self.invoke("DeleteUMemcacheGroup", d)
        return apis.DeleteUMemcacheGroupResponseSchema().loads(resp)
