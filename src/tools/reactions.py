from discord.channel import TextChannel
from discord.member import Member
from discord.message import Message
from discord.raw_models import RawReactionActionEvent
from discord.role import Role
from tools import embeds
from models.guild_options import GuildOptions, IssueCategory

async def handle_create_issue(bot, payload: RawReactionActionEvent):
    async def create_message(guild: GuildOptions, msg: Message, category: IssueCategory):
        proj, card = bot.github_app.add_card(guild, embeds.generate_issue_markdown(guild, msg, payload, category))
        await bot.bot.get_channel(guild.log_channel).send(embed=embeds.generate_issue_embed(msg, proj, card.id, category))

    guild = bot.get_guild(payload.guild_id)
    category = next((category for category in guild.categories if category.icon == str(payload.emoji)), None)
    channel: TextChannel = bot.bot.get_channel(payload.channel_id)
    if not category or not channel:
        return
    msg: Message = await channel.fetch_message(payload.message_id)

    if payload.channel_id in guild.voting_channels:
        member: Member = payload.member
        roles = [r.id for r in member.roles]

        if guild.admin_role in roles:
            await create_message(guild, msg, category)

        elif guild.voter_role in roles:
            # Not implemented yet
            pass


async def handle_modify_issue(bot, payload: RawReactionActionEvent):
    pass