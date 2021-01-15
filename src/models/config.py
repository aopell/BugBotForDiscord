from dataclasses import dataclass
from typing import List, Dict, Union
from .guild_options import GuildOptions
import jsons

@dataclass
class Config:
    default_prefix: str
    guild_options: Dict[int,GuildOptions]

    def save(self):
        with open("config/config.json", "w") as f:
            f.write(jsons.dumps(self))