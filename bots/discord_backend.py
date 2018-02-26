import discord
import discord.ext.commands
import configparser

class discord_bot(object):
    def __init__(self, token, command, add_command=False):
        config = configparser.ConfigParser()
        config.read('api_keys.ini')
        self.command = command
        self.add_command = add_command
        self.client = discord.Client()
        self.client.event(self.on_ready)
        self.client.event(self.on_message)
        self.client.run(config["DISCORD_KEYS"][command])

    async def on_ready(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('------')
#discord ei toeta videosid ega mp4-jasid. ainult gif-e nii et persse
    async def on_message(self, message):
        if message.content.startswith('!' + self.command):
            args = message.content
            args = args.replace('!' + self.command, "").strip()
            response = self.create_response(args.split(" "))
            for resp in response:
                if resp[0] == "photo":
                    await self.client.send_file(message.channel, resp[1])
                elif resp[0] == "gif_link" or resp[0] == "photo_link":
                    photo = discord.Embed()
                    photo.set_image(url=resp[1])
                    await self.client.send_message(message.channel, embed=photo)
                elif resp[0] == "string":
                    await self.client.send_message(message.channel, resp[1])
                else:
                    await self.client.send_message(message.channel, "Unsupported format")
        elif self.add_command and message.content.startswith('!add'):
            add_string = "!add " + self.command
            if add_string == (" ".join(message.content.split(" ")[:2])):
                args = message.content
                args = args.replace(add_string, "").strip()
                await self.client.send_message(message.channel, self.add(args.split(" ")))
