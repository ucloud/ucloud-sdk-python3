import logging

from ucloud.core.typesystem import schema, fields


class ConfigSchema(schema.Schema):
    fields = {
        "region": fields.Str(),
        "project_id": fields.Str(),
        "base_url": fields.Str(default="https://api.ucloud.cn"),
        "user_agent": fields.Str(),
        "timeout": fields.Int(default=30),
        "max_retries": fields.Int(default=3),
        "log_level": fields.Int(default=logging.INFO),
        "validate_request": fields.Bool(default=True),
        "ssl_verify": fields.Bool(default=True),
        "ssl_cacert": fields.Str(),
        "ssl_cert": fields.Str(),
        "ssl_key": fields.Str(),
    }


class Config:
    """
    Config is the config of ucloud sdk, use for setting up

    :type region: str
    :param region: Region is the region of backend service,
        See also `Region list Documentation <https://docs.ucloud.cn/api/summary/regionlist>`_
    :type project_id: str
    :param project_id: ProjectId is the unique identify of project, used for organize resources,
                       Most of resources should belong to a project. Sub-Account must have an project id.
                       See also `Project list Documentation <https://docs.ucloud.cn/api/summary/get_project_list>`_
    :type base_url: str
    :param base_url: BaseUrl is the url of backend api
    :param user_agent: UserAgent is an attribute for sdk client, used for distinguish who is using sdk.
                       See also `User Agent <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent>`_
                       It will be appended to the end of sdk user-agent.
                       eg. "MyAPP/0.10.1" -> "Python/3.7.0 Python-SDK/0.1.0 MyAPP/0.10.1"
    :type timeout: int
    :param timeout: Timeout is timeout for every request.
    :type max_retries: int
    :param max_retries: MaxRetries is the number of max retry times.
                        Set MaxRetries more than 0 to enable auto-retry for network and service availability problem
                        if auto-retry is enabled, it will enable default retry policy using exponential backoff.
    :type log_level: int
    :param log_level:  LogLevel is equal to builtin logging level,
        if logLevel not be set, use INFO level as default.
    """

    def __init__(
        self,
        region: str = None,
        project_id: str = None,
        base_url: str = "https://api.ucloud.cn",
        user_agent: str = None,
        timeout: int = 30,
        max_retries: int = 3,
        log_level: int = logging.INFO,
        ssl_verify: bool = True,
        ssl_cacert: str = None,
        ssl_cert: str = None,
        ssl_key: str = None,
        **kwargs
    ):
        self.region = region
        self.project_id = project_id
        self.base_url = base_url
        self.user_agent = user_agent
        self.timeout = timeout
        self.max_retries = max_retries
        self.log_level = log_level
        self.ssl_verify = ssl_verify
        self.ssl_cacert = ssl_cacert
        self.ssl_cert = ssl_cert
        self.ssl_key = ssl_key

    @classmethod
    def from_dict(cls, d: dict):
        parsed = ConfigSchema().dumps(d)
        return cls(**parsed)

    def to_dict(self) -> dict:
        return {
            "region": self.region,
            "project_id": self.project_id,
            "base_url": self.base_url,
            "user_agent": self.user_agent,
            "timeout": self.timeout,
            "max_retries": self.max_retries,
            "log_level": self.log_level,
            "ssl_verify": self.ssl_verify,
            "ssl_cacert": self.ssl_cacert,
            "ssl_cert": self.ssl_cert,
            "ssl_key": self.ssl_key,
        }
