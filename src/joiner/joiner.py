from src.utils.color import Color
from src.utils.utils import Utils
import requests
import random

class Joiner():
    def __init__(self):
        self.color = Color()
        self.utils = Utils()

    def join(self, battle, max_ticket_cost, token):
        if battle["isFreeBattle"] and len(battle['users']) < battle['maxUserCount'] and int(battle['freeBattleTicketCost']) == max_ticket_cost:
            max_users = int(battle['maxUserCount']) - 1
            #print(f"\n   {self.color.cyan}Battle {self.color.yellow}{battle['id']} {self.color.cyan}is valid, trying to join...")
            spot_to_join = str(random.randint(0, max_users))
            battle_id = str(battle['id'])
            battle_cases = list(battle['CasesNames'])
            battle_url = f'https://kdrp2.com/CaseBattle/joinCaseBattle/{battle_id}/{spot_to_join}'

            headers = {
                "authority": "kdrp2.com",
                "method": "POST",
                "path": f"/CaseBattle/joinCaseBattle/{battle_id}/{spot_to_join}",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "authorization": f"Bearer {token}",
                "content-length": "0",
                "origin": "https://key-drop.com",
                "referer": "https://key-drop.com/",
                "sec-ch-ua": '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition std-1)",
                "x-currency": "usd"
            }

            req = requests.post(battle_url, headers=headers, timeout=5)

            if req.status_code == 201:
                response_data = req.json()
                if not response_data['success']:
                    return 'bad', f"   {self.color.cyan}Failed to join battle {self.color.yellow}{battle_id}: {self.color.red}{response_data['message']}"
                else:
                    return 'joined', f"   {self.color.green}Joined battle {self.color.yellow}{battle_id} - {battle_cases} {self.color.green}successfully!"
            else:
                return 'bad', f"   {self.color.cyan}Failed to join battle {self.color.yellow}{battle_id}: {self.color.red}{req.content}"
        else:
            return 'notfree', 'hi'