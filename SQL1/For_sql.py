import sqlite3
class database:
    def __init__(self, path) :
        self.conn= sqlite3.connect(path)
    def get_cursor(self): #?
        self.cur=self.conn.cursor()

    def get_password(self,login,user_name):
        command = "SELECT FIO, login,user_password FROM user WHERE login=? and FIO= ?"
        self.cur.execute(command, (login,user_name))
        return self.cur.fetchone()
   
    def get_products(self,cat):
        command="SELECT id,name AS product_name FROM products WHERE id_category = (SELECT id FROM category WHERE name= ?)"
        self.cur.execute(command,(cat,))
        return self.cur.fetchone()
    def get_number_order(self,date_order):
        command="""SELECT id as 'order number',
     (SELECT FIO FROM user WHERE user.id=id_order) as 'user name',
     (SELECT address FROM user WHERE user.id=id_order) as 'delivery address'
     FROM order_history WHERE id_order= (SELECT id_user from order_user where order_date=?)"""
        self.cur.execute(command, (date_order,))
        return self.cur.fetchone()

    def get_order(self,name,date):
        command="""
        SELECT (SELECT name FROM products WHERE products.id=id_products) as 'products name',
    id_order as 'order number' FROM order_history WHERE id_order= 
     (SELECT id_user from order_user where order_date=? and id_order=(SELECT id from user where FIO=?));"""
        self.cur.execute(command, (date,name))
        return self.cur.fetchone()

    def get_amount(self,prod_name):
        command="SELECT amount FROM products WHERE name=?"
        self.cur.execute(command, (prod_name,))
        return self.cur.fetchone()
    def delete_user(self,name,login):
        self.cur.execute("BEGIN TRANSACTION;")
        self.cur.execute("DELETE FROM card WHERE id=(SELECT id_card FROM user WHERE FIO=? and login=?)",(name,login))
        self.cur.execute("DELETE FROM order_history WHERE id_order=(SELECT id FROM order_user WHERE id_user=(SELECT id FROM user WHERE FIO=? and login=?))",(name,login))
        self.cur.execute("DELETE FROM order_user WHERE id_user=(SELECT id FROM user WHERE FIO=? and login=?)",(name,login))
        self.cur.execute("DELETE FROM user WHERE FIO =? and login= ?;",(name,login))
        self.cur.execute("COMMIT;")
        self.conn.commit()

    def add_user(self,login,fio, password='password' , address='address', id_card='card', dat_reg='2001/01/01', date_birth='2001/01/01') :
        self.cur.execute("INSERT INTO user(login,user_password,FIO,address,id_card,registation_date,birth_date) VALUES (?,?,?,?,?,?,?)",
            (login, password, fio, address, id_card, dat_reg, date_birth))
        self.conn.commit()
        return self.cur.lastrowid

path="../TestRepo/SQL1/test_db.db"

#
# conn.commit()
# conn.close()
