from flask import flask
from flask_sqlalchemy import SQLAlchemy

app.config['Secret Key'] = ''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

@app.route('/')
@app.route('/login')
def login():
    return test

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
    username = db.Column(db.String(30), nullabl=False, unique=True)
    password = db.Column(db.String(30), nullable=False)

class equipment():
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Integer(), )
if __name__ == '__main__':
    app.run(debug=True)