def make_decision(buy_price: float, sell_price: float) -> str:
    """
    Simple trading decision based on spread.
    """

    if buy_price is None or sell_price is None:
        return "WAIT"

    spread = sell_price - buy_price

    if spread >= 3000:
        return "SELL"
    elif spread <= 1000:
        return "BUY"
    else:
        return "WAIT"
