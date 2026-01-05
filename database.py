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
    conn = get_connection()
    c = conn.cursor()

    result = []
    worlds = ['Secura', 'Bona', 'Refugia']

    for world in worlds:
        c.execute("""
            SELECT buy, sell
            FROM world_prices
            WHERE world = ?
            ORDER BY timestamp DESC
            LIMIT 12
        """, (world,))

        rows = c.fetchall()

        buy_prices = [r[0] for r in rows if r[0] is not None]
        sell_prices = [r[1] for r in rows if r[1] is not None]

        trend = calculate_trend(buy_prices)

        latest_buy = buy_prices[0] if buy_prices else None
        latest_sell = sell_prices[0] if sell_prices else None

        result.append({
            "world": world,
            "buy": latest_buy,
            "sell": latest_sell,
            "trend": trend
        })

    conn.close()
    return result

