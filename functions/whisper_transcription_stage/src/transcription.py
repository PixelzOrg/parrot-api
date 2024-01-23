import torch
import whisper

class WhisperModel:
    def __init__(self, model_name: str):
        """
        Initialize the Whisper model.

        Args:
            model_name: Model name.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self.load_whisper_model(model_name)

    def load_whisper_model(self, model_name: str) -> whisper:
        """
        Load the Whisper model.
        """
        try:
            return whisper.load_model(model_name).to(self.device)
        except Exception as e:
            raise ValueError(f"Error loading the model: {e}") from e
