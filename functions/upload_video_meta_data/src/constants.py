import os

DB_HOST = os.environ.get('AWS_USER_VIDEO_RDS_HOST')
DB_NAME = os.environ.get('AWS_USER_VIDEO_RDS_NAME')
DB_USER = os.environ.get('AWS_USER_VIDEO_RDS_USER')
DB_PASSWORD = os.environ.get('AWS_USER_VIDEO_RDS_PASSWORD')

INSERT_VIDEO_METADATA_SQL = """
    INSERT INTO VideoMetadata 
    (video_uuid, title, uploader_username, uploader_email, upload_date, duration, resolution, frame_rate, language, location) 
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s)
"""