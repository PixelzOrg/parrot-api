"""
This module contains functions for servicing our Azure Storage Blob

This handles all data validation, making sure everything is sent correctly.

Checks if the file is empty, if the user exists, and if the file is a video.
"""

from app.database.videos import upload_new_video
from app.api import blob_service_client

def upload_video_for_user(username: str, file) -> str:
    """
    Uploads a video file to a user's container in Azure Blob Storage

    Args:
        username (str): The username of the user.
        file (File): The video to upload.
    
    Returns:
        str: The URL of the uploaded video.
    """
    if not file:
        return jsonify({'error': 'No video file provided.'}), 400
    if not user:
        return jsonify({'error': 'No user provided.'}), 400
    
    return video_blob_url

def fetch_video_for_user(username: str, video_id: str) -> str:
    """
    Fetches a video file from a user's container in Azure Blob Storage

    Args:
        username (str): The username of the user.
        video_id (str): The ID of the video to fetch.
    
    Returns:
        str: The URL of the fetched video.
    """
    if not username:
        return jsonify({'error': 'No username provided.'}), 400
    if not video_id:
        return jsonify({'error': 'No video ID provided.'}), 400
    
    return video_blob_url

def fetch_videos_based_on_date(username: str, date: str) -> str:
    """
    Fetches all video files from a user's container in Azure Blob Storage based on a date

    Args:
        username (str): The username of the user.
        date (str): The date to fetch videos for.
    
    Returns:
        str: The URL of the fetched video.
    """
    if not username:
        return jsonify({'error': 'No username provided.'}), 400
    if not date:
        return jsonify({'error': 'No date provided.'}), 400
    
    return video_blob_url

def fetch_all_videos_for_user(username: str) -> str:
    """
    Fetches all video files from a user's container in Azure Blob Storage

    Args:
        username (str): The username of the user.
    
    Returns:
        str: The URL of the fetched video.
    """
    if not username:
        return jsonify({'error': 'No username provided.'}), 400
    if not video_id:
        return jsonify({'error': 'No video ID provided.'}), 400
    
    return video_blob_url