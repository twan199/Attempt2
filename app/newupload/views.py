# app/newupload/views.py

from flask import flash, redirect, render_template, url_for

from . import newupload
from .forms import RegistrationForm
from .. import db
from ..models import Imagedata


@newupload.route('/upload', methods=['GET', 'POST'])
def upload():
    form = RegistrationForm()
    if form.validate_on_submit():
        image = Imagedata(startdate=form.startdate.data,
                            enddate=form.enddate.data,
                            text=form.text.data)

        # add employee to the database
        db.session.add(image)
        db.session.commit()
        flash('You have successfully uploaded')

        # redirect to the login page
        return redirect(url_for('uploadedimages.homepage'))

    # load registration template
    return render_template('newupload/register.html', form=form, title='Upload')
