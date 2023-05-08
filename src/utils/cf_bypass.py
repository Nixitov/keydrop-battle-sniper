import undetected_chromedriver as uc
from src.utils.color import Color
import json

class CfBypass():
    def __init__(self):
        self.color = Color()

    def bypass_cf(self, session_id):
        try:
            options = uc.ChromeOptions()
            options.add_argument('--headless')
            driver = uc.Chrome(options=options)
            driver.get('https://key-drop.com')
            driver.add_cookie({"name": "session_id", "value": session_id})
            driver.refresh()

            cf_bm = json.loads(json.dumps(driver.get_cookie("__cf_bm")))
            vio_shield = json.loads(json.dumps(driver.get_cookie("__vioShield")))
            driver.close()
            driver.quit()
            return 'valid', str(vio_shield["value"]), str(cf_bm["value"])
        except Exception as err:
            return 'invalid', f'There was an error bypassing cloudflare, make sure your session_id is valid! {err}'

    def get_token_req(self, session_id, vioShield, cf_bm):
        try:
            import requests

            url = 'https://key-drop.com/es/token'

            headers = {
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Accept-Language": "es-ES,es;q=0.9",
                "Cookie": f"session_id={session_id}; __vioShield={vioShield}; __cf_bm={cf_bm}"
            }

            req = requests.get(url, headers=headers)

            return(req.text)
        except Exception as err:
            return 'error', err

    def get_token(self, session_id):
            answer = self.bypass_cf(session_id)
            if answer[0] == 'valid':
                return self.get_token_req(session_id, answer[1], answer[2])
            else:
                print(answer)

if __name__ == '__main__':
    CfBypass()