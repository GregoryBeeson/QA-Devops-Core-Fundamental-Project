from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

template_dir = "../templates"
app = Flask(__name__, template_folder=template_dir)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'caD1ObGOHzqV1Trn'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:NLsc8KzhOgr7aeaP@35.197.197.61/test"

from application import routes