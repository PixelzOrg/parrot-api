import json
import os
import uuid
from boto3 import client
from constants import ERROR_READING_JSON, S3_CLIENT_ERROR

try:
    s3_client = boto3.client('s3')
except client.exceptions.ClientError as e:
    print(e)
    
BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
BUCKET_ARN = os.environ.get('S3_BUCKET_ARN')

def handler(event, context):

    try:

        body = json.loads(event['body'])
        video_path = body['video_path']
        upload_id = body['upload_id']
        parts = body['parts']

    except json.decoder.JSONDecodeError as json_decode_error:
        return [
            ERROR_READING_JSON,
            str(json_decode_error)
        ]

    try:
        response = s3_client.complete_multipart_upload(
            Bucket = BUCKET_NAME,
            Key = video_path,
            MultipartUpload = {'Parts': parts},
            UploadId= upload_id
        )
    except s3_client.exceptions.ClientError as s3_client_error:
        return [
            S3_CLIENT_ERROR,
            str(s3_client_error)
        ]

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'message': f'Successfully uploaded file with upload id: {upload_id}',
                'response': response
            }
        )
    }
