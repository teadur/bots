from bot_backend import bot
from random import randint
import json

class InsultBot(bot):

    def get_gif(self):
        with open ("fuckyou.json", "r") as f:
            lines = [line for line in f if line.strip()]
        data = json.loads(" ".join(lines))
        link = []
        for insult in data["data"]:
            mp4 = insult.get("mp4")
            if not mp4:
                link.append(insult.get("link"))
            else:
                link.append(mp4)
        return link[randint(0, len(link) - 1)]

    def send_response(self, bot, update, args):
        if args[0] == "arvamus":
            bot.send_photo(chat_id=update.message.chat_id, photo=open('arvamus.jpg', 'rb'))
        elif args[0] == "ultimate":
            bot.sendMessage(chat_id=update.message.chat_id, text="You... dirty... stuck-up... sadistic... shit-eating, cocksucking, buttfucking, penis-smelling, crotch-grabbing, ball-licking, semen-drinking, dog-raping, Nazi-loving, child-touching, cow-humping, perverted, spineless, heartless, mindless, dickless, testicle-choking, urine-gargling, jerk-offing, horse face, sheep-fondling, toilet-kissing, self-centered, feces-puking, dildo-shoving, snot-spitting, crap-gathering, big-nosed, monkey-slapping, bastard-screwing, bean-shitting, fart-knocking, sack-busting, splooge-tasting, bear-blowing, head-swallowing, bitch-snatching, handjobbing, donkey-caressing, mucus-spewing, anal-plugging, ho-grabbing, uncircumsized, sewer-sipping, whore mongering, piss-swimming, midget-munching, douchebag, ho-biting, carnivorous, mail-order prostituting asshole!")
        elif args[0] == "rick":
            bot.send_document(chat_id=update.message.chat_id, document=open('arvamus_rick.mp4', 'rb'))
        elif args[0] == "hardbass":
            bot.sendMessage(chat_id=update.message.chat_id, text="Опа опа пидорас , рушит город мой Хард басс , пиво, семки и напас , весь район боится нас")
        elif " ".join(args).lower() == "fuck you":
            photo = self.get_gif()
            bot.send_video(chat_id=update.message.chat_id, video=photo)
        else:
            super(InsultBot, self).send_response(bot,update,args)

filename = "insults.txt"
token='297812849:AAFGeKrSX3lyWv3m5XGiu3pr9G6wuLae1E8'
command = 'insult'

InsultBot(token, filename, command)
