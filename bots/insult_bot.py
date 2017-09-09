from telegram_backend import telegram_bot
from discord_backend import discord_bot
from common import common_bot
from random import randint
import json

class InsultBot(common_bot):

    def get_gif(self):
        with open ("fuckyou.json", "r") as f:
            lines = [line for line in f if line.strip()]
        data = json.loads(" ".join(lines))
        links = []
        for insult in data["data"]:
            link = insult.get("link")
            if not link:
                links.append(insult.get("mp4"))
            else:
                links.append(link)
        return links[randint(0, len(links) - 1)]

    def create_response(self, args):
        response = []
        if args[0] == "arvamus":
            response.append(('photo', 'arvamus.jpg'))
        elif args[0] == "ultimate":
            response.append(("string", "You... dirty... stuck-up... sadistic... shit-eating, cocksucking, buttfucking, penis-smelling, crotch-grabbing, ball-licking, semen-drinking, dog-raping, Nazi-loving, child-touching, cow-humping, perverted, spineless, heartless, mindless, dickless, testicle-choking, urine-gargling, jerk-offing, horse face, sheep-fondling, toilet-kissing, self-centered, feces-puking, dildo-shoving, snot-spitting, crap-gathering, big-nosed, monkey-slapping, bastard-screwing, bean-shitting, fart-knocking, sack-busting, splooge-tasting, bear-blowing, head-swallowing, bitch-snatching, handjobbing, donkey-caressing, mucus-spewing, anal-plugging, ho-grabbing, uncircumsized, sewer-sipping, whore mongering, piss-swimming, midget-munching, douchebag, ho-biting, carnivorous, mail-order prostituting asshole!"))
        elif args[0] == "rick":
            response.append(("mp4", 'arvamus_rick.mp4'))
        elif args[0] == "hardbass":
            response.append(("string", "Опа опа пидорас , рушит город мой Хард басс , пиво, семки и напас , весь район боится нас"))
        elif args[0] == "pegi":
            response.append (("string",
"""
On Sanity

One lovely sunday afternoon
some quy shot up a greasy spoon
They found by looking trough his room
that he made custom maps for doom
A spokesman for the NRA
said that things just cant go on this way
Lets ban all the violent games
and then go back to being sane

Tuesday lunch was also mard
when at a showing of Die Hard
someone looking pale and scarred
employed an ArmaLite AR
The man who owned the weaponshop
said that this has got to stop
Lets ban films and violent games
and then go back to being sane

A musician was shot in the eye
by a youth just passing by
who sat down with a heavy sigh
and read The Catcher in the Rye
The gunseller stood at his pulpit
soon identified the culprit
Lets ban books and films and violent games
then all go back to being sane

A man who'd been gone for a while
was found shot execution style
His body wore a frozen smile
and clutched a picture of his child
They said: "Thank god he was disarmed,
before that picture did more harm!
Lets ban pictures, books, films and games,
then go back to being sane."

A child who stole an iron brew
suspected that his parents knew
shot them with a 22
because a friend advised him to
The gunspokesman said: "Its absurd
we tolerate the spoken word!
Lets ban talking pictures books and films and games
then all go back to being sane."

But with the spokesmans work complete
we couldnt ask for food to eat
we dragged him out into the street
to be shot and butchered for his meat
He cried: "But I kept you sane!
I banned the things that were to blame!"
But we'd all forgotten spoken language
so he went unheard into a sandwich

Yahtzee
"""))
        elif " ".join(args[:2]).lower() == "fuck you":
            photo = self.get_gif()
            response.append(("gif_link", photo))
        elif " ".join(args[:2]).lower() == "fidget spinner":
            response.append(("mp4", 'fidget_spinner.mp4'))
        else:
            response.append(("string", super(InsultBot, self).create_response(args)))
        return response

class TelegramInsultBot(InsultBot, telegram_bot):
    def __init__(self):
        InsultBot.__init__(self, "insults.txt")
        telegram_bot.__init__(self, '297812849:AAFGeKrSX3lyWv3m5XGiu3pr9G6wuLae1E8', 'insult', add_command=True)

class DiscordInsultBot(InsultBot, discord_bot):
    def __init__(self):
        InsultBot.__init__(self, "insults.txt")
        discord_bot.__init__(self, 'MzU1Mzg2MjMyNjA5NDM5NzU2.DJMDKQ.AFHnEsjsQaLgKT61bBtBKdY1fag', 'insult', add_command=True)

TelegramInsultBot()
#DiscordInsultBot()