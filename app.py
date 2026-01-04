from flask import Flask, render_template, jsonify
from datetime import datetime
from fetcher import fetch_tc_price
from database import get_prices

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/prices")
def api_prices():
    prices = get_prices(limit=100)
    return jsonify(prices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
