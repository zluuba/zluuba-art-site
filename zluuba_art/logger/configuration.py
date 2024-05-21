from logging import (
    basicConfig, getLogger, Logger,
    DEBUG, INFO, WARNING, ERROR, CRITICAL,
)
from os import path
from pathlib import Path, PosixPath
from typing import Union


DEFAULT_NAME = 'zluuba_art'
DEFAULT_LEVEL = 'info'
DATE_FORMAT = '%Y-%m-%d, %H:%M:%S'
OUTPUT_FORMAT = '%(asctime)s : %(levelname)s : %(message)s'

LEVELS = {
    'debug': DEBUG,
    'info': INFO,
    'warning': WARNING,
    'error': ERROR,
    'critical': CRITICAL,
}


def get_logger(filename: str,
               basedir: Union[Path, PosixPath],
               name: str = DEFAULT_NAME,
               log_level: str = DEFAULT_LEVEL) -> Logger:
    """
    Configures and returns a logger.

    :param filename: Name of the log file.
    :param basedir: Base directory for the log file.
    :param name: Name of the logger.
    :param log_level: Logging level as a string.
    :return: Configured Logger instance.
    """

    level = LEVELS[log_level]
    filename = str(path.join(basedir, filename))

    basicConfig(
        filename=filename,
        filemode='a',
        format=OUTPUT_FORMAT,
        datefmt=DATE_FORMAT,
        level=level,
    )
    return getLogger(name)
