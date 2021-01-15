from os import access
import github
from github.ProjectCard import ProjectCard
from github.ProjectColumn import ProjectColumn
from models.guild_options import GuildOptions

class GitHubApp:
    def __init__(self, app_id, priv_key):
        self.app_id = app_id
        self.app = github.GithubIntegration(app_id, priv_key)

    def client(self, owner, repo) -> github.Github:
        # TODO: caching
        installation = self.app.get_installation(owner, repo)
        access = self.app.get_access_token(installation.id)

        return github.Github(access.token)
    
    def add_card(self, guild: GuildOptions, content: str) -> ProjectCard:
        gh = self.client(guild.github_owner, guild.github_repo)
        proj = gh.get_project(guild.github_project)

        col: ProjectColumn = proj.get_columns()[0]
        
        # content_type: "Issue" or "PullRequest" (not well documented)
        # content_id: Global ID, not issue/PR number
        card = col.create_card(content)

        return proj, card