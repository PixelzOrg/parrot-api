import os
import json
import urllib.parse
import whisper
import torch
import boto3


s3 = boto3.client("s3")
dynamoDb = boto3.client("dynamodb")
table = dynamoDb.Table('memory_id')

def handler(event, context):
    try:
        print("Received event: " + json.dumps(event, indent=2))
        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        
        print("Bucket:", bucket, "key:", key)
        os.makedirs("/tmp/data", exist_ok=True)
        os.chdir('/tmp/data')

        audio_file=f"/tmp/data/{key}"
        # Downloading file to transcribe
        s3.download_file(bucket, key, audio_file)

        # GPU!! (if available)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = whisper.load_model("medium", download_root="/usr/local").to(device)

        result = model.transcribe(audio_file, fp16=False, language='English')
        print(result['text'].strip())

        memory_id, _ = os.path.splitext(key)
        update_dynamodb(memory_id, result["text"].strip())

    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps("Error processing the file")
        }
    
def update_dynamodb(memory_id, transcription):
    try:
        response = table.put_item(
            Item={
                'memory_id': memory_id,
                'transcription': transcription
            }
        )
        print("DynamoDB update response:", response)
    except Exception as e:
        print("Error updating DynamoDB:", e)