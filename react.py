import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

class React(Cog_Extension):

    @commands.command()
    async def logo(self,ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file= pic)

def setup(bot):
    bot.add_cog(React(bot))