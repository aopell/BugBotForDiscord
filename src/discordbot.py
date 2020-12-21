import discord
from discord.ext import commands
import jsons
import cogs
import models
import logging
import github

logging.basicConfig(level=logging.INFO)

class BugBot():
    def __init__(self):
        with open("config/secret.json") as f:
            self.secret = jsons.loads(f.read(), models.Secret)
        with open("config/config.json") as f:
            self.config = jsons.loads(f.read(), models.Config)
        with open("config/gh-app-key.pem") as f:
            self.github_app = github.GithubIntegration(self.secret.github_app_id, f.read())

        self.bot = commands.Bot(self.config.default_prefix, description="A bot for interfacing with GitHub project boards")
        self.bot.add_cog(cogs.Debug(self))

    async def on_ready(self):
        logging.info("READY!")
        pass

    async def on_message(self, message):
        logging.info("MESSAGE!")
        pass

    async def on_raw_reaction_add(self, payload):
        logging.info("REACTION!")
        pass

bugbot = BugBot()
bugbot.bot.run(bugbot.secret.discord_token)