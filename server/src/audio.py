import torch
import ffmpeg
import whisper
import logging

class AudioProcessor:
    """
    This class abstracts all of the audio processing.
    """
    def __init__(self, model_name: str):
        """
        Initialize the Whisper model.

        Args:
            model_name: Model name.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.whisper_model = whisper.load_model(model_name).to(self.device)
        
    def transcribe(self, local_file_path: str) -> dict:
        """
        This function transcribes the audio file.
        """
        result = self.whisper_model.transcribe(local_file_path)
        return result

    @staticmethod
    def convert_caf_to_mp3(local_file_path: str) -> bool:
        """
        Converts the CAF file to an MP3 file using ffmpeg.

        Args:
            local_file_path: Local file path of the CAF file.

        Returns:
            True if the conversion was successful, False otherwise.
        """
        try:
            output_file = local_file_path + '.mp3'
            ffmpeg.input(local_file_path).output(output_file).run(overwrite_output=True)
            logging.info(
                "Successfully converted %s to %s", local_file_path, output_file
            )
            return output_file
        except ffmpeg.Error as e:
            logging.error(
                "Error converting %s to %s: %s", local_file_path, output_file, e
            )
            raise e
