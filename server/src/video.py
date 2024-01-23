import os
import openai
from utils.utlity import get_open_ai_key
import ffmpeg
import logging

class VideoProcessor:
    """
    This class handles all of the video processing.
    """
    def __init__(self, open_ai_client):
        self.open_ai_client = open_ai_client
    
    def analyze_frame(self, frame_path: str) -> str:
        """
        Analyzes a single frame using OpenAI's image processing API.

        :param frame_path: File path to the frame.
        :return: Contextual summary of the frame.
        """
        try:
            with open(frame_path, 'rb') as f:
                response = self.open_ai_client.chat.completions.create(
                    image=f.read(),
                    model="gpt-4-vision-preview"
                )
                return response.choices[0].message.content
        except Exception as e:
            logging.error("Error analyzing frame %s: %s, %s", frame_path, e, response)
            return ""

    def analyze_frames_and_summarize(self, frames_files: list) -> str:
        """
        This functions calls OpenAI with 
        the image file to get context for the set of frames we have sent

        :param frame_files: List of file paths to the frames
        :return: The video context.
        """
        summaries = []
        for frame_path in frames_files:

            frame_summary = self.analyze_frame(frame_path)

            if not frame_summary:
                error_message = "No summary returned for frame: %s", frame_path
                logging.error(error_message)
                raise ValueError(error_message)

            summaries.append(frame_summary)

        video_summary = " ".join(summaries)
        logging.info("Video summary: %s", video_summary)
        return video_summary

    @staticmethod
    def convert_mov_to_mp4(input_file: str) -> bool:
        """
        Converts a MOV file to an MP4 file using ffmpeg.

        :param input_file: The path to the input MOV file.
        :param output_file: The path where the output MP4 file will be saved.
        :return: True if the conversion was successful, False otherwise.
        """
        try:
            output_file = input_file + '.mp3'
            ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)
            logging.info(
                "Successfully converted %s to %s", input_file, output_file
            )
            return True
        except ffmpeg.Error as e:
            logging.error(
                "Error converting %s to %s: %s", input_file, output_file, e
            )
            return False

    def split_video_into_one_frame_per_second(
            self,
            input_file: str,
            frame_dir: str
        ) -> list:
        """
        Splits a video file into frames and saves them in a specified directory.

        Args:
            input_file: Path to the input video file.
            frame_dir: Directory where the frames will be saved.

        Returns:
            List of file paths to the extracted frames.
        """
        try:
            if not os.path.exists(frame_dir):
                os.makedirs(frame_dir)

            (
                ffmpeg
                .input(input_file)
                .output(os.path.join(frame_dir, 'frame_%04d.png'), r=1)
                .run()
            )

            # Get list of frame file paths
            frame_files = [
                os.path.join(frame_dir, f)
                for f in os.listdir(frame_dir)
                if f.endswith('.png')
            ]

            logging.info("Extracted %d frames from %s.", len(frame_files), input_file)
            return frame_files

        except ffmpeg.Error as e:
            logging.error("Error splitting video into frames: %s", e)
            return []
