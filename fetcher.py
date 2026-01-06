import requests
from bs4 import BeautifulSoup

WORLDS = ["Secura", "Bona", "Refugia"]

URL = "https://www.tibia.com/charactertrade/?subtopic=currenttrades"


def fetch_world_prices():
    response = requests.get(URL, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = []

    table = soup.find("table", class_="TableContent")
    if not table:
        return rows

    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 5:
            continue

        world = tds[1].text.strip()
        if world not in WORLDS:
            continue

        try:
            buy = int(tds[3].text.replace(",", "").strip())
            sell = int(tds[4].text.replace(",", "").strip())
        except ValueError:
            continue

        rows.append({
            "world": world,
            "buy": buy,
            "sell": sell
        })

    return rows
