# app/newupload/views.py

from flask import flash, redirect, render_template, url_for, send_from_directory
from . import newupload
from .forms import RegistrationForm
from .. import db
from ..models import Imagedata
from werkzeug.utils import secure_filename
import os
from flask import current_app as app
from .imageprocessor import create_hash


@newupload.route('/upload', methods=['GET', 'POST'])
def upload():
    form = RegistrationForm()
    if form.validate_on_submit():
        f = form.path.data
        filename = secure_filename(f.filename)
        newpath = os.path.join(app.instance_path, "images")
        os.makedirs(newpath, exist_ok=True)
        f.save(os.path.join(newpath, filename))
        newfilename = create_hash(filename, newpath)
        image = Imagedata(startdate=form.startdate.data.strftime('%d.%m.%Y'),
                          enddate=form.enddate.data.strftime('%d.%m.%Y'),
                          text=form.text.data,
                          path=newfilename)
        # print(form.text.data)
        # add employee to the database
        db.session.add(image)
        db.session.commit()
        flash('You have successfully uploaded')

        # redirect to the login page
        return redirect(url_for('uploadedimages.homepage'))

    # load registration template
    return render_template('newupload/register.html',
                           form=form,
                           title='Upload')


# MEDIA_FOLDER = '/mnt/c/Users/Bouts/Documents/Biogrund/attempt2test/Attempt2/instance/'

# @app.fixture
# def app_context(self):
#     with app.app_context():
#         yield

# @app.route('/<path:filename>')
# def download_file(filename):
#     return send_from_directory(MEDIA_FOLDER, filename, as_attachment=True)
