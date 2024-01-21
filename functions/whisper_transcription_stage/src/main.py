import os
import json
import urllib.parse
import whisper
import torch
import boto3

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('memory_id')
sqs_client = boto3.client("sqs")

SUMMARY_QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/975050052244/SummaryQueue'

def handler(event, context):
    try:
        print("Received event: " + json.dumps(event, indent=2))

        # Process the SQS message
        for record in event['Records']:
            message = json.loads(record['body'])
            bucket = message["Records"][0]["s3"]["bucket"]["name"]
            key = urllib.parse.unquote_plus(message['Records'][0]['s3']['object']['key'], encoding='utf-8')
            
            print("Bucket:", bucket, "key:", key)
            os.makedirs("/tmp/data", exist_ok=True)
            os.chdir('/tmp/data')

            audio_file = f"/tmp/data/{key}"
            # Downloading file to transcribe
            s3.download_file(bucket, key, audio_file)

            # GPU!! (if available)
            device = "cuda" if torch.cuda.is_available() else "cpu"
            model = whisper.load_model("base", download_root="/usr/local").to(device)

            result = model.transcribe(audio_file, fp16=False, language='English')
            print(result['text'].strip())

            user_uid, _ = os.path.splitext(os.path.basename(key))
            update_dynamodb(user_uid, result["text"].strip())

            # Send message to Summary queue
            send_message_to_summary_queue(user_uid, result["text"].strip())

    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps("Error processing the file")
        }

def update_dynamodb(user_uid, transcription):
    try:
        response = table.put_item(
            Item={
                'user_uid': user_uid,
                'transcription': transcription
            }
        )
        print("DynamoDB update response:", response)
    except Exception as e:
        print("Error updating DynamoDB:", e)

def send_message_to_summary_queue(user_uid, transcription):
    try:
        message = {
            'user_uid': user_uid,
            'transcription': transcription
        }
        response = sqs_client.send_message(QueueUrl=SUMMARY_QUEUE_URL, MessageBody=json.dumps(message))
        print("Message sent to Summary queue:", response)
    except Exception as e:
        print("Error sending message to Summary queue:", e)
