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

## How do I get the token?

The token required for this tool is a personal api key for your Key-Drop account. You can get this token from your account settings or create a new one from the api keys section of the website.

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
2. Make the won checker work. 🔃