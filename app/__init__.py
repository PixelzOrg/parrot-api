import os
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from celery import Celery, Task
from app.routes.videos import videos
from app.routes.health_checks import health_checks

def create_server():
    """
    Creates a Flask server instance, sets up the config and imports the routes
    """
    server = Flask(__name__)

    server.config['VIDEO_FOLDER'] = "app/data/videos/"

    # SET DEBUG
    debug = os.environ.get('IS_DEBUG')
    server.debug = True if debug == "TRUE" else False

    # CREATE SWAGGER DOCS
    swagger_url = os.environ.get('SWAGGER_URL')
    api_url = os.environ.get('API_URL')

    swagger_ui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': "Storage API"
        }
    )
    server.register_blueprint(swagger_ui_blueprint, url_prefix=swagger_url)

    # REGISTER ALL ROUTES
    server.register_blueprint(videos, url_prefix='/videos')
    server.register_blueprint(health_checks, url_prefix='/')

    return server
