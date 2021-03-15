from flask import Flask, render_template, request
from application.models import loginModel
from application.__init__ import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    displaySection = "Error"
    loginForm = loginModel()
    if(request.method=='POST'):
        tableIndicator = loginForm.tableIndicator.data
        username = loginForm.username.data
        password = loginForm.username.data
    return render_template('login_page.html', loginForm = login())