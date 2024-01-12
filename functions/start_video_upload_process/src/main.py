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
    
    
    except json.decoder.JSONDecodeError as json_decode_error:
        return [
            ERROR_READING_JSON,
            str(json_decode_error)
        ]
    
    video_uuid = str(uuid.uuid4())
    seed = str(uuid.uuid4())
    video_location = f"{seed}/{video_uuid}.mp4"

    try:
        presigned_url = s3_client.create_multipart_upload(
            Params = {
                'Bucket': BUCKET_NAME,
                'Key': video_uuid, 
                'ContentType': 'video/mp4'
            }
        )
        upload_id = presigned_url['UploadId']

    except s3_client.exceptions.ClientError as s3_client_error:
        return [
            S3_CLIENT_ERROR,
            str(s3_client_error)
        ]

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'message': 'Multipart upload initiated successfully',
                'video_path': video_location,
                'upload_id': upload_id
            }
        )
    }
