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
    "wait_user": cur.execute("SELECT * FROM wait_user WHERE id = ?", (id,)).fetchone(),
    "product": cur.execute("SELECT * FROM product WHERE id = ?", (id,)).fetchone(),
  }

def get_user_by_username(username):
  return cur.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()


def get_user_by_email(email):
  return cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()


def get_wait_user_by_token(token):
  return cur.execute("SELECT * FROM wait_users WHERE token = ?", (token,)).fetchall()


def create_wait_user(username, email, password, token):
  cur.execute("INSERT INTO wait_users(username, email, password, token) VALUES(?,?,?,?)", (username, email, password, token,))
  db.commit()


def create_user(username, email, password):
  cur.execute("INSERT INTO users(username, email, password) VALUES(?,?,?)", (username, email, password,))
  db.commit()


def create_product(title, description, price):
  cur.execute("INSERT INTO products(title, description, price) VALUES(?,?,?)", (title, description, price))
  db.commit()


create_product("iPhone", "Phone", 1500)
create_product("Samsung", "Best Phone", 1200)
create_product("Nokia", "Phone", 1500)
create_product("Novey", "Best Phone", 1200)
create_product("Nivea", "Phone", 1500)
create_product("BMW", "Best Phone", 1200)

