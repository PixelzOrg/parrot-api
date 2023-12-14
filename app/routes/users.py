from flask import Blueprint, jsonify, request

users = Blueprint('users', __name__)

@users.route('/create', methods=['POST'])
def create_new_user(username: str):
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
        username = request.json.get('username')

        if not username:
            raise ValueError('Username must be provided in request body.')

        # create new user in s3 and sql

        return jsonify({
            "message": f"User '{username}' created successfully."
            }), 200

    except ValueError as e:
        return jsonify({
            "message": "Something is wrong with your request", 
            "error": str(e)
            }), 400

    except Exception as e:
        return jsonify({
            "message": "Internal server error",
            "error": str(e)
            }), 500

@users.route('/<username>/delete', methods=['DELETE'])
def delete_user(username: str):
    """
    Deletes a user and all their data from S3 and SQL.

    Args:
        username (str): The username of the user.

    Returns:
        None
    """
    pass
