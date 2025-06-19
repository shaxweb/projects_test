import sqlite3 as sql

db = sql.connect("data.db")
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
  email TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products(
  id INTEGER PRIMARY KEY,
  title TEXT,
  description TEXT,
  price TEXT
)
""")

db.commit()

