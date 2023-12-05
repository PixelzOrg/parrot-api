import cv2  # We're using OpenCV to read video, to install !pip install opencv-python
import base64
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openAI_api_key = os.getenv("OPEN_AI_KEY")

client = OpenAI(api_key=openAI_api_key)

def analyze_video(video_name, video_path):
    video = cv2.VideoCapture(os.path.join(video_path, video_name))

    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

    video.release()
    print(len(base64Frames), "frames read.")

    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                "These are frames from a video that I want to upload. I want you to tell me what is happening throughout the video. Be detailed and specific to paint a picture for the reader.",
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::50]),
            ],
        },
    ]
    params = {
        "model": "gpt-4-vision-preview",
        "messages": PROMPT_MESSAGES,
        "max_tokens": 200,
    }

    result = client.chat.completions.create(**params)
    print(result.choices[0].message.content)
