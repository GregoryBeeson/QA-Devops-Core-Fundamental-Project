from flask import Flask, render_template, request
from application.models import loginModel
from flask_bcrypt import Bcrypt
from application.__init__ import app, bcrypt


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    displaySection = "Error"
    loginForm = loginModel()
    if(request.method=='POST'):
        tableIndicator = loginForm.tableIndicator.data
        username = loginForm.username.data
        password = bcrypt.generate_password_hash(loginForm.password.data) 
        print(password)
        if(tableIndicator == Member):
            
    return render_template('login_page.html', loginForm = loginModel())