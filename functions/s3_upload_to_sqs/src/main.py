import json
import boto3
import os
import logging
from typing import Dict, Any


sqs_client = boto3.client('sqs')
SQS_SERVER_QUEUE_URL = os.environ['SQS_SERVER_QUEUE_URL']

def extract_key_components(object_key: str) -> Dict[str, str]:
    """
    Extracts user_uid, file_uid, and extension from the object key.

    :param object_key: The S3 object key.
    :return: A dict containing the user_uid, file_uid, and extension.
    """
    parts = object_key.split('/')
    user_uid = parts[0]
    file_name = parts[1] if len(parts) > 1 else ''
    file_uid, extension_with_period = os.path.splitext(file_name)
    extension = extension_with_period.lstrip('.')
    return (user_uid, file_uid, extension)

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function to handle S3 put events and send a message to SQS.

    :param event: Event data that triggered the Lambda function.
    :param context: Information about the invocation, function, and execution environment.
    :return: A response dict with message and status.
    """
    logging.info("Lambda function started. Processing S3 event.")
    try:
        for record in event['Records']:
            s3_info = record['s3']
            bucket_name = s3_info['bucket']['name']
            object_key = s3_info['object']['key']
            user_uid, file_uid, extension = extract_key_components(object_key)
            logging.info(
                "Processing record from bucket: %s, key: %s", bucket_name, object_key
            )

            message = {
                'bucket': bucket_name, 
                'object_key': object_key,
                'user_uid': user_uid,
                'file_uid': file_uid,
                'extension': extension
            }
            message_body = json.dumps(message)
            response = sqs_client.send_message(
                QueueUrl=SQS_SERVER_QUEUE_URL,
                MessageBody=message_body
            )
            logging.info("Message sent to SQS: %s", response)

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed S3 event.')
        }

    except Exception as e:
        logging.error("Error processing S3 event: %s", e, exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing S3 event.')
        }
