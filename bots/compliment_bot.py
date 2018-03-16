from telegram_backend import telegram_bot
from discord_backend import discord_bot
from common import common_bot
import sys

class ComplimentBot(common_bot):
    def create_response(self, args):
        response = []
        if args[0] == "skiimoovi":
            response.append (("string",
            """
            Norra on nii ilus vää
            https://youtu.be/gD8Hs4xWVhQ
            """))
        elif " ".join(args).lower() == "hugo boss":
            response.append(("mp4", "hugo_boss.mp4"))
        elif " ".join(args).lower() == "liisi":
            response.append(("string", "http://leib.tk/media/MM_Liisi_NoGi_First_Match.mp4"))
            response.append(("string", "http://leib.tk/media/MM_Liisi_NoGi_Second_Match.mp4"))
            response.append(("string", "http://leib.tk/media/MM_Liisi_Overtime.mp4"))
            response.append(("string", "http://leib.tk/media/MM_Liisi_GI.mp4"))
        else:
            response.append(("string", super(ComplimentBot, self).create_response(args)))
        return response

class TelegramComplimentBot(ComplimentBot, telegram_bot):
    def __init__(self):
        ComplimentBot.__init__(self, "compliment.txt")
        telegram_bot.__init__(self, 'compliment', add_command=True)

class DiscordComplimentBot(ComplimentBot, discord_bot):
    def __init__(self):
        ComplimentBot.__init__(self, "compliment.txt")
        discord_bot.__init__(self, 'MzU1NDU5OTk1NzE5OTU4NTI4.DJNHbg.NeNstLhB9Vo_erH1gnoCEnBdIFk', 'compliment', add_command=True)


if sys.argv[1] == "telegram":
    TelegramComplimentBot()
elif sys.argv[1] == "discord":
    DiscordComplimentBot()
