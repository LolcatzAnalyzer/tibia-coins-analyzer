import sqlite3
from pathlib import Path

DB_PATH = Path("prices.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tc_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            world TEXT NOT NULL,
            buy INTEGER NOT NULL,
            sell INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_world_prices(prices: list[dict]):
    conn = get_connection()
    cur = conn.cursor()

    for row in prices:
        cur.execute(
            """
            INSERT INTO tc_prices (timestamp, world, buy, sell)
            VALUES (?, ?, ?, ?)
            """,
            (
                row["timestamp"],
                row["world"],
                row["buy"],
                row["sell"]
            )
        )

    conn.commit()
    conn.close()


def get_latest_world_prices():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT world, buy, sell, MAX(timestamp)
        FROM tc_prices
        GROUP BY world
    """)

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "world": r[0],
            "buy": r[1],
            "sell": r[2],
            "timestamp": r[3]
        }
        for r in rows
    ]
