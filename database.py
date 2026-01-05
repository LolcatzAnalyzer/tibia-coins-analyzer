import sqlite3
from datetime import datetime

DB_PATH = "prices.db"


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS world_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            world TEXT NOT NULL,
            buy INTEGER,
            sell INTEGER,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_world_prices(rows):
    conn = get_connection()
    cur = conn.cursor()

    for row in rows:
        cur.execute(
            """
            INSERT INTO world_prices (world, buy, sell, timestamp)
            VALUES (?, ?, ?, ?)
            """,
            (
                row["world"],
                row["buy"],
                row["sell"],
                datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            )
        )

    conn.commit()
    conn.close()


def get_latest_world_prices():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT world, buy, sell, MAX(timestamp)
        FROM world_prices
        GROUP BY world
        ORDER BY world
    """)

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "world": r[0],
            "buy": r[1],
            "sell": r[2],
            "timestamp": r[3],
        }
        for r in rows
    ]
