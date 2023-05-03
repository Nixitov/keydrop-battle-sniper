from src.utils.color import Color
import os
import toml

class Utils():
    def __init__(self):
        self.color = Color()

    def cls(self): os.system('cls' if os.name == 'nt' else 'clear')

    def exists(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

    def load_config(self):
        if not self.exists('config.toml'):
            with open('config.toml', 'w') as configfile:
                print(f'\n   {self.color.red}Config file was not found, creating it...')
                configfile.writelines(f'[Main]\n\nsteam_user_id = 123456\nmax_ticket_cost = 1')
                configfile.flush()
                print(f'   {self.color.green}Config file was created, edit it and press enter')
                input()
        config = toml.load('config.toml')

        return config['Main']['steam_user_id'], int(config['Main']['max_ticket_cost'])

    def ask_for_token(self):
        print(f'\n   {self.color.cyan}Input your token! ')
        return input(f'\n  {self.color.green}> ')