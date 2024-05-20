from flask import abort, Flask, render_template, send_from_directory
from .constants import PET_PROJECTS


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/cv')
def cv_page():
    return render_template('cv.html')


@app.route('/projects')
def projects_page():
    return render_template('pet_projects.html')


@app.route('/projects/<project>')
def project_page(project):
    project_html_page = PET_PROJECTS.get(project)

    if not project_html_page:
        abort(404)

    return render_template(f'projects/{project_html_page}')


@app.route('/links')
def links_page():
    return render_template('links.html')


@app.route('/robots.txt')
def robots_page():
    return send_from_directory(app.static_folder, 'robots.txt')


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        'page_not_found.html'
    ), 404


@app.errorhandler(Exception)
def internal_server_error(error):
    return render_template(
        'internal_server_error.html'
    ), 500
