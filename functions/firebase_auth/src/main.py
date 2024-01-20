import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path_to_your_firebase_adminsdk.json')
firebase_admin.initialize_app(cred)

def lambda_handler(event, context):
    token = event.get('authorizationToken')
    try:
        if not token:
            raise Exception('Unauthorized')

        # Verify the token with Firebase
        decoded_token = auth.verify_id_token(token)
        if not decoded_token:
            raise Exception('Unauthorized')

        # Token is valid, allow the request
        return generate_policy('user', 'Allow', event['methodArn'])
    except Exception as e:
        print(e)
        # Token is invalid, deny the request
        return generate_policy('user', 'Deny', event['methodArn'])

def generate_policy(principal_id, effect, resource):
    auth_response = {
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
    return auth_response
