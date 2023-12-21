import boto3
import json
import uuid
import os
import logging
from botocore.exceptions import ClientError
from datetime import datetime

s3_client = boto3.client('s3')

BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
BUCKET_ARN = os.environ.get('S3_BUCKET_ARN')

def handler(event, context):
    try:
        # Parse the JSON body
        body = json.loads(event['body'])
        username = body['username']
        
        # Generate a unique filename for the video
        video_filename = f"{username}/{uuid.uuid4().hex}.mp4"

        # Generate a presigned URL for the S3 upload
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': video_filename,
                'ContentType': 'video/mp4'
            },
            ExpiresIn=360
        )
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(
                {
                    'message': 'Invalid request format',
                    'error': str(e)
                }
            )
        }

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'message': 'Presigned URL generated successfully', 
                'expires': 360,
                'presigned_url': presigned_url
            }
        )
    }
