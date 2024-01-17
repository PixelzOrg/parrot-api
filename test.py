import requests

object_name = './rick_roll.mp4'


response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "file_path": "dc002629-2678-4ddc-8415-a1b0effd07d5/7c43ebf1-675b-40c9-bb92-b2edab03b326.mp4",
    "presigned_url": {
        "url": "https://user-file-upload-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "dc002629-2678-4ddc-8415-a1b0effd07d5/7c43ebf1-675b-40c9-bb92-b2edab03b326.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIA6GBMDCKKLNCXQYO6/20240117/us-east-2/s3/aws4_request",
            "x-amz-date": "20240117T020929Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEAoaCXVzLWVhc3QtMiJHMEUCIQDGT4/r6xIlGg7sLEheJvgtLiDXWC6zHoys54JID6M8xAIgLaSEJXt0c8HRa28axdAMAFfvmZFE7K4t9IaWaMwVcrUqvgMIs///////////ARAAGgw5NzUwNTAwNTIyNDQiDNH4IepVO9ik5v952CqSA20cgxT++VyOB2ntDAONwRadEL2+p0nABBnCzQjDN/4driR7/aaCFHlZKrdoHtB9Evx+ZIPQ+pMrybVTgmKmAdkJ1/7WHnuoK/trQZ9lmXFW97BVyIzwpIBai9uQkrxhPaY3ZRZ3hFYvqJ/S/9RLKYB4qt8mFu2VGEF/Rf9MpRMbNiuBJFZ059JX/J8J0z74hjo/O0PEi9QqpuEoT+1MThBrHoO3wr1mA3s/nu5U1HtlY6ZU7uPmEWSCVdKtP1TOg8CBmg7JHdqMZlV3RmukfamGby+oSF/OBdO5USk9KKxNWiWAHJ7r+JQUMceikjL/0mZlVXJFXqsygIg3+TyyhlmEYGs6osiU/2Ygz85SJbwmaLlwFd5J3DMm8+zHj2ajhIZYeabyOPr6YArA4PZA8b1oNkmG2eetc3QbeNFOYveiaAGJfc2wXdp9hlZ/0+3uWIS+mCUJ51wXj78Edr2ZezQeMl14MOx3oWRNI6GSF2Zr0/b83dA8LAQpVu7+yz5V2eGImLahsCs/xmJLAG9RkU858jDX7ZytBjqeATMyeUvdsWZoHM02B0i8phkw/0mxP1hEZSClgVdNk/PN9UlKPuSxbS4YDAofdUyalQ8cTRiB53XV8G2eobi38EP4nRWcSgQ6y67eNQ1gMFI3jIZTXgShQJYulshxus6nf2nhzT5ryIufsElQIlJhdGlVY0jW0yaD7V81938avSxJFm12j1LoVQccLdR3z42WB+u4HFEPSU/EMfk2ozBv",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDUtMTFUMTk6NTY6MDlaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci1maWxlLXVwbG9hZC1idWNrZXQifSwgeyJrZXkiOiAiZGMwMDI2MjktMjY3OC00ZGRjLTg0MTUtYTFiMGVmZmQwN2Q1LzdjNDNlYmYxLTY3NWItNDBjOS1iYjkyLWIyZWRhYjAzYjMyNi5tcDQifSwgeyJ4LWFtei1hbGdvcml0aG0iOiAiQVdTNC1ITUFDLVNIQTI1NiJ9LCB7IngtYW16LWNyZWRlbnRpYWwiOiAiQVNJQTZHQk1EQ0tLTE5DWFFZTzYvMjAyNDAxMTcvdXMtZWFzdC0yL3MzL2F3czRfcmVxdWVzdCJ9LCB7IngtYW16LWRhdGUiOiAiMjAyNDAxMTdUMDIwOTI5WiJ9LCB7IngtYW16LXNlY3VyaXR5LXRva2VuIjogIklRb0piM0pwWjJsdVgyVmpFQW9hQ1hWekxXVmhjM1F0TWlKSE1FVUNJUURHVDQvcjZ4SWxHZzdzTEVoZUp2Z3RMaURYV0M2ekhveXM1NEpJRDZNOHhBSWdMYVNFSlh0MGM4SFJhMjhheGRBTUFGZnZtWkZFN0s0dDlJYVdhTXdWY3JVcXZnTUlzLy8vLy8vLy8vLy9BUkFBR2d3NU56VXdOVEF3TlRJeU5EUWlETkg0SWVwVk85aWs1djk1MkNxU0EyMGNneFQrK1Z5T0IybnREQU9Od1JhZEVMMitwMG5BQkJuQ3pRakROLzRkcmlSNy9hYUNGSGxaS3Jkb0h0QjlFdngrWklQUStwTXJ5YlZUZ21LbUFka0oxLzdXSG51b0svdHJRWjlsbVhGVzk3QlZ5SXp3cElCYWk5dVFrcnhoUGFZM1pSWjNoRll2cUovUy85UkxLWUI0cXQ4bUZ1MlZHRUYvUmY5TXBSTWJOaXVCSkZaMDU5SlgvSjhKMHo3NGhqby9PMFBFaTlRcXB1RW9UKzFNVGhCckhvTzN3cjFtQTNzL251NVUxSHRsWTZaVTd1UG1FV1NDVmRLdFAxVE9nOENCbWc3SkhkcU1abFYzUm11a2ZhbUdieStvU0YvT0JkTzVVU2s5S0t4TldpV0FISjdyK0pRVU1jZWlrakwvMG1abFZYSkZYcXN5Z0lnMytUeXlobG1FWUdzNm9zaVUvMllnejg1U0pid21hTGx3RmQ1SjNETW04K3pIajJhamhJWlllYWJ5T1ByNllBckE0UFpBOGIxb05rbUcyZWV0YzNRYmVORk9ZdmVpYUFHSmZjMndYZHA5aGxaLzArM3VXSVMrbUNVSjUxd1hqNzhFZHIyWmV6UWVNbDE0TU94M29XUk5JNkdTRjJacjAvYjgzZEE4TEFRcFZ1Nyt5ejVWMmVHSW1MYWhzQ3MveG1KTEFHOVJrVTg1OGpEWDdaeXRCanFlQVRNeWVVdmRzV1pvSE0wMkIwaThwaGt3LzBteFAxaEVaU0NsZ1ZkTmsvUE45VWxLUHVTeGJTNFlEQW9mZFV5YWxROGNUUmlCNTNYVjhHMmVvYmkzOEVQNG5SV2NTZ1E2eTY3ZU5RMWdNRkkzaklaVFhnU2hRSll1bHNoeHVzNm5mMm5oelQ1cnlJdWZzRWxRSWxKaGRHbFZZMGpXMHlhRDdWODE5MzhhdlN4SkZtMTJqMUxvVlFjY0xkUjN6NDJXQit1NEhGRVBTVS9FTWZrMm96QnYifV19",
            "x-amz-signature": "fd4fa71b12f7e36afb43821431499f23b8a2ecc6bdfcf41e0ea7f770d9e86a5b"
        }
    }
}

with open(object_name, 'rb') as f:
    files = {'file': (object_name, f)}
    http_response = requests.post(
        response['presigned_url']['url'], data=response['presigned_url']['fields'], files=files)
    
print(f'File upload HTTP status response: {http_response}')
print(f'File upload HTTP status code: {http_response.status_code}')
