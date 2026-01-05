from trend import calculate_trend
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
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    result = []

    worlds = ['Secura', 'Bona', 'Refugia']

    for world in worlds:
        c.execute("""
            SELECT price
            FROM world_prices
            WHERE world = ?
            ORDER BY timestamp DESC
            LIMIT 12
        """, (world,))

        rows = c.fetchall()
        prices = [r[0] for r in rows]

        trend = calculate_trend(prices)

        latest_price = prices[0] if prices else None

        result.append({
            "world": world,
            "price": latest_price,
            "trend": trend
        })

    conn.close()
    return result
