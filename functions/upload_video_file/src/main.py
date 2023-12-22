import boto3
import json
import os
from utility import generate_presigned_post


s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket('your_bucket_name')

BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
BUCKET_ARN = os.environ.get('S3_BUCKET_ARN')


def handler(event, context):
    try:
        # Parse the JSON body
        body = json.loads(event['body'])
        username = body['username']

        # Generate a presigned URL for the S3 upload
        presigned_url = generate_presigned_post(
            bucket=bucket,
            username=username,
            expires_in=3600
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
                'expires': 3600,
                'presigned_url': presigned_url
            }
        )
    }
