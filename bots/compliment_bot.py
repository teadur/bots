from bot_backend import bot

class ComplimentBot(bot):
    def send_response(self, bot, update, args):
        if args[0] == "skiimoovi":
            bot.sendMessage(chat_id=update.message.chat_id, text="Norra on nii ilus vää")
            bot.sendMessage(chat_id=update.message.chat_id, text="https://youtu.be/gD8Hs4xWVhQ")
        else:
            super(ComplimentBot, self).send_response(bot,update,args)
filename = "compliment.txt"
token='261401432:AAGLQFIehbRt6zH2TNYTJyvr2PUbnfYRcew'
command = 'compliment'
ComplimentBot(token, filename, command)
