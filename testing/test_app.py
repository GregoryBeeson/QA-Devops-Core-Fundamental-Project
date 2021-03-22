from flask import Flask, session, url_for
from flask_testing import TestCase
from datetime import datetime

from application.__init__ import db, app, bcrypt
from application.models import loginInformation, member, orders, product


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY='TEST_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app
    
    def setUp(self):
        db.create_all()

        test_member = member()
        test_member_login_information = loginInformation(member_id = test_member, username = "TEST_USERNAME", password = bcrypt.generate_password_hash(("TEST_PASSWORD"), rounds=12).decode('utf-8'))
        test_member = member(login = test_member_login_information, name = "TEST_NAME", contact_number = "TEST_NUM", start_date = datetime.now())
        test_product = product(name = "TEST_PRODUCT", price = 5)
        test_order = orders(product_id = test_product.id, customer_id = test_member.id)
        db.session.add(test_member_login_information)
        db.session.add(test_member)
        db.session.add(test_product)
        db.session.add(test_order)
        db.session.commit()
        session['logged_in'] = True
        session['username'] = test_member_login_information.id
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

#pytest --cov .

#Testing

class TestViews(TestBase):

    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_get(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_logout_get(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 302)

    def test_profile_redirect_get(self):
        response = self.client.get(url_for('profile'))
        self.assertEqual(response.status_code, 302)

    def test_neworder_redirect_get(self):
        response = self.client.get(url_for('neworder'))
        self.assertEqual(response.status_code, 302)
    
    def test_createorder_get(self):
        response = self.client.get(url_for('createorder', id=1, price=1))
        self.assertEqual(response.status_code, 302)

    def test_vieworder_redirect_get(self):
        response = self.client.get(url_for('vieworder'))
        self.assertEqual(response.status_code, 302)
    
    def test_newproduct_redirect_get(self):
        response = self.client.get(url_for('newproduct'))
        self.assertEqual(response.status_code, 302)

    def test_viewproduct_redirect_get(self):
        response = self.client.get(url_for('vieworder'))
        self.assertEqual(response.status_code, 302)

    def test_updateproduct_redirect_get(self):
        response = self.client.get(url_for('updateProduct', id=1))
        self.assertEqual(response.status_code, 302)