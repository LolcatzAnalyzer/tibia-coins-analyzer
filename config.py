from dotenv import load_dotenv
import os

load_dotenv()

APP_PASSWORD = os.getenv('APP_PASSWORD')
DISCORD_WEBHOOK_BUY = os.getenv('DISCORD_WEBHOOK_BUY')
DISCORD_WEBHOOK_SELL = os.getenv('DISCORD_WEBHOOK_SELL')

WORLDS = ['Secura', 'Bona', 'Refugia']
CHECK_INTERVAL_MINUTES = 5
