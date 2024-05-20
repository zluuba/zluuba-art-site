from logging import basicConfig, getLogger, INFO
from os import path
from pathlib import Path
import requests


BASE_DIR = Path(__file__).parents[1]
USERS_LOG_FILENAME = 'website_users.log'


def get_logs_path(filename):
    return str(path.join(BASE_DIR, filename))


def get_logger(log_filename, name='zluuba_art', level=INFO):
    filename = get_logs_path(log_filename)
    date_format = '%Y-%m-%d, %H:%M:%S'
    output_format = '%(asctime)s : %(levelname)s : %(message)s'

    basicConfig(
        filename=filename,
        filemode='w',
        format=output_format,
        datefmt=date_format,
        level=level,
    )
    return getLogger(name)


def get_log_message(request):
    ip_address = request.remote_addr
    referer = request.headers.get('Referer')
    user_agent = request.headers.get('User-Agent')

    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    country = response.get('country_name', 'Unknown')
    city = response.get('city', 'Unknown')
    region = response.get('region', 'Unknown')

    return (f'Visit from {ip_address} - Country: {country}, City: {city}, '
            f'Region: {region}. Referer: {referer}, User-Agent: {user_agent}')


def log(request, logger=None, log_type='info'):
    logger_ = logger if logger else get_logger(USERS_LOG_FILENAME)
    write_log_func = getattr(logger_, log_type)
    log_message = get_log_message(request)

    write_log_func(log_message)
