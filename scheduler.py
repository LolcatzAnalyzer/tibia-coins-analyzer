import random
from database import insert_price
from analyzer import analyze
from config import WORLDS

def simulate():
    for world in WORLDS:
        price = random.randint(30000, 45000)
        insert_price(world, price)
        analyze(world)
