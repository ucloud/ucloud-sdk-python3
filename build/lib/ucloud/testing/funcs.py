import datetime
import time


def concat(*args):
    """cancat strings

    >>> concat(42, 'foo', 'bar')
    '42foobar'
    """
    return "".join([str(s) for s in args])


def concat_without_dot(args):
    """replace blank

    >>> concat_without_dot('42foo bar')
    '42foobar'
    """
    return "".join([str(s) for s in args.split()])


def search_value(array, origin_key, origin_value, dest_key):
    """given origin key and value,search dest_value form array by dest_key

    >>> d = [{"UHostId": "foo", "Name": "testing"}]
    >>> search_value(d, "Name", "testing", "UHostId")
    'foo'
    """
    arr = [i.get(dest_key, "") for i in array if i[origin_key] == origin_value]
    if arr:
        return arr[0]
    return ""


def timedelta(timestamp, value, typ="days"):
    """given timestamp(10bit) and calculate relative delta time

    >>> timedelta(0, 1, "days")
    86400.0

    :param timestamp: timestamp (round to second)
    :param value: float, can as positive or negative
    :param typ: days/hours
    :return: timestamp
    """
    value = int(value)
    dt = datetime.datetime.fromtimestamp(float(timestamp))
    if typ == "days":
        dt += datetime.timedelta(days=value)
    elif typ == "hours":
        dt += datetime.timedelta(hours=value)
    return time.mktime(dt.timetuple())


def get_timestamp(length=13):
    """get current timestamp string

    >>> len(str(int(get_timestamp(10))))
    10

    :param length: length of timestamp, can only between 0 and 16
    :return:
    """
    if isinstance(length, int) and 0 < length < 17:
        return int("{:.6f}".format(time.time()).replace(".", "")[:length])

    raise ValueError("timestamp length can only between 0 and 16.")
