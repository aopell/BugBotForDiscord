import discord
from discord.ext import commands

class Debug(commands.Cog):
    def __init__(self, bugbot):
        print("Setting up Debug cog")
        self.bugbot = bugbot
    
    @commands.command()
    async def hello(self, ctx: commands.Context, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        await ctx.reply(f"Hello {member.mention}!")