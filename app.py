from flask import Flask, render_template, jsonify
from fetcher import fetch_tc_price
from database import get_prices, insert_price, init_db
from database import init_db, get_latest_world_prices

app = Flask(__name__)
init_db()

# 🔹 inicjalizacja bazy przy starcie aplikacji
init_db()


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/prices")
def api_prices():
    prices = get_prices(limit=100)
    return jsonify(prices)
@app.route("/api/worlds")
def api_worlds():
    return jsonify(get_latest_world_prices())


@app.route("/api/fetch")
def fetch_price():
    timestamp, price = fetch_tc_price()
    insert_price(timestamp, price)
    return {"status": "ok", "price": price}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
