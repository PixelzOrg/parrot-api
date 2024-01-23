import os
import logging
import json
import openai
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('OPEN_AI_KEY'),
)
logging.info("OpenAI client configured")

def handler(event, context):
    try:
        body = json.loads(event['body'])
        logging.info("Received event: %s", json.dumps(body, indent=2))
        memory = body['memory']
        prompt = body['prompt']

        memory_context = (
            f"Title: {memory['title']}\n"
            f"Location: {memory['location']}\n"
            f"Time: {memory['time']}\n"
            f"Context: {memory['video_context']}\n"
            f"Summary: {memory['summary']}\n"
            f"Transcription: {memory['transcription']}"
        )

        focus_instruction = """Please pay close attention to the details of the memory
        provided above, as the upcoming question relates closely to it."""

        messages = [
            {"role": "system", "content": memory_context},
            {"role": "system", "content": focus_instruction},
            {"role": "user", "content": prompt}
        ]

    except (json.decoder.JSONDecodeError, KeyError, ValueError) as e:
        logging.error("Error processing request: %s", e)
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request', 'error': str(e)})
        }

    try:
        logging.info("Sending prompt to OpenAI")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
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
