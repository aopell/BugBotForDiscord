import discord
from discord.channel import TextChannel
from discord.ext import commands
from discord.role import Role
from models.guild_options import GuildOptions, IssueCategory

class Category(commands.Cog):
    def __init__(self, bugbot):
        print("Setting up Category cog")
        self.bugbot = bugbot
    
    @commands.group()
    async def category(self, ctx: commands.Context):
        pass

    @category.command()
    async def create(self, ctx: commands.Context, name: str, prefix: str, icon: str, emoji: str):
        """Creates a category"""
        options = self.bugbot.config.guild_options[ctx.guild.id]
        options.categories.append(IssueCategory(name, prefix.upper(), icon, emoji))
        self.bugbot.config.save()
        await ctx.reply(f"Created category **{name}** ({prefix.upper()}) with icon {icon} and emoji {emoji}")