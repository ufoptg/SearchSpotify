from . import calls
from .classes import Authenticator, Results
import re  # Import regular expression module for link parsing


class Client:

    def __init__(self, client_id, client_secret):
        self.auth = Authenticator(client_id, client_secret)

    def search(
        self,
        query: str,  # Accept query or link
        *,
        types: list = ["track"],
        filters: dict = {},
        market: str = None,
        limit: int = None,
        offset: int = None
    ) -> Results:
        access_token = self.auth.get_acess_token()
        # Check if the input is a link
        if "spotify.com" in query:
            if "track" in query:
                # Extract track ID from the track link
                track_id = self.extract_track_id(query)
                if not track_id:
                    raise ValueError("Invalid Spotify link")
                query = f"track:{track_id}"  # Modify query to search by track ID
            elif "playlist" in query:
                # Extract playlist ID from the playlist link
                playlist_id = self.extract_playlist_id(query)
                if not playlist_id:
                    raise ValueError("Invalid Spotify link")
                query = f"playlist:{playlist_id}"  # Modify query to search by playlist ID
            elif "album" in query:
                # Extract album ID from the album link
                album_id = self.extract_album_id(query)
                if not album_id:
                    raise ValueError("Invalid Spotify link")
                query = f"album:{album_id}"  # Modify query to search by album ID
            elif "artist" in query:
                # Extract artist ID from the artist link
                artist_id = self.extract_artist_id(query)
                if not artist_id:
                    raise ValueError("Invalid Spotify link")
                query = f"artist:{artist_id}"  # Modify query to search by artist ID
            else:
                raise ValueError("Unsupported Spotify link")
        args = (query, types, filters, market, limit, offset)
        response = calls.call_search(access_token, args)
        return Results(response.json())

    def extract_track_id(self, link):
        # Use regular expression to extract track ID from Spotify track link
        match = re.search(r'/track/([a-zA-Z0-9]+)', link)
        if match:
            return match.group(1)
        return None
    
    def extract_playlist_id(self, link):
        # Use regular expression to extract playlist ID from Spotify playlist link
        match = re.search(r'/playlist/([a-zA-Z0-9]+)', link)
        if match:
            return match.group(1)
        return None

    def extract_album_id(self, link):
        # Use regular expression to extract album ID from Spotify album link
        match = re.search(r'/album/([a-zA-Z0-9]+)', link)
        if match:
            return match.group(1)
        return None

    def extract_artist_id(self, link):
        # Use regular expression to extract artist ID from Spotify artist link
        match = re.search(r'/artist/([a-zA-Z0-9]+)', link)
        if match:
            return match.group(1)
        return None
