from models import *

def addCard(number='4732112818833292', valid_thru='09/1977', holder_name='Gavriil Troyepolsky', cvc=143):
    card=Card(number=number, valid_thru=valid_thru, holder_name=holder_name, cvc=cvc)
    db.session.add(card)
    return card

def addUser(card:Card,login='com@gmail.com',password='eralex',FIO ='Gavriil Nikolayevich Troyepolsky',address='Tambov Governorate',\
            registration_date=datetime.now(),birth_date=datetime.now()):
    user=User(login=login, user_password=password, FIO=FIO,address=address,card = card,registration_date=registration_date,birth_date=birth_date)
    db.session.add(user)
    return user
def addCategory(name='category_0'):
    category = Category(name=name)
    db.session.add(category)
    return category
def addProduct(category:Category, name='Margaret Fletcher: Architectural Styles. A Visual Guide', amount=10,price=1000, description="don't doubt it, it's a book",image="Architectural Styles.jpg" ):
    product=Product(category=category,name=name, amount=amount,price=price, description=description,img=image)
    db.session.add(product)
    return product
def addOrderUser(user:User,cost=1000,order_date=datetime.now()):
    order=OrderUser(user=user,order_date=order_date,cost=cost)
    db.session.add(order)
    return order

def addOrderLine(order_num:OrderUser,product:Product,amount=1):
    order_line=OrderHistory(order=order_num,product=product,amount=amount)
    db.session.add(order_line)
    return order_line
