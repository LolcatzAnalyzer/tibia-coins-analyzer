from flask import Flask, render_template, jsonify
from database import init_db, get_latest_world_prices, insert_world_price

app = Flask(__name__)

# inicjalizacja bazy przy starcie
init_db()


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/worlds")
def api_worlds():
    return jsonify(get_latest_world_prices())


# tymczasowy endpoint do testowych danych
@app.route("/api/mock")
def mock_data():
    insert_world_price("Secura", 35200, 35800)
    insert_world_price("Bona", 34900, 35400)
    insert_world_price("Refugia", 34600, 35100)
    return {"status": "mock inserted"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
