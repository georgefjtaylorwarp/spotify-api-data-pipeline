from google.cloud import storage

def upload_blob(source_file, bucket_name, destination_blob_name):

    # Make an authenticated API request
    # buckets = list(storage_client.list_buckets())
    # print(buckets)

    storage_client = storage.Client.from_service_account_json('credentials/gcs_service_account.json')

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(source_file)

    print(f"File {source_file} uploaded to {destination_blob_name}.")
