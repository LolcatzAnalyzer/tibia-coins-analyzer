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

            market = data.get("market", {}).get("data", {})

            buy_list = market.get("buy", [])
            sell_list = market.get("sell", [])

            if not buy_list or not sell_list:
                print(f"No market data for {world}")
                continue

            buy = buy_list[0]["price"]
            sell = sell_list[0]["price"]

            rows.append({
                "world": world,
                "buy": int(buy),
                "sell": int(sell)
            })

            print(f"[FETCH] {world}: buy={buy}, sell={sell}")

        except Exception as e:
            print(f"Fetcher error for {world}: {e}")

    return rows
