import os
from dotenv import load_dotenv
import base64
import requests

def spotify_auth():
    # load environment variables from .env file
    load_dotenv()

    CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

    # encode credentials into bytes, then decode into ascii
    BASE64_ENCODED_HEADER_STRING = base64.b64encode(bytes(f"{CLIENT_ID}:{CLIENT_SECRET}", "ISO-8859-1")).decode("ascii")

    # initializing dictionaries for the request
    headers = {
        'Authorization': f"Basic {BASE64_ENCODED_HEADER_STRING}"
    }

    data = {
        'grant_type': "client_credentials",
        'json': True
    }

    request_url = "https://accounts.spotify.com/api/token"
    r = requests.post(url=request_url, headers=headers, data=data)
    
    token = r.json()['access_token']
    return token
