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