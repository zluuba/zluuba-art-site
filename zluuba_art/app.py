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
    return render_template('projects.html')


@app.get('/about')
def about_page():
    return render_template('about.html')


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
