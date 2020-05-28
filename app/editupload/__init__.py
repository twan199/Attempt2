# app/editupload/__init__.py

from flask import Blueprint
editupload = Blueprint('editupload', __name__)

from . import views