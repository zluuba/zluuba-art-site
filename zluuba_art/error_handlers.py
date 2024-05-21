from flask import render_template, typing as ft
from werkzeug.exceptions import HTTPException

# from zluuba_art.logger.logger import log


def handle_404(error: HTTPException) -> ft.ResponseReturnValue:
    """
    Handles Page Not Found error (404).

    :return: The rendered 'page_not_found.html' template.
    """

    return render_template('errors/page_not_found.html'), 404


def handle_generic_exception(error: Exception) -> ft.ResponseReturnValue:
    """
    Handles server error (any 500's error), logs this error.

    :return: The rendered 'internal_server_error.html' template.
    """

    # log('server_error', error)
    return render_template('errors/internal_server_error.html'), 500
