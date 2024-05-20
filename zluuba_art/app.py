from flask import (
    abort, Flask, request, Response,
    render_template, send_from_directory,
)
from werkzeug.exceptions import HTTPException

from .constants import PET_PROJECTS
from .logger import log


app = Flask(__name__)


@app.route('/')
def main_page() -> Response:
    """
    Handles the main page route, logs user statistics,
    and renders the main page.

    :return: The rendered 'index.html' template.
    """

    log('users_statistic', request)
    return render_template('index.html')


@app.route('/cv')
def cv_page() -> Response:
    """
    Renders the cv page.

    :return: The rendered 'cv.html' template.
    """

    return render_template('cv.html')


@app.route('/projects')
def projects_page() -> Response:
    """
    Renders the pet projects page.

    :return: The rendered 'pet_projects.html' template.
    """

    return render_template('pet_projects.html')


@app.route('/projects/<project>')
def project_page(project: str) -> Response:
    """
    Renders the specified pet project page.

    :param project: Name of the pet project.
    :return: The rendered project template.
    """

    project_html_page = PET_PROJECTS.get(project)

    if not project_html_page:
        abort(404)

    return render_template(f'projects/{project_html_page}')


@app.route('/links')
def links_page() -> Response:
    """
    Renders the links page.

    :return: The rendered 'links.html' template.
    """

    return render_template('links.html')


@app.route('/robots.txt')
def robots_page() -> Response:
    """
    Renders the robots.txt page.

    :return: The robots.txt file.
    """

    return send_from_directory(app.static_folder, 'robots.txt')


@app.errorhandler(404)
def page_not_found(error: HTTPException) -> Response:
    """
    Handles Page Not Found error (404).

    :return: The rendered 'page_not_found.html' template.
    """

    return render_template('errors/page_not_found.html'), 404


@app.errorhandler(500)
def internal_server_error(error: HTTPException) -> Response:
    """
    Handles Internal Server Error (500), logs this error.

    :return: The rendered 'internal_server_error.html' template.
    """

    log('server_error', error)
    return render_template('errors/internal_server_error.html'), 500


@app.errorhandler(Exception)
def internal_server_error(error: Exception) -> Response:
    """
    Handles server error (any 500's error), logs this error.

    :return: The rendered 'internal_server_error.html' template.
    """

    log('server_error', error)
    return render_template('errors/error.html'), 500
