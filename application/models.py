from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from flask_sqlalchemy import SQLAlchemy
from application.__init__ import db

class loginModel(FlaskForm):
    tableIndicator = SelectField('Please select an option:', choices=[('Member'), ('Staff')])
    username = StringField('Login: ')
    password = StringField('Password: ')
    submit = SubmitField('Submit')

class registerModel(FlaskForm):
    tableIndicator = 'Member'
    username = StringField('Username: ')
    password = StringField('Password: ')
    submit = SubmitField('Submit')

class loginInformation(db.Model):
    #Primary Key for test will be changed to foreigh linked to the user
    id = db.Column(db.Integer, primary_key=True)
    userClass = db.Column(db.String(7), nullable = False)
    username = db.Column(db.String(30), nullable = False, unique=True)
    password = db.Column(db.String(60), nullable = False)

db.create_all()