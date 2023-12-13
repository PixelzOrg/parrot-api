"""
This module contains functions for uploading files to Azure Blob Storage.
"""

from azure.storage.blob import ContainerClient
from app.api import blob_service_client

def create_user_container(username: str) -> ContainerClient:
    """
    Creates a container for a specific user.

    Args:
        blob_service_client (BlobServiceClient): Initialized Azure Blob Storage client.
        user_id (str): Unique identifier for the user.

    Returns:
        ContainerClient: The client for the created user container.
    """
    container_name = f"{username}_container"

    try:
        container_client = blob_service_client.get_container_client(container_name)
        container_client.get_container_properties()
    except Exception as e:
        print(e)
        print(f"Creating container {container_name}...")

    new_container_client = blob_service_client.create_container(container_name)

    return new_container_client


def upload_video_user_container(container_client: ContainerClient, file, username: str) -> str:
    """
    Uploads a file to a user's container.

    Args:
        container_client (ContainerClient): The client for the user's container.
        file (File): The file to upload.
    """
    try:
        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload(file)

        file_url = blob_client.url

        return file_url
    except Exception as e:
        print(f'Error uploading file: {e}')
        return None
