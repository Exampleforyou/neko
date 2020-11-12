import discord
from discord.ext import commands
from discord.ext.commands import Bot
import discord

token = 'NjYzMjE2NTg4NDIxMzMyOTky.XhFSlA.W3fhuIlFzbWT8ZaQtBkMR9Ry1gI'


class MyClient(discord.client):

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            with open('neko.jpg', 'rb') as picture:
                await bot.send(file=picture)


bot = MyClient()
bot.run(token)
