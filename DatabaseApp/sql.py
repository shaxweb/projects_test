import sqlite3 as sql

db = sql.connect("data.db")
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY,
  username TEXT,
  password TEXT
)""")


def register(username, password):
  cur.execute("INSERT INTO users(username, password) VALUES(?,?)", (username, password))
  db.commit()


def get_users():
  return cur.execute("SELECT * FROM users").fetchall()