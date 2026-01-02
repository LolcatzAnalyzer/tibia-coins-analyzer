from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from database import init_db
from scheduler import simulate

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Tibia Coins Analyzer</h1><p>System działa. Alerty aktywne.</p>'

if __name__ == '__main__':
    init_db()

    scheduler = BackgroundScheduler()
    scheduler.add_job(simulate, 'interval', minutes=5)
    scheduler.start()

    app.run(host='0.0.0.0', port=5000)
