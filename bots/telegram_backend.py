import ast
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

class telegram_bot(object):
    def __init__(self, token, command, add_command=False):
        self.add_command = add_command
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
        self.response_handler = CommandHandler(command, self.response, pass_args = True, pass_user_data=True, pass_chat_data=True)
        self.dispatcher.add_handler(self.response_handler)

        if self.add_command:
            self.add_command_handler = CommandHandler('add', self.add_callback, pass_args = True, pass_user_data=True, pass_chat_data=True)
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
            if resp[0] == "string":
                bot.sendMessage(chat_id=update.message.chat_id, text=resp[1])
            elif resp[0] == "mp4":
                bot.send_document(chat_id=update.message.chat_id, document=open(resp[1], 'rb'))
            elif resp[0] == "photo":
                bot.send_photo(chat_id=update.message.chat_id, photo=open(resp[1], 'rb'))
            elif resp[0] == "gif_link":
                bot.send_video(chat_id=update.message.chat_id, video=resp[1])
            elif resp[0] == "photo_link":
                bot.sendPhoto(chat_id=update.message.chat_id, photo=resp[1])
            else:
                bot.sendMessage(chat_id=update.message.chat_id, text="Unsupported format")

