import os
import cv2 as cv
from moviepy.editor import VideoFileClip

def video_to_img(filename, video_path):
    """
    Converts a video to a series of images and saves them in a folder with the same name as the video file
    """
    capture = cv.VideoCapture(os.path.join(video_path, filename))
    frame_number = 0

    img_folder = os.path.join(video_path, 'frames')
    os.makedirs(img_folder, exist_ok=True)

    while True:
        success, frame = capture.read()
        if success:
            # Save the image in the 'img' subfolder
            img_filename = f"frame{frame_number}.png"
            img_path = os.path.join(img_folder, img_filename)
            cv.imwrite(img_path, frame)
        else:
            break

        frame_number += 1

    capture.release()
