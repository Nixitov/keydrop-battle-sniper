from src.joiner.websocket_scraper import WbScraper
from src.joiner.battle_info import BattleInfo
from src.utils.cf_bypass import CfBypass
from src.joiner.scraper import Scraper
from src.joiner.joiner import Joiner
from src.utils.color import Color
from src.utils.utils import Utils
import threading
import asyncio
import time

class BattleSniper():
    def __init__(self):
        self.color = Color()
        self.utils = Utils()
        self.joiner = Joiner()
        self.scraper = Scraper()
        self.cf_bypass = CfBypass()
        self.wb_scraper = WbScraper()
        self.battle_info = BattleInfo()
        self.token = ''
        self.session_id = ''
        self.steam_user_id = 123123123
        self.max_ticket_cost = 1
        self.use_token = False
        self.auto_open_joined_battles = True
        self.delay = 0.2
        self.case_filter = []
        self.errors = 0
        self.times_scraped = 0
        self.join_tries = 0
        self.message_history = []
        self.stop = False
        self.start()

    def load(self):
        self.session_id, self.steam_user_id, self.max_ticket_cost, self.use_token, self.auto_open_joined_battles, self.delay, self.case_filter = self.utils.load_config()
        self.utils.cls()
        if self.use_token:
            self.token = self.utils.ask_for_token()
        else:
            print(f'\n   {self.color.cyan}Getting token from session_id...')
            self.token = self.cf_bypass.get_token(self.session_id)
            print(f'\n   {self.color.green}Bypassed cloudflare, token generated')

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
                battle = asyncio.run(self.wb_scraper.get_battle(self.token, self.case_filter))
                battle_id = str(battle['id'])
                answer = self.joiner.join(battle, self.max_ticket_cost, self.token)
                if 'message":"Unauthorized"' in answer:
                    self.token = self.cf_bypass.get_token(self.session_id)
                self.times_scraped +=1
                if answer[0] == 'joined':
                    if len(self.message_history) > 9:
                        self.message_history.pop(0)
                    self.message_history.append(answer[1])
                    self.message_history.append(f'   {self.color.cyan}Getting battle {self.color.green}{battle_id}{self.color.cyan} info...')
                    if self.auto_open_joined_battles:
                        self.utils.open_url(f'https://key-drop.com/es/case-battle/{battle_id}')
                    else:
                        self.message_history.append(self.battle_info.get_battle_info(battle_id, str(self.steam_user_id), self.token))
                elif answer[0] == 'bad':
                    if len(self.message_history) > 9:
                        self.message_history.pop(0)
                    self.message_history.append(answer[1])
                    self.join_tries +=1
                    time.sleep(2)
                time.sleep(self.delay)
            except Exception as err:
                self.errors +=1
                self.message_history.append(err)
                time.sleep(1)

if __name__ == '__main__':
    BattleSniper()