from flask import (
    abort, Flask, typing as ft,
    render_template, send_from_directory,
    # request,
)
from flask.views import View
from typing import Any

from zluuba_art.constants import PET_PROJECTS
from zluuba_art.error_handlers import handle_404, handle_generic_exception
# from zluuba_art.logger.logger import log


class HomeView(View):
    methods = ['GET']
    init_every_request = False

    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Handles the main page route, logs user statistics,
        and renders the main page.

        :return: The rendered 'index.html' template.
        """

        # log('users_statistic', request)
        return render_template('index.html')


class CVPageView(View):
    methods = ['GET']
    init_every_request = False

    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Renders the cv page.

        :return: The rendered 'cv.html' template.
        """

        return render_template('cv.html')


class ProjectsPageView(View):
    methods = ['GET']
    init_every_request = False

    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Renders the pet projects page.

        :return: The rendered 'pet_projects.html' template.
        """

        return render_template('pet_projects.html')


class ProjectPageView(View):
    methods = ['GET']
    init_every_request = False

    def dispatch_request(self, *args: Any, **kwargs: Any
                         ) -> ft.ResponseReturnValue:
        """
        Renders the specified pet project page.

        :param project: Name of the pet project.
        :return: The rendered project template.
        """
        project = kwargs['project']
        project_html_page = PET_PROJECTS.get(project)

        if not project_html_page:
            abort(404)

        return render_template(f'projects/{project_html_page}')


class LinksPageView(View):
    methods = ['GET']
    init_every_request = False

    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Renders the links page.

        :return: The rendered 'links.html' template.
        """

        return render_template('links.html')


class RobotsPageView(View):
    methods = ['GET']
    init_every_request = False

    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Serves the robots.txt file.

        :return: The robots.txt file.
        """

        static_folder = app.static_folder

        if static_folder is None:
            abort(404)

        return send_from_directory(static_folder, 'robots.txt')


def register_api(app):
    app.add_url_rule(
        '/',
        view_func=HomeView.as_view('main_page'),
    )
    app.add_url_rule(
        '/cv',
        view_func=CVPageView.as_view('cv_page'),
    )
    app.add_url_rule(
        '/projects',
        view_func=ProjectsPageView.as_view('projects_page')
    )
    app.add_url_rule(
        '/projects/<project>',
        view_func=ProjectPageView.as_view('project_page')
    )
    app.add_url_rule(
        '/links',
        view_func=LinksPageView.as_view('links_page')
    )
    app.add_url_rule(
        '/robots.txt',
        view_func=RobotsPageView.as_view('robots_page')
    )

    app.register_error_handler(404, handle_404)
    app.register_error_handler(Exception, handle_generic_exception)


app = Flask(__name__)
register_api(app)
