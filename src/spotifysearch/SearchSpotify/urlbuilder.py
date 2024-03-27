from typing import List, Dict, Optional
from urllib.parse import urlencode


def search_endpoint(keywords: str, allowed_types: List[str], filters: Dict[str, str], 
                    market: Optional[str] = None, limit: Optional[int] = None, 
                    offset: Optional[int] = None) -> str:
    """
    Function to build a dynamic URL for Spotify search endpoint.

    :param keywords: Search keywords.
    :param allowed_types: List of allowed types.
    :param filters: Dictionary of filters.
    :param market: Market filter.
    :param limit: Limit for the number of results.
    :param offset: Offset for the results.
    :return: Formatted URL.
    """
    base_url = 'https://api.spotify.com/v1/search?'

    # Format query items and filters
    query_items = keywords.split(' ')
    for filter, value in filters.items():
        item = f'{filter}:{value}'
        query_items.append(item)

    # Required arguments
    query = ' '.join(query_items)
    types = ','.join(allowed_types)

    # Optional arguments
    params = {'q': query, 'type': types, 'market': market, 'limit': limit, 'offset': offset}
    params = {k: v for k, v in params.items() if v is not None}  # Remove None values

    return base_url + urlencode(params)
