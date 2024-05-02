from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.get('/cv')
def cv_page():
    return render_template('cv.html')


@app.get('/projects')
def projects_page():
    return render_template('pet_projects.html')


@app.get('/projects/zluuba-art-website')
def zluuba_art_website_project():
    return render_template('projects/zluuba_art_website.html')


@app.get('/projects/games-of-terminal')
def games_of_terminal_project():
    return render_template('projects/games_of_terminal.html')


@app.get('/projects/task-manager')
def task_manager_project():
    return render_template('projects/task_manager.html')


@app.get('/projects/page-analyzer')
def page_analyzer_project():
    return render_template('projects/page_analyzer.html')


@app.get('/links')
def links_page():
    return render_template('links.html')


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
