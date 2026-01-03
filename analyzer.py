from database import get_last_prices
from alerts import send_buy_alert, send_sell_alert

WINDOW = 10

def analyze():
    prices = get_last_prices(WINDOW)

    if len(prices) < WINDOW:
        return

    avg = sum(prices) / len(prices)
    current = prices[-1]
    prev = prices[-2]

    # BUY
    if current < avg * 0.99:
        send_buy_alert(current, avg)

    # SELL
    if current > avg * 1.01:
        send_sell_alert(current, avg)
