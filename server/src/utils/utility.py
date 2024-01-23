import os
import logging
import boto3
from botocore.exceptions import ClientError
from models.sqs_models import SqsServerMessage

def setup_directory() -> str:
    """
    Setup the local directory where we will download the files from S3

    :return: the local directory
    """
    local_dir = os.path.join(os.getcwd(), 'tmp')
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    return local_dir

def extract_file_from_message(message: dict, local_dir: str) -> SqsServerMessage:
    """
    Extract the file from the SQS message

    :return: the file from the SQS message
    """
    try:
        logging.info("Extracting file from message: %s", message)
        bucket = message['bucket_name']
        object_key = message['object_key']
        file_uid = message['file_uid']
        user_uid = message['user_uid']
        file_extension = message['file_extension']
        local_path = os.path.join(local_dir, os.path.basename(object_key))

        return SqsServerMessage(
            bucket=bucket,
            object_key=object_key,
            user_uid=user_uid,
            file_uid=file_uid,
            file_extension=file_extension,
            local_path=local_path
        )
    except ValueError as e:
        logging.error("Error extracting file from message: %s", e)
        raise ValueError("Error extracting file from message") from e

def get_open_ai_key():

    secret_name = "OPEN_AI_KEY"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return secret