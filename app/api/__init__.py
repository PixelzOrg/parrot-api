import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

connect_str = os.getenv('AZURE_MEDIA_STORAGE_CONN_STR')
if not connect_str:
    raise ValueError("Please set the AZURE_MEDIA_STORAGE_CONN_STR environment variable")

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
