from flask import Flask, render_template, request, redirect, session, url_for
from application.models import loginModel, loginInformation, registerModel, member, orders, product, productModel, productEditModel
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from application.__init__ import app, db, bcrypt
from flask_wtf import FlaskForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    loginForm = loginModel()
    if(request.method=='POST'):
        stored_password = bcrypt.generate_password_hash(("password"), rounds=12).decode('utf-8')
        input_username = loginForm.username.data
        inputed_password = loginForm.password.data
        user = loginInformation.query.filter_by(username=input_username).first()
        if(user != None and inputed_password != None):
            if(bcrypt.check_password_hash(user.password, inputed_password) == True):
                session['logged_in'] = True
                session['username'] = user.id
                return redirect(url_for("profile"))
        else:
            message = 'Invalid Username or Password'
            return render_template('login_page.html', loginForm = loginModel(), message = message)

    return render_template('login_page.html', loginForm = loginModel(), message = message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = registerModel()
    message = ""
    if(request.method == 'POST'):
        input_username = registerForm.username.data
        input_password = registerForm.password.data
        input_name = registerForm.name.data
        input_contact_number = registerForm.contact_number.data
        encrypted_password = bcrypt.generate_password_hash((input_password), rounds=12).decode('utf-8')
        new_user_main = member()
        new_user_login = loginInformation(username=input_username, password=encrypted_password)
        new_user_main = member(name = input_name, contact_number = input_contact_number, start_date = datetime.now(), login=new_user_login)
        user = loginInformation.query.filter_by(username=input_username).first()
        if(user == None):
            db.session.add(new_user_login)
            db.session.add(new_user_main)
            db.session.commit()
            return redirect(url_for("login"))
        else:
            message = "Invalid Username"    
    return render_template('register_page.html', registerForm = registerModel(), message = message)

@app.route('/logout')
def logout():
    if(session.get('logged_in', None) == True):
        session['logged_in'] = None
        session['username'] = None
        return redirect(url_for("login"))

    else:
        return redirect(url_for("login"))

@app.route('/profile')
def profile():
    if(session.get('logged_in', None) == True):
        user_order = orders.query.filter_by(customer_id = session['username']).first()
        user = member.query.filter_by(id = session['username']).first()
        user_name = user.name
        joined_on = user.start_date
        return render_template('profile.html', user_order = user_order, user_name = user_name, joined_on = joined_on)
    return redirect(url_for("login"))


@app.route('/neworder')
def neworder():
    if(session.get('logged_in', None) == True):
        all_products = product.query.all()
        return render_template('new_order.html', all_products = all_products)
    else:
        return redirect(url_for('login'))

@app.route('/createorder/<int:id>/<int:price>', methods=['GET', 'POST'])
def createorder(id, price):
    if(session.get('logged_in', None) == True):
        new_order = orders(product_id = id, customer_id = session.get('logged_in'), price = price)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('profile'))
    else: 
        return redirect(url_for('login'))

@app.route('/vieworder')
def vieworder():
    if(session.get('logged_in', None) == True):
        all_orders = orders.query.filter_by(customer_id= session.get('username', None)).all()
        all_products = product.query.all()
        username_query = member.query.filter_by(id = session.get('username')).first()
        user_name = username_query.name
        return render_template('view_order.html', all_orders = all_orders, all_products = all_products, user_name = user_name)
    else:
        return redirect(url_for('login'))



@app.route('/newproduct', methods=['GET', 'POST'])
def newproduct():
    if(session.get('logged_in', None) == True):
        message = ''
        
        if(request.method=='POST'):
            productForm = productModel()
            input_name = productForm.name.data
            input_price = productForm.price.data
            new_prod = product(name = input_name, price = input_price)
            same_product_check = product.query.filter_by(name=input_name).first()
            if(same_product_check == None):
                db.session.add(new_prod)
                db.session.commit()
                all_products = product.query.all()
                return redirect(url_for('profile'))
            else:
                message = "Invalid Product name"
                return render_template('new_product.html', productForm = productModel(), message = message)
    
        return render_template('new_product.html', productForm = productModel(), message = message)
    else:
        return redirect(url_for('login'))
    return render_template('new_product.html', productForm = productModel(), message = message)
    
@app.route('/viewproduct')
def viewproduct():
    if(session.get('logged_in', None) == True):
        all_products = product.query.all()
        return render_template('view_products.html', all_products = all_products)
    else:
        return redirect(url_for('login'))
    return render_template('view_products.html', all_products = all_products)

@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updateProduct(id):
    product_name = ''
    if(session.get('logged_in', None) == True):
        product_in_use = product.query.get(id)
        product_name = product_in_use.name
        if(request.method=='POST'):
            updateproductForm = productEditModel()
            new_name = updateproductForm.name.data
            new_price = updateproductForm.price.data
            product_in_use.name = new_name
            product_in_use.price = new_price
            db.session.commit()
            return redirect(url_for('viewproduct'))
        return render_template('update_product.html', product_name = product_name, updateproductForm = productEditModel())
    else:
        return redirect(url_for('login'))
