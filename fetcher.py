import requests

WORLDS = ["Secura", "Bona", "Refugia"]

MARKET_API = "https://api.tibiadata.com/v4/market/tibia-coins/{world}"


def fetch_world_prices():
    rows = []

    for world in WORLDS:
        try:
            url = MARKET_API.format(world=world)
            resp = requests.get(url, timeout=10)
            data = resp.json()

            coins = data.get("market", {}).get("tibia_coins", {})

            buy = coins.get("highest_buy_offer")
            sell = coins.get("lowest_sell_offer")

            if buy and sell:
                rows.append({
                    "world": world,
                    "buy": int(buy),
                    "sell": int(sell)
                })

        except Exception as e:
            print(f"Fetcher error for {world}: {e}")

    return rows
