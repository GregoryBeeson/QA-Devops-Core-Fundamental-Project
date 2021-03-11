from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class member(db.Model()):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(50))
    number = db.Column(db.Integer(10))
    starDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime)
    equipmentInUse = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=True)

class staff(db.Model()):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(50))
    number = db.Column(db.Integer(10))
    starDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime)
    Employed = db.Column(db.Bool, nullable=False)
    equipmentInUse = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=True)

class LoginDetails():
    id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)

class equipment():
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(30), nullable=False)
    inUse = db.Column(db.Bool, nullable=False)