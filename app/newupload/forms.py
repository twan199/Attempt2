# app/newupload/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Optional
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..models import Imagedata


class RegistrationForm(FlaskForm):
    """

    """
    path = FileField('Bild hier hochladen',
                     validators=[
                         Optional(),
                         FileRequired(),
                         FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
                     ])
    startdate = DateField('Anfangsdatum',
                          format='%Y-%m-%d',
                          validators=[DataRequired()])
    enddate = DateField('Enddatum',
                        format='%Y-%m-%d',
                        validators=[DataRequired()])
    text = StringField('Anmerkungen')
    submit = SubmitField('Einreichen')
