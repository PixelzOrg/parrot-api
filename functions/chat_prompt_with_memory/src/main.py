import os
import logging
import json
from openai import OpenAI

# Configure OpenAI client
client = OpenAI(
    api_key=os.environ.get('OPEN_AI_KEY'),
)
logging.info("OpenAI client configured")

def handler(event, context):
    try:
        body = json.loads(event['body'])
        logging.info("Received event: %s", json.dumps(body, indent=2))
        chat_history = body['chat_history']
        prompt = body['prompt']

    except (json.decoder.JSONDecodeError, KeyError, ValueError) as e:
        logging.error("Error processing request: %s", e)
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request', 'error': str(e)})
        }

    messages = chat_history
    messages.append({"role": "user", "content": prompt})

    try:
        logging.info("Sending prompt to OpenAI")
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=messages)
        logging.info("Received response from OpenAI")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Chat generated successfully',
                'chat': response.choices[0].message.content
            })
        }
    except Exception as e:
        logging.error("Error while calling OpenAI API: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error in OpenAI API call', 'error': str(e)})
        }

