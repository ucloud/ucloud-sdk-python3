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
        return

    indices = path.split(".")
    result = d

    for index in indices:
        if isinstance(result, list):
            if not index.isdigit():
                return
            else:
                result = result[int(index)]
                continue

        if isinstance(result, dict):
            result = result.get(index)
            if result is None:
                logger.warning(
                    "dict key {} is missing for {}".format(index, result))
                return
            continue

    return result


def set_value_with_path(d: dict, path: str, value: typing.Any):
    """ set value with path syntax

    >>> d = set_value_with_path({}, 'Network.0.EIP.Bandwidth', 1)
    >>> d
    {'Network': [{'EIP': {'Bandwidth': 1}}]}
    >>> set_value_with_path(d, 'Network.0.EIP.OperatorName', 'BGP')
    {'Network': [{'EIP': {'Bandwidth': 1, 'OperatorName': 'BGP'}}]}
    """
    d = d.copy()
    if d is None:
        return

    ref = d
    indices = path.split(".")
    current = indices[0]
    it = iter(indices[1:])
    for look_ahead in it:
        if look_ahead.isdigit():
            index = int(look_ahead)
            array = ref.setdefault(current, [])
            ref = set_array_item(array, index)
            current = next(it)
        else:
            ref.setdefault(current, {})
            ref = ref[current]
            current = look_ahead

    ref[current] = value
    return d


def set_array_item(d, index):
    """ set array will set all item less than specific index

    >>> array = []
    >>> d = set_array_item(array, 2)
    >>> array
    [{}, {}, {}]
    >>> d['foo'] = 'bar'
    >>> array
    [{}, {}, {'foo': 'bar'}]
    """
    try:
        return d[index]
    except IndexError:
        d.extend([{} for _ in range((index + 1) - len(d))])
        return d[-1]


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
