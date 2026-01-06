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

            stats = data.get("market", {}).get("statistics", {})

            buy = stats.get("buy", {}).get("highest")
            sell = stats.get("sell", {}).get("lowest")

            if buy is None or sell is None:
                print(f"[WARN] No prices for {world}: {stats}")
                continue

            rows.append({
                "world": world,
                "buy": int(buy),
                "sell": int(sell)
            })

            print(f"[FETCH] {world}: buy={buy}, sell={sell}")

        except Exception as e:
            print(f"[ERROR] Fetcher error for {world}: {e}")

    return rows
