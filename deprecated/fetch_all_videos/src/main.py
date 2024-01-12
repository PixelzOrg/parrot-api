def handler(event, context):
    """
    Pulls username from request body and creates a 
    new user in our S3 bucket and SQL database.

    params:
        request.json (dict): A dictionary representing the JSON payload with the following structure:
            {
                "username": "string"
            }

    Returns:
        A JSON response with the result of the upload 
    """
    try:
        #

        # create new user in s3 and sql

        return {
            "message": "User created successfully."
            }, 200

    except ValueError as e:
        return ({
            "message": "Something is wrong with your request", 
            "error": str(e)
            }), 400

    except Exception as e:
        return ({
            "message": "Internal server error",
            "error": str(e)
            }), 500