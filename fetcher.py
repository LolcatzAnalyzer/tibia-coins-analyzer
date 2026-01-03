import requests
from bs4 import BeautifulSoup

def fetch_tc_price():
    url = "https://www.tibia.com/charactertrade/?subtopic=currentcharactertrades"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10)

    soup = BeautifulSoup(r.text, "html.parser")

    prices = []
    for cell in soup.select("td.Right"):
        text = cell.get_text(strip=True).replace(",", "")
        if text.isdigit():
            value = int(text)
            if 20000 < value < 100000:
                prices.append(value)

    if not prices:
        raise ValueError("No TC prices found")

    return sum(prices) // len(prices)
