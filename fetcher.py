import requests

WORLDS = ["Secura", "Bona", "Refugia"]

TIBIA_API = "https://api.tibiadata.com/v4/world/{world}"


def fetch_world_prices():
    rows = []

    for world in WORLDS:
        try:
            url = TIBIA_API.format(world=world)
            resp = requests.get(url, timeout=10)
            data = resp.json()

            world_data = data.get("world", {})
            market = world_data.get("market", {})

            buy = market.get("buy")
            sell = market.get("sell")

            if buy and sell:
                rows.append({
                    "world": world,
                    "buy": buy,
                    "sell": sell
                })

        except Exception as e:
            print(f"Fetcher error for {world}:", e)

    return rows
