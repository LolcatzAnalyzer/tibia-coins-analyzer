import requests

WORLDS = ["Secura", "Bona", "Refugia"]

def fetch_world_tc_prices():
    results = []

    for world in WORLDS:
        url = f"https://api.tibiadata.com/v4/world/{world}"
        r = requests.get(url, timeout=10)
        data = r.json()

        offers = data["world"]["market"]["offers"]
        tc_offers = [o for o in offers if o["item"] == "Tibia Coin"]

        buy = max((o["price"] for o in tc_offers if o["type"] == "buy"), default=None)
        sell = min((o["price"] for o in tc_offers if o["type"] == "sell"), default=None)

        results.append({
            "world": world,
            "buy": buy,
            "sell": sell
        })

    return results
