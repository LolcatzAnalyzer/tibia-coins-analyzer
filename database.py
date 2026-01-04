import sqlite3
import os

DB_PATH = "data/prices.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_price(timestamp, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO prices (timestamp, price) VALUES (?, ?)",
        (timestamp, price)
    )
    conn.commit()
    conn.close()

def get_prices(limit=100):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT timestamp, price FROM prices ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cur.fetchall()
    conn.close()

    return [
        {"timestamp": ts, "price": price}
        for ts, price in reversed(rows)
    ]
