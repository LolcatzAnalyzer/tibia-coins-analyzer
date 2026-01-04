from database import get_last_prices

LAST_SIGNAL = None

def analyze():
    global LAST_SIGNAL

    prices = get_last_prices(10)
    if len(prices) < 10:
        return None

    avg = sum(prices) / len(prices)
    current = prices[-1]

    diff = (current - avg) / avg * 100

    print(f"AVG={avg:.2f} CURRENT={current} DIFF={diff:.2f}%")

    if diff <= -1.0 and LAST_SIGNAL != "BUY":
        LAST_SIGNAL = "BUY"
        return "BUY"

    if diff >= 1.0 and LAST_SIGNAL != "SELL":
        LAST_SIGNAL = "SELL"
        return "SELL"

    return None
