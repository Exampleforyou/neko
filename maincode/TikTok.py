import discord
from discord.ext import commands
import requests
import random as ran

print('TikTok')


class TikTok(commands.Cog, name='TikTok'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startNeko(self, ctx):
        await ctx.send()

    async def ДаняХуй(self):
        pass
