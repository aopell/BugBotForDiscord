from datetime import datetime
from discord.embeds import Embed
from discord.message import Message
from github.Project import Project
from github.ProjectCard import ProjectCard
from models.guild_options import GuildOptions, IssueCategory
from discord.raw_models import RawReactionActionEvent

NEWLINE = '\n'

def generate_issue_embed(msg: Message, proj: Project, card_id: int, category: IssueCategory) -> Embed:
    embed = Embed(title=f"{category.icon} `{category.prefix}-{card_id}`", description=msg.content, timestamp=msg.created_at, color=0xc4ff0e).set_author(name=str(msg.author), icon_url=msg.author.avatar_url)
    if len(msg.attachments) > 0:
        embed.set_image(url=msg.attachments[0].url)
    
    embed = embed.set_footer(text=card_id).add_field(name="Jump to Message", value=f"[Click Here]({msg.jump_url})").add_field(name="GitHub Card", value=f"[Click Here]({proj.html_url}#card-{card_id})")

    return embed


def generate_issue_markdown(guild: GuildOptions, msg: Message, payload: RawReactionActionEvent, category: IssueCategory) -> str:
    return (
f"""
**{category.emoji} {category.name}**
{msg.content}
> ***{msg.author}** in **{msg.guild.name} #{msg.channel.name}** [at {msg.created_at.isoformat()}]({msg.jump_url})*

{NEWLINE.join([f'![{att.filename}]({att.url})' for att in msg.attachments])}
"""
    ).strip()