import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jFile:
	jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member}join')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(F'{member}leave')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['FLA Bot','FLA Bot!','Help me', 'Help me!']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('FLA Bot Here! I can help you!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command,'on_error'):
            return

        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Correct,but missing required argument")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("Wrong,command not found")
        else:
            await ctx.send("Error,please check the characters for spelling mistakes and try again")

def setup(bot):
    bot.add_cog(Event(bot))
