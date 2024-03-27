import requests
from . import urlbuilder


# THIS FILE IS RESPONSABLE FOR API CALLS

def call_access_token(credentials):
    endpoint = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type':'client_credentials'
    }
    headers = {
        'Authorization':f'Basic {credentials}'
    }
    response = requests.post(url=endpoint, data=data, headers=headers)
    
    # Check if request was successful
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.text}")
    
    return response.json()


def call_search(access_token, *args):
    endpoint = urlbuilder.search_endpoint(*args)
    headers = {
        'Authorization':f'Bearer {access_token}'
    }
    response = requests.get(url=endpoint, headers=headers)
    
    # Check if request was successful
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.text}")
    
    return response.json()