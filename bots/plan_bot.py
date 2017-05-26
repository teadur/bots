from bot_backend import *
from ernie import get_random_xkcd_image
from ernie import get_random_ernie_image
from ernie import get_random_hagar_image
import time, datetime, random, requests, urllib, telegram, lxml.html as html

class PlanBot(bot):
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

    def send_response(self, bot, update, args):
        if args[0] == "decide":
            args.pop(0)
            args = [n.strip() for n in " ".join(args).split("või")]
            response = args[randint(0, len(args)-1)]
            bot.sendMessage(chat_id=update.message.chat_id, text="hmmm...")
        elif args[0] == "võtame":
            with open("võtame.txt", "r") as f:
                lines = f.readlines()
                response = lines[randint(0, len(lines) - 1)]
        elif args[0] == "installi":
            with open("installi.txt", "r") as f:
                lines = f.readlines()
                distro = lines[randint(0, len(lines) - 1)]
                response = "installi " + distro
                page = html.document_fromstring(requests.get("https://distrowatch.com/table.php?distribution={}".format(distro.lower())).text)
                element = page.xpath("//td[@class='TablesTitle']/text()")
                for i in element:
                    if len(i)>35:
                        response += i
        elif args[0].lower() == "dilbert":
            bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO )
            result = self.get_random_image()
            bot.sendPhoto(chat_id=update.message.chat_id, photo=result[0])
            response = "Dilbert comic on " + result[1]
        elif args[0].lower() == "xkcd":
            bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO )
            data = get_random_xkcd_image()
            print (data)
            bot.sendMessage(chat_id=update.message.chat_id, text=data[0])
            bot.sendPhoto(chat_id=update.message.chat_id, photo=data[1])
            response = data[2]
        elif args[0].lower() == "ernie":
            bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO )
            data  = get_random_ernie_image()
            bot.sendPhoto(chat_id=update.message.chat_id, photo=data[0])
            response="Ernie comic on "+data[1]
        elif args[0].lower() == "hagar":
            bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO )
            data  = get_random_hagar_image()
            bot.sendPhoto(chat_id=update.message.chat_id, photo=data[0])
            response="Hagar comic on "+data[1]
        elif  " ".join(args).lower() == "star wars" or " ".join(args).lower() == "fantastic beasts" or " ".join(args).lower() == "rammstein":
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
            elif " ".join(args).lower() == "rammstein":
                name = "Rammstein"
                year = 2017
                month = 6
                day = 11
            delta = datetime.datetime(year, month, day) - datetime.datetime.now()
            bot.sendMessage(chat_id=update.message.chat_id, text=name + " tuleb välja:")
            bot.sendMessage(chat_id=update.message.chat_id, text=str(delta.days) + " päeva")
            hours = 23 - datetime.datetime.now().hour
            if hours != 0:
                bot.sendMessage(chat_id=update.message.chat_id, text=str(hours) + " tunni")
            minutes = 59 - datetime.datetime.now().minute
            if minutes != 0:
                bot.sendMessage(chat_id=update.message.chat_id, text=str(minutes) + " minuti")
            seconds = str(59 - datetime.datetime.now().second) + " sekundi"
            bot.sendMessage(chat_id=update.message.chat_id, text=str(seconds))
            response = "pärast"
        elif " ".join(args).lower() == "türa kus mu buss on":
            bot.send_photo(chat_id=update.message.chat_id, photo=open('buss.jpg', 'rb'))
            response = "Saue buss nr 190 läks põlema"
        elif " ".join(args).lower() == "flap slap":
            bot.send_photo(chat_id=update.message.chat_id, photo=open('flapslap.jpg', 'rb'))
            response = ":)"
        elif " ".join(args).lower() == "calmyotits":
            bot.send_document(chat_id=update.message.chat_id, document=open('bill.mp4', 'rb'))
        elif " ".join(args).lower() == "clamyotits":
            bot.send_document(chat_id=update.message.chat_id, document=open('clamyot.mp4', 'rb'))
        elif " ".join(args).lower() == "nope":
            bot.send_document(chat_id=update.message.chat_id, document=open('nope_spongebob.mp4', 'rb'))
        else:
            with open(self.filename, "r") as f:
                lines = f.readlines()
            response = create_response(lines, args)
            bot.sendMessage(chat_id=update.message.chat_id, text="1. " + " ".join(args))
            bot.sendMessage(chat_id=update.message.chat_id, text="2. ...")
        bot.sendMessage(chat_id=update.message.chat_id, text=response)

filename = "plan.txt"
token='265390616:AAGquQAVoMm0WO7HsmEKPscLwbYNvd3fsdE'
command = 'plan'
PlanBot(token, filename, command)
