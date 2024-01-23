import logging
import boto3

class SQSInterface:
    """
    This class abstracts all of the SQS interactions.
    """
    def __init__(self):
        self.sqs_client = boto3.client("sqs")
        self.summaryQueueUrl = 'https://sqs.us-east-2.amazonaws.com/027494880079/SummaryQueue'
  
    def get_message_from_queue(self) -> dict:
        """
        Get message from a specified SQS queue.

        Args:
            queue_url: SQS queue URL.

        Returns:
            Message from the SQS queue.
        """
        logging.info("Getting message from %s", self.summaryQueueUrl)

        try:
            response = self.sqs_client.receive_message(
                QueueUrl=self.summaryQueueUrl,
                MaxNumberOfMessages=1,
            )
            logging.info({"SQS response": response})
        except Exception as e:
            logging.error("Error getting message from %s: %s", self.summaryQueueUrl, e)

        return response
