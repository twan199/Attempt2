# app/uploadedimages/__init__.py

from flask import Blueprint
uploadedimages = Blueprint('uploadedimages', __name__)

from . import views