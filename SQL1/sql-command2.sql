UPDATE user SET birth_date = SUBSTR(birth_date, 7, 4) || '-' || SUBSTR(birth_date, 4, 2) || '-' ||
SUBSTR(birth_date, 1, 2);

UPDATE user SET registration_date = SUBSTR(registration_date, 7, 4) || '-' || SUBSTR(registration_date, 4, 2) || '-' ||
SUBSTR(registration_date, 1, 2);

SELECT login, MAX(registation_date) AS 'last_registration' FROM user GROUP BY registation_date;

SELECT  DISTINCT strftime('%Y', birth_date ) FROM user;
SELECT SUM(amount) as 'total_items' FROM products;

SELECT AVG ((strftime('%Y', 'now') - strftime('%Y', birth_date)) - (strftime('%m-%d', 'now') < strftime('%m-%d', birth_date))) as 'middle age'  FROM user WHERE 12*(strftime('%Y', 'now') - strftime('%Y', registation_date)) - (strftime('%m-%d', 'now') < strftime('%m-%d',registation_date)) + 
(strftime('%m', 'now') - strftime('%m', registation_date)) - (strftime('%d', 'now') < strftime('%d', registation_date)) < 2;