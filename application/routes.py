from application import __init__
from application import models, member, staff, LoginDetails, equipment


@app.route('/')
@app.route('/login')
def login():
    return test