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
        part_number = body['part_number']

    except json.decoder.JSONDecodeError as json_decode_error:
        return [
            ERROR_READING_JSON,
            str(json_decode_error)
        ]

    try:
        presigned_url = s3_client.generate_presigned_url(
            ClientMethod ='upload_part',
            Params = {
                'Bucket': BUCKET_NAME,
                'Key': video_path,
                'UploadId': upload_id, 
                'PartNumber': part_number
            }
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
                'message': f'Your URL for part: {part_number} is ready',
                'presigned_url': presigned_url
            }
        )
    }
