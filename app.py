from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta

from alerts import send_buy_alert
from scheduler import simulate
from database import get_last_prices

app = Flask(__name__)

# --- DASHBOARD ---
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# --- API: REAL DATA FROM DB ---
@app.route("/api/prices")
def api_prices():
    return jsonify(get_last_prices())

# 🔥 TEST ALERT — WYSYŁANY PRZY STARCIE APLIKACJI
send_buy_alert(
    price=99999,
    reason="START TEST – jeśli to widzisz, webhook działa"
)

if __name__ == "__main__":
    simulate()  # uruchamia scheduler (fetch + analiza)
    app.run(host="0.0.0.0", port=5000)
