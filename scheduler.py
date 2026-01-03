import time
from fetcher import fetch_tc_price
from database import insert_price
from analyzer import analyze

def simulate():
    while True:
        try:
            price = fetch_tc_price()
            insert_price(price)
            analyze()
            time.sleep(300)  # co 5 minut
        except Exception as e:
            print("Scheduler error:", e)
            time.sleep(60)
