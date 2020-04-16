# app/newupload/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..models import Imagedata


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    path = FileField('Upload image here',
                     validators=[
                         FileRequired(),
                         FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
                     ])
    startdate = DateField('Start date',
                          format='%Y-%m-%d',
                          validators=[DataRequired()])
    enddate = DateField('End date',
                        format='%Y-%m-%d',
                        validators=[DataRequired()])
    text = StringField('Comments')
    submit = SubmitField('Submit')
