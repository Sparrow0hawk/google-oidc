from authlib.integrations.flask_client import OAuth
from flask import Flask, session, url_for, redirect, render_template

app = Flask(__name__)
app.secret_key = b'!secret'
app.config.from_prefixed_env()

oauth = OAuth(app)

oauth.register(
    "google",
    client_id=app.config["GOOGLE_OAUTH_CLIENT_ID"],
    client_secret=app.config["GOOGLE_OAUTH_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope":"openid email",
    }
)

@app.route('/')
def homepage():
    user = session.get('user')
    return render_template('home.html', user=user)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/auth')
def auth():
    token = oauth.google.authorize_access_token()
    session['user'] = oauth.google.userinfo(token=token)
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')