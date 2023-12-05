import torch
from whisper import load_model

def create_whisper_instance():
    """
    Sets up our whisper model to transcribe audio files
    """
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    return load_model("base").to(DEVICE)