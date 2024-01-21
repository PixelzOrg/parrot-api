import json
import os
import uuid
from utility import create_presigned_post


BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

def handler(event, context):
    try:
        # Parse the JSON body
        body = json.loads(event['body'])
        user_uid = body['user_uid']
        file_type = body['file_type']

    except json.decoder.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(
                {
                    'message': 'Invalid request format',
                    'error': str(e)
                }
            )
        }
    
    file_uid = str(uuid.uuid4())

    filename = f"{user_uid}/{file_uid}.{file_type}"

    # Generate a presigned URL for the S3 upload
    presigned_url = create_presigned_post(BUCKET_NAME, filename)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'message': 'Presigned URL generated successfully',
                'expires': 3600,
                'file_uid': file_uid,
                'presigned_url': presigned_url
            }
        )
    }
