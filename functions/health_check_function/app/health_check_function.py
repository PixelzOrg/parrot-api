from flask import Blueprint, jsonify

health_checks = Blueprint('health_check', __name__)

@health_checks.route('/', methods=['GET'])
def check_if_server_is_running():
    """
    Health check endpoint for the API
    """
    return jsonify({'message': 'Server is running'}), 200
