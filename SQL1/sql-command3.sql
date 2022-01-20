SELECT FIO, login,user_password FROM user WHERE login= 'kdibbert@hotmail.com' and FIO='Ульянова Валерия Александровна'
-- вывод по имени и логину соответсвующего пароля пользователя

SELECT id,name AS product_name FROM products WHERE id_category = (SELECT id from category where name='Книга') ;
-- вывод наименований и номеров всех товаров,соответсвующих выбранной категории

SELECT id as 'order number',
 (SELECT FIO FROM user WHERE user.id=id_order) as 'user name',
 (SELECT address FROM user WHERE user.id=id_order) as 'delivery address'
 FROM order_history WHERE id_order= (SELECT id_user from order_user where order_date='12-01-2021');
-- вывод номера заказа, имени пользователя и адреса доставки, пользователей, заказавших в определенную дату

SELECT (SELECT name FROM products WHERE products.id=id_products) as 'products name',
id_order as 'order number' FROM order_history WHERE id_order= 
 (SELECT id_user from order_user where order_date='11-08-2021' and id_order=(SELECT id from user where FIO='Орлова Дарья Евгеньевна'));
-- вывод по имени и дате заказа его содержимое

SELECT name as 'product name',amount FROM products WHERE name='Louis Vuitton: Catwalk' ;
-- вывод кол-ва выбранного товара на складе 
