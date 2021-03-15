from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField


class loginModel(FlaskForm):
    tableIndicator = SelectField('Please select an option', choices=[('Member'), ('Staff')])
    username = StringField('Login: ')
    password = StringField('Password: ')
    submit = SubmitField('Submit')