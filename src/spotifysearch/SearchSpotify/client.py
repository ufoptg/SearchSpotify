from typing import List, Dict, Optional
from .classes import Authenticator, Results
from . import calls


class Client:
    """
    Client class for handling Spotify search
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Initialize the client with client_id and client_secret
        """
        self.auth = Authenticator(client_id, client_secret)

    def search(self, keywords: str, *, types: Optional[List[str]] = None, filters: Optional[Dict] = None, 
               market: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Results:
        """
        Search Spotify with given parameters
        """
        if types is None:
            types = ['track']
        if filters is None:
            filters = {}
        if limit is not None and limit < 0:
            raise ValueError("Limit should be a positive integer")
        if offset is not None and offset < 0:
            raise ValueError("Offset should be a positive integer")
        
        access_token = self.auth.get_acess_token()
        args = (keywords, types, filters, market, limit, offset)
        response = calls.call_search(access_token, args)
        return Results(response.json())
