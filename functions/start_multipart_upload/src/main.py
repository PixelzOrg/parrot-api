import json
import os
import uuid
import boto3


BUCKET_NAME: str = os.environ.get('S3_BUCKET_NAME')

def handler(event, context):

    s3_client = boto3.client('s3')

    try:

        body = json.loads(event['body'])

        metadata = body['metadata']
        content_type = body['ContentType']

        folder_uuid = str(uuid.uuid4())
        file_uuid = str(uuid.uuid4())

        file_location = f"{folder_uuid}/{file_uuid}.mp4"

    except json.decoder.JSONDecodeError as json_decode_error:
        return {
            'statusCode': 500,
            'body': json.dumps(
                {
                    'message': 'Something went wrong reading the JSON',
                    'error' : str(json_decode_error)
                }
            )
        }

    try:
        response = s3_client.create_multipart_upload(
            Bucket=BUCKET_NAME,
            Key=file_location,
            Metadata=metadata,
            ContentType=content_type
        )
        upload_id = response['UploadId']

    except s3_client.exceptions.ClientError as s3_client_error:
        return {
            'statusCode': 500,
            'body': json.dumps(
                {
                    'message': 'Something went wrong completing the multipart upload',
                    'error' : str(s3_client_error)
                }
            )
        }

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'message': 'Started multipart upload',
                'file_location': file_location,
                'upload_id': upload_id,
            }
        )
    }
