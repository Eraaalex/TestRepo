CREATE TABLE card (
id INTEGER PRIMARY KEY AUTOINCREMENT,
number TEXT UNIQUE NOT NULL,
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
	FOREIGN KEY (id_order) REFERENCES order_user(id)
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




