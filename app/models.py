from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager

app = Flask(__name__)


class Users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    username = db.Column(db.String(50))
    password = db.Column(db.String(20))
    phone = db.Column(db.String(10))

    def __init__(self, name, username, phone, password):
        self.name = name
        self.username = username
        self.phone = phone
        self.password = password

    @property
    def password(self):
        '''prevents access to password
        property
        '''
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        '''Sets password to a hashed password
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        '''Checks if password matches
        '''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Products(db.Model):
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Integer)
    category = db.Column(db.String(10))

    def __init__(self, name, category, unit_price, quantity):
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.quantity = quantity

    def __repr__(self):
        return '<User %r>' % self.username\



class Store(db.Model):
    id = db.Column('store_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
