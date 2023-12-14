from flask import Blueprint

videos = Blueprint('users/videos', __name__)

@videos.route('/upload', methods=['POST'])
def upload_video():
    """
    Uploads a video file to the s3 bucket for a specific user

    params:
        request.json (dict): A dictionary representing the JSON payload with the following structure:
            {
                "username": "string",
                "video": <video file.mp4>
            }

    Returns:
        A JSON response with the result of the upload
    """
    pass

@videos.route('/<username>/by-date/<date>', methods=['GET'])
def fetch_video_by_date(username: str, date: str):
    """
    Fetches a video from our database based on date

    params:
        username (str): the username of the user
        date (str): the date of the video
    
    Returns:
        A JSON response with the video   
    """
    pass

@videos.route('/<username>/', methods=['GET'])
def fetch_all_videos(username: str):
    """
    Fetches all videos from our database based on a username

    params:
        username (str): the username of the user
    
    Returns:
        A JSON response with all the videos   
    """
    pass