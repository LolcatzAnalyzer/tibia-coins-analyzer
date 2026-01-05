def calculate_trend(prices: list[float]) -> str:
    if len(prices) < 6:
        return "NO DATA"

    first_half = prices[:len(prices)//2]
    second_half = prices[len(prices)//2:]

    avg_first = sum(first_half) / len(first_half)
    avg_second = sum(second_half) / len(second_half)

    if avg_second > avg_first * 1.01:
        return "UP"
    elif avg_second < avg_first * 0.99:
        return "DOWN"
    else:
        return "FLAT"
