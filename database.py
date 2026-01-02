import sqlite3

def init_db():
    conn = sqlite3.connect('data/prices.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            world TEXT,
            price INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_price(world, price):
    conn = sqlite3.connect('data/prices.db')
    c = conn.cursor()
    c.execute('INSERT INTO prices (world, price) VALUES (?, ?)', (world, price))
    conn.commit()
    conn.close()

def get_last_prices(world, limit=20):
    conn = sqlite3.connect('data/prices.db')
    c = conn.cursor()
    c.execute(
        'SELECT price FROM prices WHERE world=? ORDER BY timestamp DESC LIMIT ?',
        (world, limit)
    )
    rows = c.fetchall()
    conn.close()
    return [r[0] for r in rows]
