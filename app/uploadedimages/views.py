# app/uploadedimages/views.py

from flask import render_template
from . import uploadedimages

@uploadedimages.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('uploadedimages/index.html', title="View Images")

