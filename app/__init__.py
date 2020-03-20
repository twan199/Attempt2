# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    #@app.route('/')
    #def hello_world():
    #    return 'Hello, World!'

    migrate = Migrate(app, db)
    from app import models

    from .newupload import newupload as newupload_blueprint
    app.register_blueprint(newupload_blueprint, url_prefix='/upload')

    from .uploadedimages import uploadedimages as uploadedimages_blueprint
    app.register_blueprint(uploadedimages_blueprint, url_prefix='/')

    return app
