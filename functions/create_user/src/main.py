import boto3
import os
import json
import uuid

s3_client = boto3.client('s3')
BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        username = body['username']
        video_content = event['video']
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid request format'})
        }

    # Generate a unique filename for the video
    video_filename = f"{username}/{uuid.uuid4().hex}.mp4"

    try:
        # Upload the video to the S3 bucket
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=video_filename,
            Body=video_content,
            ContentType='video/mp4'
        )
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to upload video to S3'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Video uploaded successfully', 'video_url': f"s3://{BUCKET_NAME}/{video_filename}"})
    }
