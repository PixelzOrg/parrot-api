import logging
import uuid
from botocore.exceptions import ClientError


def generate_presigned_post(bucket, username, expires_in):
    """
    Generate a presigned Amazon S3 POST request to upload a file.
    A presigned POST can be used for a limited time to let someone without an AWS
    account upload a file to a bucket.
    :param object_key: The object key to identify the uploaded object.
    :param expires_in: The number of seconds the presigned POST is valid.
    :return: A dictionary that contains the URL and form fields that contain
         required access data.
    """

    object_key = f'{username}/videos/{uuid.uuid4().hex}'

    try:
        response = bucket.meta.client.generate_presigned_post(
            Bucket=bucket.name, Key=object_key, ExpiresIn=expires_in
        )
        logging.info("Got presigned POST URL: %s", response["url"])
    except ClientError as error:
        logging.exception(
            "Couldn't get a presigned POST URL for bucket '%s' and object '%s'",
            bucket.name,
            object_key,
        )
        raise error

    return response
