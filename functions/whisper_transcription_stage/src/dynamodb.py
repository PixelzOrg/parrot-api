import logging

def update_dynamodb(table, file_uid, transcription):
    """
    Update DynamoDB with the transcription.

    Args:
        table: DynamoDB table object.
        file_uid: File Uid.
        transcription: Transcription text.
    """
    logging.info(
        "Updating DynamoDB with user_uid: %s, transcription: %s", 
        file_uid, transcription
    )
    try:
        response = table.put_item(
            Item={
                'file_uid': file_uid,
                'transcription': transcription
            }
        )
        logging.info({"DynamoDB response": response})
    except Exception as e:
        logging.error("Error updating DynamoDB: %s", e)