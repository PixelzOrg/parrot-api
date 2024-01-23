import logging

class SummaryProcessor:
    """
    This class abstracts all of summary processing.
    Along with connections to OpenAI.
    """
    def __init__(self, open_ai_client):
        self.open_ai_client = open_ai_client

    def process_mp4_summary(self, video_context: str, transcription: str) -> str:
        """
        Processes the summary for MP4 files.

        :param video_context: Context from the video.
        :param transcription: Transcription from the video.
        :return: A human-readable summary narrative.
        """
        prompt = (
            "Create a summary of a user's experience as if narrating a personal memory. "
            "Combine the following video context and transcription into a coherent narrative:\n\n"
            "Video Context:\n"
            f"{video_context}\n\n"
            "Transcription:\n"
            f"{transcription}\n\n"
            "Narrative Summary:\n"
        )
        return self.create_summary(prompt)

    def process_mp3_summary(self, transcription: str) -> str:
        """
        Processes the summary for MP3 files.

        :param transcription: Transcription from the audio file.
        :return: A human-readable summary narrative.
        """
        prompt = (
            "Create a summary of a user's experience as if narrating a personal memory. "
            "Use the following transcription to create a coherent narrative:\n\n"
            "Transcription:\n"
            f"{transcription}\n\n"
            "Narrative Summary:\n"
        )

        return self.create_summary(prompt)

    def create_summary(self, prompt: str) -> str:
        """
        Creates a summary using OpenAI's GPT model based on the provided prompt.

        :param prompt: The prompt for the language model.
        :return: A human-readable summary narrative.
        """
        try:
            response = self.open_ai_client.chat.completions.create(
                prompt=prompt,
                model="gpt-3.5-turbo",
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error("Error in generating summary: %s", e)
            return "An error occurred in generating the summary."