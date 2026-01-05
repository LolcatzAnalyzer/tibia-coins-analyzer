def trading_hint(buy, sell):
    spread = sell - buy

    if spread >= 1500:
        return "BUY"
    elif spread <= 600:
        return "SELL"
    else:
        return "WAIT"
