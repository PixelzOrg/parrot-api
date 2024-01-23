import logging
import boto3
import json

# Define the queue URLs
SUMMARY_QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/975050052244/SummaryQueue'
TRANSCRIPTION_QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/975050052244/TranscriptionQueue'

# Initialize SQS client
sqs_client = boto3.client("sqs")

def send_message_to_queue(object_key: str, queue_type: str) -> None:
    """
    Send message to a specified SQS queue to trigger an action.

    Args:
        object_key: S3 object key.
        queue_type: Type of queue ('summary' or 'transcription').
    """
    # Determine the queue URL based on the queue type
    queue_url = SUMMARY_QUEUE_URL if queue_type == 'summary' else TRANSCRIPTION_QUEUE_URL

    logging.info("Sending message to %s with object_key: %s", queue_url, object_key)

    try:
        message = {
            'object_key': object_key,
        }
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message)
        )
        logging.info({"SQS response": response})
    except Exception as e:
        logging.error("Error sending message to %s: %s", queue_url, e)

# Example usage
send_message_to_queue("example_key.mp3", "summary")
send_message_to_queue("example_key.mp4", "transcription")
