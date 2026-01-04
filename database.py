import sqlite3
from datetime import datetime

DB_NAME = "prices.db"

def get_conn():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS world_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            world TEXT,
            buy INTEGER,
            sell INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_world_price(world, buy, sell):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO world_prices (world, buy, sell, timestamp) VALUES (?, ?, ?, ?)",
        (world, buy, sell, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

def get_latest_world_prices():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT world, buy, sell
        FROM world_prices
        WHERE id IN (
            SELECT MAX(id)
            FROM world_prices
            GROUP BY world
        )
    """)
    rows = cur.fetchall()
    conn.close()

    return [
        {"world": r[0], "buy": r[1], "sell": r[2]}
        for r in rows
    ]
