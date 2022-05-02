import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
 
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('hello,I am FLA_Bot ')

    @commands.command()
    async def FYR(self, ctx):
        embed=discord.Embed(title="We are building FYR now", description="We are building FYR now", color=0x4372df, 
        timestamp= datetime.datetime.now())
        embed.set_author(name="FLA Studio")
        embed.add_field(name="FYR", value="FYR Builder", inline=True)
        embed.set_footer(text="FLA Studio")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num : int):
        await ctx.channel.purge(limit=num+1)
    
    @commands.command()
    async def cmd(self, ctx, num:int):
        await ctx.send(num)

    @commands.group()
    async def giverole(self, ctx):
        await ctx.send("Please use 'give???' and try again")

    @giverole.command()
    async def giveguest(self, ctx, member: discord.Member):
        guild=self.bot.get_guild(950740793323323452)
        giverole =guild.get_role(950757340376879165)
        await member.add_roles(giverole)

    @giverole.command()
    async def giveadmin(self, ctx, member: discord.Member):
        guild=self.bot.get_guild(950740793323323452)
        giverole =guild.get_role(950751256438263829)
        await member.add_roles(giverole)

    @giverole.command()
    async def giveimportadmin(self, ctx, member: discord.Member):
        guild=self.bot.get_guild(950740793323323452)
        giverole =guild.get_role(950745484274827304)
        await member.add_roles(giverole)




def setup(bot):
    bot.add_cog(Main(bot))