from ucloud.core import client


class CompactClient(client.Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        self._config = config
        super(CompactClient, self).__init__(config, transport, middleware)

    def pathx(self):
        from ucloud.services.pathx.client import PathXClient

        return PathXClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def vpc(self):
        from ucloud.services.vpc.client import VPCClient

        return VPCClient(
            self._config, self.transport, self.middleware, self.logger
        )
