from ucloud.core import client


class Client(client.Client):
    def __init__(self, config: dict):
        self.config = config

    def udb(self):
        from ucloud.services.udb.client import UDBClient
        return UDBClient(self.config, self.transport, self.middleware)

    def udisk(self):
        from ucloud.services.udisk.client import UDiskClient
        return UDiskClient(self.config)

    def uaccount(self):
        from ucloud.services.uaccount.client import UAccountClient
        return UAccountClient(self.config)

    def pathx(self):
        from ucloud.services.pathx.client import PathXClient
        return PathXClient(self.config)

    def udpn(self):
        from ucloud.services.udpn.client import UDPNClient
        return UDPNClient(self.config)

    def uphost(self):
        from ucloud.services.uphost.client import UPHostClient
        return UPHostClient(self.config)

    def ulb(self):
        from ucloud.services.ulb.client import ULBClient
        return ULBClient(self.config)

    def uhost(self):
        from ucloud.services.uhost.client import UHostClient
        return UHostClient(self.config)

    def umem(self):
        from ucloud.services.umem.client import UMemClient
        return UMemClient(self.config)

    def unet(self):
        from ucloud.services.unet.client import UNetClient
        return UNetClient(self.config)

    def vpc(self):
        from ucloud.services.vpc.client import VPCClient
        return VPCClient(self.config)
