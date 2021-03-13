from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import routes


app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['Secret Key'] = ''
db = SQLAlchemy(app)