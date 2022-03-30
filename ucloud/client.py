""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core import client


class Client(client.Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        self._config = config
        super(Client, self).__init__(self._auto_config(), transport, middleware, logger)

    def pathx(self):
        from ucloud.services.pathx.client import PathXClient

        return PathXClient(
            self._auto_config('pathx'), self.transport, self.middleware, self.logger
        )


    
    
    def cube(self):
        from ucloud.services.cube.client import CubeClient
        return CubeClient(self._auto_config('cube'), self.transport, self.middleware, self.logger)
    

    
    
    def iam(self):
        from ucloud.services.iam.client import IAMClient
        return IAMClient(self._auto_config('iam'), self.transport, self.middleware, self.logger)
    

    
    
    def ipsecvpn(self):
        from ucloud.services.ipsecvpn.client import IPSecVPNClient
        return IPSecVPNClient(self._auto_config('ipsecvpn'), self.transport, self.middleware, self.logger)
    

    
    
    def isms(self):
        from ucloud.services.isms.client import ISMSClient
        return ISMSClient(self._auto_config('isms'), self.transport, self.middleware, self.logger)
    

    
    

    
    
    def stepflow(self):
        from ucloud.services.stepflow.client import StepFlowClient
        return StepFlowClient(self._auto_config('stepflow'), self.transport, self.middleware, self.logger)
    

    
    
    def tidb(self):
        from ucloud.services.tidb.client import TiDBClient
        return TiDBClient(self._auto_config('tidb'), self.transport, self.middleware, self.logger)
    

    
    
    def uaccount(self):
        from ucloud.services.uaccount.client import UAccountClient
        return UAccountClient(self._auto_config('uaccount'), self.transport, self.middleware, self.logger)
    

    
    
    def uarchive(self):
        from ucloud.services.uarchive.client import UArchiveClient
        return UArchiveClient(self._auto_config('uarchive'), self.transport, self.middleware, self.logger)
    

    
    
    def ubill(self):
        from ucloud.services.ubill.client import UBillClient
        return UBillClient(self._auto_config('ubill'), self.transport, self.middleware, self.logger)
    

    
    
    def ubox(self):
        from ucloud.services.ubox.client import UBoxClient
        return UBoxClient(self._auto_config('ubox'), self.transport, self.middleware, self.logger)
    

    
    
    def ucdn(self):
        from ucloud.services.ucdn.client import UCDNClient
        return UCDNClient(self._auto_config('ucdn'), self.transport, self.middleware, self.logger)
    

    
    
    def ucloudstack(self):
        from ucloud.services.ucloudstack.client import UCloudStackClient
        return UCloudStackClient(self._auto_config('ucloudstack'), self.transport, self.middleware, self.logger)
    

    
    
    def udb(self):
        from ucloud.services.udb.client import UDBClient
        return UDBClient(self._auto_config('udb'), self.transport, self.middleware, self.logger)
    

    
    
    def uddb(self):
        from ucloud.services.uddb.client import UDDBClient
        return UDDBClient(self._auto_config('uddb'), self.transport, self.middleware, self.logger)
    

    
    
    def uddos_uclean(self):
        from ucloud.services.uddos_uclean.client import UDDoS_UCleanClient
        return UDDoS_UCleanClient(self._auto_config('uddos_uclean'), self.transport, self.middleware, self.logger)
    

    
    
    def udhost(self):
        from ucloud.services.udhost.client import UDHostClient
        return UDHostClient(self._auto_config('udhost'), self.transport, self.middleware, self.logger)
    

    
    
    def udnrv2(self):
        from ucloud.services.udnrv2.client import UDNRV2Client
        return UDNRV2Client(self._auto_config('udnrv2'), self.transport, self.middleware, self.logger)
    

    
    
    def udpn(self):
        from ucloud.services.udpn.client import UDPNClient
        return UDPNClient(self._auto_config('udpn'), self.transport, self.middleware, self.logger)
    

    
    
    def udts(self):
        from ucloud.services.udts.client import UDTSClient
        return UDTSClient(self._auto_config('udts'), self.transport, self.middleware, self.logger)
    

    
    
    def udisk(self):
        from ucloud.services.udisk.client import UDiskClient
        return UDiskClient(self._auto_config('udisk'), self.transport, self.middleware, self.logger)
    

    
    
    def udocker(self):
        from ucloud.services.udocker.client import UDockerClient
        return UDockerClient(self._auto_config('udocker'), self.transport, self.middleware, self.logger)
    

    
    
    def uec(self):
        from ucloud.services.uec.client import UECClient
        return UECClient(self._auto_config('uec'), self.transport, self.middleware, self.logger)
    

    
    
    def uewaf(self):
        from ucloud.services.uewaf.client import UEWAFClient
        return UEWAFClient(self._auto_config('uewaf'), self.transport, self.middleware, self.logger)
    

    
    
    def ufs(self):
        from ucloud.services.ufs.client import UFSClient
        return UFSClient(self._auto_config('ufs'), self.transport, self.middleware, self.logger)
    

    
    
    def ufile(self):
        from ucloud.services.ufile.client import UFileClient
        return UFileClient(self._auto_config('ufile'), self.transport, self.middleware, self.logger)
    

    
    
    def ugc(self):
        from ucloud.services.ugc.client import UGCClient
        return UGCClient(self._auto_config('ugc'), self.transport, self.middleware, self.logger)
    

    
    
    def ugn(self):
        from ucloud.services.ugn.client import UGNClient
        return UGNClient(self._auto_config('ugn'), self.transport, self.middleware, self.logger)
    

    
    
    def uhost(self):
        from ucloud.services.uhost.client import UHostClient
        return UHostClient(self._auto_config('uhost'), self.transport, self.middleware, self.logger)
    

    
    
    def uhub(self):
        from ucloud.services.uhub.client import UHubClient
        return UHubClient(self._auto_config('uhub'), self.transport, self.middleware, self.logger)
    

    
    
    def uhybridv2(self):
        from ucloud.services.uhybridv2.client import UHybridV2Client
        return UHybridV2Client(self._auto_config('uhybridv2'), self.transport, self.middleware, self.logger)
    

    
    
    def uhybridv3(self):
        from ucloud.services.uhybridv3.client import UHybridV3Client
        return UHybridV3Client(self._auto_config('uhybridv3'), self.transport, self.middleware, self.logger)
    

    
    
    def uk8s(self):
        from ucloud.services.uk8s.client import UK8SClient
        return UK8SClient(self._auto_config('uk8s'), self.transport, self.middleware, self.logger)
    

    
    
    def ukms(self):
        from ucloud.services.ukms.client import UKMSClient
        return UKMSClient(self._auto_config('ukms'), self.transport, self.middleware, self.logger)
    

    
    
    def ukafka(self):
        from ucloud.services.ukafka.client import UKafkaClient
        return UKafkaClient(self._auto_config('ukafka'), self.transport, self.middleware, self.logger)
    

    
    
    def ulb(self):
        from ucloud.services.ulb.client import ULBClient
        return ULBClient(self._auto_config('ulb'), self.transport, self.middleware, self.logger)
    

    
    
    def ulive(self):
        from ucloud.services.ulive.client import ULiveClient
        return ULiveClient(self._auto_config('ulive'), self.transport, self.middleware, self.logger)
    

    
    
    def umai(self):
        from ucloud.services.umai.client import UMAIClient
        return UMAIClient(self._auto_config('umai'), self.transport, self.middleware, self.logger)
    

    
    
    def umedia(self):
        from ucloud.services.umedia.client import UMediaClient
        return UMediaClient(self._auto_config('umedia'), self.transport, self.middleware, self.logger)
    

    
    
    def umem(self):
        from ucloud.services.umem.client import UMemClient
        return UMemClient(self._auto_config('umem'), self.transport, self.middleware, self.logger)
    

    
    
    def umon(self):
        from ucloud.services.umon.client import UMonClient
        return UMonClient(self._auto_config('umon'), self.transport, self.middleware, self.logger)
    

    
    
    def unvs(self):
        from ucloud.services.unvs.client import UNVSClient
        return UNVSClient(self._auto_config('unvs'), self.transport, self.middleware, self.logger)
    

    
    
    def unet(self):
        from ucloud.services.unet.client import UNetClient
        return UNetClient(self._auto_config('unet'), self.transport, self.middleware, self.logger)
    

    
    
    def uphost(self):
        from ucloud.services.uphost.client import UPHostClient
        return UPHostClient(self._auto_config('uphost'), self.transport, self.middleware, self.logger)
    

    
    
    def urtc(self):
        from ucloud.services.urtc.client import URTCClient
        return URTCClient(self._auto_config('urtc'), self.transport, self.middleware, self.logger)
    

    
    
    def urocketmq(self):
        from ucloud.services.urocketmq.client import URocketMQClient
        return URocketMQClient(self._auto_config('urocketmq'), self.transport, self.middleware, self.logger)
    

    
    
    def usa(self):
        from ucloud.services.usa.client import USAClient
        return USAClient(self._auto_config('usa'), self.transport, self.middleware, self.logger)
    

    
    
    def usms(self):
        from ucloud.services.usms.client import USMSClient
        return USMSClient(self._auto_config('usms'), self.transport, self.middleware, self.logger)
    

    
    
    def usql(self):
        from ucloud.services.usql.client import USQLClient
        return USQLClient(self._auto_config('usql'), self.transport, self.middleware, self.logger)
    

    
    
    def usnap(self):
        from ucloud.services.usnap.client import USnapClient
        return USnapClient(self._auto_config('usnap'), self.transport, self.middleware, self.logger)
    

    
    
    def utsdb(self):
        from ucloud.services.utsdb.client import UTSDBClient
        return UTSDBClient(self._auto_config('utsdb'), self.transport, self.middleware, self.logger)
    

    
    
    def uvms(self):
        from ucloud.services.uvms.client import UVMSClient
        return UVMSClient(self._auto_config('uvms'), self.transport, self.middleware, self.logger)
    

    
    
    def uvideo(self):
        from ucloud.services.uvideo.client import UVideoClient
        return UVideoClient(self._auto_config('uvideo'), self.transport, self.middleware, self.logger)
    

    
    


    def vpc(self):
        from ucloud.services.vpc.client import VPCClient

        return VPCClient(
            self._auto_config('vpc'), self.transport, self.middleware, self.logger
        )

    def _auto_config(self, package="generic"):
        user_agent = "Package/{} {}".format(package, self._config.get('user_agent') or '')
        return dict(
            user_agent=user_agent.rstrip(),
            **self._config
        )
