from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    middlename = StringField('Middle Name')
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Save User Information')


class AddressForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=30)])

    submit = SubmitField('Save Address')


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Save Email Address')