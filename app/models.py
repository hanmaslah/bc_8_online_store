# import os
from flask import Flask
from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# os.chdir('/users/maslah/documents/Python/bc-8-online-store')


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(10))

    def __init__(self, fname, lname, username, password, phone):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.phone = phone
        self.set_password(password)

    def set_password(self, password_hash):
        '''Sets password to a hashed password
        '''
        self.password = generate_password_hash(password_hash)

    def verify_password(self, password_hash):
        '''Checks if password matches
        '''
        return check_password_hash(self.password, password_hash)

    def __repr__(self):
        return '<Users %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Products(db.Model):
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    unit_price = db.Column(db.Integer)
    description = db.Column(db.Text)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))

    def __init__(self, name, unit_price, store_id, description):
        self.name = name
        self.unit_price = unit_price
        self.store_id = store_id
        self.description = description

    def __repr__(self):
        return '<Product %r>' % self.name


class Stores(db.Model):
    __tablename__ = 'stores'
    id = db.Column('store_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    user = db.relationship(Users, foreign_keys=[user_id], backref='users')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Store %r>' % self.name
