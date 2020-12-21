import github

APP_ID = 0 # redacted
OWNER = ""
REPO = ""

with open("config/gh-app-key.pem") as f:
    app = github.GithubIntegration(APP_ID, f.read())

installation = app.get_installation(OWNER, REPO)
token = app.get_access_token(installation.id)

github.Github(token)