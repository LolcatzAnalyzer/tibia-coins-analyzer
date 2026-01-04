import requests
from datetime import datetime
import random

def fetch_tc_price():
    # TEMP: symulacja realnej ceny (na razie)
    price = random.randint(35000, 37000)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return timestamp, price
