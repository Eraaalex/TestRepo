from datetime import datetime
from service import *





db.create_all()
# card = addCard()
# user = addUser(card)
# category= addCategory()
# # product = addProduct(category)
# order = addOrderUser(user)
# order_line = addOrderLine(order,product)

card = addCard()
user = addUser(card,login='special@gmail.com')
# descr=['description of this wonderful book in progress']*6
# name_pr=['C.P. Company 971-021','Louis Vuitton: Catwalk','Louis Vuitton: Celebrating Monogram','Hello, My Name Is Paul','A Denim Story: Inspirations From Bellbottoms To Boyfriends','Skira']
# link_img=['CP Company.jpg','LouviusVuitton.jpg','Lv.jpg','PaulSmith.jpg','Rizzoli.jpg','Basquiat.jpg']
# products=[]
# for i in range(len(descr)):
#     product=addProduct(category=category,name=name_pr[i], description=descr[i], image=link_img[i])
#

db.session.commit()