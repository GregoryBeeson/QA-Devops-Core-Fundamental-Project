from flask import Flask

template_dir = "../templates"
app = Flask(__name__, template_folder=template_dir)
app.config['SECRET_KEY'] = 'caD1ObGOHzqV1Trn'

from application import routes