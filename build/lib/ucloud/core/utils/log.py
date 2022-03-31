import logging

DEFAULT_LOGGER_NAME = "ucloud"
DEFAULT_FORMAT = "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s %(name)s)"
DEFAULT_LEVEL = logging.INFO


def init_default_logger():
    logger = logging.getLogger(DEFAULT_LOGGER_NAME)
    logger.setLevel(DEFAULT_LEVEL)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(DEFAULT_LEVEL)

    # create formatter
    formatter = logging.Formatter(DEFAULT_FORMAT)

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.removeHandler(ch)
    logger.addHandler(ch)

    return logger


default_logger = init_default_logger()
