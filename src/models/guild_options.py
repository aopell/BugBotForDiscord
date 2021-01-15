from dataclasses import dataclass
from typing import List, Union


@dataclass
class IssueCategory:
    name: str
    prefix: str
    icon: str
    emoji: str


@dataclass
class GuildOptions:
    guild_id: int
    admin_role: int
    voter_role: int

    min_votes: int
    log_channel: int
    
    github_owner: str
    github_repo: str
    github_project: int

    voting_channels: List[int]
    categories: List[IssueCategory]