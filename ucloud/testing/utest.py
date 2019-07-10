import functools
import logging
import time
import typing

from ucloud.testing import op

logger = logging.getLogger(__name__)


def value_at_path(d, path):
    """ access value by object path

    >>> d = {"Data": [{"UHostId": "foo"}, {"UHostId": "bar"}]}
    >>> value_at_path(d, "Data.1.UHostId")
    'bar'

    :param d: dict or list of dict
    :param path: object path like `Data.1.UHostId`
    :return: any value access by path
    """
    if d is None:
        return None

    indices = path.split(".")
    result = d

    for index in indices:
        if isinstance(result, list):
            if not index.isdigit():
                return None
            else:
                result = result[int(index)]
                continue

        if isinstance(result, dict):
            result = result.get(index)
            if result is None:
                logger.warning("dict key {} is missing for {}".format(index, result))
                return None
            continue

    return result


def value_set_path():
    pass


def case(
    max_retries=0,
    retry_interval=0,
    retry_for=(op.CompareError,),
    startup_delay=0,
    fast_fail=False,
):
    """ wrap a function as a test case

    :param max_retries: the maximum retry number by the `retry_for` exception,
                        it will resolve the flaky testing case
    :param retry_interval: the interval between twice retrying
    :param retry_for: the exceptions to retrying
    :param startup_delay: the delay seconds before any action execution
    :param fast_fail: if fast fail is true, the test will fail when got
                      unexpected exception
    :return:
    """

    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # wait for delay before startup
            if startup_delay:
                time.sleep(startup_delay)

            for i in range(max_retries + 1):
                try:
                    result = fn(*args, **kwargs)
                except Exception as e:
                    # retrying for retryable error
                    if isinstance(e, retry_for) and i != max_retries:
                        if retry_interval:
                            time.sleep(retry_interval)
                        continue

                    if fast_fail:
                        raise e
                    else:
                        logger.exception(e)
                        return
                else:
                    return result

        return wrapper

    return deco


def validate(resp: dict, validators: typing.List[typing.Tuple]):
    """ validate dict by 3-tuple (comparator, value, expected)
    """
    for validator in validators:
        op.check(validator[0], value_at_path(resp, validator[1]), validator[2])
