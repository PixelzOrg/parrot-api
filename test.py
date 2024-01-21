import requests    # To install: pip install requests

# Generate a presigned S3 POST URL
object_name = 'rick_roll.mp4'
response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "file_uid": "25c6063d-7ccf-4305-81c8-bdedfc3f0ff6",
    "presigned_url": {
        "url": "https://user-file-upload-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "irfoismfosmdv9020943234/25c6063d-7ccf-4305-81c8-bdedfc3f0ff6.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIA6GBMDCKKJKOGKKD3/20240121/us-east-2/s3/aws4_request",
            "x-amz-date": "20240121T123326Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEHUaCXVzLWVhc3QtMiJGMEQCIBSUV+6WsSDFqtIcvb7an7gNzivNo2JpfrHlInLUcVwxAiBGg+GTtB2lQrx3uIYt1k9wynM8PWAdORmBPOD/YDaxISr2AgguEAAaDDk3NTA1MDA1MjI0NCIMxDAdwJ8YqRxU4cFLKtMC2r36MBtvsPUAbafcBraCN69qvyEK81VULpNgwRtOzwv5vzYwKBVx9ZKEzMoYCsiD+VdG6gMMyoYzS7eeMJvABvlKXFq/RURVX7MmwjY8lnANZlZpavvGWtx/TjK1IQQFniGrlN/W+V7JwX0PpjVKSqDeLWOy8LXkDipbyDaTi6xbNjJ9eiWruCRaRQSBvMGzJbXXBDf7uFqyTdRNKZy2ZluH6olhcmuOGYqcbuwW9IdVmFJqWW9eDiXWpQT4KjTssLRneqJgI0qxfSUULt9HwP4ubZU8Dwcqwpb/+Qhm8CzAmWQLetsWwGF0ZpodaAh1W/A7NqxEBkYZoLXMyKkrUXTV4rN1dsnnHRZv60DA4+VO8OtP4nZyPz/uzB5lCoUodDTZzlY/aR+7iAOKPgp+qeR8VB7K6BkHQZkLXRfSgF5uAdHXK7aens4AzlP4N2hYDemtMO2dtK0GOp8BITeNJQYNE53UTPBn6bbfJVkpIzHS8woRJqRV/LKBK+JXC/UT8n06iEgSfsim8XXYb0AfuSBcZNUKGBaqigd6QF/4neXQWxUvgx85HnD+dirlVKBppLfeh7CUvUX39z35jccz272cJcGaaOWnYeBT0azo2/lfU/6UQ5kVgh9v0dkJ3piQTV6wG3KWwETMMh0jmSfsHmfVf1j1ET7uK9Jb",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDEtMjFUMTM6MzM6MjZaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci1maWxlLXVwbG9hZC1idWNrZXQifSwgeyJrZXkiOiAiaXJmb2lzbWZvc21kdjkwMjA5NDMyMzQvMjVjNjA2M2QtN2NjZi00MzA1LTgxYzgtYmRlZGZjM2YwZmY2Lm1wNCJ9LCB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sIHsieC1hbXotY3JlZGVudGlhbCI6ICJBU0lBNkdCTURDS0tKS09HS0tEMy8yMDI0MDEyMS91cy1lYXN0LTIvczMvYXdzNF9yZXF1ZXN0In0sIHsieC1hbXotZGF0ZSI6ICIyMDI0MDEyMVQxMjMzMjZaIn0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiSVFvSmIzSnBaMmx1WDJWakVIVWFDWFZ6TFdWaGMzUXRNaUpHTUVRQ0lCU1VWKzZXc1NERnF0SWN2YjdhbjdnTnppdk5vMkpwZnJIbEluTFVjVnd4QWlCR2crR1R0QjJsUXJ4M3VJWXQxazl3eW5NOFBXQWRPUm1CUE9EL1lEYXhJU3IyQWdndUVBQWFERGszTlRBMU1EQTFNakkwTkNJTXhEQWR3SjhZcVJ4VTRjRkxLdE1DMnIzNk1CdHZzUFVBYmFmY0JyYUNONjlxdnlFSzgxVlVMcE5nd1J0T3p3djV2ell3S0JWeDlaS0V6TW9ZQ3NpRCtWZEc2Z01NeW9ZelM3ZWVNSnZBQnZsS1hGcS9SVVJWWDdNbXdqWThsbkFOWmxacGF2dkdXdHgvVGpLMUlRUUZuaUdybE4vVytWN0p3WDBQcGpWS1NxRGVMV095OExYa0RpcGJ5RGFUaTZ4Yk5qSjllaVdydUNSYVJRU0J2TUd6SmJYWEJEZjd1RnF5VGRSTktaeTJabHVINm9saGNtdU9HWXFjYnV3VzlJZFZtRkpxV1c5ZURpWFdwUVQ0S2pUc3NMUm5lcUpnSTBxeGZTVVVMdDlId1A0dWJaVThEd2Nxd3BiLytRaG04Q3pBbVdRTGV0c1d3R0YwWnBvZGFBaDFXL0E3TnF4RUJrWVpvTFhNeUtrclVYVFY0ck4xZHNubkhSWnY2MERBNCtWTzhPdFA0blp5UHovdXpCNWxDb1VvZERUWnpsWS9hUis3aUFPS1BncCtxZVI4VkI3SzZCa0hRWmtMWFJmU2dGNXVBZEhYSzdhZW5zNEF6bFA0TjJoWURlbXRNTzJkdEswR09wOEJJVGVOSlFZTkU1M1VUUEJuNmJiZkpWa3BJekhTOHdvUkpxUlYvTEtCSytKWEMvVVQ4bjA2aUVnU2ZzaW04WFhZYjBBZnVTQmNaTlVLR0JhcWlnZDZRRi80bmVYUVd4VXZneDg1SG5EK2RpcmxWS0JwcExmZWg3Q1V2VVgzOXozNWpjY3oyNzJjSmNHYWFPV25ZZUJUMGF6bzIvbGZVLzZVUTVrVmdoOXYwZGtKM3BpUVRWNndHM0tXd0VUTU1oMGptU2ZzSG1mVmYxajFFVDd1SzlKYiJ9XX0=",
            "x-amz-signature": "45edce2c3cb40886ee8f2a8ed39e1f00559e0d673e70c4d2d58a81175504982e"
        }
    }
}
url = response['presigned_url']['url']
fields = response['presigned_url']['fields']

# Open the file in binary mode for upload
with open(object_name, 'rb') as f:
    files = {'file': (object_name, f)}

    # Send the POST request to S3
    http_response = requests.post(url, data=fields, files=files)

    print(f'HTTP Status Code: {http_response.status_code}')