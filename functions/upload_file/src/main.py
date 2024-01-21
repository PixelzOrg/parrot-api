import json
import os
import uuid
import logging
from utility import create_presigned_post


BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

def handler(event, context):
    try:
        body = json.loads(event['body'])
        user_uid = body['user_uid']
        file_type = body['file_type']

        file_uid = str(uuid.uuid4())

        filename = f"{user_uid}/{file_uid}.{file_type}"

        presigned_url = create_presigned_post(
            bucket_name=BUCKET_NAME,
            object_name=filename,
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Presigned URL generated successfully',
                'expires': 3600,
                'file_uid': file_uid,
                'presigned_url': presigned_url
            })
        }

    except (json.decoder.JSONDecodeError, ValueError, EnvironmentError) as e:
        logging.error("Error in handler: %s", e)
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request', 'error': str(e)})
        }
