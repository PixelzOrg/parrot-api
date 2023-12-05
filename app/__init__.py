import os
import torch
from flask import Flask
from celery import Celery, Task
from app.routes.videos import videos
from app.routes.health_checks import health_checks


def create_server():
    """
    Creates a Flask server instance, sets up the config and imports the routes
    """
    server = Flask(__name__)

    debug = os.environ.get('IS_DEBUG')
    server.debug = True if debug == "TRUE" else False
    server.config['VIDEO_FOLDER'] = "app/data/videos/"

    server.register_blueprint(videos, url_prefix='/videos')
    server.register_blueprint(health_checks, url_prefix='/health_checks')

    return server
