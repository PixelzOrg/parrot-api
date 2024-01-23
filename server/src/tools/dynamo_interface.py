import logging
import boto3

class DynamoDbInterface:
    """
    This class abstracts our connection from DynamoDB.
    """
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")
        self.mp3_table = self.dynamodb.Table("mp3-file-dump")
        self.mp4_table = self.dynamodb.Table("mp4-file-dump")

    def update_mp4_table(
        self,
        file_uid: str,
        object_name: str,
        object_data: str
        ) -> None:
        """
        Update the MP3 table with the object name and object data.

        Args:
            table: DynamoDB table object.
            file_uid: File Uid.
            transcription: Transcription text.
        """
        logging.info(
            "Updating MP4 Table with file_uid: %s, %s: %s", 
            file_uid, object_name, object_data
        )
        try:
            response = self.mp4_table.put_item(
                Item={
                    'file_uid': file_uid,
                    object_name: object_data
                }
            )
            logging.info({"DynamoDB response": response})
        except Exception as e:
            logging.error("Error updating DynamoDB: %s", e)

    def update_mp3_table(
        self,
        file_uid: str,
        object_name: str,
        object_data: str
    ) -> None:
        """
        Update the MP3 table with the object name and object data.

        Args:
            file_uid: File Uid.
            object_name: Object name.
            object_data: Object data.
        """
        logging.info(
            "Updating MP3 Table with file_uid: %s, %s: %s",
            file_uid, object_name, object_data
        )
        try:
            response = self.mp3_table.put_item(
                Item={
                    'file_uid': file_uid,
                    object_name: object_data
                }
            )
            logging.info({"DynamoDB response": response})
        except Exception as e:
            raise Exception(f"Error updating MP3 table: %s", e)
            logging.error("Error updating MP3 table")
    
        