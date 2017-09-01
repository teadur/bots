import re, ast
from random import randint
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

class bot(object):
    def __init__(self, token, filename, command):
        self.filename = filename

        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
        self.insult_handler = CommandHandler(command, self.response, pass_args = True, pass_user_data=True, pass_chat_data=True)
        self.add_command_handler = CommandHandler('add', self.add_callback, pass_args = True, pass_user_data=True, pass_chat_data=True)
        self.dispatcher.add_handler(self.insult_handler)
        self.dispatcher.add_handler(self.add_command_handler)
        self.echo_handler = MessageHandler(Filters.all, self.echo)
        self.dispatcher.add_handler(self.echo_handler)
        self.updater.start_polling()

    def echo(self, bot, update):
        chatname = update.message.chat.title
        chatid = update.message.chat_id
        if(chatid != -1001071499716):
            new_update = ast.literal_eval(str(update).replace("from", "form"))
            new_username = new_update["message"]["form"]["username"]
            bot.send_message(chat_id="164813180", text=new_username + "@" + chatname  + " " + str(chatid) + " " + update.message.text)

    def add_callback(self, bot, update, args, chat_data, user_data):
        new_line = " ".join(args)

        if new_line:
            with open (self.filename, "r") as f:
                lines = [line for line in f if line.strip()]
            with open (self.filename, "w") as f:
                for line in lines:
                    f.write(line)
                if line[-1].find("\n") == -1:
                    f.write("\n")
                f.write(new_line)

            bot.sendMessage(chat_id=update.message.chat_id, text="Added " + new_line + " to " + self.filename)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Õpi kirjutama, loll. Tühja asja ma ei söö.")

    def response(self, bot, update, args, chat_data, user_data):
        self.send_response(bot, update, args)
        chatname = update.message.chat.title
        chatid = update.message.chat_id
        new_update = ast.literal_eval(str(update).replace("from", "form"))
        new_username = new_update["message"]["form"]["username"]
        print(new_username + "@" + chatname + " " + " ".join(args))
        bot.sendMessage(chat_id="164813180", text=new_username + "@" + chatname  + " " + str(chatid) + " " + " ".join(args))

    def send_response(self, bot, update, args):
        with open(self.filename, "r") as f:
            lines = f.readlines()
        response = create_response(lines, args)
        bot.sendMessage(chat_id=update.message.chat_id, text=response)

def create_response(lines, args):
    return formatString(lines[randint(0, len(lines) - 1)]).replace("$1", " ".join(args))

def formatString(s):
    if s.find("{") != -1:
        result = re.findall('{(.+?)}', s)
        s = s.replace("{", "")
        s = s.replace("}", "")
        arguments = result
        for a in arguments:
            choices = a.split("|")
            s = s.replace(a, choices[randint(0, len(choices) - 1)].strip())
    return (s)

if __name__ == "__main__":
    #s = "3. {Marilyn | Annika | Siiri} hakkab {naisi | mehi} {kohe | varsti} vaatama"
    s = "3. {ITÜN-i | PlayFairi | TTÜ e-Spordi} parimad {pojad | tütred} võtavad {Läti|Hollandi|Tonga|Korea|Põhja-Korea|Lõuna-Korea|Kuuba|Hiina|Andorra|Uus-Meremaa} kodakondsuse"
    print(formatString(s))