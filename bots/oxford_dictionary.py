# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
from pprint import pprint

def query_oxford_english(word_id):
	# TODO: replace with your own app_id and app_key
	app_id = 'f7693439'
	app_key = '34ab113c354e1970d75bac7316a9e0cf'
	
	language = 'en'
	#word_id = 'play'
	
	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
	
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	
	#print("code {}\n".format(r.status_code))
	#print("text \n" + r.text)
	#print("json \n" + json.dumps(r.json()))
	#pprint(r.json())
	#print "\n\nvahepeal\n\n"
	reply = []
	if r.status_code == 200:
		for result in r.json().get('results', []):
			reply.append(result.get('id', ""))
			#reply.append("")
			for lexicalEntrie in result.get('lexicalEntries', []):
				reply.append(lexicalEntrie.get("lexicalCategory", ""))
				#reply.append("")
				for entrie in lexicalEntrie.get('entries', []):
					for sense in entrie.get("senses", []):
						#pprint(sense)
						for definition in sense.get("definitions", []):
							reply.append("DEFINITION: " + definition)
						for example in sense.get("examples", []):
							reply.append("EXAMPLE: " + example["text"])
						for subsense in sense.get("subsenses", []):
							for definiton in subsense.get("definitions", []):
								reply.append("SUBDEFINITON: " + definiton)
							for example in subsense.get("examples", []):
								reply.append("SUBEXAMPLE: " + example["text"])
				#		reply.append("")
				#reply.append("")
	if reply != []:
		reply = "\n".join(reply)
	else:
		reply = None
	#print (reply)
	return reply
	#url = "https://api.telegram.org/bot{}/".format("228030866:AAGFH13_njpLJA2qNhOQDAfaSGxo0y2Ggco") + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(reply, "-1001071499716")
	#requests.get(url)
	#for line in reply:
	#	url = "https://api.telegram.org/bot{}/".format("228030866:AAGFH13_njpLJA2qNhOQDAfaSGxo0y2Ggco") + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(line, "164813180")
	#	requests.get(url)
#print (query_oxford_english("asi"))