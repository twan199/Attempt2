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
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    #@app.route('/')
    #def hello_world():
    #    return 'Hello, World!'
    app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))
    Bootstrap(app)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/sqlalchemy_database.db'
    migrate = Migrate(app, db)
    
    db.init_app(app)

    from app import models

    from .newupload import newupload as newupload_blueprint
    app.register_blueprint(newupload_blueprint, url_prefix='/')

    from .uploadedimages import uploadedimages as uploadedimages_blueprint
    app.register_blueprint(uploadedimages_blueprint, url_prefix='/')

    return app