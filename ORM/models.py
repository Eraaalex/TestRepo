from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # объект приложения Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store_2.db' # привязываем базу данных
db = SQLAlchemy(app) # создаем объект SQLAlchemy

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(80), nullable=False)
    valid_thru = db.Column(db.String(10), nullable=False)
    holder_name = db.Column(db.String(80), nullable=False)
    cvc = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.number}'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80))
    user_password = db.Column(db.String)
    FIO=db.Column(db.String)
    address=db.Column(db.String)

    id_card=db.Column(db.Integer, db.ForeignKey('cards.id'))
    card = db.relationship('Card', backref=db.backref('User', lazy=False))

    registration_date=db.Column(db.DateTime)
    birth_date=db.Column(db.DateTime)
    def __repr__(self):
        return f'{self.id} {self.login} {self.FIO} '

class Category(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.name}'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    id_category=db.Column(db.Integer, db.ForeignKey('Category.id'))
    category= db.relationship('Category', backref=db.backref('Product', lazy=False))

    name=db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id} {self.name}'



class OrderUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    id_user = db.Column(db.Integer, db.ForeignKey('User.id'))
    user= db.relationship('User', backref=db.backref('OrderUser', lazy=False))

    order_date= db.Column(db.DateTime)
    cost=db.Column(db.Integer)
    def __repr__(self):
        return f'{self.id} {self.id_user} {self.order_date}'

class OrderHistory(db.Model):
    id=db.Column(db.Integer, primary_key=True)

    id_order= db.Column(db.Integer, db.ForeignKey('OrderUser.id'))
    order = db.relationship('OrderUser', backref = db.backref('OrderHistory', lazy=False))

    id_products = db.Column(db.Integer, db.ForeignKey('Product.id'))
    products = db.relationship('Product', backref=db.backref('OrderHistory', lazy=False))

    amount= db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id} {self.name}'


    # card = Card(number='4732112818833292', valid_thru='05/2023', holder_name='Judith Wagner', cvc=143)
    # user = User(login='1i9rh@gmail.com1i9rh@gmail.com', user_password='xC_w6w', FIO='Орлов Дмитрий Даниилович',
    #             address='123627, Москва, ул.Новотушинская, 20, кв.99', id_card=1, registration_date=datetime.now(),
    #             birth_date=datetime.now, cards=card)
    # db.session.add(user)
