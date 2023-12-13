"""
This module contains functions for uploading data to the SQL database.
"""

from azure.storage.blob import ContainerClient

def upload_new_user(username: str, container_client: ContainerClient):
    """
    Uploads a new user to the database.

    Args:
        username (str): The username of the user.
        container_client (ContainerClient): The client for the user's container.
    
    Returns:
        None
    """


def upload_new_video_link(username: str, video_blob_link: str):
    """
    Uploads a new video link to the database.

    Args:
        username (str): The username of the user.
        video_blob_link (str): The blob link of the video.

    Returns:
        None
    """

