from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    printers = db.relationship('Printer', back_populates='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Printer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    brand = db.Column(db.String(64), index=True)
    model = db.Column(db.String(64), index=True)
    vendor = db.Column(db.String(64), index=True)
    product_url = db.Column(db.String(120), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='printers')
    cartridges = db.relationship('Cartridge', back_populates='printer')


class Cartridge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(64), index=True)
    brand = db.Column(db.String(64), index=True)
    model = db.Column(db.String(64), index=True)
    vendor = db.Column(db.String(64), index=True)
    product_url = db.Column(db.String(120), index=True)
    quantity = db.Column(db.Integer)
    printer_id = db.Column(db.Integer, db.ForeignKey('printer.id'))
    printer = db.relationship('Printer', back_populates='cartridges')