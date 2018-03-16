import lxml.html, sys
import json
import urllib.request
import urllib.parse
from telegram_backend import telegram_bot
from discord_backend import discord_bot
from oxford_dictionary import query_oxford_english

class GrammarBot(object):
	def create_response(self, args):
		if len(args) > 1:
			return [("string", "Lollakas! Tegu on sõnaraamatuga mitte sõnaderaamatuga!")]
		elif not args:
			return [("string", "Nii loll et ei oska isegi sõnaraamatult küsida jah!")]
		try:

			response = query_oxford_english(args[0])
			if not response:
				request = urllib.request.urlopen("http://www.eki.ee/dict/ekss/index.cgi?Q=" + urllib.parse.quote(args[0]) + "&Z=json&X=jvee211116&C01=1")
				html = request.read()
				data = json.loads(html.decode('utf-8'))
				if not data['result']:
					return [("string", "Ise mõtlesid selle sõna välja või. Lollakas!")]
				else:
					document = lxml.html.document_fromstring(data['result'])
					response = document.text_content()
		except Exception as e:
			print ("exception thrown")
			print (e)

		if len(response) > 4096:
			return [("string", response[:4090]+"...")]
		return [("string", response)]

class TelegramGrammarBot(telegram_bot, GrammarBot):
	def __init__(self):
		telegram_bot.__init__(self, "targuta")

class DiscordGrammarBot(discord_bot, GrammarBot):
	def __init__(self):
		discord_bot.__init__(self, "MzU1NTgzMzYwMzI1NjQ4Mzk0.DJO6Uw.YP_WH7Oo76QWJc9Y2ZNMIeV53Ys", "targuta")

if sys.argv[1] == "telegram":
	TelegramGrammarBot()
elif sys.argv[1] == "discord":
	DiscordGrammarBot()