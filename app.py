from flask import Flask, render_template, jsonify
from fetcher import fetch_world_prices
from database import init_db, insert_world_prices, get_latest_world_prices

app = Flask(__name__)

# inicjalizacja bazy przy starcie
init_db()


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/worlds")
def api_worlds():
    data = get_latest_world_prices()
    return jsonify(data)


@app.route("/api/fetch")
def api_fetch():
    rows = fetch_world_prices()
    if rows:
        insert_world_prices(rows)
    return {"status": "ok", "rows": len(rows)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
