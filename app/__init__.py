# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    myapp = Flask(__name__, instance_relative_config=True)
    myapp.config.from_object(app_config[config_name])
    myapp.config.from_pyfile('config.py')
    myapp.config.update(
        dict(SECRET_KEY="powerful secretkey",
             WTF_CSRF_SECRET_KEY="a csrf secret key"))

    Bootstrap(myapp)
    migrate = Migrate(myapp, db)

    db.init_app(myapp)

    from app import models

    from .newupload import newupload as newupload_blueprint
    myapp.register_blueprint(newupload_blueprint, url_prefix='/')

    from .uploadedimages import uploadedimages as uploadedimages_blueprint
    myapp.register_blueprint(uploadedimages_blueprint, url_prefix='/')

    from .editupload import editupload as editupload_blueprint
    myapp.register_blueprint(editupload_blueprint, url_prefix='/')

    return myapp