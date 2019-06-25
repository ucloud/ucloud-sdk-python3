import sys

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = (str,)
    from collections.abc import Callable
else:
    import types

    string_types = types.StringTypes

    from collections import Callable
