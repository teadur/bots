import discord
import discord.ext.commands

class discord_bot(object):
    def __init__(self, token, command):
        self.command = '!' + command
        self.client = discord.Client()
        self.client.event(self.on_ready)
        self.client.event(self.on_message)
        self.client.run(token)

    async def on_ready(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('------')
#discord ei toeta videosid ega mp4-jasid. ainult gif-e nii et persse
    async def on_message(self, message):
        if message.content.startswith(self.command):
            args = message.content
            args = args.replace(self.command, "").strip()
            await self.client.send_message(message.channel, self.create_response([args]))
            #photo = discord.Embed()
            #photo.set_image(url="http://i.imgur.com/zl8Z8tY.mp4")
            #await self.client.send_message(message.channel, embed=photo)
            #await client.send_file(message.channel, 'arvamus.jpg')