import boto3
import logging

class S3Interface:
    def __init__(self):
        self.s3 = boto3.client("s3")
    
    def download_file(self, bucket_name, object_key, local_file_path):
        """
        Download the file from S3.

        Args:
            bucket_name: Bucket name.
            object_key: Object key.
            local_file_path: Local file path.
        """
        logging.info("Starting to download file from S3: %s", object_key)
        self.s3.download_file(bucket_name, object_key, local_file_path)
        logging.info("Downloaded file to: %s", local_file_path)