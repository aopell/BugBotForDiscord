from dataclasses import dataclass
from typing import List, Union
from .guild_options import GuildOptions

@dataclass
class Config:
    default_prefix: str
    guild_options: List[GuildOptions]