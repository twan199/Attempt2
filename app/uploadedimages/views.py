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
    data = Imagedata.query.all()
    result = [d.as_dict() for d in data]
    return jsonify(result=result)