import os
import base64
import json
import requests
from dotenv import load_dotenv


def spotify_auth():
    # load environment variables from .env file
    load_dotenv()

    request_url = "https://accounts.spotify.com/api/token"
    CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

    # encode credentials into bytes, then decode into a string for the HTTP POST request to Spotify to authenticate
    BASE64_ENCODED_HEADER_STRING = base64.b64encode(bytes(f"{CLIENT_ID}:{CLIENT_SECRET}", "ISO-8859-1")).decode("ascii")

    # initializing dictionaries for the request
    headers = {
        'Authorization': f"Basic {BASE64_ENCODED_HEADER_STRING}"
    }

    data = {
        'grant_type': "client_credentials",
        'json': True
    }

    # make request
    r = requests.post(url=request_url, headers=headers, data=data)

    # print(json.dumps(r.json(), indent=2))
    
    token = r.json()['access_token']
    return token
