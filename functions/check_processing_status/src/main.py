import json
import os
import boto3
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
MP4_DYNAMODB_TABLE_NAME = os.environ.get('MP4_DYNAMO_DB_TABLE_NAME')
MP3_DYNAMODB_TABLE_NAME = os.environ.get('MP3_DYNAMO_DB_TABLE_NAME')

def handler(event, context):
    try:
        body = json.loads(event['body'])
        file_uid = body['file_uid']
        file_type = body.get('file_type')


        if file_type == 'mp4':
            table_name = MP4_DYNAMODB_TABLE_NAME
        elif file_type == 'mp3':
            table_name = MP3_DYNAMODB_TABLE_NAME
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid file type'})
            }

        table = dynamodb.Table(table_name)
        response = table.query(
            KeyConditionExpression=Key('file_uid').eq(file_uid)
        )

        if 'Items' in response and response['Items']:
            item = response['Items'][0] 

            # Check if summary exists
            if 'summary' in item and item['summary']:
                return {
                    'statusCode': 200,
                    'body': json.dumps(item)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'Summary not found'})
                }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error processing the request',
                'error': str(e)
            })
        }
