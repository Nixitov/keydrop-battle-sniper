import requests
import time
import random
import toml
import os

url = "https://kdrp2.com/CaseBattle/battle?type=active&page=0&priceFrom=0&priceTo=0&searchText=&sort=latest&players=all&roundsCount=all"
token = input('Input your token: ') #get it from "https://key-drop.com/es/token"

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

cls()

if not os.path.exists('config.toml'):
    with open('config.toml', 'w') as configfile:
        print('Config file was not found, creating it...')
        configfile.writelines(f'[Main]\n\nsteam_user_id = 123456\nmax_ticket_cost = 1')
        configfile.flush()
        print('Config file was created, edit it and press enter')
        input()

config = toml.load('config.toml')
steam_user_id = config['Main']['steam_user_id']
max_ticket_cost = int(config['Main']['max_ticket_cost'])

while True:
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        battle_found = False

        for i in range(min(len(data["data"]), 10)):
            battle = data["data"][i]
            if battle["isFreeBattle"] and len(battle['users']) < battle['maxUserCount'] and int(battle['freeBattleTicketCost']) == max_ticket_cost:
                battle_found = True
                max_users = int(battle['maxUserCount']) - 1
                print(f"Battle {battle['id']} meets the criteria.")
                spot_to_join = str(random.randint(0, max_users))
                battle_id = str(battle['id'])
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
                        print(f"Failed to join battle {battle_id}: {response_data['message']}")
                        if response_data['errorCode'] == 'slotUnavailable':
                            time.sleep(2)
                            break
                        continue
                    else:
                        print(f"Joined battle {battle_id} successfully!")
                        info_url = f'https://kdrp2.com/CaseBattle/gameFullData/{battle_id}'
                        exit()
                else:
                    print(f"Failed to join battle {battle_id}: {req.content}")
                    time.sleep(2)
                    continue

        if not battle_found:
            print('No battles found :(')
        time.sleep(1)
    except Exception as err:
        print(f'Timeout on request - {err}')
        time.sleep(1)
