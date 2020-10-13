# Spotify Top Artists

**Built on the base code from: <a href="https://github.com/nitisha-b/spotify-flask-tutorial">spotify-flask-tutorial</a> from <a href="https://hobbyhacks.techtogether.io">HobbyHacks</a>**

The program will first ask for the user's authorization, and once authorized, will display the user's top 5 artists, these artists' top track, another artist related to each of the 5 artists, and the related artist's top track. 

If the user has their Spotify running, all of the tracks shown in the webpage can be added to their current queue on Spotify. 

If the user is listening to a song on Spotify it will be displayed at the top of the screen as "Currently Playing". 

## Walkthrough
<img src="http://g.recordit.co/WfTo79DUDH.gif" width=550 height=350>

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

3. How to run this app locally:

i. Navigate to your terminal
ii. `git clone https://github.com/nitisha-b/spotify-flask-tutorial.git`
iii. `export FLASK_APP=spotify-app`
iv. `export FLASK_ENV=development`
v. `flask run`