from upload_gcs import upload_blob
from fetch_spotify_metadata import fetch_spotify_track_metadata

query = "Never Gonna Give You Up"

# fetch info
track_metadata = fetch_spotify_track_metadata(query)

# upload gcs
upload_blob(track_metadata, "spotify_metadata", f"{query}.json")
