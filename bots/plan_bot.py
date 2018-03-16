from telegram_backend import telegram_bot
from discord_backend import discord_bot
from common import common_bot
from ernie import get_random_xkcd_image
from ernie import get_random_ernie_image
from ernie import get_random_hagar_image
import time, datetime, random, requests, lxml.html as html
from random import randint
from crypto import getCryptoPrice
import re, sys

class PlanBot(common_bot):
    def strTimeProp(self, start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.
            start and end should be strings specifying times formated in the
            given format (strftime-style), giving an interval [start, end].
            prop specifies how a proportion of the interval to be taken after
            start.  The returned time will be in the specified format.
        """
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))
        ptime = stime + prop * (etime - stime)
        return time.strftime(format, time.localtime(ptime))

    def randomDate(self, start, end, prop):
        return self.strTimeProp(start, end, '%Y-%m-%d', prop)

    def get_random_image(self):
        random_date = self.randomDate("1989-4-16", datetime.datetime.now().strftime("%Y-%m-%d"), random.random())
        url_to_dilbert_page = "http://www.dilbert.com/%s/" % random_date
        response = requests.get(url_to_dilbert_page)
        first_half = response.text[response.text.find("data-image"):]
        data_image = first_half[:first_half.find(" ")]
        url_to_dilbert_page = re.findall(r'"([^"]*)"', data_image)[0]
        return url_to_dilbert_page, random_date

    def create_response(self, args):
        response = []
        if args[0] == "decide":
            args.pop(0)
            args = [n.strip() for n in " ".join(args).split(" or ")]
            response.append(("string", "hmmm..."))
            response.append(("string", args[randint(0, len(args) - 1)]))
        elif args[0] == "võtame":
            with open("võtame.txt", "r", encoding = "UTF-8") as f:
                lines = f.readlines()
                response.append(("string", lines[randint(0, len(lines) - 1)]))
        elif args[0] == "installi":
            with open("installi.txt", "r") as f:
                lines = f.readlines()
                distro = lines[randint(0, len(lines) - 1)]
                response.append(("string", "installi " + distro))
                page = html.document_fromstring(requests.get("https://distrowatch.com/table.php?distribution={}".format(distro.lower())).text)
                element = page.xpath("//td[@class='TablesTitle']/text()")
                for i in element:
                    if len(i)>35:
                        response.append(("string", i))
        elif args[0].lower() == "dilbert":
            result = self.get_random_image()
            response.append(("photo_link", result[0]))
            response.append(("string", "Dilbert comic on " + result[1]))
        elif args[0].lower() == "xkcd":
            data = get_random_xkcd_image()
            response.append(("string", data[0]))
            response.append(("photo_link", data[1]))
            response.append(("string", data[2]))
        elif args[0].lower() == "ernie":
            data  = get_random_ernie_image()
            response.append(("photo_link", data[0]))
            response.append(("string", "Ernie comic on " + data[1]))
        elif args[0].lower() == "hagar":
            data  = get_random_hagar_image()
            response.append(("photo_link", data[0]))
            response.append(("string", "Hagar comic on " + data[1]))
        elif  " ".join(args).lower() == "star wars" or " ".join(args).lower() == "fantastic beasts":
            if " ".join(args).lower() == "star wars": 
                name = "Star Wars"
                year = 2017  
                month = 12
                day = 15
            elif " ".join(args).lower() == "fantastic beasts":
                name = "Fantastic Beasts 2"
                year = 2018  
                month = 11
                day = 16
            delta = datetime.datetime(year, month, day) - datetime.datetime.now()
            response.append(("string", name + " tuleb välja:"))
            response.append(("string", str(delta.days) + " päeva"))
            hours = 23 - datetime.datetime.now().hour
            if hours != 0:
                response.append(("string", str(hours) + " tunni"))
            minutes = 59 - datetime.datetime.now().minute
            if minutes != 0:
                response.append(("string", str(minutes) + " minuti"))
            seconds = str(59 - datetime.datetime.now().second) + " sekundi"
            response.append(("string", str(seconds)))
            response.append(("string", "pärast"))
        elif " ".join(args).lower() == "türa kus mu buss on":
            response.append(("photo", 'buss.jpg'))
            response.append(("string", "Saue buss nr 190 läks põlema"))
        elif args[0].lower() == "price":
            response.append(("string", getCryptoPrice(args[1])))
        elif " ".join(args).lower() == "flap slap":
            response.append(("photo", 'flapslap.jpg'))
            response.append(("string", ":))))"))
        elif " ".join(args).lower() == "calmyotits":
            response.append(("mp4", 'bill.mp4'))
        elif " ".join(args).lower() == "clamyotits":
            response.append(("mp4", 'clamyot.mp4'))
        elif " ".join(args).lower() == "nope":
            response.append(("mp4", 'nope_spongebob.mp4'))
        elif " ".join(args).lower() == "appi mumble":
            response.append(("string",
                            """kahtlane.info server
server: mumble.kahtlane.info
kanal: PlayFair
access token: plfreu"""))
            response.append(("photo", "mumble/step1.png"))
            response.append(("photo", "mumble/step2.png"))
            response.append(("photo", "mumble/step3.png"))
            response.append(("photo", "mumble/step4.png"))
        elif " ".join(args).lower() == "annika läheb mehele":
            response.append(("string", """
/     /                   ‾‾ Y \\
|     (\     (.         /)    |)    \\
  ◝       ◝  ' ( ͡° ͜ʖ ͡°) _  ◞      )
     \    |    ︵ Y  ︵ /    /
      |    ◝        |       )   /
       \  ト ‾‾ 本 ‾‾   イ
           |  ミ ホ ミ /
            )\     ∘    /
          (   \        /
        /       /ώ≡≡≡≡≡≡≡D
      /        /    \\      \\
    (         (/      \\       \\
      \      \         \)      )
       \     /         /    /"""))
        else:
            response.append(("string", "1. " + " ".join(args)))
            response.append(("string", "2. ..."))
            response.append(("string", super(PlanBot, self).create_response(args)))
        return response

class TelegramPlanBot(PlanBot, telegram_bot):
    def __init__(self):
        PlanBot.__init__(self, "plan.txt")
        telegram_bot.__init__(self, 'plan', add_command=True)

class DiscordPlantBot(PlanBot, discord_bot):
    def __init__(self):
        PlanBot.__init__(self, "plan.txt")
        discord_bot.__init__(self, 'MzU1NTg0ODYzOTk2MjE1Mjk2.DJO7uQ.bEL995vgQzPbXjS3LmwHsYpOMfY', 'plan', add_command=True)


if sys.argv[1] == "telegram":
    TelegramPlanBot()
elif sys.argv[1] == "discord":
    DiscordPlantBot()
