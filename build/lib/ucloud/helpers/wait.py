import time
import typing
import logging
from ucloud.core import exc


MAX_BACKOFF_INTERVAL = 10

logger = logging.getLogger(__name__)


class WaitTimeoutException(exc.UCloudException):
    pass


class StateConf:
    """StateConf is the utilities class to wait the state return by refresh function achieve the specific state,
    the generally usage is wait the cloud resource, such as uhost, udb ... is
    ready after created.
    """

    def __init__(
        self,
        pending: typing.List[str],
        target: typing.List[str],
        refresh: typing.Callable,
        timeout: float,
        startup_delay: float = 0,
        min_backoff_interval: float = 0.1,
        max_backoff_interval: float = MAX_BACKOFF_INTERVAL,
    ):
        self.pending = pending
        self.target = target
        self.refresh = refresh
        self.timeout = timeout
        self.startup_delay = startup_delay
        self.min_backoff_interval = min_backoff_interval
        self.max_backoff_interval = max_backoff_interval

    def wait(self):
        start_time = time.time()
        interval = self.min_backoff_interval

        # delay on start up
        time.sleep(self.startup_delay)

        # waiting for state changed to target state
        while time.time() - start_time < self.timeout:
            state = self.refresh()

            if state in self.pending:
                time.sleep(interval)
                interval *= 2
                if interval > self.max_backoff_interval:
                    interval = self.max_backoff_interval
                logger.info(
                    "waiting state for {self.refresh}, got state {state}".format(
                        self=self, state=state
                    )
                )
                continue

            if state in self.target:
                return

        raise WaitTimeoutException(
            "wait timeout {self.timeout}s for {self.refresh}".format(self=self)
        )


def wait_for_state(
    pending: typing.List[str],
    target: typing.List[str],
    refresh: typing.Callable,
    timeout: float,
    startup_delay: float = 0,
    min_backoff_interval: float = 0.1,
    max_backoff_interval: float = MAX_BACKOFF_INTERVAL,
):
    """wait_for_state is a utilities function to wait the state return by refresh function achieve the specific state,
    the generally usage is wait the cloud resource, such as uhost, udb ... is
    ready after created.

    >>> wait_for_state(
    ...     pending=["pending"],
    ...     target=["running"],
    ...     refresh=lambda: "running",
    ...     timeout=0.5,
    ... )

    :param pending: pending is the list of pending state, the state is returned by refresh function
    :param target: target is the list of target state, it is usually the terminate state, eg. running and fail
    :param refresh: the customized refresh function, expect no arguments and return a state
    :param timeout: timeout is the total time to wait state is achieved
    :param startup_delay: the time to wait before first refresh function is called
    :param min_backoff_interval: the backoff time for first refresh interval
    :param max_backoff_interval: the max backoff time for refresh interval
    """
    conf = StateConf(
        pending=pending,
        target=target,
        refresh=refresh,
        timeout=timeout,
        startup_delay=startup_delay,
        min_backoff_interval=min_backoff_interval,
        max_backoff_interval=max_backoff_interval,
    )
    return conf.wait()
