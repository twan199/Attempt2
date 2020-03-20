# app/newupload/__init__.py

from flask import Blueprint
newupload = Blueprint('newupload', __name__)

from . import views