

def encode(d: dict) -> dict:
    result = {}

    for k, v in d.items():
        if isinstance(v, dict):
            for ek, ev in encode(v).items():
                result["{}.{}".format(k, ek)] = ev
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    for ek, ev in encode(item).items():
                        result["{}.{}.{}".format(k, i, ek)] = ev
                else:
                    result["{}.{}".format(k, i)] = item
        else:
            result[k] = v

    return result
