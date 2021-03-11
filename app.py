from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import app

app.config['Secret Key'] = ''

if __name__ == '__main__':
    app.run(debug=True)