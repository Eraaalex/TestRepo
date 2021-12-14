
from For_sql import *
import unittest

class Test_DB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db=database(path=":memory:")
        cursor = cls.db.get_cursor()
        # create table
        command='''
        CREATE TABLE card(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT NOT NULL,
        valid_thru TEXT NOT NULL,
        holder_name TEXT NOT NULL,
        cvc INTEGER NOT NULL
        );

        CREATE TABLE category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE order_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_order INTEGER,
            id_products INTEGER,
            amount INTEGER,
            FOREIGN KEY (id_order) REFERENCES order_user(id),
            FOREIGN KEY (id_products) REFERENCES products(id)
        );

        CREATE TABLE order_user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER,
            order_date TEXT,
            cost INTEGER,
            FOREIGN KEY (id_user) REFERENCES user(id)
        );

        CREATE TABLE products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_category INTEGER NOT NULL,
        name TEXT NOT NULL,
        amount INTEGER,
        price INTEGER,
        discount INTEGER,
        FOREIGN KEY (id_category) REFERENCES category(id)
        );

        CREATE TABLE user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT,
        user_password TEXT,
        FIO TEXT,
        address TEXT,
        id_card INTEGER UNIQUE,
        registation_date TEXT,
        birth_date TEXT,
        FOREIGN KEY (id_card) REFERENCES card(id)
        );
        '''
        cls.db.cur.executescript(command)
        cls.db.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.db.conn.close()

    def setUp(self):
        self.db.get_cursor()

        # add test_user's card
        self.db.cur.execute("INSERT INTO card(number,valid_thru,holder_name,cvc) VALUES (?,?,?,?)",('55369138700144016','08/2026','Cardholder Name',390)) #вставляем данные карты пользователя

        # add test_user
        self.inf_test_user=('com@gmail.com', 'Eralex','PersonName', 'PersonAdress', 1,'2019-11-23','2019-11-23')
        self.db.cur.execute("INSERT INTO user(login,user_password,FIO,address,id_card,registation_date, birth_date) VALUES (?,?,?,?,?,?,?)",self.inf_test_user)
        self.id_user=self.db.cur.lastrowid

        # add category
        self.db.cur.execute("INSERT INTO category(name) VALUES ('category_0')")
        self.id_category=self.db.cur.lastrowid

        # add product
        comma="INSERT INTO products(id_category,name,amount) VALUES (?,?,?)"
        self.db.cur.execute(comma,(self.id_category,'product_0',123))
        self.id_product_0 =self.db.cur.lastrowid
        self.db.cur.execute(comma,(self.id_category,'product_1',113))
        self.id_product_1 = self.db.cur.lastrowid

        # add order by test_user
        self.db.cur.execute('INSERT INTO order_user(id_user,order_date) VALUES (?,?)', (self.id_user,'2021-12-21'))
        self.id_order=self.db.cur.lastrowid

        # add products include order
        self.db.cur.execute('INSERT INTO order_history(id_order,id_products) VALUES (?,?)',
                            (self.id_order,self.id_product_0))
        self.db.cur.execute('INSERT INTO order_history(id_order,id_products) VALUES (?,?)',
                            (self.id_order, self.id_product_1))
                            
        # save users who bought smth on test_date '2021-12-21'
        self.users=[(self.id_order,self.inf_test_user[2], self.inf_test_user[3])]

        self.db.conn.commit()

    def tearDown(self) -> None:
        self.db.cur.execute('DELETE FROM order_history where id_order=?', (self.id_order,))
        self.db.cur.execute('DELETE FROM order_user where id_user=?', (self.id_user,))
        self.db.cur.execute('DELETE FROM products where id=?', (self.id_product_1,))
        self.db.cur.execute('DELETE FROM products where id=?', (self.id_product_0,))
        self.db.cur.execute('DELETE FROM card where id=(SELECT id_card FROM user where id=?)', (self.id_user,))
        self.db.cur.execute('DELETE FROM user where id=?', (self.id_user,))
        self.db.cur.execute('DELETE FROM category where id=?', (self.id_category,))

        self.db.conn.commit()
        self.db.cur.close()

    def test_get_password(self): # вывод по логину и имени соответсвующего пароля пользователя
        id = self.db.get_password('com@gmail.com','PersonName')
        self.assertEqual(id,(self.inf_test_user[2],self.inf_test_user[0],self.inf_test_user[1]))

    def test_get_products(self): # вывод наименований и номеров всех товаров,соответсвующих выбранной категории
        self.assertEqual(self.db.get_products('category_0'),(self.id_product_0,'product_0')) # the function outputs two values

    def test_get_number_order(self):  # вывод номера заказа, имени пользователя и адреса доставки, пользователей, заказавших в определенную дату
        users=self.db.get_number_order('2021-12-21')
        self.assertEqual(users,self.users) # сравнение, что кортежи выведенных пользователей совпадают


    def test_get_order(self): # вывод по id_user и дате заказа его содержимое
        id=self.db.get_order(self.id_user,'2021-12-21')
        self.assertEqual(id,[('product_0',self.id_order),('product_1',self.id_order)])

    def test_get_amount(self): # вывод количества товара в наличие
        amount=self.db.get_amount('product_0')
        self.assertEqual(amount,(123,))

    def test_add_user(self):
        id=self.db.add_user('smth@smth.com','Name')
        test=self.db.cur.execute("SELECT id FROM user WHERE FIO='Name' and login='smth@smth.com'").fetchone()[0]
        self.db.cur.execute("DELETE FROM user WHERE FIO='Name' and login='smth@smth.com'")
        self.db.conn.commit()
        self.assertEqual(test,id)

if __name__=='__main__':
    unittest.main(failfast=True)
