import json
import logging
import boto3

def lambda_handler(event, context):
    
    # Initialize the SQS client
    sqs = boto3.client('sqs')

    queue = sqs.get_queue_url(QueueName='WhisperQueue')

    # Process each record in the event
    for record in event['Records']:
        try:
            # Get bucket name and object key from the record
            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
        except KeyError:
            logging.warning("Invalid record format: %s", record)

        # Construct the Object ARN
        object_arn = f"arn:aws:s3:::{bucket_name}/{object_key}"

        logging.info("Processing file: %s, from bucket: %s", object_key, bucket_name)

        try:
            # Send message to SQS queue
            response = sqs.send_message(
                QueueUrl=queue.url,
                DelaySeconds=10,
                MessageAttributes={
                    'BucketName': {
                        'DataType': 'String',
                        'StringValue': bucket_name
                    },
                    'ObjectKey': {
                        'DataType': 'String',
                        'StringValue': object_key
                    },
                    'ObjectArn': {
                        'DataType': 'String',
                        'StringValue': object_arn
                    }
                },
                MessageBody=json.dumps(record)
            )
        except Exception as e:
            logging.error("Error processing record: %s. Error: %s", record, e)

        print(response['MessageId'])

    return {
        'statusCode': 200,
        'body': json.dumps('Event processed successfully!')
    }
