import os
from werkzeug.utils import secure_filename
from flask import Blueprint, jsonify, request, send_file
from app.src.facial_recognition import extract_faces
from app.src.transcribe import transcribe_file
from app.src.vision import analyze_video
from app.utils.files import allowed_file
from app.utils.videos import video_to_img

videos = Blueprint('videos', __name__)

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

@videos.route('/names', methods=['GET'])
def get_all_video_names():
    """
    Iterates through the data/videos folder and returns a list of all the video names

    Returns:
        dict: a JSON response with a list of all the video names
    """
    try: 
        video_files = [f for f in os.listdir("app/data/videos/")]
        return jsonify({'videos': video_files})
    except Exception as e:
        return jsonify({'message': f'Error reading from directory "app/data/videos/"', 'error': f'{e}'}), 500


@videos.route('/<filename>', methods=['GET'])
def get_video_file(filename):
    """
    Returns a video file from the data/videos folder

    params:
        filename: the name of the video file to return

    Returns:
        file: mp4 video file
    """
    video_path = os.path.join("app/data/videos/", filename)

    try:
        return send_file(video_path, mimetype='video/mp4')
    except Exception as e:
        return jsonify({'message': f'File {filename} not found', 'error': f'{e}'}), 404
