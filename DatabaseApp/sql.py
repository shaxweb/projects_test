import sqlite3 as sql

db_file = "templates/data.db"

# Создание таблицы — можно оставить глобально
with sql.connect(db_file) as db:
    cur = db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY,
      username TEXT,
      password TEXT
    )""")
    db.commit()

# Всегда создавать новое подключение внутри функции
def register(username, password):
    with sql.connect(db_file) as db:
        cur = db.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
        db.commit()

def get_users():
    with sql.connect("data.db") as db:
        cur = db.cursor()
        return cur.execute("SELECT * FROM users").fetchall()