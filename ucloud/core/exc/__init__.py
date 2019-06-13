import collections
import typing


class UCloudException(Exception):
    @property
    def retryable(self):
        return False


MAX_COMMON_RET_CODE = 2000


class RetCodeException(UCloudException):
    def __init__(self, action: str, code: int, message: str):
        self.action = action
        self.code = code
        self.message = message

    @property
    def retryable(self):
        return self.code > MAX_COMMON_RET_CODE

    def __str__(self):
        return f"{self.action} - {self.code}: {self.message}"


class RetryTimeoutException(UCloudException):
    pass


class ValidationException(UCloudException):
    def __init__(self, e=None):
        if isinstance(e, collections.Iterable):
            self.errors: typing.List[Exception] = e or []
        else:
            self.errors: typing.List[Exception] = [e]

    @property
    def retryable(self):
        return False
