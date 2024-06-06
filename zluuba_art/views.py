from flask import (
    abort, current_app, render_template,
    send_from_directory, typing as ft,
)
from flask.views import View
from typing import Any

from .constants import PET_PROJECTS


class BaseView(View):
    methods = ['GET']
    init_every_request = False


class HomeView(BaseView):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Handles the main page route, logs user statistics,
        and renders the main page.

        :return: The rendered 'index.html' template.
        """

        # log('users_statistic', request)
        return render_template('index.html')


class CVPageView(BaseView):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Renders the cv page.

        :return: The rendered 'cv.html' template.
        """

        return render_template('cv.html')


class ProjectsPageView(BaseView):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Renders the pet projects page.

        :return: The rendered 'pet_projects.html' template.
        """

        return render_template('pet_projects.html')


class ProjectPageView(BaseView):
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


class LinksPageView(BaseView):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Renders the links page.

        :return: The rendered 'links.html' template.
        """

        return render_template('links.html')


class RobotsPageView(BaseView):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        """
        Serves the robots.txt file.

        :return: The robots.txt file.
        """

        static_folder = current_app.static_folder

        if static_folder is None:
            abort(404)

        return send_from_directory(static_folder, 'robots.txt')
