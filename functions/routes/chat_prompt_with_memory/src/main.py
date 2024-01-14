import json
import os
import boto3

    
BUCKET_NAME: str = os.environ.get('S3_BUCKET_NAME')

def handler(event, context):

    s3_client = boto3.client('s3')

    try:

        body = json.loads(event['body'])

        part = body['part_number']
        upload_id = body['upload_id']
        file_location = body['file_location']

    except json.decoder.JSONDecodeError as json_decode_error:
        return {
            'statusCode': 500,
            'body': json.dumps(
                {
                    'message': 'Something went wrong reading the JSON',
                    'error' : str(json_decode_error)
                }
            )
        }

    try:
        presigned_url = s3_client.generate_presigned_url(
            ClientMethod='upload_part',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': file_location,
                'UploadId': upload_id,
                'PartNumber': part
            }
        )
    except s3_client.exceptions.ClientError as s3_client_error:
        return {
            'statusCode': 500,
            'body': json.dumps(
                {
                    'message': 'Error uploading part, please try again using the same part number',
                    'error' : str(s3_client_error)
                }
            )
        }

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'message': 'Part uploaded successfully',
                'memory_id': file_location,
                'upload_response': presigned_url
            }
        )
    }
