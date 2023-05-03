from src.joiner.battle_info import BattleInfo
from src.joiner.scraper import Scraper
from src.joiner.joiner import Joiner
from src.utils.color import Color
from src.utils.utils import Utils
import threading
import time

class BattleSniper():
    def __init__(self):
        self.color = Color()
        self.utils = Utils()
        self.joiner = Joiner()
        self.scraper = Scraper()
        self.battle_info = BattleInfo()
        self.token = ''
        self.steam_user_id = 123123123
        self.max_ticket_cost = 1
        self.errors = 0
        self.times_scraped = 0
        self.join_tries = 0
        self.message_history = []
        self.stop = False
        self.start()

    def load(self):
        self.steam_user_id, self.max_ticket_cost = self.utils.load_config()
        self.utils.cls()
        self.token = self.utils.ask_for_token()

    def print_status(self):
        while not self.stop:
            time.sleep(0.5)
            self.utils.cls()
            print(f'\n      {self.color.green}Sniper started!\n\n   Times Scraped: {self.color.yellow}{self.times_scraped}\n   {self.color.cyan}Join Tries: {self.color.yellow}{self.join_tries}\n   {self.color.cyan}Errors: {self.color.red}{self.errors}\n')
            if len(self.message_history) != 0:
                for message in self.message_history:
                    print(message)

    def start(self):
        self.utils.cls()
        self.load()
        self.utils.cls()
        print(f'\n   {self.color.cyan}Starting sniper! - {self.color.green}Scraping battles...\n')
        threading.Thread(target=self.print_status).start()
        while True:
            try:
                data = self.scraper.scrape_battles()
                for i in range(min(len(data["data"]), 10)):
                    battle = data["data"][i]
                    answer = self.joiner.join(battle, self.max_ticket_cost, self.token)
                    self.times_scraped +=1
                    if answer[0] == 'joined':
                        if len(self.message_history) > 9:
                            self.message_history.pop(0)
                        self.message_history.append(answer[1])
                        self.stop = True
                        time.sleep(1)
                        self.cls()
                        print(f'\n   Joiner finished, getting battle info...')
                        time.sleep(5)
                        self.battle_info.get_battle_info(str(battle['id']), str(self.steam_user_id), self.token)
                        break
                    elif answer[0] == 'bad':
                        if len(self.message_history) > 9:
                            self.message_history.pop(0)
                        self.message_history.append(answer[1])
                        self.join_tries +=1
                    time.sleep(2)
            except:
                self.errors +=1
                time.sleep(0.5)

if __name__ == '__main__':
    BattleSniper()