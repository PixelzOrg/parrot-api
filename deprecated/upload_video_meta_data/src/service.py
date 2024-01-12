import json
from database import DatabaseManager
from models import validate_video_metadata
from constants import INSERT_VIDEO_METADATA_SQL

db = DatabaseManager()

def upload_video_meta_data_service(video_uuid, video_meta_data):
    """
    Validates the video metadata and uploads it to the database.

    Args:
      video_uuid (str): The video's UUID.
      video_meta_data (Dict[str, Optional[str]]): A dictionary representing the video metadata.
    """
    # Validate the video metadata
    try:
      validate_video_metadata(video_meta_data)
    except Exception as e:
      raise ValueError(
        f"Invalid video metadata: {e}"
      )

    try:
      params = (
         video_meta_data.title,
         video_meta_data.uploader_username,
         video_meta_data.uploader_email,
         video_meta_data.upload_date,
         video_meta_data.duration,
         video_meta_data.resolution,
         video_meta_data.frame_rate,
         video_meta_data.language,
         video_meta_data.location
      )
      db.execute_query(INSERT_VIDEO_METADATA_SQL, params)
      db.close_connection()
      return "Video metadata uploaded successfully"
    except Exception as e:
      raise Exception(
        f"Failed to upload video metadata to database: {e}"
      )

