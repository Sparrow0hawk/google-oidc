# Using Google as OIDC provider 

This is a project testing out how to use Google as an OIDC IdP for use with Flask and Authlib.

## Prerequisites

- Google Cloud project
- Python3.12

## Registering an OAuth2 Client with Google

1. Navigate to https://console.cloud.google.com/apis/credentials
2. Select Create Credentials
3. This opens the Create an OAuth Consent Screen
   1. App name: Example Flask Authlib
   1. User support email: Google group you created for this test
   1. Authorized domain: example.com 
   1. Developer contact email: your email
   1. User type: External
   1. Non sensitive scopes: /auth/userinfo.email openid
1. Back to credentials dashboard, click Create Credentials
1. OAuth client ID
   1. Application type: Web Application
   1. Application name: Test app
   1. Authorized javascript origins: http://127.0.0.1:5000
   1. Authorized redirect URI: http://127.0.0.1:5000/auth
1. Copy your client secret and client ID into a local `.env` file with variable names `FLASK_GOOGLE_OAUTH_CLIENT_ID` and `FLASK_GOOGLE_OAUTH_CLIENT_SECRET`

## App setup

1. Create virtual environment
   ```bash
   python3.12 -m venv --prompt . --upgrade-deps .venv
   ```
1. Activate virtual environment
   ```bash
   . .venv/bin/activate
   ```
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
1. Run app
   ```bash
   flask run
   ```

## Fly.io test deploy

Test this out on Fly.io.

1. Add fly.io domain to Authorized Origin and redirect URI to Google Client.
   Using HTTP protocol as it is Fly.io handling HTTPS enforcement.
1. Set secrets
   ```bash
   fly secrets import < .env
   ```
1. Deploy locally to fly.io
   ```bash
   fly deploy
   ```

## Notes

When testing with localhost I found I was always required to provide consent after selecting my account no matter 
if I'd logged in previously and provided consent. I couldn't find anything in the documentation about this behaviour 
and saw suggestion online there was special treatment of [localhost](https://stackoverflow.com/a/14929345/10651182) forcing
re-consent on every login.

When testing on Fly.io I found I didn't need to provide consent at all (after consenting using localhost) so the 
undocumented behaviour described on Stackoverflow does indeed appear to be the case.
