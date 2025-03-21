from google.cloud import storage
import os

def download_pdf_from_gcs(bucket_name: str, source_blob_name: str):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    destination_file_name = f"/tmp/{source_blob_name}"
    blob.download_to_filename(destination_file_name)
    return destination_file_name

def upload_pdf_to_gcs(bucket_name: str, file):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file.file)
    return file.filename

def delete_pdf_from_gcs(bucket_name: str, blob_name: str):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()
    return True