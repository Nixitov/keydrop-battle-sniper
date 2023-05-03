from src.utils.color import Color
from src.utils.utils import Utils
import requests

class Scraper():
    def __init__(self):
        self.color = Color()
        self.utils = Utils()

    def scrape_battles(self):
        url = "https://kdrp2.com/CaseBattle/battle?type=active&page=0&priceFrom=0&priceTo=0&searchText=&sort=latest&players=all&roundsCount=all"
        response = requests.get(url, timeout=5)
        return response.json()
