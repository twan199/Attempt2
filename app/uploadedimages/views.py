# app/uploadedimages/views.py

from flask import render_template, jsonify
from . import uploadedimages
from ..models import Imagedata, Imagedataschema
from app import db

@uploadedimages.route('/')
def homepage():
    return render_template('uploadedimages/index.html', title="View Images")

@uploadedimages.route("/view/", methods=["GET"])
def user_detail():
    images_schema = Imagedataschema(many=False)
    all_users = Imagedata.query.all()
    result = images_schema.dump(all_users)
    return images_schema.jsonify(result)