from flask import Request
from logging import Logger
from pathlib import Path
import requests
from typing import Union

from .configuration import get_logger


BASE_DIR = Path(__file__).parents[1]
USERS_LOG_FILENAME = 'website_users.log'
SERVER_ERR_LOG_FILENAME = 'website_server_errors.log'

users_logger = get_logger(
    USERS_LOG_FILENAME, BASE_DIR,
    name='users_logger',
)
server_error_logger = get_logger(
    SERVER_ERR_LOG_FILENAME, BASE_DIR,
    name='server_error_logger',
)


def get_users_statistic_log_msg(request: Request) -> str:
    """
    Constructs a log message for user statistics.

    :param request: Flask request object.
    :return: Formatted log message.
    """

    ip_address = request.remote_addr
    referer = request.headers.get('Referer')
    user_agent = request.headers.get('User-Agent')

    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        response.raise_for_status()
        geo_data = response.json()

        country = geo_data.get('country_name', 'Unknown')
        city = geo_data.get('city', 'Unknown')
        region = geo_data.get('region', 'Unknown')

    except requests.RequestException:
        country = city = region = 'Unknown'

    return (f'Visit from {ip_address} - Country: {country}, '
            f'City: {city}, Region: {region}. '
            f'Referer: {referer}, User-Agent: {user_agent}.')


def get_server_error_log_msg(error: Exception) -> str:
    """
    Constructs a log message for server errors.

    :param error: Exception instance.
    :return: Formatted log message.
    """

    return f'Server error: {error}.'


def log(log_type: str,
        data: Union[Request, Exception],
        logger: Logger = None,
        log_level: str = 'info'):
    """
    Logs a message based on the log type and data provided.

    :param log_type: Type of log ('users_statistic' or 'server_error').
    :param data: Data to log (Request for 'users_statistic' or Exception for 'server_error').
    :param logger: Logger instance to use.
    :param log_level: Log level as a string.
    """

    log_msg_funcs = {
        'users_statistic': {
            'log_msg_func': get_users_statistic_log_msg,
            'logger': users_logger,
        },
        'server_error': {
            'log_msg_func': get_server_error_log_msg,
            'logger': server_error_logger,
        },
    }

    log_setting = log_msg_funcs.get(log_type)

    if not log_setting:
        return

    get_log_msg = log_setting['log_msg_func']
    logger_ = logger if logger else log_setting['logger']
    write_log_func = getattr(logger_, log_level)

    log_msg = get_log_msg(data)
    write_log_func(log_msg)
