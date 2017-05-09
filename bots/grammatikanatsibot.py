import lxml.html
import json
import urllib.request
import urllib.parse
from bot_backend import bot
import sys
import telegram
from oxford_dictionary import query_oxford_english

class GrammarBot(bot):
	def send_response(self, bot, update, args):
		if len(args) > 1:
			bot.sendMessage(chat_id=update.message.chat_id, text="Lollakas! Tegu on sõnaraamatuga mitte sõnaderaamatuga!")
			return
		elif not args:
			bot.sendMessage(chat_id=update.message.chat_id, text="Nii loll et ei oska isegi sõnaraamatult küsida jah!")
			return
		try:

			response = query_oxford_english(args[0])
			if not response:
				request = urllib.request.urlopen("http://www.eki.ee/dict/ekss/index.cgi?Q=" + urllib.parse.quote(args[0]) + "&Z=json&X=jvee211116&C01=1")
				html = request.read()
				data = json.loads(html.decode('utf-8'))
				if not data['result']:				
					bot.sendMessage(chat_id=update.message.chat_id, text="Ise mõtlesid selle sõna välja või. Lollakas!")
					return
				else:
					document = lxml.html.document_fromstring(data['result'])
					response = document.text_content()
		except Exception as e:
			print ("exception thrown")
			print (e)

		if len(response) > 4096:
			bot.sendMessage(chat_id=update.message.chat_id, text="See küsimus on nii loll et vastus ei mahu sõnumisse ära.")
			return
		bot.sendMessage(chat_id=update.message.chat_id, text=response)
		
	def add_callback(self, bot, update, args, chat_data, user_data):
		bot.sendMessage(chat_id=update.message.chat_id, text="Sõnaraamatusse sina loll küll midagi lisada ei tohiks!")

filename = ""
token='228030866:AAGFH13_njpLJA2qNhOQDAfaSGxo0y2Ggco'
command = 'targuta'

GrammarBot(token, filename, command)