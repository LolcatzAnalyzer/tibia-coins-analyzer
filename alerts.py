import requests
from config import DISCORD_WEBHOOK_BUY, DISCORD_WEBHOOK_SELL

def send_buy(world, price):
    requests.post(DISCORD_WEBHOOK_BUY, json={'content': f'🟢 BUY ALERT | {world} | {price} TC'})

def send_sell(world, price):
    requests.post(DISCORD_WEBHOOK_SELL, json={'content': f'🔴 SELL ALERT | {world} | {price} TC'})
