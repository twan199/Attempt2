# app/newupload/views.py

from flask import flash, redirect, render_template, url_for
from . import newupload
from .forms import RegistrationForm
from .. import db
from ..models import Imagedata
from werkzeug.utils import secure_filename
import os
from flask import current_app as app


@newupload.route('/upload', methods=['GET', 'POST'])
def upload():
    form = RegistrationForm()
    if form.validate_on_submit():
        f = form.path.data
        filename = secure_filename(f.filename)

        newpath = os.path.join(app.instance_path, "images")
        if not os.path.isdir(newpath):
            os.mkdir(os.path.join(newpath))
        f.save(os.path.join(newpath, filename))
        image = Imagedata(startdate=form.startdate.data,
                          enddate=form.enddate.data,
                          text=form.text.data,
                          path=filename)
        print(form.text.data)
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
