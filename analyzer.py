from database import get_last_prices
from alerts import send_buy, send_sell

def analyze(world):
    prices = get_last_prices(world)

    if len(prices) < 5:
        return

    avg = sum(prices) / len(prices)
    current = prices[0]

    if current < avg * 0.95:
        send_buy(world, current)

    if current > avg * 1.05:
        send_sell(world, current)
