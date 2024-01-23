import os
import logging
import urllib.parse

def setup_directory() -> str:
    local_dir = "/tmp/data"
    os.makedirs(local_dir, exist_ok=True)
    return local_dir

def process_event(event: dict) -> tuple:
    """
    Process the event.

    Args:
        event: Event.

    Returns:
        Tuple containing the bucket name and object key.
    """
    logging.info("Receiving Event: %s", event)
    s3_info = event['body']['Records'][0]['s3']
    bucket_name = s3_info['bucket']['name']
    object_key = urllib.parse.unquote_plus(
        s3_info['object']['key'],
        encoding='utf-8'
    )
    logging.info("Bucket: %s, Key: %s", bucket_name, object_key)

    file_extension = os.path.splitext(object_key)[1].lower()

    return bucket_name, object_key, file_extension

def verify_file_extension(file_extension: str) -> bool:
    """
    Verify that the file extension is .mp3 or .mp4.

    Args:
        file_extension: File extension.

    Returns:
        True if the file extension is .mp3 or .mp4, False otherwise.
    """
    return file_extension in ['.mp3', '.mp4']

def extract_file_uid(object_key: str) -> str:
    """
    Extract the file UID from the object key.

    Args:
        object_key: The S3 object key.

    Returns:
        The extracted file UID.
    """
    # Assuming the object key is in the format: <user_uid>/<file_uid>.<extension>
    file_uid_with_extension = object_key.split('/')[-1]  # Get the last part after '/'
    file_uid = os.path.splitext(file_uid_with_extension)[0]  # Remove the file extension
    return file_uid