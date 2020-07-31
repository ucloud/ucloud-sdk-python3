import collections

from ucloud.core.utils import compat


class UCloudException(Exception):
    @property
    def retryable(self):
        return False


MAX_COMMON_RET_CODE = 2000


class TransportException(UCloudException):
    pass


class HTTPStatusException(TransportException):
    def __init__(self, status_code: int, request_uuid: str = None):
        self.status_code = status_code
        self.request_uuid = request_uuid

    @property
    def retryable(self):
        return self.status_code in [429, 502, 503, 504]

    def __str__(self):
        return "[{uuid}] {self.status_code} http status error".format(
            self=self, uuid=self.request_uuid or "*"
        )


class InvalidResponseException(TransportException):
    def __init__(self, content: bytes, message: str, request_uuid: str = None):
        self.content = content
        self.message = message
        self.request_uuid = request_uuid

    @property
    def retryable(self):
        return False

    def __str__(self):
        return "[{uuid}] {self.message}: {self.content}".format(
            self=self, uuid=self.request_uuid or "*"
        )


class RetCodeException(UCloudException):
    def __init__(
        self, action: str, code: int, message: str, request_uuid: str = None
    ):
        self.action = action
        self.code = code
        self.message = message
        self.request_uuid = request_uuid

    @property
    def retryable(self):
        return self.code > MAX_COMMON_RET_CODE

    def __str__(self):
        return "[{uuid}] {self.action} - {self.code}: {self.message}".format(
            self=self, uuid=self.request_uuid or "*"
        )

    def json(self):
        return {
            "RetCode": self.code,
            "Message": self.message or "",
            "Action": self.action or "",
        }


class RetryTimeoutException(UCloudException):
    pass


class ValidationException(UCloudException):
    def __init__(self, e=None):
        if isinstance(e, compat.string_types):
            self.errors = [e]
        elif isinstance(e, collections.Iterable):
            self.errors = e or []
        else:
            self.errors = [e]

    @property
    def retryable(self):
        return False

    def __str__(self):
        return str([str(e) for e in self.errors])
