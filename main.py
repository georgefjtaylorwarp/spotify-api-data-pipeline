from upload_gcs import upload_blob
from fetch_spotify_metadata import fetch_spotify_track_metadata

query = "Aphex Twin"

# fetch info
track_metadata = str(fetch_spotify_track_metadata(query))

# upload gcs: source_json, bucket_name, destination_blob_name
upload_blob(track_metadata, "spotify_metadata", f"{query}.json")
