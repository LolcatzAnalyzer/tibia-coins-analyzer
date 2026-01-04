from flask import Flask, render_template, jsonify
from fetcher import fetch_tc_price
from database import get_prices, insert_price, init_db

app = Flask(__name__)

# ⬇️ TO JEST KLUCZOWE
init_db()

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/prices")
def api_prices():
    prices = get_prices(limit=100)
    return jsonify(prices)

@app.route("/api/fetch")
def fetch_price():
    timestamp, price = fetch_tc_price()
    insert_price(timestamp, price)
    return {"status": "ok", "price": price}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
