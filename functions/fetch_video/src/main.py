import boto3
import json
from utility import create_presigned_url

s3_client = boto3.client('s3')
BUCKET_NAME = 'user-videos-bucket'

def handler(event, context):
    try:
        body = json.loads(event['body'])
        username = body['username']
        video_id = body['video_uuid']

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

    try:
        # Generate a unique presigned URL for the video
        url = create_presigned_url(BUCKET_NAME, f"{username}/{video_id}.mp4")

        if url:
            return {
            'statusCode': 200,
            'body': json.dumps(
                {
                    'message': 'Video URL generated successfully', 
                    'video_url': url
                }
            )
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(
                {
                    'message': 'Failed to generate presigned URL',
                    'error': str(e)
                }
            )
        }
