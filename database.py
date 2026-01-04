import sqlite3

DB_PATH = "prices.db"

def get_prices(limit=100):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            price INTEGER
        )
    """)

    cur.execute("""
        SELECT timestamp, price
        FROM prices
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cur.fetchall()
    conn.close()

    return [
        {"timestamp": row["timestamp"], "price": row["price"]}
        for row in reversed(rows)
    ]
