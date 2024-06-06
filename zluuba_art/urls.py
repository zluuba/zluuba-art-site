from .error_handlers import (
    handle_404, handle_generic_exception,
)
from .views import (
    HomeView, CVPageView, ProjectsPageView,
    ProjectPageView, LinksPageView, RobotsPageView,
)


def register_app(app):
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
