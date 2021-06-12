# CS50 SpotiQuery
#### Video Demo: https://youtu.be/xmQRsamhOGQ
#### Description:
Hello world! In CS50 final project, I've made myself a web app, which call CS50 SpotiQuery that use Spotify API to query the information that I'm curious about.
By using this web app, you and I can search for any artists that Spotify have in their database, and it will show you some useful information about that artists.

##### What CS50 SpotiQuery does?
Firtly, when going to the homepage, you will notice that there are 2 functions that this web app has, which are "All Albums" and "Top 10 Tracks".

"All Albums" function will show some information of any artist that you want to know and all allbums of the artist that Spotify have in their database. All you have to do is just click "All Albums" and search for the artist, that's it.

The remaining function is "Top 10 Tracks". This function will ask you to enter an artist and the country code to limit the result to a specific market of that artist. Then it will show you the top 10 tracks of that artist in the market you have entered. If you don't know what your country code is, then you can lookup by click the link below which is showm "Read ISO 3166-1 alpha-2 country code".

Finally, I could add some more features to this web app in the future if anyone want me to do that. By now, those 2 functions have shown all the information that I'm curious about.

##### Understanding:
`**helpers.py**`
Atop of the file are some imports, among them are `spotipy` library, which someone wrote to handle with Spotify API. So, I just use that (it is published on pypi.org).

Next you will encounter `client_credentials_manager` which is used to set up my web app that Spotify request me to do.

I keep using the `apology` function from CS50 Finance which is use to render an message when encounter error to the user, because it's useful and funny.

Then I create `all_albums`function to return a simplified an artist object (as dict) to contain most useful information when I receive the response of Spotify API. In the first `try` block, I contact the API for an artist that the user type in. To do that, I initialize a `spotipy` object and use its `search` function.
In the second `try` block, I parse the respone by  just return information that I need and get rid of redundancy. The information that I need to return in `all_albums` function is the artist's info and all of his/her albums in Spotify database.

Next, `top_10_tracks` almost the same thing as `all_albums`, except it returns "top 10 tracks" of him/her instead of all the albums.

At the bottom, `commafy` is just a "filter", which is use to format the "followers" values which you will see when you use the web app.

`**app.py**`
This is the main file of my web app. Atop of the file are some basic imports and configuring Flask.

Right below you can see a `COUNTRY_CODES` list with a bunch of 2-letters country codes which is later used to check for validation of country codes when the user enter in the form of the web app.
`app.py` contains 3 routes in total, which are `'/'`, `'/albums'` and `'/toptracks'`.

The logic in both `'/albums'` and `'/toptracks'` are quite simple, all the `if` block in both routes are to check validation for the user input. The whole bunch of assignments below are just to simplify and take all information that I wrote in `helpers.py` and then pass all of them to `render_template` to show on the web.

`**static/**`
Inside of this folder is `style.css` which is used for aesthetic of the website.

`**templates/**`
All the html file are put in this folder.

That's all, thank you for your time and your attention!

And this is CS50!