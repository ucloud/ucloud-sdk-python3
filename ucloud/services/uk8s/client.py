""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.uk8s.schemas import apis


class UK8SClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UK8SClient, self).__init__(config, transport, middleware, logger)

    def add_uk8s_existing_uhost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """AddUK8SExistingUHost - 将预先创建好的云主机加入到UK8S集群，需要注意的是，该云主机依然会执行重装系统的操作。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ClusterId** (str) - (Required) UK8S集群ID。 可从UK8S控制台获取。
        - **Password** (str) - (Required) Node节点密码。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定密码。密码需使用base64进行编码，如下：# echo -n Password1 | base64
        - **UHostId** (str) - (Required) 云主机Id，为了保证节点正常运行，该主机配置不得低于2C4G。
        - **DisableSchedule** (bool) - 用于标示添加完节点后是否将节点临时禁用. 传入 "true" 表示禁用,传入其它或不传表示不禁用
        - **ImageId** (str) - 镜像 Id，不填时后台程序会自动选用一个可用的镜像 Id，支持用户自定义镜像，自定义镜像必须基于基础镜像制作。
        - **InitScript** (str) - 用户自定义Shell脚本。与UserData的区别在于InitScript在节点初始化完毕后才执行，UserData则是云主机初始化时执行。
        - **Labels** (str) - Node节点标签。key=value形式,多组用”,“隔开，最多5组。 如env=pro,type=game
        - **MaxPods** (int) - 默认110，生产环境建议小于等于110。
        - **SubnetId** (str) - 该云主机所属子网Id。
        - **UserData** (str) - 用户自定义数据。当镜像支持Cloud-init Feature时可填写此字段。注意：1、总数据量大小不超过 16K；2、使用base64编码。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Message** (str) - 返回错误消息，当 RetCode 非 0 时提供详细的描述信息。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.AddUK8SExistingUHostRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AddUK8SExistingUHost", d, **kwargs)
        return apis.AddUK8SExistingUHostResponseSchema().loads(resp)

    def add_uk8s_phost_node(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """AddUK8SPHostNode - 为UK8S集群添加一台或多台物理云主机类型的节点。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ChargeType** (str) - (Required) 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ 默认为月付
        - **ClusterId** (str) - (Required) UK8S集群ID。 可从UK8S控制台获取。
        - **Count** (int) - (Required) 最大创建Node节点数量，取值范围是[1,10]。
        - **Password** (str) - (Required) Node节点密码。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定密码。密码需使用base64进行编码，如下：# echo -n Password1 | base64
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **DisableSchedule** (bool) - 用于标示添加完节点后是否将节点临时禁用. 传入 "true" 表示禁用,传入其它或不传表示不禁用
        - **ImageId** (str) - 镜像 Id，不填时后台程序会自动选用一个可用的镜像 Id，支持用户自定义镜像，自定义镜像必须基于基础镜像制作。
        - **InitScript** (str) - 用户自定义Shell脚本。与UserData的区别在于InitScript在节点初始化完毕后才执行。
        - **Labels** (str) - Node节点标签。key=value形式,多组用”,“隔开，最多5组。 如env=pro,type=game
        - **MaxPods** (int) - 默认110，生产环境建议小于等于110。
        - **NIC** (str) - 网络环境，可选千兆：1G ，万兆：10G， 默认1G。
        - **Quantity** (int) - 购买时长。默认: 1。月付时，此参数传0，代表了购买至月末。
        - **Raid** (str) - Raid配置，默认Raid10 支持:Raid0、Raid1、Raid5、Raid10，NoRaid
        - **SubnetId** (str) - 子网 ID。默认为集群创建时填写的子网ID，也可以填写集群同VPC内的子网ID。
        - **Type** (str) - 物理机类型，默认为：db-2(基础型-SAS-V3)

        **Response**

        - **Message** (str) - 返回错误消息，当 RetCode 非 0 时提供详细的描述信息。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.AddUK8SPHostNodeRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AddUK8SPHostNode", d, **kwargs)
        return apis.AddUK8SPHostNodeResponseSchema().loads(resp)

    def add_uk8s_uhost_node(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """AddUK8SUHostNode - 为UK8S集群添加一台Node节点，机型类型为云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CPU** (int) - (Required) 虚拟CPU核数。可选参数：2-64（具体机型与CPU的对应关系参照控制台）。默认值: 4。
        - **ChargeType** (str) - (Required) 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Dynamic，按小时预付费 \\ > Postpay，按小时后付费（支持关机不收费，目前仅部分可用区支持，请联系您的客户经理） \\ 默认为月付
        - **ClusterId** (str) - (Required) UK8S集群ID。 可从UK8S控制台获取。
        - **Count** (int) - (Required) 最大创建Node节点数量，取值范围是[1,10]。
        - **Mem** (int) - (Required) 内存大小。单位：MB。范围 ：[4096, 262144]，取值为1024的倍数（可选范围参考控制台）。默认值：8192
        - **Password** (str) - (Required) Node节点密码。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定密码。密码需使用base64进行编码，如下：# echo -n Password1 | base64
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **BootDiskType** (str) - 磁盘类型。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。默认为SSD云盘
        - **DataDiskSize** (str) - 数据磁盘大小，单位GB。默认0。范围 ：[20, 1000]
        - **DataDiskType** (str) - 磁盘类型。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。默认为SSD云盘
        - **DisableSchedule** (bool) - 用于标示添加完节点后是否将节点临时禁用. 传入 "true" 表示禁用,传入其它或不传表示不禁用
        - **GPU** (int) - GPU卡核心数。仅GPU机型支持此字段（可选范围与MachineType+GpuType相关）
        - **GpuType** (str) - GPU类型，枚举值["K80", "P40", "V100",]，MachineType为G时必填
        - **ImageId** (str) - 镜像 Id，不填时后台程序会自动选用一个可用的镜像 Id，支持用户自定义镜像，自定义镜像必须基于基础镜像制作。
        - **InitScript** (str) - 用户自定义Shell脚本。与UserData的区别在于InitScript在节点初始化完毕后才执行，UserData则是云主机初始化时执行。
        - **IsolationGroup** (str) - 硬件隔离组id。可通过DescribeIsolationGroup获取。
        - **Labels** (str) - Node节点标签。key=value形式,多组用”,“隔开，最多5组。 如env=pro,type=game
        - **MachineType** (str) - 云主机机型。枚举值["N", "C", "G", "O", "OS"]。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。
        - **MaxPods** (int) - 默认110，生产环境建议小于等于110。
        - **MinmalCpuPlatform** (str) - 最低cpu平台，枚举值["Intel/Auto", "Intel/IvyBridge", "Intel/Haswell", "Intel/Broadwell", "Intel/Skylake", "Intel/Cascadelake"；"Intel/CascadelakeR"; “Amd/Epyc2”,"Amd/Auto"],默认值是"Intel/Auto"
        - **Quantity** (int) - 购买时长。默认: 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表了购买至月末。
        - **SubnetId** (str) - 子网 ID。默认为集群创建时填写的子网ID，也可以填写集群同VPC内的子网ID。
        - **UserData** (str) - 用户自定义数据。当镜像支持Cloud-init Feature时可填写此字段。注意：1、总数据量大小不超过 16K；2、使用base64编码。

        **Response**

        - **Message** (str) - 返回错误消息，当 RetCode 非 0 时提供详细的描述信息。
        - **NodeIds** (list) - Node实例Id集合

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.AddUK8SUHostNodeRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AddUK8SUHostNode", d, **kwargs)
        return apis.AddUK8SUHostNodeResponseSchema().loads(resp)

    def create_uk8s_cluster_v2(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUK8SClusterV2 - 创建UK8S集群

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ClusterName** (str) - (Required) 集群名称
        - **MasterCPU** (int) - (Required) Master节点的虚拟CPU核数。可选参数：2-64（具体机型与CPU的对应关系参照控制台）。
        - **MasterMachineType** (str) - (Required) Master节点的云主机机型（V2.0），如["N", "C", "O", "OS"]，具体请参照云主机机型。
        - **MasterMem** (int) - (Required) Master节点的内存大小。单位：MB。范围 ：[4096, 262144]，取值为1024的倍数（可选范围参考控制台）。
        - **Password** (str) - (Required) 集群节点密码，包括Master和Node。密码需包含最少一个大写字母，请使用base64进行编码，举例如下：# echo -n Password1 | base64
        - **ServiceCIDR** (str) - (Required) Service 网段，用于分配ClusterIP，如172.17.0.0/16。该网段不能与集群所属VPC网段重叠。
        - **SubnetId** (str) - (Required) 集群Node及Pod所属子网
        - **VPCId** (str) - (Required) 集群Node及Pod所属VPC
        - **ChargeType** (str) - 集群所有节点的付费模式。枚举值为： Year，按年付费； Month，按月付费； Dynamic，按小时付费（需开启权限），默认按月。
        - **ExternalApiServer** (str) - 是否允许外网访问apiserver，开启：Yes 不开启：No。默认为No。
        - **ImageId** (str) - Master节点和Node节点的镜像 ID，不填则随机选择可用的基础镜像。支持用户自定义镜像。
        - **InitScript** (str) - 用户自定义脚本，与UserData不同，自定义脚本将在集群安装完毕后执行。注意：1、总数据量大小不超多16K；2、使用base64编码。
        - **K8sVersion** (str) - k8s集群的版本，版本信息请参考UK8S集群创建页，不指定的话默认为当前支持的最高版本。
        - **KubeProxy** (dict) - 见 **CreateUK8SClusterV2ParamKubeProxy** 模型定义
        - **Master** (list) - 见 **CreateUK8SClusterV2ParamMaster** 模型定义
        - **MasterBootDiskType** (str) - Master节点系统盘类型。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。默认为SSD云盘
        - **MasterDataDiskSize** (int) - Master节点的数据盘大小，单位GB，默认为0。范围 ：[20, 1000]
        - **MasterDataDiskType** (str) - Master节点数据盘类型。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。默认为SSD云盘
        - **MasterIsolationGroup** (str) - 【无效，已删除】当前将自动为Master节点创建隔离组，确保Master节点归属于不同物理机。
        - **MasterMinmalCpuPlatform** (str) - Master节点的最低cpu平台，不选则随机。枚举值["Intel/Auto", "Intel/IvyBridge", "Intel/Haswell", "Intel/Broadwell", "Intel/Skylake", "Intel/Cascadelake"。
        - **Nodes** (list) - 见 **CreateUK8SClusterV2ParamNodes** 模型定义
        - **Quantity** (int) - 购买时长。默认为1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表了购买至月末。
        - **UserData** (str) - 用户自定义数据。注意：1、总数据量大小不超多16K；2、使用base64编码。

        **Response**

        - **ClusterId** (str) - 集群ID

        **Request Model**

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUK8SClusterV2RequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUK8SClusterV2", d, **kwargs)
        return apis.CreateUK8SClusterV2ResponseSchema().loads(resp)

    def del_uk8s_cluster(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DelUK8SCluster - 删除UK8S集群

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ClusterId** (str) - (Required) 集群id
        - **ReleaseUDisk** (bool) - 是否删除节点挂载的数据盘。枚举值[true:删除，false: 不删除]，默认不删除

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DelUK8SClusterRequestSchema().dumps(d)

        resp = self.invoke("DelUK8SCluster", d, **kwargs)
        return apis.DelUK8SClusterResponseSchema().loads(resp)

    def del_uk8s_cluster_node_v2(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DelUK8SClusterNodeV2 - 删除集群中的Node节点，删除前务必先将其中的Pod驱逐。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ClusterId** (str) - (Required) UK8S集群ID。 可从UK8S控制台获取。
        - **NodeId** (str) - (Required) Node在UK8S处的唯一标示，如uk8s-reewqe5-sdasadsda。**非云主机或物理云主机资源Id**
        - **ReleaseDataUDisk** (bool) - 删除节点时是否释放数据盘。 枚举值[true:释放，false: 不释放]，默认为true。

        **Response**

        - **Message** (str) - 返回错误消息，当 RetCode 非 0 时提供详细的描述信息。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DelUK8SClusterNodeV2RequestSchema().dumps(d)

        resp = self.invoke("DelUK8SClusterNodeV2", d, **kwargs)
        return apis.DelUK8SClusterNodeV2ResponseSchema().loads(resp)

    def describe_uk8s_image(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUK8SImage - 获取UK8S支持的Node节点操作系统，可基于该操作系统制定自定义镜像

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **ImageSet** (list) - 见 **ImageInfo** 模型定义
        - **Message** (str) - 返回错误消息，当 RetCode 非 0 时提供详细的描述信息。
        - **PHostImageSet** (list) - 见 **ImageInfo** 模型定义

        **Response Model**

        **ImageInfo**

        - **ImageId** (str) - 镜像 Id
        - **ImageName** (str) - 镜像名称
        - **NotSupportGPU** (bool) - 该镜像是否支持GPU机型，枚举值[true:不支持，false:支持]。
        - **ZoneId** (int) - 可用区 Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUK8SImageRequestSchema().dumps(d)

        resp = self.invoke("DescribeUK8SImage", d, **kwargs)
        return apis.DescribeUK8SImageResponseSchema().loads(resp)

    def list_uk8s_cluster_node_v2(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUK8SClusterNodeV2 - 获取UK8S集群节点信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ClusterId** (str) - (Required) UK8S集群ID

        **Response**

        - **NodeSet** (list) - 见 **NodeInfoV2** 模型定义
        - **TotalCount** (int) - 满足条件的节点数量，包括Master。

        **Response Model**

        **UHostIPSet**

        - **Bandwidth** (int) - IP对应的带宽, 单位: Mb (内网IP不显示带宽信息)
        - **Default** (str) - 是否默认的弹性网卡的信息。true: 是默认弹性网卡；其他值：不是。
        - **IP** (str) - IP地址
        - **IPId** (str) - IP资源ID (内网IP无对应的资源ID)
        - **Mac** (str) - Mac地址
        - **SubnetId** (str) - IP地址对应的子网 ID
        - **Type** (str) - 国际: Internation，BGP: Bgp，内网: Private
        - **VPCId** (str) - IP地址对应的VPC ID

        **KubeProxy**

        - **Mode** (str) - KubeProxy模式，枚举值为[ipvs,iptables]

        **NodeInfoV2**

        - **AsgId** (str) - 节点所属伸缩组ID，非伸缩组创建出来的节点，伸缩组ID为Default。
        - **CPU** (int) - Node节点CPU核数，单位: 个。
        - **CreateTime** (int) - 节点创建时间
        - **ExpireTime** (int) - 节点计费到期时间
        - **GPU** (int) - 节点的GPU颗数。
        - **IPSet** (list) - 见 **UHostIPSet** 模型定义
        - **InstanceId** (str) - 资源ID，如uhost-xxxx，或uphost-xxxxx。
        - **InstanceName** (str) - 资源名称，初始值等于NodeId，用户可在UHost或UPHost处修改。
        - **InstanceType** (str) - Node节点的资源类型，枚举值为UHost或UPHost。
        - **KubeProxy** (dict) - 见 **KubeProxy** 模型定义
        - **MachineType** (str) - 机型类别，分别对应Uhost的MachineType或PHost的PHostType。
        - **Memory** (int) - 内存大小，单位: MB。
        - **NodeId** (str) - NodeId，Node在UK8S处的唯一标示，如uk8s-reewqe5-sdasadsda
        - **NodeRole** (str) - node角色，枚举值为master、node
        - **NodeStatus** (str) - Node的状态
        - **OsName** (str) - Node节点的镜像名称。
        - **OsType** (str) - Node节点的操作系统类别，如Linux或Windows。
        - **Unschedulable** (bool) - 是否允许Pod调度到该节点，枚举值为true或false。
        - **Zone** (str) - Node所在可用区

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUK8SClusterNodeV2RequestSchema().dumps(d)

        resp = self.invoke("ListUK8SClusterNodeV2", d, **kwargs)
        return apis.ListUK8SClusterNodeV2ResponseSchema().loads(resp)

    def list_uk8s_cluster_v2(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUK8SClusterV2 - 获取UK8S集群列表信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ClusterId** (str) - UK8S集群ID
        - **Limit** (int) - 返回数据长度，默认为20。
        - **Offset** (int) - 列表起始位置偏移量，默认为0。

        **Response**

        - **ClusterCount** (int) - 满足条件的集群数量
        - **ClusterSet** (list) - 见 **ClusterSet** 模型定义

        **Response Model**

        **ClusterSet**

        - **ApiServer** (str) - 集群apiserver地址
        - **ClusterId** (str) - 集群ID
        - **ClusterName** (str) - 资源名字
        - **CreateTime** (int) - 创建时间
        - **ExternalApiServer** (str) - 集群外部apiserver地址
        - **K8sVersion** (str) - 集群版本
        - **MasterCount** (int) - Master 节点数量
        - **NodeCount** (int) - Node节点数量
        - **PodCIDR** (str) - Pod网段
        - **ServiceCIDR** (str) - 服务网段
        - **Status** (str) - 状态
        - **SubnetId** (str) - 所属子网
        - **VPCId** (str) - 所属VPC

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUK8SClusterV2RequestSchema().dumps(d)

        resp = self.invoke("ListUK8SClusterV2", d, **kwargs)
        return apis.ListUK8SClusterV2ResponseSchema().loads(resp)
