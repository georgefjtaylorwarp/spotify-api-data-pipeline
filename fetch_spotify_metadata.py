import requests
from spotify_auth import spotify_auth

def parse_spotify_metadata(json_data):

    metadata = []

    for i in range(len(json_data['tracks']['items'])):
        track = {
            'name': json_data['tracks']['items'][i]['name'],
            'artist': json_data['tracks']['items'][i]['artists'][0]['name'],
            'album': json_data['tracks']['items'][i]['album']['name'],
            'url': json_data['tracks']['items'][i]['external_urls']['spotify']
        }
        metadata.append(track)
    
    return metadata

def fetch_spotify_track_metadata(q):
    token = spotify_auth()

    url = f"https://api.spotify.com/v1/search?q={q}&type=track"

    headers = {
        'Authorization': f"Bearer {token}"
    }

    r = requests.get(url=url, headers=headers)
    metadata = parse_spotify_metadata(r.json())
    
    return metadata
