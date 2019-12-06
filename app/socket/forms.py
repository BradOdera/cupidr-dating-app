from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class SendText(FlaskForm):
    submit = SubmitField('Type here ...')
