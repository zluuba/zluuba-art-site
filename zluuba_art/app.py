from flask import Flask
from .urls import register_app


app = Flask(__name__)
register_app(app)
