from flask import Blueprint, jsonify, request, send_file

users = Blueprint('users', __name__)

@users.route('/create', methods=['POST'])
def create_new_user(username: str):
    """
    Creates a new user.

    Args:
        username (str): The username of the user.

    Returns:
        container_client (ContainerClient): The client for the created user container. 
    """
    pass

