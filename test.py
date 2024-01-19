import requests

object_name = './rick_roll.mp4'


response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "file_path": "49c6ed0f-d311-48eb-85c8-83e0c7d011d1/2f7c8a1e-30e8-4e69-a6c0-8d104537532d.mp4",
    "presigned_url": {
        "url": "https://user-file-upload-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "49c6ed0f-d311-48eb-85c8-83e0c7d011d1/2f7c8a1e-30e8-4e69-a6c0-8d104537532d.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIA6GBMDCKKBGZWAJPH/20240118/us-east-2/s3/aws4_request",
            "x-amz-date": "20240118T221154Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEDYaCXVzLWVhc3QtMiJIMEYCIQCpF84mExt6NgnGFeE6Mez6WdBsMjTWy0pKIGvGULnkaQIhAPmsMZmMaFh5yDQsD2eQ8fvhC7E08K2gzhJW7F+OT3+MKv8CCN///////////wEQABoMOTc1MDUwMDUyMjQ0IgyZ6zxz1vaWdrkQOEsq0wLI48a8mCJw3n+CMVYgrPBCq0303UuXXrFfw5c2Lud1UYPG9Yx9ofKtdzD0bcdtiKZAHXplzu8hrVT2NY3RLngZ609+QK2vaevSSs5d29meLXlNSX2qFty2jWJgn0PYeBnx4p7/TsFAtzQWZfOghWUaXJOQ9hq/l4EgHDUF8PJWQtUfL2S6KRmXQ6PYbWlnS5CBsJHaOiIxTmYEDuztsKrpQAgHoFQ6BhY7vM3HjOP0X235tmpvWLXSEwQPdMjn8CQGEC7wCZ3HAaixyUN/sTnPym9YaPynXEsDcMiPOTVxPxS1Y5rIt1305rQhIalvU0fSHF5fIoXGOAOCdmvSwMpJCFVI13lb7U44mF+Zof5txmCCz1Bn9Ce13SuJQuiG/7qPXJi6Bxmd683N94BkoWr0z5tXXCZyX1IN3a+kC8pI5v0D2GnmSOqlQfOepC+d7oJFyAswp8SmrQY6nQEglezzIhu2hF8K5ZETI+UDul+E401VQ+m0QmkmjRlLQh3faCf4lAN/LmG+WjVed9Nx7ey5FJPihDL4Bo3vbivu+cX94AHF/Fi3aFQ4zrQ5KtA55L0d5bSMr6kUgJshtayTrIsJdLdim5u6cL+3s+duhpVmTD9GSfgE/vrpZVv4FBCLHw9IDiXBX4ikx5tkAN2WvdB+BEW6syvtO4Qt",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDUtMTNUMTU6NTg6MzRaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci1maWxlLXVwbG9hZC1idWNrZXQifSwgeyJrZXkiOiAiNDljNmVkMGYtZDMxMS00OGViLTg1YzgtODNlMGM3ZDAxMWQxLzJmN2M4YTFlLTMwZTgtNGU2OS1hNmMwLThkMTA0NTM3NTMyZC5tcDQifSwgeyJ4LWFtei1hbGdvcml0aG0iOiAiQVdTNC1ITUFDLVNIQTI1NiJ9LCB7IngtYW16LWNyZWRlbnRpYWwiOiAiQVNJQTZHQk1EQ0tLQkdaV0FKUEgvMjAyNDAxMTgvdXMtZWFzdC0yL3MzL2F3czRfcmVxdWVzdCJ9LCB7IngtYW16LWRhdGUiOiAiMjAyNDAxMThUMjIxMTU0WiJ9LCB7IngtYW16LXNlY3VyaXR5LXRva2VuIjogIklRb0piM0pwWjJsdVgyVmpFRFlhQ1hWekxXVmhjM1F0TWlKSU1FWUNJUUNwRjg0bUV4dDZOZ25HRmVFNk1lejZXZEJzTWpUV3kwcEtJR3ZHVUxua2FRSWhBUG1zTVptTWFGaDV5RFFzRDJlUThmdmhDN0UwOEsyZ3poSlc3RitPVDMrTUt2OENDTi8vLy8vLy8vLy8vd0VRQUJvTU9UYzFNRFV3TURVeU1qUTBJZ3laNnp4ejF2YVdkcmtRT0VzcTB3TEk0OGE4bUNKdzNuK0NNVllnclBCQ3EwMzAzVXVYWHJGZnc1YzJMdWQxVVlQRzlZeDlvZkt0ZHpEMGJjZHRpS1pBSFhwbHp1OGhyVlQyTlkzUkxuZ1o2MDkrUUsydmFldlNTczVkMjltZUxYbE5TWDJxRnR5MmpXSmduMFBZZUJueDRwNy9Uc0ZBdHpRV1pmT2doV1VhWEpPUTlocS9sNEVnSERVRjhQSldRdFVmTDJTNktSbVhRNlBZYldsblM1Q0JzSkhhT2lJeFRtWUVEdXp0c0tycFFBZ0hvRlE2QmhZN3ZNM0hqT1AwWDIzNXRtcHZXTFhTRXdRUGRNam44Q1FHRUM3d0NaM0hBYWl4eVVOL3NUblB5bTlZYVB5blhFc0RjTWlQT1RWeFB4UzFZNXJJdDEzMDVyUWhJYWx2VTBmU0hGNWZJb1hHT0FPQ2RtdlN3TXBKQ0ZWSTEzbGI3VTQ0bUYrWm9mNXR4bUNDejFCbjlDZTEzU3VKUXVpRy83cVBYSmk2QnhtZDY4M045NEJrb1dyMHo1dFhYQ1p5WDFJTjNhK2tDOHBJNXYwRDJHbm1TT3FsUWZPZXBDK2Q3b0pGeUFzd3A4U21yUVk2blFFZ2xlenpJaHUyaEY4SzVaRVRJK1VEdWwrRTQwMVZRK20wUW1rbWpSbExRaDNmYUNmNGxBTi9MbUcrV2pWZWQ5Tng3ZXk1RkpQaWhETDRCbzN2Yml2dStjWDk0QUhGL0ZpM2FGUTR6clE1S3RBNTVMMGQ1YlNNcjZrVWdKc2h0YXlUcklzSmRMZGltNXU2Y0wrM3MrZHVocFZtVEQ5R1NmZ0UvdnJwWlZ2NEZCQ0xIdzlJRGlYQlg0aWt4NXRrQU4yV3ZkQitCRVc2c3l2dE80UXQifV19",
            "x-amz-signature": "563786184c0ad49ef481344b9593a5be3f1c337c3e3ef8005e14b5cc53a7a7e2"
        }
    }
}

with open(object_name, 'rb') as f:
    files = {'file': (object_name, f)}
    http_response = requests.post(
        response['presigned_url']['url'], data=response['presigned_url']['fields'], files=files)
    
print(f'File upload HTTP status response: {http_response}')
print(f'File upload HTTP status code: {http_response.status_code}')
