from bot_backend import bot

class InsultBot(bot):
    def send_response(self, bot, update, args):
        if args[0] == "arvamus":
            bot.send_photo(chat_id=update.message.chat_id, photo=open('buss.jpg', 'rb'))
            bot.sendMessage(chat_id=update.message.chat_id, text = "Saue buss nr 190 läks põlema")
        elif args[0] == "ultimate":
            bot.sendMessage(chat_id=update.message.chat_id, text="You... dirty... stuck-up... sadistic... shit-eating, cocksucking, buttfucking, penis-smelling, crotch-grabbing, ball-licking, semen-drinking, dog-raping, Nazi-loving, child-touching, cow-humping, perverted, spineless, heartless, mindless, dickless, testicle-choking, urine-gargling, jerk-offing, horse face, sheep-fondling, toilet-kissing, self-centered, feces-puking, dildo-shoving, snot-spitting, crap-gathering, big-nosed, monkey-slapping, bastard-screwing, bean-shitting, fart-knocking, sack-busting, splooge-tasting, bear-blowing, head-swallowing, bitch-snatching, handjobbing, donkey-caressing, mucus-spewing, anal-plugging, ho-grabbing, uncircumsized, sewer-sipping, whore mongering, piss-swimming, midget-munching, douchebag, ho-biting, carnivorous, mail-order prostituting asshole!")
        else:
            super(InsultBot, self).send_response(bot,update,args)

filename = "insults.txt"
token='297812849:AAFGeKrSX3lyWv3m5XGiu3pr9G6wuLae1E8'
command = 'insult'

bot(token, filename, command)