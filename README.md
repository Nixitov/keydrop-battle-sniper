# Battle Sniper

Battle Sniper is a Python-based tool for automatically joining free battles on the Key-Drop platform.   

This project uses Python 3.x and depends on several packages, such as colorama, requests, and toml.

--------------

Installation

1. Make sure you have Python 3.x installed on your machine.

3. Clone the repository:
```
git clone https://github.com/NixV37/keydrop-battle-sniper.git
```

then:

```
cd keydrop-battle-sniper
```

Install the required Python packages:
```
pip install -r requirements.txt
```

## Config info:
`session_id`: Login into https://key-drop.com, then open developer tab, go into application, cookies and copy session_id value.

`steam_user_id` Your steam user id, steam has a guide on how to get it.(https://help.steampowered.com/en/faqs/view/2816-BE67-5B69-0FEC).

`max_ticket_cost`: Max ticket price to join a giveaway.

`use_token (not recomended)`: true or false, enabling it will ask for token instead of using session_id.

`auto_open_joined_battles`: Opens a browser with the battle so that u can see it when joined.

`delay`: Delay for every battle scrape.

## How do I get the token?

1. Login into your browser and go into this site:
```
https://key-drop.com/es/token
```
2. Copy the whole text.

## How to use

1. Edit the `config.toml` file to set your desired options.

2. Run the `main.py` script:
```
python main.py
```

Follow the prompts to input your token and start sniping battles.

## How to contribute

Contributions are welcome! To contribute, fork the repository, make your changes, and submit a pull request.

## Todo:

1. Make it use websocket instead of refreshing it every time. ✅
2. Use session_id instead of token. ✅
3. Make the won checker work. ✅
4. Add case filter ✅
5. Add user filter ✅
6. Add queue system. 🔃