from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)
import spotipy
from spotipy import oauth2

bp = Blueprint('spotify', __name__)

SCOPE = 'user-top-read user-read-currently-playing user-modify-playback-state'
CACHE = '.spotifycache'
# Reads client id and client secret from environment variables
sp_oauth = oauth2.SpotifyOAuth(scope=SCOPE,cache_path=CACHE )

@bp.route('/', methods=['GET'])
def login():
    # If auth token is already cached and not expired, use that else redirect
    # user to login or refresh token
    token_info = sp_oauth.get_cached_token()
    if token_info and not sp_oauth.is_token_expired(token_info):
        access_token = token_info['access_token']
        session['access_token'] = access_token
        return redirect(url_for('spotify.top_artists'))
    else:
        login_url = sp_oauth.get_authorize_url()
        return redirect(login_url)

# After generating code, Spotify redirects to this endpoint
@bp.route('/oauth/callback', methods=['GET'])
def set_token():
    code = request.args['code']
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    session['access_token'] = access_token
    return redirect(url_for('spotify.top_artists'))

# Get all of your top artists and your currently playing song
@bp.route('/top_tracks', methods=['GET'])
def top_artists():
    access_token = session['access_token']
    sp_api = spotipy.Spotify(access_token)
    top_artists_result = sp_api.current_user_top_artists()
        
    all_top_artists = []
    for t in top_artists_result['items']:
        top_artist = {}
        top_artist['artist_name'] = t['name']
        top_artist['id'] = t['id']
        top_artist['top_tracks_list'] = sp_api.artist_top_tracks(t['id'])
        top_artist['artist_image'] = t['images'][0]['url']
        top_artist['related_artists_list'] = sp_api.artist_related_artists(t['id'])
        all_top_artists.append(top_artist)

    for artist in all_top_artists:
        # Sort top tracks by popularity to get the most popular one
        # tracks_list = artist['top_tracks_list']['tracks']
        # print(tracks_list.sort(key= lambda x:x['popularity'])
        
        artist['top_track'] = artist['top_tracks_list']['tracks'][0]['name']
        artist['top_track_id'] = artist['top_tracks_list']['tracks'][0]['id']
        
        # Get top related artist name, id, and image
        artist['related_artist'] = artist['related_artists_list']['artists'][0]['name']
        artist['related_artist_id'] = artist['related_artists_list']['artists'][0]['id']
        artist['related_artist_top_tracks'] = sp_api.artist_top_tracks(artist['related_artist_id'])

    # Process related artist's information
    for art in all_top_artists:
        art['related_artist_image'] = art['related_artists_list']['artists'][0]['images'][0]['url']
        print(art['related_artist'])
        print("\n")

        # Get related artist's top track
        art['related_artist_top_track'] = art['related_artist_top_tracks']['tracks'][0]['name']
        art['related_artist_top_track_id'] = art['related_artist_top_tracks']['tracks'][0]['id']

    current_playing = {}
    result = sp_api.current_user_playing_track()
    if result:
        current_song_result = result['item']
        current_playing['song'] = current_song_result['name']
        current_playing['image'] = current_song_result['album']['images'][0]['url']
        current_playing['artist'] = current_song_result['artists'][0]['name']
    return render_template('top_tracks.html', top_tracks=all_top_artists, 
    current_playing=current_playing)

# Add one of your top songs to the back of your queue
@bp.route('/add_to_queue/<track_id>', methods=['POST'])
def add_to_queue(track_id):
    access_token = session['access_token']
    sp_api = spotipy.Spotify(access_token)
    sp_api.add_to_queue(track_id)
    # return redirect(url_for('spotify.top_tracks'))
    return redirect(url_for('spotify.top_artists'))