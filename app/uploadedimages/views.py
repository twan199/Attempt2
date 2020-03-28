# app/uploadedimages/views.py

from flask import render_template
from . import uploadedimages

@uploadedimages.route('/')
def homepage():
    return render_template('uploadedimages/index.html', title="View Images")

