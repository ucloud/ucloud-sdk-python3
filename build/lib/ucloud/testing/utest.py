import logging
import time
import typing

from ucloud.client import Client
from ucloud.testing import op
from ucloud.testing.exc import ValueNotFoundError, CompareError, ValidateError

logger = logging.getLogger(__name__)


class Step:
    def __init__(
        self,
        invoker: typing.Callable[[Client, dict], dict],
        max_retries: int = 0,
        retry_interval: int = 0,
        startup_delay: int = 0,
        retry_for: typing.Tuple = (CompareError, ValueNotFoundError),
        fast_fail: bool = False,
        validators: typing.Callable[[dict], typing.List[typing.Tuple]] = None,
        **kwargs
    ):
        """Step is the test step in a test scenario
        :param invoker: invoker is a callable function
        :param max_retries: the maximum retry number by the `retry_for` exception,
                            it will resolve the flaky testing case
        :param retry_interval: the interval between twice retrying
        :param retry_for: the exceptions to retrying
        :param startup_delay: the delay seconds before any action execution
        :param fast_fail: if fast fail is true, the test will fail when got
                          unexpected exception
        :return:
        """
        self.invoker = invoker
        self.max_retries = max_retries
        self.retry_interval = retry_interval
        self.startup_delay = startup_delay
        self.retry_for = retry_for
        self.fast_fail = fast_fail
        self.validators = validators or (lambda _: [])
        self.extras = kwargs

    def run(self, client: Client, variables: dict):
        # wait for delay before startup
        if self.startup_delay:
            time.sleep(self.startup_delay)

        for i in range(self.max_retries + 1):
            # invoke function to load result
            try:
                result = self.invoker(client, variables)
            except self.retry_for as e:
                if i == self.max_retries:
                    raise e

                if self.retry_interval:
                    time.sleep(self.retry_interval)
                continue
            else:
                result = self.set_default_response(result)

            # validate result
            errors = []
            for validator in self.validators(variables):
                try:
                    op.check(
                        validator[0],
                        value_at_path(result, validator[1]),
                        validator[2],
                    )
                except self.retry_for as e:
                    errors.append(e)

            # if got error, retrying or raise it
            if errors:
                if i == self.max_retries:
                    raise ValidateError(errors)

                if self.retry_interval:
                    time.sleep(self.retry_interval)
                continue

            return result

    def set_default_response(self, resp: dict):
        resp = resp.copy()
        resp.setdefault("RetCode", 0)
        if "action" in self.extras:
            resp["Action"] = "{}Response".format(self.extras["action"])
        return resp


class Scenario:
    def __init__(self, id_):
        self.id = id_
        self.variables = {}
        self.errors = []
        self.steps = []

    def summary(self):
        logger.info("=" * 42)
        logger.info("TEST SET {}".format(self.id))
        logger.info("=" * 42)

        if self.errors:
            logger.info("-" * 42)
            logger.info("ERRORS")
            logger.info("-" * 42)
            for err in self.errors:
                logger.error(err)
            logger.info("Errors!")
        else:
            logger.info("Success!")

    def step(
        self,
        max_retries: int = 0,
        retry_interval: int = 0,
        startup_delay: int = 0,
        retry_for: typing.Tuple = (CompareError, ValueNotFoundError),
        fast_fail: bool = False,
        validators: typing.Callable[[dict], typing.List[typing.Tuple]] = None,
        **kwargs
    ):
        def deco(fn: typing.Callable[[Client, dict], dict]):
            step = Step(
                invoker=fn,
                max_retries=max_retries,
                retry_interval=retry_interval,
                startup_delay=startup_delay,
                retry_for=retry_for,
                fast_fail=fast_fail,
                validators=validators,
                **kwargs
            )
            self.steps.append(step)
            return fn

        return deco

    def run(self, client):
        for i, step in enumerate(self.steps):
            try:
                action = step.extras.get("action", "unknown")
                client.logger.info(
                    "running {} step {} {}".format(self.id, i + 1, action)
                )
                step.run(client, self.variables)
            except CompareError as e:
                self.errors.append(e)
                if step.fast_fail:
                    self.summary()
                    raise e
                client.logger.error(e)

        self.summary()

    def initial(self, variables: typing.Optional[dict] = None):
        self.variables = variables


def value_at_path(d: dict, path: str):
    """access value by object path

    :param d: dict or list of dict
    :param path: object path like `Data.1.UHostId`
    :return: any value access by path
    """
    if d is None:
        return

    indices = path.split(".")
    result = d

    for i, key in enumerate(indices):
        if isinstance(result, list):
            if not key.isdigit():
                return

            if len(result) <= int(key):
                msg = "{} not found".format(".".join(indices[: i + 1]))
                raise ValueNotFoundError(msg)

            result = result[int(key)]
            continue

        if isinstance(result, dict):
            result = {k.lower(): v for k, v in result.items()}.get(key.lower())
            if result is None:
                msg = "{} not found".format(".".join(indices[: i + 1]))
                raise ValueNotFoundError(msg)
            continue

    return result
