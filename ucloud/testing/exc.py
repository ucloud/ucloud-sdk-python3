class UTestError(Exception):
    pass


class ValidateError(UTestError):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return str(self.errors)


class ValueNotFoundError(UTestError):
    pass


class CompareError(UTestError):
    pass
