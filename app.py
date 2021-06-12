from helpers import apology, all_albums, top_10_tracks, commafy
from flask import Flask, request, render_template

# Configure application
app = Flask(__name__)

COUNTRY_CODES = [
    "AD", "AE", "AF", "AG", "AI", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ",
    "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ",
    "CA", "CC", "CD", "CF", "CG", "CH", " CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ",
    "DE", "DJ", "DK", "DM", "DO", "DZ",
    "EC", "EE", "EG", "EH", "ER", "ES", "ET",
    "FI", "FJ", "FK", "FM", "FO", "FR",
    "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY",
    "HK", "HM", "HN", "HR", "HT", "HU",
    "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT",
    "JE", "JM", "JO", "JP",
    "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ",
    "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV",
    "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ",
    "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ",
    "OM",
    "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY",
    "QA",
    "RE", "RO", "RS", "RU", "RW",
    "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ",
    "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TW", "TZ",
    "UA", "UG", "UM", "US", "UY", "UZ",
    "VA", "VC", "VE", "VG", "VI", "VN", "VU",
    "WF", "WS",
    "YE", "YT",
    "ZA", "ZM", "ZW"]


@app.route('/')
def index():
    """ Welcome screen """
    return render_template('index.html')


@app.route('/albums', methods=['GET', 'POST'])
def albums():
    ''' Search for an artist then show some info
        that Spotify has on the artist
        and show all the albums of the artist. '''

    # User submit a form via POST  
    if request.method == 'POST':

        # Ensure user enter artist name
        if not request.form.get('artist'):
            return apology("Don't leave that form blank!", 400)

        # Ensure artist is exist
        if all_albums(request.form.get('artist')) == None:
            return apology('invalid artist!', 404)

        # Extract info from artist object

        artist_url = all_albums(request.form.get("artist"))['url']
        name       = all_albums(request.form.get("artist"))['name']
        followers  = commafy(all_albums(request.form.get("artist"))['followers'])
        popularity = all_albums(request.form.get("artist"))['popularity']
        img        = all_albums(request.form.get("artist"))['image']
        albums     = all_albums(request.form.get("artist"))['albums']

        return render_template("show_albums.html", img=img, artist_url=artist_url, name=name, followers=followers, popularity=popularity, albums=albums)
    
    else:
        return render_template('search_albums.html')
    

@app.route('/toptracks', methods=['GET', 'POST'])
def toptracks():
    ''' Search for artist then show the artwork and top 10 tracks of artist '''

    # User submit form via POST
    if request.method == 'POST':

        # Ensure user enter artist name and country code
        if not request.form.get('artist') or not request.form.get('country'):
            return apology("Don't leave that form blank!")

        # Ensure artist or country is exist
        if request.form.get('artist') == None:
            return apology('invalid artist!')

        # Ensure country code is alphabetical
        if request.form.get('country').isalpha() == False:
            return apology('country code must be alphabetical')

        # Ensure country code is exist
        for i in COUNTRY_CODES:
            if request.form.get('country').upper() not in COUNTRY_CODES:
                return apology('invalid country code!')

        # Extract info from artist object
        artist_url = top_10_tracks(request.form.get("artist"), request.form.get('country'))['url']
        name       = top_10_tracks(request.form.get("artist"), request.form.get('country'))['name']
        followers  = commafy(top_10_tracks(request.form.get("artist"), request.form.get('country'))['followers'])
        popularity = top_10_tracks(request.form.get("artist"), request.form.get('country'))['popularity']
        img        = top_10_tracks(request.form.get("artist"), request.form.get('country'))['image']
        tracks     = top_10_tracks(request.form.get("artist"), request.form.get('country'))['tracks']

        return render_template("show_toptracks.html", img=img, artist_url=artist_url, name=name, followers=followers, popularity=popularity, tracks=tracks)
    else:
        return render_template('search_toptracks.html')