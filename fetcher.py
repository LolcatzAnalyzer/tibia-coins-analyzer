import requests
from bs4 import BeautifulSoup
from datetime import datetime

WORLDS = ["Secura", "Bona", "Refugia"]
BASE_URL = "https://tibiatrade.gg/coins"


def fetch_world_prices():
    """
    Zwraca listę:
    [
      {
        "timestamp": "...",
        "world": "Secura",
        "buy": 35200,
        "sell": 36100
      },
      ...
    ]
    """
    response = requests.get(BASE_URL, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("table tbody tr")

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    results = []

    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all("td")]
        if len(cols) < 4:
            continue

        world = cols[0]
        if world not in WORLDS:
            continue

        try:
            buy = int(cols[1].replace(",", ""))
            sell = int(cols[2].replace(",", ""))
        except ValueError:
            continue

        results.append({
            "timestamp": timestamp,
            "world": world,
            "buy": buy,
            "sell": sell
        })

    return results
