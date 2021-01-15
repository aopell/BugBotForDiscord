import re
from attr import s
from discord.ext import commands
import discord
from discord.message import Message
from discord.raw_models import RawReactionActionEvent
import jsons
import cogs
from cogs.debug import Debug
import models
import logging
import github
from models.guild_options import GuildOptions
from tools.github import GitHubApp
from tools import reactions, embeds

logging.basicConfig(level=logging.INFO)

class BugBot():
    def __init__(self):
        with open("config/secret.json") as f:
            self.secret = jsons.loads(f.read(), models.Secret)
        with open("config/config.json") as f:
            self.config = jsons.loads(f.read(), models.Config)
        with open("config/gh-app-key.pem") as f:
            self.github_app = GitHubApp(self.secret.github_app_id, f.read())

        self.bot = commands.Bot(command_prefix=commands.bot.when_mentioned_or(self.config.default_prefix), description="A bot for interfacing with GitHub project boards")
        
        for cog in cogs.__dict__.values():
            if type(cog) == commands.cog.CogMeta:
                self.bot.add_cog(cog(self))
        
        @self.bot.event
        async def on_ready():
            logging.info("READY!")
            [print(str(x) + ": " + repr(x)) for x in self.bot.commands]
            pass
        
        @self.bot.event
        async def on_message(message: Message):
            # match = re.search(r'`([A-Z]+)-(\d+)`', str(message.content))
            # if match:
            #     category = match.group(1)
            #     number = int(match.group(2))

            #     guild = self.get_guild(message.guild.id)
                                    

            await self.bot.process_commands(message)

        @self.bot.event
        async def on_raw_reaction_add(payload: RawReactionActionEvent):
            await reactions.handle_create_issue(self, payload)
            await reactions.handle_modify_issue(self, payload)
    
    def get_guild(self, guild_id: int) -> GuildOptions:
        return self.config.guild_options[guild_id]

bugbot = BugBot()
bugbot.bot.run(bugbot.secret.discord_token)