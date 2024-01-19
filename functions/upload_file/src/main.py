import json
import os
import uuid
from .utility import create_presigned_post


BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
BUCKET_ARN = os.environ.get('S3_BUCKET_ARN')

def handler(event, context):
    try:
        
        file_uuid = str(uuid.uuid4())

        file_path = f"upload/{file_uuid}.mp4"

        # Generate a presigned URL for the S3 upload
        presigned_url = create_presigned_post(
            BUCKET_NAME,
            file_path
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
                'file_path': file_path,
                'presigned_url': presigned_url
            }
        )
    }
