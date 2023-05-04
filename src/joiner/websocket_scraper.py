from src.utils.color import Color
import asyncio
import websockets
import json

class WbScraper():
    def __init__(self):
        self.color = Color()

    async def scrape(self, auth_token):
        async with websockets.connect('wss://kdrp3.com/socket.io/?connection=battle&EIO=4&transport=websocket') as websocket:
            auth_payload = {
                "token": auth_token
            }
            auth_message = f"40/case-battle,{json.dumps(auth_payload)}"
            await websocket.send(auth_message)

            while True:
                message = await websocket.recv()

                message_type, message_data = message.split(",", maxsplit=1)
                if message_type == "42/case-battle":
                    if '"public",true,' in message_data and ',null]],[],' in message_data:
                        battle_id = int(message_data.split('["BC_CREATE_V3",[')[1].split(",")[0])
                        battle_cost = int(message_data.split(',null]],[],')[1].split("]]")[0])
                        battle_max_users = int(message_data.split(f'["BC_CREATE_V3",[{battle_id},')[1].split(",")[0])
                        battle = {'id': battle_id, 'isFreeBattle': True, 'freeBattleTicketCost': battle_cost, 'maxUserCount': battle_max_users, 'users': ["null"]}
                        return battle

    async def get_battle(self, auth_token):
        return await self.scrape(auth_token)
