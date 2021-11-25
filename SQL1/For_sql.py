import sqlite3
def output_password(login,FIO):
    command = "SELECT FIO, login,user_password FROM user WHERE login=? and FIO= ?"
    cursor.execute(command, (login, FIO))
    print(cursor.fetchall())

def output_products(cat):
    command="SELECT id,name AS product_name FROM products WHERE id_category = (SELECT id FROM category WHERE name= ?)"
    cursor.execute(command,(cat,))
    print(cursor.fetchall())
def output_NumberOrder(date_order):
    command="""SELECT id as 'order number',
 (SELECT FIO FROM user WHERE user.id=id_order) as 'user name',
 (SELECT address FROM user WHERE user.id=id_order) as 'delivery address'
 FROM order_history WHERE id_order= (SELECT id_user from order_user where order_date=?)
"""
    cursor.execute(command, (date_order,))
    print(cursor.fetchall())
def output_order(name,date):
    command="""
    SELECT (SELECT name FROM products WHERE products.id=id_products) as 'products name',
id_order as 'order number' FROM order_history WHERE id_order= 
 (SELECT id_user from order_user where order_date=? and id_order=(SELECT id from user where FIO=?));
    """
    cursor.execute(command, (date,name))
    print(cursor.fetchall())
def output_amount(prod_name):
    command="SELECT name as 'product name',amount FROM products WHERE name=?"
    cursor.execute(command, (prod_name,))
    print(cursor.fetchall())

conn=sqlite3.connect('store.db')
cursor=conn.cursor()


login='fadel.devon@gmail.com'
FIO='Орлова Дарья Евгеньевна'
category='Книга'
date='11-08-2021'
product='Louis Vuitton: Catwalk'
output_password(login,FIO)
print()
output_products(category)
print()
output_NumberOrder(date)
print()
output_order(FIO,date)
print()
output_amount(product)
print()

conn.commit()
conn.close()
