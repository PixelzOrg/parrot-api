from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class VideoMetadata:
    video_uuid: str = ""             # The video's UUID.
    title: str = ""                  # The title or name of the video.
    uploader_username: str = ""      # The username of the user who uploaded the video.
    uploader_email: str = ""         # The email address of the user who uploaded the video.
    upload_date: str = ""            # The date and time when the video was uploaded.
    duration: str = ""               # The length or duration of the video.
    resolution: str = ""             # The video's resolution (e.g., "1920x1080").
    frame_rate: str = ""             # Number of frames per second (e.g., "30 FPS").
    language: str = ""               # The primary language(s) spoken in the video.
    location: str = ""               # Geographical location where the video was recorded.

def validate_video_metadata(video_metadata: Dict[str, Optional[str]]) -> None:
    """
    Validate the video metadata to ensure it meets the required criteria before entering the database.
    
    Args:
        video_metadata (Dict[str, Optional[str]]): A dictionary representing the video metadata.
        
    Raises:
        ValueError: If any attribute does not match its expected type or exceeds its maximum length.
    """
    # Define the expected types and maximum lengths for each attribute
    expected_types = {
        "video_uuid": str,
        "title": str,
        "uploader": dict,
        "upload_date": str,
        "duration": str,
        "resolution": str,
        "frame_rate": str,
        "language": str,
        "location": str
    }

    max_lengths = {
        "video_uuid": 36,
        "title": 100,
        "upload_date": 10,
        "duration": 10,
        "resolution": 10,
        "frame_rate": 10,
        "language": 50,
        "location": 100
    }

    # Validate each attribute against its expected type and maximum length
    for attr_name, expected_type in expected_types.items():
        actual_value = video_metadata.get(attr_name)
        
        if not isinstance(actual_value, expected_type):
            raise ValueError(
                f"Expected type {expected_type} for attribute {attr_name}, \
                but got {type(actual_value)}"
            )
        
        if actual_value is not None and \
        len(str(actual_value)) > max_lengths.get(attr_name, 0):
            raise ValueError(
                f"Attribute {attr_name} exceeds the maximum length \
                of {max_lengths[attr_name]} characters."
            )
        