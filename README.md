# Spotify Top Artists

**Built on the base code from: <a href="https://github.com/nitisha-b/spotify-flask-tutorial>spotify-flask-tutorial</a> from <a href="https://hobbyhacks.techtogether.io">HobbyHacks</a>**

Once a user is authorized, this program will showcase the user's top 5 artists and 3 other artists related to those artists. 

### Prerequisites:

1. Make sure you have Python 3.7, Flask installed
```
pip install Flask
pip install spotipy --upgrade
```

2. Get a client and secret key from Spotify and export them: 
```
export SPOTIPY_CLIENT_ID='YOUR CLIENT'
export SPOTIPY_CLIENT_SECRET='YOUR SECRET'
export SPOTIPY_REDIRECT_URI='http://127.0.0.1:5000/oauth/callback'
```

How to run this app locally:

1. Navigate to your terminal
2. `git clone https://github.com/nitisha-b/spotify-flask-tutorial.git`
3. `export FLASK_APP=spotify-app`
4. `export FLASK_ENV=development`
5. `flask run`