from datetime import datetime
from service import *

db.create_all()
card = addCard()
user = addUser(card)
category= addCategory()
product = addProduct(category)
order = addOrderUser(user)
order_line = addOrderLine(order,product)
db.session.commit()
