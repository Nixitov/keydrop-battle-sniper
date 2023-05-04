from src.utils.utils import Utils
from src.utils.color import Color
import requests

class BattleInfo():
    def __init__(self):
        self.color = Color()
        self.utils = Utils()

    def get_battle_info(self, battle_id, steam_user_id, token):
        while True:
            headers = {
                "authorization": f"Bearer {token}"
            }
            req = requests.get(f"https://kdrp2.com/CaseBattle/gameFullData/{battle_id}", headers=headers)

            if req.status_code == 200:
                data = req.json()["data"]
                rounds = data["rounds"]
                cases = data["cases"]
                users = data["users"]
                
                won_steam_id = data["wonSteamId"]
                
                won_items = []
                for round_1 in rounds:
                    if round_1["wonItems"]:
                        won_items.extend(round_1["wonItems"])
                total_winning_amount = sum([item["price"] for item in won_items])
                
                for user in users:
                    if user["idSteam"] == won_steam_id:
                        total_winning_amount += user["cashback"]
                
                if won_steam_id == steam_user_id:
                    return f'\n   {self.color.green}Congratulations! You won the battle - Profit: {round(total_winning_amount, 2)}$'
                else:
                    return f'\n   {self.color.red}Oh :( Sadly you lost the battle'
            else:
                print(f'\n   {self.color.red}Error getting battle info! - retrying')

