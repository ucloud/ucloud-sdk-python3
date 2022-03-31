import functools
import logging

logger = logging.getLogger("ucloud")


def deprecated(instead_of="", message=""):
    """deprecated is a decorator to mark a function is deprecated.
    it will logging warning when this function called

    >>> @deprecated(instead_of="new_function")
    ... def an_old_function():
    ...     pass
    """

    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            msg = [
                "this function/method `{}` is deprecated".format(fn.__name__)
            ]
            instead_of and msg.append(
                "please use `{}` instead".format(instead_of)
            )
            message and msg.append(message)
            logger.warning(", ".join(msg))
            return fn(*args, **kwargs)

        return wrapper

    return deco
