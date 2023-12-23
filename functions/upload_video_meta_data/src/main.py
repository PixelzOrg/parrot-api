import psycopg2
import json
import os

# Get RDS credentials from environment variables or AWS Secrets Manager
DB_HOST = os.environ.get('AWS_USER_VIDEO_RDS_HOST')
DB_PORT = os.environ.get('AWS_USER_VIDEO_RDS_PORT')
DB_NAME = os.environ.get('AWS_USER_VIDEO_RDS_NAME')
DB_USER = os.environ.get('AWS_USER_VIDEO_RDS_USER')
DB_PASSWORD = os.environ.get('AWS_USER_VIDEO_RDS_PASSWORD')

def handler(event, context):
    # Connect to the RDS database
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    # Use the connection to execute queries
    with conn.cursor() as cur:
        # Example: Insert metadata into a "videos" table
        cur.execute("INSERT INTO videos (video_id, metadata) VALUES (%s, %s)", (event['video_id'], event['metadata']))
        conn.commit()

    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Metadata uploaded successfully!')
    }