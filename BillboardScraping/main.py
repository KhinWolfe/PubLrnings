import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
URL = "https://www.billboard.com/charts/hot-100/"
#year = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD:\n")
year = "1991-04-06"

response = requests.get(URL + year)
response.encoding = "utf-8"
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

song_list = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_list]


SPOTIFY_UN = "plrning@outlook.com"
# t3mporaryaccount

SPOTIPY_REDIRECT_URI = "http://example.com"
SPOTIPY_CLIENT_ID="141ab2c13f384a59b524285d3fdf67fa"
SPOTIPY_CLIENT_SECRET = "76c98021c4114279855ba686bd72ffb3"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_UN
    )
)
user_id = sp.current_user()["id"]
print(user_id)
song_uris = []
header = {
    "Authorization":user_id
}
query = {
    "q":song_names[0],
    "type":"track",
    "limit":1
}
for song in song_names:
    result = sp.search(q=f"{song}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["id"]#["album"]["artists"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found. Skipped")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{year} Billboard 100",
    public=False
)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("ok")