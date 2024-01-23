import os
import json
import logging
import boto3
from utility import process_event, verify_file_extension, setup_directory, extract_file_uid
from dynamodb import update_dynamodb
from sqs import send_message_to_queue
from transcription import WhisperModel

s3 = boto3.client("s3")
local_dir = setup_directory()
whisper = WhisperModel("base")
dynamodb = boto3.resource("dynamodb")
mp3_table = dynamodb.Table("mp3-file-dump")
mp4_table = dynamodb.Table("mp4-file-dump")

def handler(event, context):
    try:
        bucket_name, object_key, file_extension = process_event(event)

        if not verify_file_extension(file_extension):
            logging.info("Invalid file extension: %s", file_extension)
            raise ValueError(
                f"""Invalid file extension, 
                only .mp3 and .mp4 are supported,
                received: {file_extension}"""
            )
        
        local_file_path = os.path.join(local_dir, os.path.basename(object_key))

        logging.info("Downloading file to: %s", local_file_path)
        s3.download_file(bucket_name, object_key, local_file_path)
        logging.info("Downloaded file to: %s", local_file_path)

        if file_extension == '.mp3':
            process_mp3_file(local_file_path, object_key)
        
        if file_extension == '.mp4':
            process_mp4_file(local_file_path, object_key)

    except Exception as e:
        logging.info("Error processing the file: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps("Error processing the file")
        }
def process_mp3_file(local_file_path: str, object_key: str):
    """
    Process the MP3 file.

    Args:
        local_file_path: Local file path.
        object_key: Object key.
    """
    result = whisper.model.transcribe(local_file_path)
    logging.info("Transcribed file")
    
    transcription_text = result['text'].strip()
    file_uid = extract_file_uid(object_key)

    update_dynamodb(mp3_table, file_uid, transcription_text)
    send_message_to_summary_queue(object_key)

def process_mp4_file(local_file_path: str, object_key: str):
    """
    Process the MP4 file.

    Args:
        local_file_path: Local file path.
        object_key: Object key.
    """
    result = whisper.model.transcribe(local_file_path)
    logging.info("Transcribed file")

    transcription_text = result['text'].strip()
    file_uid = extract_file_uid(object_key)

    update_dynamodb(mp4_table, file_uid, transcription_text)
    send_message_to_summary_queue(object_key)
