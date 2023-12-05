from . import create_whisper_instance
from pathlib import Path
from whisper.utils import get_writer

whisper_model = create_whisper_instance()

def transcribe_file(file, plain, vtt):
    """"
    Runs Whisper on an audio file

    Parameters
    ----------
    model: Whisper
        The Whisper model instance.

    file: str
        The file path of the file to be transcribed.

    plain: bool
        Whether to save the transcription as a text file or not.

    vtt: bool
        Whether to save the transcription as a VTT file or not.

    Returns
    -------
    A dictionary containing the resulting text ("text") and segment-level details ("segments"), and
    the spoken language ("language"), which is detected when `decode_options["language"]` is None.
    """
    file_path = Path(file)
    print(f"Transcribing file: {file_path}\n")

    output_directory = file_path.parent

    # Run Whisper
    result = whisper_model.transcribe(file, verbose = False, language = "en")

    if plain:
        txt_path = file_path.with_suffix(".txt")
        with open(txt_path, "w", encoding="utf-8") as txt:
            txt.write(result["text"])

    if vtt:
        vtt_writer = get_writer("vtt", output_directory)
        vtt_writer(result, str(file_path.stem))

    return result
