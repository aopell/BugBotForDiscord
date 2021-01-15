import discord
from discord.channel import TextChannel
from discord.ext import commands
from discord.role import Role
from models.guild_options import GuildOptions

class Setup(commands.Cog):
    def __init__(self, bugbot):
        print("Setting up Setup cog")
        self.bugbot = bugbot
    
    @commands.group()
    async def setup(self, ctx: commands.Context):
        pass

    @setup.command()
    async def guild(self, ctx: commands.Context, admin: Role, voter: Role, min_votes: int, log_channel: TextChannel):
        """Sets up the guild"""
        self.bugbot.config.guild_options[ctx.guild.id] = GuildOptions(ctx.guild.id, admin.id, voter.id, min_votes, log_channel.id, "", "", 0, [], [])
        self.bugbot.config.save()
        await ctx.reply("Guild set up successfully. Use `setup github`, `setup channel`, and `category create` to finish setup.")
    
    @setup.command()
    async def github(self, ctx: commands.Context, owner: str, repo: str, proj_name: str):
        """Sets up github options for the guild"""
        print(self.bugbot.config.guild_options)
        options = self.bugbot.config.guild_options[ctx.guild.id]
        options.github_owner = owner
        options.github_repo = repo
        options.github_project = next((p for p in self.bugbot.github_app.client(owner, repo).get_repo(f"{owner}/{repo}").get_projects() if p.name == proj_name)).id
        self.bugbot.config.guild_options[ctx.guild.id] = options
        print(self.bugbot.config.guild_options)
        self.bugbot.config.save()
        await ctx.reply(f"Successfully connected to GitHub repository `{owner}/{repo}`")
    
    @setup.command()
    async def channel(self, ctx: commands.Context):
        options = self.bugbot.config.guild_options[ctx.guild.id]
        options.voting_channels.append(ctx.channel.id)
        self.bugbot.config.guild_options[ctx.guild.id] = options
        self.bugbot.config.save()
        await ctx.reply(f"Successfully set up this channel for issue creation")