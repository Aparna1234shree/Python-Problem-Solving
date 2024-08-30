class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration

    def set_title(self, title):
        self.title = title

    def set_artist(self, artist):
        self.artist = artist

    def set_duration(self, duration):
        self.duration = duration


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def get_songs(self):
        return self.songs

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def remove_playlist(self, playlist):
        self.playlists.remove(playlist)

    def get_playlists(self):
        return self.playlists

    def play_song(self, song):
        print(f"Playing: {song.get_title()} by {song.get_artist()}")

    def stop_song(self):
        print("Stopping the song")

    def next_song(self):
        print("Skipping to the next song")

    def previous_song(self):
        print("Going back to the previous song")
