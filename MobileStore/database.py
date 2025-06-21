import sqlite3 as sql

db = sql.connect("data.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY,
  username TEXT,
  password TEXT,
  email TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS wait_users(
  id INTEGER PRIMARY KEY,
  username TEXT,
  password TEXT,
  email TEXT,
  token TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products(
  id INTEGER PRIMARY KEY,
  title TEXT,
  description TEXT,
  price INTEGER
)
""")

db.commit()


def get_all_data():
  return {
    "users": cur.execute("SELECT * FROM users").fetchall(),
    "wait_users": cur.execute("SELECT * FROM wait_users").fetchall(),
    "products": cur.execute("SELECT * FROM products").fetchall()
  }


def get_data(id):
  return {
    "user": cur.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone(),
    "wait_user": cur.execute("SELECT * FROM wait_users WHERE id = ?", (id,)).fetchone(),
    "product": cur.execute("SELECT * FROM products WHERE id = ?", (id,)).fetchone(),
  }

def get_user_by_username(username):
  return cur.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()


def get_user_by_email(email):
  return cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()


def get_wait_user_by_token(token):
  return cur.execute("SELECT * FROM wait_users WHERE token = ?", (token,)).fetchone()


def create_wait_user(username, email, password, token):
  cur.execute("INSERT INTO wait_users(username, email, password, token) VALUES(?,?,?,?)", (username, email, password, token,))
  db.commit()


def create_user(username, email, password):
  cur.execute("INSERT INTO users(username, email, password) VALUES(?,?,?)", (username, email, password,))
  db.commit()


def create_product(title, description, price):
  cur.execute("INSERT INTO products(title, description, price) VALUES(?,?,?)", (title, description, price))
  db.commit()


def delete_wait_user(id):
  cur.execute("DELETE FROM wait_users WHERE id = ?", (id,))
  db.commit()


create_product("iPhone 14", "Apple smartphone", 899)
create_product("Samsung Galaxy S22", "Android Phone", 799)
create_product("MacBook Pro", "Apple laptop", 1499)
create_product("Xiaomi Redmi", "Budget Phone", 299)
create_product("PlayStation 5", "Gaming Console", 499)
create_product("AirPods Pro", "Wireless earbuds", 249)
create_user("Shaxrux", "igrayunagitare@gmail.com", "shaxcoder")
