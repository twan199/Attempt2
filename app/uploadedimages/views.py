# app/uploadedimages/views.py

from flask import render_template, jsonify, send_from_directory
from . import uploadedimages
from ..models import Imagedata, Imagedataschema
from app import db
import sqlite3
import os
from flask import current_app as app


@uploadedimages.route('/')
def homepage():
    conn = sqlite3.connect('instance/sqlalchemy_database.db')
    c = conn.cursor()
    cur = c.execute('SELECT * FROM db_imagesdata')
    return render_template('uploadedimages/index.html',
                           title="View Images",
                           rows=cur.fetchall())

    #data = Imagedata.query.all()
    #result = [d.as_dict() for d in data]
    #return render_template('uploadedimages/index.html', title="View Images", output_data = result)


@uploadedimages.route("/view/", methods=["GET"])
def user_detail():
    data = Imagedata.query.all()
    result = [d.as_dict() for d in data]
    return jsonify(result=result)


@uploadedimages.route('/images/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.join(app.instance_path, 'images'),
                               filename,
                               conditional=True)