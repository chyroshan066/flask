from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, RadioField, SelectField, validators, SubmitField

class ContactForm(FlaskForm):
    name = StringField("Name of Student", [validators.DataRequired("Please enter your name.")])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField('Address')
    email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    age = IntegerField("Age")
    language = SelectField("Languages", choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")