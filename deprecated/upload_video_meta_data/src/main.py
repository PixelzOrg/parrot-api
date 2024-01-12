import json
from models import VideoMetadata
from service import upload_video_meta_data_service


def handler(event, context):
    try:
        body = json.loads(event['body'])

        video_uuid = body['video_uuid']
        unvalidated_meta_data: VideoMetadata = body['video_meta_data']

    except Exception as e:
        return {
            'statusCode': 400,
            'message': 'Something went wrong while parsing the request body',
            'error': str(e)
        }

    try:    
        response = upload_video_meta_data_service(video_uuid, unvalidated_meta_data)
    except Exception as e:
        return {
            'statusCode': 500,
            'message': 'Something went wrong while uploading the video metadata',
            'error': str(e)
        }
    return {
        'statusCode': 200,
        'message': 'Video metadata updated successfully for video_uuid: {video_uuid}',
        'detail': response
    }
