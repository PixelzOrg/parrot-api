

def extract_faces(folder_path):
    """
    Extracts faces from a video and saves them in a folder with the same name as the video file

    Args:
        video_path (str): the path to the video file
    """
    frames_folder = os.path.join(folder_path, 'frames')

    try:
        for filename in os.listdir(frames_folder):
            if filename.endswith(".png"):
                frame_path = os.path.join(frames_folder, filename)
                detected_aligned_face = RetinaFace.detect_faces(img_path=frame_path)
                print(detected_aligned_face)
    except Exception as e:
        return e
