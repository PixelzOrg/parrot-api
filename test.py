import requests    # To install: pip install requests

# Generate a presigned S3 POST URL
object_name = 'rick_roll.mp4'
response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "file_uid": "1f1e0cba-817a-452e-8b98-f2f2a57eeb2a",
    "presigned_url": {
        "url": "https://user-file-upload-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "4EEKDlfvK5eXDxJRgzQwUYxsJSH2/1f1e0cba-817a-452e-8b98-f2f2a57eeb2a.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIA6GBMDCKKD5NSYH6F/20240121/us-east-2/s3/aws4_request",
            "x-amz-date": "20240121T062646Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEG4aCXVzLWVhc3QtMiJGMEQCIFNsZccaTx5Vd7qUcTgwOFeI5JJ7stFwtlrsDBkTZ23kAiAf6sPh/JKu8jcryiNvbp1H3HnIv43ZzOuO+O5FrMJy8Sr2AggoEAAaDDk3NTA1MDA1MjI0NCIMnXsI1PeS2cN/WkyqKtMCG2wIfKksI1PVU7hLKugb25t7Z+yHEg9VTmESeiff7sCxMIh/yjgpURpcttbH5Zpr8FFs1kuair3DC1OYdbH6AmJev6AvljbgMekmgF2J1QR00O0zZNLVvBn9XDZQn7S9SBSiCKF1d9ySVdz0USDHwyu5rMsWFsq5+CS3C2j4rduCJeBY5WwC5BhflHvwJPFLfz6vWMJjIYoPVyWG6U3aAsgi3+VaJMnhrV3gYXH8CXJkz+Plh2D5tE5OpCGt4iHuFUy8tSQdpRKbmXg5zda0/YUkyx6PA15w9rfhuAYNzWAAND7k7fmV/i9mtSy3lNwxTPI8eusPQYQZcZ+dLwWrgYscUx8bUjiqP9aZhTEm7BFRuz32qznVnWAXHFv7IbcEpYaZbk4woPOpLub/1dprLzxJj/GMa+JsT/Ogu2hNlnTrtlGjAv3Xkuxtj6fMJE4Ytpz3MKPysq0GOp8BGdXbOZ+D1X8EnG1ElodbusVKc2jMvyX/1+3kjiBMQhJnGmxTcAIX8fvqlCpSldIN3qoIp+LkzkCypjrUg+OU41JyTNoiXjEdrFz1Ylbb3jPg+Q5JaQvlfTPfqjAuXF63IaGPF8SEs+/HAhVtOXybbArRmRqoEU7akn626M9GYmGyOrbHgqugtXyljiHy5etD6MmO1Iti+/VFZvFVXDrk",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDEtMjFUMDc6MjY6NDZaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci1maWxlLXVwbG9hZC1idWNrZXQifSwgeyJrZXkiOiAiNEVFS0RsZnZLNWVYRHhKUmd6UXdVWXhzSlNIMi8xZjFlMGNiYS04MTdhLTQ1MmUtOGI5OC1mMmYyYTU3ZWViMmEubXA0In0sIHsieC1hbXotYWxnb3JpdGhtIjogIkFXUzQtSE1BQy1TSEEyNTYifSwgeyJ4LWFtei1jcmVkZW50aWFsIjogIkFTSUE2R0JNRENLS0Q1TlNZSDZGLzIwMjQwMTIxL3VzLWVhc3QtMi9zMy9hd3M0X3JlcXVlc3QifSwgeyJ4LWFtei1kYXRlIjogIjIwMjQwMTIxVDA2MjY0NloifSwgeyJ4LWFtei1zZWN1cml0eS10b2tlbiI6ICJJUW9KYjNKcFoybHVYMlZqRUc0YUNYVnpMV1ZoYzNRdE1pSkdNRVFDSUZOc1pjY2FUeDVWZDdxVWNUZ3dPRmVJNUpKN3N0Rnd0bHJzREJrVFoyM2tBaUFmNnNQaC9KS3U4amNyeWlOdmJwMUgzSG5JdjQzWnpPdU8rTzVGck1KeThTcjJBZ2dvRUFBYUREazNOVEExTURBMU1qSTBOQ0lNblhzSTFQZVMyY04vV2t5cUt0TUNHMndJZktrc0kxUFZVN2hMS3VnYjI1dDdaK3lIRWc5VlRtRVNlaWZmN3NDeE1JaC95amdwVVJwY3R0Ykg1WnByOEZGczFrdWFpcjNEQzFPWWRiSDZBbUpldjZBdmxqYmdNZWttZ0YySjFRUjAwTzB6Wk5MVnZCbjlYRFpRbjdTOVNCU2lDS0YxZDl5U1ZkejBVU0RId3l1NXJNc1dGc3E1K0NTM0MyajRyZHVDSmVCWTVXd0M1QmhmbEh2d0pQRkxmejZ2V01KaklZb1BWeVdHNlUzYUFzZ2kzK1ZhSk1uaHJWM2dZWEg4Q1hKa3orUGxoMkQ1dEU1T3BDR3Q0aUh1RlV5OHRTUWRwUktibVhnNXpkYTAvWVVreXg2UEExNXc5cmZodUFZTnpXQUFORDdrN2ZtVi9pOW10U3kzbE53eFRQSThldXNQUVlRWmNaK2RMd1dyZ1lzY1V4OGJVamlxUDlhWmhURW03QkZSdXozMnF6blZuV0FYSEZ2N0liY0VwWWFaYms0d29QT3BMdWIvMWRwckx6eEpqL0dNYStKc1QvT2d1MmhObG5UcnRsR2pBdjNYa3V4dGo2Zk1KRTRZdHB6M01LUHlzcTBHT3A4QkdkWGJPWitEMVg4RW5HMUVsb2RidXNWS2Myak12eVgvMSsza2ppQk1RaEpuR214VGNBSVg4ZnZxbENwU2xkSU4zcW9JcCtMa3prQ3lwanJVZytPVTQxSnlUTm9pWGpFZHJGejFZbGJiM2pQZytRNUphUXZsZlRQZnFqQXVYRjYzSWFHUEY4U0VzKy9IQWhWdE9YeWJiQXJSbVJxb0VVN2FrbjYyNk05R1ltR3lPcmJIZ3F1Z3RYeWxqaUh5NWV0RDZNbU8xSXRpKy9WRlp2RlZYRHJrIn1dfQ==",
            "x-amz-signature": "31c963e63fbe5cf8307e96f429654d7777bb6d877c489a4b531563f21f5a04dd"
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