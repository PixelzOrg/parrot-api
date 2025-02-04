import os
import json
import logging
from typing import Any, Dict
import firebase_admin
from firebase_admin import credentials, auth, exceptions as firebase_exceptions

from aws_lambda_typing import events, responses


# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS')
    if not FIREBASE_CREDENTIALS:
        raise ValueError("Missing Firebase credentials in environment variables")
    
    cred = firebase_admin.credentials.Certificate(json.loads(FIREBASE_CREDENTIALS))
    firebase_admin.initialize_app(cred)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event: events.APIGatewayProxyEventV2, context: Any) -> responses.APIGatewayProxyResponseV2:
    """
    Lambda function to handle AWS Gateway events for authentication using Firebase.

    Args:
        event: The event dict from the AWS Gateway.
        context: Lambda context.

    Returns:
        APIGatewayProxyResponseV2: The response object for the AWS Gateway.
    """
    logger.info('Processing event: %s', json.dumps(event))

    # Extract the token from the header
    token = event.get('headers', {}).get('Authorization')
    methodArn = event.get('methodArn')

    if not token:
        logger.error('Unauthorized: No token provided')
        return {'statusCode': 401, 'body': json.dumps({'message': 'Unauthorized'})}

    logger.info('Token received for verification')

    try:
        # Verify the token with Firebase
        decoded_token = firebase_admin.auth.verify_id_token(token)
        if not decoded_token:
            raise ValueError('Unauthorized: Something went wrong in token verification, check firebase auth')

        logger.info('Token verified successfully')
        return generate_policy('user', 'Allow', '*')
    
    except firebase_exceptions.UnavailableError as e:
        logger.error({
            "message": 'Error in token verification: Firebase error', 
             "error": {e}
        })
        return {
            'statusCode': 503,
            'body': json.dumps({'message': 'Database unavailable'})
        }
    except firebase_exceptions.UnauthenticatedError as e:
        logger.error({
            "message": 'Error in token verification: Firebase error', 
             "error": {e}
        })
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Unauthorized: Token invalid'})
        }
    except firebase_exceptions.FirebaseError as e:
        logger.error({
            "message": 'Error in token verification: Firebase error', 
             "error": {e}
        })
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Serverside verification failed'})
        }
    
def generate_policy(principal_id: str, effect: str, resource: str) -> Dict[str, Any]:
    """
    Generates an IAM policy for a user.

    Args:
        principal_id: The principal user ID.
        effect: Either 'Allow' or 'Deny'.
        resource: The AWS resource.

    Returns:
        Dict: A policy document.
    """
    logger.info(
        'Generating policy with principalId: %s, effect: %s, resource: %s', 
        principal_id,
        effect,
        resource
    )

    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': resource
            }]
        }
    }
