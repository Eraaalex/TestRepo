from For_sql import *
import unittest
class Test_DB(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.db=database(path=":memory:")
        cursor = self.db.get_cursor()
    @classmethod
    def tearDownClass(self):
        self.db.conn.close()
    def setUp(self):
        self.db.get_cursor()
        test_user=('com@gmail.com', 'Eralex','PersonName', 'PersonAdress', 1,'2020-07-30' , '11-08-1998')
        self.db.cur.execute("INSERT INTO user(login,user_password,FIO,address,id_card,registation_date,birth_date) VALUES (?,?,?,?,?,?,?)",test_user)
        self.id_user=self.db.cur.lastrowid
        self.db.cur.execute("INSERT INTO card(number,valid_thru,holder_name,cvc) VALUES (?,?,?,?)",('55369138700144016','08/2026','Cardholder Name',390)) #вставляем данные карты пользователя


        self.db.cur.execute('INSERT INTO category(name) VALUES (category_0)')
        self.id_test_cat=self.db.cur.lastrowid
        self.db.cur.execute('INSERT INTO products(name,amount) VALUES (product_0,14)')
        self.id_test_pro =self.db.cur.lastrowid
        self.amount_test_pro=14

        self.db.commit()

    def tearDown(self) -> None:
        self.db.cur.execute('DELETE FROM card where id=(SELECT id_card FROM user where id=?)', (self.id_user,))
        self.db.cur.execute('DELETE FROM user where id=?',(self.id_user,))
        self.db.commit()
        self.db.cur.close()

    def test_get_password(self):
        id=self.db.get_password('com@gmail.com','PersonName')
        self.assertEqual(out_id,self.id)

    # def test_get_products(self):#(?)
    #     self.assertEqual(self.db.get_products(categoty),self.id_test_cat) # the function outputs two values

    def test_get_number_order(self):
        pass
    def test_get_order(self):
        pass

    def test_get_amount(self):
        amount=self.db.get_amount(self.name_test_pro)
        self.assertEqual(amount,self.amount_test_pro)
    def test_add_user(self):
        id=self.db.add_user('smth@smth.com','Name')
        test=self.db.cur.execute("SELECT id FROM users WHERE FIO='Name' and login='smth@smth.com'")
        self.db.cur.execute("DELETE FROM users WHERE FIO='Name' and login='smth@smth.com'")
        self.db.conn.commit()
        self.assertEqual(test,id)

if __name__=='__main__':
    unittest.main(failfast=True)


