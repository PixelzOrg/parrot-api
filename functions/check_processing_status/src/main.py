import json
import os
import boto3
import logging
from boto3.dynamodb.conditions import Key

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
MP4_DYNAMODB_TABLE_NAME = os.environ.get('MP4_DYNAMO_DB_TABLE_NAME')
MP3_DYNAMODB_TABLE_NAME = os.environ.get('MP3_DYNAMO_DB_TABLE_NAME')

def handler(event, context):
    try:
        body = json.loads(event['body'])
        file_uid = body['file_uid']
        file_type = body.get('file_type')

        if not file_uid:
            raise ValueError("file_uid is required")

        if file_type == 'mp4':
            table_name = MP4_DYNAMODB_TABLE_NAME
            required_fields = ['summary', 'transcription', 'videoContext']
        elif file_type == 'mp3':
            table_name = MP3_DYNAMODB_TABLE_NAME
            required_fields = ['summary', 'transcription']
        else:
            logging.error("Invalid file type provided.")
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

            if all(field in item for field in required_fields):
                return {
                    'statusCode': 200,
                    'body': json.dumps(item)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({
                        'message': 'Not all required items are available'
                    })
                }

    except json.JSONDecodeError:
        logging.error("JSON decoding error.")
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request body'})
        }
    except ValueError as ve:
        logging.error(str(ve))
        return {
            'statusCode': 400,
            'body': json.dumps({'message': str(ve)})
        }
    except Exception as e:
        logging.error("Error processing the request: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error processing the request',
                'error': str(e)
            })
        }
