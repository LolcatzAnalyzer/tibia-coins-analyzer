import os
import requests

def send_buy_alert(price, reason):
    webhook = os.getenv("DISCORD_WEBHOOK_BUY")

    if not webhook:
        print("❌ BUY webhook not set")
        return

    data = {
        "content": f"🟢 **BUY SIGNAL**\nCena: {price}\nPowód: {reason}"
    }

    r = requests.post(webhook, json=data)
    print("BUY alert status:", r.status_code)


def send_sell_alert(price, reason):
    webhook = os.getenv("DISCORD_WEBHOOK_SELL")

    if not webhook:
        print("❌ SELL webhook not set")
        return

    data = {
        "content": f"🔴 **SELL SIGNAL**\nCena: {price}\nPowód: {reason}"
    }

    r = requests.post(webhook, json=data)
    print("SELL alert status:", r.status_code)
