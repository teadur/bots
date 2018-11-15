import ast
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import requests
import configparser
import datetime

class telegram_bot(object):
    def __init__(self, command, add_command=False, kick_on_empty = True):
        config = configparser.ConfigParser()
        config.read('api_keys.ini')
        self.add_command = add_command
        self.token = config["TELEGRAM_KEYS"][command]
        self.updater = Updater(token=self.token)
        self.kick_on_empty = kick_on_empty
        self.dispatcher = self.updater.dispatcher
        self.response_handler = CommandHandler(command, self.response, pass_args = True, pass_user_data=True, pass_chat_data=True)
        self.dispatcher.add_handler(self.response_handler)

        if self.add_command:
            self.add_command_handler = CommandHandler('add', self.add_callback, pass_args = True, pass_user_data=True, pass_chat_data=True)
            self.dispatcher.add_handler(self.add_command_handler)
            self.remove_command_handler = CommandHandler('remove', self.remove_callback, pass_args=True, pass_user_data=True, pass_chat_data=True)
            self.dispatcher.add_handler(self.remove_command_handler)

        self.echo_handler = MessageHandler(Filters.all, self.echo)
        self.dispatcher.add_handler(self.echo_handler)
        #hack for now
        if (command == "ilm"):
            self.updater.job_queue.run_daily(self.send_weather, datetime.time(6,0,0,0))
        self.updater.start_polling()

    def remove_callback(self, bot, update, args, chat_data, user_data):
        new_update = ast.literal_eval(str(update).replace("from", "form"))
        user_id = new_update["message"]["form"]["id"]
        if user_id == 164813180:
            response = self.remove_last()
        else:
            response = "Fuck off"
        bot.sendMessage(chat_id=update.message.chat_id, text=response)

    def echo(self, bot, update):
        chatname = update.message.chat.title
        chatid = update.message.chat_id
        if(chatid != -1001071499716 and chatid != -222974765 and chatid != -158709130):
            new_update = ast.literal_eval(str(update).replace("from", "form"))
            new_username = new_update["message"]["form"]["username"]
            bot.send_message(chat_id="164813180", text=new_username + "@" + str(chatname)  + " " + str(chatid) + " " + update.message.text)
            if(chatid == -1001174530031):
                args = update.message.text.split(" ")
                chatid = args.pop(0)
                message = " ".join(args)
                bot.send_message(chat_id=chatid, text=message)

    def add_callback(self, bot, update, args, chat_data, user_data):
        bot.sendMessage(chat_id=update.message.chat_id, text=self.add(args))

    def response(self, bot, update, args, chat_data, user_data):
        chatname = update.message.chat.title
        chatid = update.message.chat_id
        new_update = ast.literal_eval(str(update).replace("from", "form"))
        new_username = new_update["message"]["form"]["username"]
        user_id = new_update["message"]["form"]["id"]
        print(new_username + "@" + str(chatname) + " " + " ".join(args))
        bot.sendMessage(chat_id="164813180", text=new_username + "@" + str(chatname)  + " " + str(chatid) + " " + " ".join(args))
        if self.kick_on_empty and args == []:
            URL = "https://api.telegram.org/bot{}/".format(self.token)
            response = requests.get(URL + "kickChatMember?chat_id={}&user_id={}".format(chatid, user_id))
            bot.sendMessage(chat_id="164813180", text="Kick " + new_username + " from " + str(chatname)  + " " + str(chatid) + " with status " + str(response))
        self.send_response(bot, update, args)

    def send_response(self, bot, update, args):
        response = self.create_response(args)
        for resp in response:
            if resp[0] == "string":
                bot.sendMessage(chat_id=update.message.chat_id, text=resp[1])
                bot.sendMessage(chat_id="164813180", text=resp[1])
            elif resp[0] == "mp4":
                bot.send_document(chat_id=update.message.chat_id, document=open(resp[1], 'rb'))
                bot.send_document(chat_id="164813180", document=open(resp[1], 'rb'))
            elif resp[0] == "photo":
                bot.send_photo(chat_id=update.message.chat_id, photo=open(resp[1], 'rb'))
                bot.send_photo(chat_id="164813180", photo=open(resp[1], 'rb'))
            elif resp[0] == "gif_link":
                bot.send_video(chat_id=update.message.chat_id, video=resp[1])
                bot.send_video(chat_id="164813180", video=resp[1])
            elif resp[0] == "photo_link":
                bot.sendPhoto(chat_id=update.message.chat_id, photo=resp[1])
                bot.sendPhoto(chat_id="164813180", photo=resp[1])
            else:
                bot.sendMessage(chat_id=update.message.chat_id, text="Unsupported format")
                bot.sendMessage(chat_id="164813180", text="Unsupported format")
        return response

