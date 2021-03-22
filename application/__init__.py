from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

template_dir = "../templates"
app = Flask(__name__, template_folder=template_dir)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


#change on deployment
app.config['SECRET_KEY'] = 'caD1ObGOHzqV1Trn'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:NLsc8KzhOgr7aeaP@35.197.197.61/project"
app.config['SQALCHEMY_TRACK_MODIFICATIONS']=True

from application import routes