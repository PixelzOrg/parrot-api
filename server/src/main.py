import logging
import os

from openai import OpenAI
from tools.sqs_interface import SQSInterface
from tools.dynamo_interface import DynamoDbInterface
from tools.s3_interface import S3Interface
from audio import AudioProcessor
from video import VideoProcessor
from summary import SummaryProcessor
from utils.utility import setup_directory, extract_file_from_message, get_open_ai_key
from models.sqs_models import SqsServerMessage

open_ai_key = get_open_ai_key()
open_ai_client = OpenAI(api_key=open_ai_key)

audio_process = AudioProcessor("base")
video_process = VideoProcessor(open_ai_client)
summary_process = SummaryProcessor(open_ai_client)
sqs = SQSInterface()
dynamo = DynamoDbInterface()
s3 = S3Interface()
local_dir = setup_directory()

def process_message(message: dict) -> None:
    """
    Process a single message from the queue

    :param message: the message frm the sqs queue we just received
    """
    logging.info("Processing message: %s", message)
    file = extract_file_from_message(message, local_dir)

    try:
        s3.download_file(file.bucket, file.object_key, file.local_path)

        if file.file_extension == 'mov':
            process_mov_file(file)

        if file.file_extension == 'caf':
            process_caf_file(file)

    except Exception as e:
        logging.info("Error processing the file: %s", str(e))
        raise e


def process_mov_file(file: SqsServerMessage):
    """
    Processes a MOV file

    1. Convert the MOV file to an MP4 file
    2. Get the video context
    3. Transcribe the MP4 file
    4. Process the summary

    :param file: the file to process
    """
    mp4_file_path = video_process.convert_mov_to_mp4(file.local_path)

    frame_dir = os.path.join(os.path.dirname(mp4_file_path), "frames")
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)
    
    frames = video_process.split_video_into_one_frame_per_second(mp4_file_path, frame_dir)
    video_context = video_process.analyze_frames_and_summarize(frames)
    transcription = audio_process.transcribe(mp4_file_path)
    summary = summary_process.process_mp4_summary(video_context, transcription)

    dynamo.update_mp4_table(file.file_uid, 'videoContextIndex', video_context)
    dynamo.update_mp4_table(file.file_uid, 'transcriptionIndex', transcription)
    dynamo.update_mp4_table(file.file_uid, 'summaryIndex', summary)

def process_caf_file(file: SqsServerMessage):
    """
    Processes a CAF file

    1. Convert the CAF file to an MP3 file
    2. Transcribe the MP3 file
    3. Process the summary

    :param file: the file to process
    """
    mp3_file_path = audio_process.convert_caf_to_mp3(file.local_path)
    transcription = audio_process.transcribe(mp3_file_path)
    summary = summary_process.process_mp3_summary(transcription)

    dynamo.update_mp3_table(file.file_uid, 'transcriptionIndex', transcription)
    dynamo.update_mp3_table(file.file_uid, 'summaryIndex', summary)

def main():
    """
    Main function to process messages from SQS
    """
    logging.info("Starting the server")

    while True:
        message = sqs.get_message_from_queue()
        process_message(message)

if __name__ == "__main__":
    main()