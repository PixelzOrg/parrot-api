import json
import boto3
import os
import logging
from typing import Dict, Any

# Initialize logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the clients
sqs_client = boto3.client('sqs')
WHISPER_TRANSCRIPTION_URL = 'https://sqs.us-east-2.amazonaws.com/975050052244/WhisperQueue'

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function to handle S3 put events and send a message to SQS.

    :param event: Event data that triggered the Lambda function.
    :param context: Information about the invocation, function, and execution environment.
    :return: A response dict with message and status.
    """
    logger.info("Lambda function started. Processing S3 event.")
    try:
        for record in event['Records']:
            s3_info = record['s3']
            bucket_name = s3_info['bucket']['name']
            object_key = s3_info['object']['key']
            logger.info(
                "Processing record from bucket: %s, key: %s", bucket_name, object_key
            )

            # Construct and send the message to SQS
            message = {'bucket': bucket_name, 'object_key': object_key}
            message_body = json.dumps(message)
            response = sqs_client.send_message(
                QueueUrl=WHISPER_TRANSCRIPTION_URL,
                MessageBody=message_body
            )
            logger.info("Message sent to SQS: %s", response)

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed S3 event.')
        }

    except Exception as e:
        logger.error("Error processing S3 event: %s", e, exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing S3 event.')
        }
