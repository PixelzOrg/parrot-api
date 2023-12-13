import os
from werkzeug.utils import secure_filename
from flask import Blueprint, jsonify, request, send_file
from app.src.transcribe import transcribe_file
from app.utils.files import allowed_file
from app.utils.videos import video_to_img

videos = Blueprint('users/videos', __name__)

@videos.route('/upload', methods=['POST'])
def upload_video():
    """
    Uploads a video file to the data/videos folder

    params:
        file: the mp4 file to upload

    Returns:
        A JSON response with the result of the upload
    """
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file has an allowed extension
    try:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename_without_extension, _extension = os.path.splitext(filename)

            # Create a unique folder for each file using the filename (without extension)
            folder_path = os.path.join("app/data/videos/", filename_without_extension)
            os.makedirs(folder_path, exist_ok=True)

            file_path = os.path.join(folder_path, filename)
            file.save(file_path)

            transcribe_file(file_path, plain=False, vtt=True)
            video_to_img(file.filename, folder_path)
            # extract_faces(folder_path)

            return jsonify({'message': f'File {filename} uploaded successfully'}), 201
        else:
            return jsonify({'error': 'File type not allowed'}), 400
    except Exception as e:
        return jsonify({'error': f'{e}'}), 500

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