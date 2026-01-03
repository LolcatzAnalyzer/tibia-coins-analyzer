import sqlite3
import os

DB_PATH = "data/prices.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            world TEXT,
            price INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def insert_price(world, price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO prices (world, price) VALUES (?, ?)",
        (world, price)
    )

    conn.commit()
    conn.close()
