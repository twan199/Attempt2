# app/editupload/views.py
from flask import render_template, redirect, url_for, request, session
from . import editupload
from .. import db
from ..models import Imagedata, Imagedataschema
from ..newupload.views import RegistrationForm
from flask import current_app as app
import sqlite3
from datetime import datetime


@editupload.route('/edit', methods=['GET', 'POST'])
def editpagee():
    id = session.get('id', None)
    image = Imagedata.query.get_or_404(id)
    image.enddate = datetime.strptime(image.enddate, '%d.%m.%Y')
    image.startdate = datetime.strptime(image.startdate, '%d.%m.%Y')
    form = RegistrationForm(obj=image)
    if form.validate_on_submit():
        image.startdate = form.startdate.data.strftime('%d.%m.%Y')
        image.enddate = form.enddate.data.strftime('%d.%m.%Y')
        image.text = form.text.data

        db.session.merge(image)
        db.session.commit()
        return redirect(url_for('uploadedimages.homepage'))

    form.populate_obj(image)
    return render_template('editupload/editpage.html',
                           title='Bild bearbeiten',
                           form=form,
                           imagepath=image.path)


@editupload.route('/edit/<id>', methods=['POST'])
def edit(id):
    session['id'] = id
    return redirect(url_for('editupload.editpagee'))
