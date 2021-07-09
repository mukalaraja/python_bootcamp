from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to?  YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
print(song_names)

# sp = spotipy.Spotify(
#   auth_manager=SpotifyOAuth(
#     scope="playlist-modify-private",
#     redirect_uri="http://mydashboard.com/99def861a4cf479391b9b4bc78b2419d/",
#     client_id= 99def861a4cf479391b9b4bc78b2419d,
#     client_secret= e1856f5805554b4c9e1e426153634096,
#     show_dialog=True,
#     cache_path="token.txt"
#   )
# )
# user_id = sp.current_user()["id"]
# print(user_id)

# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#   result = sp.search(q=f"track:{song} year:{year}", type="track")
#   print(result)
#   try:
#     uri = result["tracks"]["items"][0]["uri"]
#     song_uris.append(uri)
#     except IndexError:
#       print(f"{song} doesn't exist in Spotify. Skipped.")

# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


