# app/newupload/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from ..models import Imagedata

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    startdate = StringField('Start date', validators=[DataRequired()])
    enddate = StringField('End date', validators=[DataRequired()])
    text = StringField('Comments', validators=[DataRequired()])
    submit = SubmitField('Submit')
  