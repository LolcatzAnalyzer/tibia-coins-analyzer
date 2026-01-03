from fetcher import fetch_tc_price
from database import insert_price
from analyzer import analyze

def simulate():
    price = fetch_tc_price()
    insert_price(price)
    analyze(price)
