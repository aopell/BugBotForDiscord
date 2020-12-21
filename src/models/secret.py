from dataclasses import dataclass
from typing import Union

@dataclass
class Secret:
    github_app_id: Union[int, str]
    discord_token: str