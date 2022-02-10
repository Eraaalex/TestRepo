from service import *
import unittest

class TestORM(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = db
        cls.db.create_all()

    @classmethod
    def tearDownClass(cls) -> None:
        db.session.close()
        cls.db.drop_all()
    def tearDown(self) -> None:
        self.db.session.rollback()
        Card.query.delete()
        User.query.delete()
        Category.query.delete()
        Product.query.delete()
        OrderUser.query.delete()
        OrderHistory.query.delete()
    def test_AddCard(self):
        card= addCard('0000000000000000','01/2021','Charlie Gordon',cvc=111)
        self.assertEqual(Card.query.one(),card)

    def test_AddUser(self):
        c = addCard('0000000000000000', '01/1966', 'Charlie Gordon', cvc=111)
        user = addUser(c,'smth@smth.com','password','Daniel Keyes', 'NewYork')
        self.assertEqual(User.query.one(),user)

    def test_AddCategory(self):
        cat = addCategory('Book')
        self.assertEqual(Category.query.one(),cat)
    def test_AddProduct(self):
        cat = addCategory('Book')
        pr = addProduct(cat,'Flowers for Algernon',1,1e6)
        self.assertEqual(Product.query.one(),pr)

    def test_AddOrderUser(self):
        c = addCard('0000000000000000', '01/2021', 'Charlie Gordon', cvc=111)
        us= addUser(c,'smth@smth.com','password','Daniel Keyes', 'NewYork')
        order= addOrderUser(us)
        self.assertEqual(OrderUser.query.one(),order)

    def test_AddOrderLine(self):
        cat = addCategory('Book')
        pr = addProduct(cat,'Flowers for Algernon',1,1e6)
        c = addCard('0000000000000000', '01/2021', 'Charlie Gordon', cvc=111)
        us = addUser(c, 'smth@smth.com', 'password', 'Daniel Keyes', 'NewYork')
        order = addOrderUser(us)
        ord_line=addOrderLine(order,pr)
        self.assertEqual(OrderHistory.query.one(),ord_line)

    def test_addFeedback(self):
        login='login.com'
        text='i love this store'
        fb=addFeedback(login,text)
        self.assertEqual(Feedback.query.one(),fb)

