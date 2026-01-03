from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# --- DASHBOARD ---
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# --- API: TEMP DATA ---
@app.route("/api/prices")
def api_prices():
    now = datetime.now()
    prices = []

    base_price = 36000

    for i in range(30):
        prices.append({
            "timestamp": (now - timedelta(minutes=30 - i)).strftime("%H:%M"),
            "price": base_price + random.randint(-300, 300)
        })

    return jsonify(prices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
