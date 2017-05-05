import requests
URL = "https://api.telegram.org/bot{}/".format("348367169:AAG4xGta0G35xRPn8nDQYngld12x-rxrCE4")
url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format("lol", "-81528940")
response = requests.get(url) 