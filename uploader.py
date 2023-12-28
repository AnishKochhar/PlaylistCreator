from dotenv import load_dotenv
from datetime import date
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyTrack():
    def __init__(self, uri, name, artist):
        self.uri = uri
        self.name = name
        self.artist = artist

class SpotifyUploader():

    def __init__(self):
        self.spotify_playlist = []
        load_dotenv()
        scope = 'playlist-modify-public playlist-modify-private user-library-read'
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def createPlaylist(self, playlist):
        print("Creating playlist of...")
        song_count = 0
        for name, artist in playlist:
            try:
                search_query = "{0}%20artist%3A{1}".format(name, artist)
                response = self.spotify.search(search_query)
                item = response["tracks"]["items"][0] # get the first track
                track = SpotifyTrack(item["uri"], item["name"], item["artists"][0])
                print("{} : {}".format(name, artist))
                print("{}. {} : {}".format(song_count, item["name"], item["artists"][0]["name"]))
                song_count += 1
                self.spotify_playlist.append(track)
            except:
                print("Track not found: {} - {}".format(name, artist))
    
    def uploadPlaylist(self):
        print("Saving to your library...")

        name = date.today().strftime("%d/%m/%Y")
        user_id = self.spotify.current_user()["id"]
        response = self.spotify.user_playlist_create(user_id, name, public=True)
     
        playlist_id = response["id"]

        tracks = [track.uri for track in self.spotify_playlist]
        self.spotify.user_playlist_add_tracks(user_id, playlist_id, tracks)
        return name
    
    def upload(self, playlist):
        print("Creating a playlist of your tracks...")
        self.createPlaylist(playlist)
        playlist_name = self.uploadPlaylist()
        print("A Spotify playlist has been created with the name {}!".format(playlist_name))

    