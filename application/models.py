from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from flask_sqlalchemy import SQLAlchemy
from application.__init__ import db

class loginModel(FlaskForm):
    username = StringField('Login: ')
    password = StringField('Password: ')
    submit = SubmitField('Submit')

class registerModel(FlaskForm):
    username = StringField('Username: ')
    password = StringField('Password: ')
    name = StringField('Name: ')
    contact_number = StringField('Number: ', validators = [Length(min=11, max=11)])
    submit = SubmitField('Submit')

class loginInformation(db.Model):
    #Primary Key for test will be changed to foreigh linked to the user
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db. Integer, db.ForeignKey("member.id"))
    username = db.Column(db.String(30), nullable = False, unique=True)
    password = db.Column(db.String(60), nullable = False)

class member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.relationship('loginInformation', backref = 'loginInformation', uselist = False)
    name = db.Column(db.String(30), nullable = False)
    contact_number = db.Column(db.String(11), nullable = False)
    start_date= db.Column(db.DateTime, default=db.func.now(), nullable = False)
    order = db.relationship('order', backref='order')

class order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    price = db.Column(db.Integer)


class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Integer, nullable=False)












"""
class staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable = False)
    contact_number = db.Column(db.String(11), nullable = False)
    start_date= db.Column(db.DateTime, default=db.func.now(), nullable = False)
    admin = db.Column(db.Boolean, nullable = False)
"""

"""

"""
"""
class loginInformationStaff(db.Model):
    #Primary Key for test will be changed to foreigh linked to the user
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db. Integer, db.ForeignKey("member.id"))
    userClass = db.Column(db.String(7), nullable = False)
    username = db.Column(db.String(30), nullable = False, unique=True)
    password = db.Column(db.String(60), nullable = False)
"""

db.create_all()
