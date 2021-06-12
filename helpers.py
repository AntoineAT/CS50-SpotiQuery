from flask import render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Set up for Spotify client credentials flow authorization
client_credentials_manager = SpotifyClientCredentials(
    client_id='b8071c873bda4fa39f4d3d68cfa2fc39',
    client_secret='9c3c1936cc1c4f9e8b7a4cf74b19e281'
)


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def all_albums(artist_name):
    """ Return a simplified artist object as a dict. """

    # Contact API for an artist
    try:
        # Initialize a Spotipy object to use functions of Spotipy library
        spotipy_object = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        response = spotipy_object.search(q='artist:' + artist_name, type='artist', limit=1)
        
    except Exception:
        return None

    # Parse response
    try:
        # Simplifiy artist object
        artist_items = response['artists']['items'][0]
        
        # Contact API for artist's albums and simplify it
        albums_respone = spotipy_object.artist_albums(artist_items['id'], limit=1,album_type='album,single')
        albums = []

        while True:
            albums.extend(albums_respone['items'])
            albums_respone = spotipy_object.next(albums_respone)
            
            if not albums_respone['next']:
                break
        
        return {
            "name": artist_items['name'],
            "followers": artist_items['followers']['total'],
            "popularity": artist_items['popularity'],
            "image": artist_items['images'][1]['url'],
            "genres": artist_items['genres'],
            "albums": albums,
            "url": artist_items['external_urls']['spotify']
        }
    except (KeyError, TypeError, ValueError, IndexError):
        return None


def top_10_tracks(artist_name, country):
    """ Return a simplified artist object as a dict. """

    # Contact API for an artist
    try:
        # Initialize a Spotipy object to use functions of Spotipy library
        spotipy_object = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        response = spotipy_object.search(q='artist:' + artist_name, type='artist', limit=1)
        
    except Exception:
        return None

    # Parse response
    try:
        # Simplifiy artist object
        artist_items = response['artists']['items'][0]
        
        # Contact API for artist's top tracks
        tracks_respone = spotipy_object.artist_top_tracks(artist_items['id'], country=country)
        tracks = tracks_respone['tracks']
        
        return {
            "name": artist_items['name'],
            "followers": artist_items['followers']['total'],
            "popularity": artist_items['popularity'],
            "image": artist_items['images'][1]['url'],
            "genres": artist_items['genres'],
            "tracks": tracks,
            "url": artist_items['external_urls']['spotify']
        }
    except (KeyError, TypeError, ValueError, IndexError):
        return None


def commafy(value):
    """Format value as USD."""
    return f"{value:,}"
