from flask import Flask, render_template, request, redirect, session, url_for
from application.models import loginModel, loginInformation, registerModel, staff
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from application.__init__ import app, db, bcrypt

#Staff Member
user = staff(name="Admin", contact_number="07856357428", start_date = db.func.now(), admin = True)
db.session.add(user)
db.session.commit()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    loginForm = loginModel()
    if(request.method=='POST'):
        tableIndicator = loginForm.tableIndicator.data
        stored_password = bcrypt.generate_password_hash(("password"), rounds=12).decode('utf-8')
        input_username = loginForm.username.data
        inputed_password = loginForm.password.data
        user = loginInformation.query.filter_by(username=input_username).first()
        if(user != 'none'):
            if(bcrypt.check_password_hash(user.password, inputed_password) == True):
                session['logged_in'] = True
                session['username'] = user.id
                return redirect(url_for("test"))
        else:
            return redirect(url_for("login"))

    return render_template('login_page.html', loginForm = loginModel())

@app.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = registerModel()
    if(request.method=='POST'):
        input_username = registerForm.username.data
        input_password = registerForm.password.data
        encrypted_password = bcrypt.generate_password_hash((input_password), rounds=12).decode('utf-8')
        new_user = loginInformation(userClass='Member', username=input_username, password=encrypted_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register_page.html', registerForm = registerModel())
        
@app.route('/test')
def test():
    if(session.get('logged_in', None) == True):
        return "YaaaaY!"
    return "No"