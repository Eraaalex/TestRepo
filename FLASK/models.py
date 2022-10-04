from datetime import datetime
from orm.app import db, app

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
    FIO = db.Column(db.String)
    address=db.Column(db.String)

    id_card=db.Column(db.Integer, db.ForeignKey('card.id'))
    card=db.relationship('Card', backref=db.backref('user',lazy=False))

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
    id_category=db.Column(db.Integer, db.ForeignKey('category.id'))
    category= db.relationship('Category', backref=db.backref('product', lazy=False))
    name=db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)

    # for flask:
    description =db.Column(db.String)
    img=db.Column(db.String)


    def __repr__(self):
        return f'{self.id} {self.name}'

class Feedback(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    # fb=db.relationship('User', backref=db.backref('feedback', lazy=False))
    text=db.Column(db.String)
    def __repr__(self):
        return f'{self.login} {self.text}'

class OrderUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('orderuser', lazy=False))

    order_date= db.Column(db.DateTime)
    cost=db.Column(db.Integer)
    def __repr__(self):
        return f'{self.id} {self.id_user} {self.order_date}'

class OrderHistory(db.Model): # связь содержимого товара с заказом пользователя
    id=db.Column(db.Integer, primary_key=True)

    id_order = db.Column(db.Integer, db.ForeignKey('order_user.id'))
    order = db.relationship('OrderUser', backref=db.backref('orderhistory', lazy=False))

    id_product = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', backref=db.backref('orderhistory', lazy=False))

    amount = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id} {self.name}'