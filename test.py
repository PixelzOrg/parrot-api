import requests    # To install: pip install requests

# Generate a presigned S3 POST URL
object_name = 'rick_roll.mp4'
response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "file_uid": "0da6e66b-380c-4c02-a987-55a3664de458",
    "presigned_url": {
        "url": "https://user-file-upload-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "4EEKDlfvK5eXDxJRgzQwUYxsJSH2/0da6e66b-380c-4c02-a987-55a3664de458.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIA6GBMDCKKMHPNFFWC/20240121/us-east-2/s3/aws4_request",
            "x-amz-date": "20240121T023232Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEGsaCXVzLWVhc3QtMiJHMEUCIQCax12qdZv900NrnWIOI4aKZn3CV3B79PWLDCMXtvDMBgIgGpHB5GOdZxJ+pOuZUc+/8bomuaabsF+J7U86uPrBsKcq9gIIJBAAGgw5NzUwNTAwNTIyNDQiDCEOKuSi8RMx2+DJWirTAgEPxlAexyO9mbOZxDoGxoK8sbmVZdKNYUSBszdMBQCniOxinl6VmEUf+NUL1UbGvd3Bctx753GeiDq3l78Z7V/stSRGrN+OZ7GrxLIP9iaDZevNRtzpyG7UC7q12knzdpAgyvqr58Xfk+fYboEqSTuIM+L+pQOGkOW9e88s7BZH2E1elMM7s2aDBsQDUkn9AhZDhuzKVujEOKnHK8kBrACl29BNGrE+t5IqOCkJwcr+Ei16Cx/0oy+D7ihJajIUtpyZnAOlAnKH9pxF42M+uR02tPTASgGqULNKo1fYUVAoXc7AiDUopjuqPFD9L4WgTYNVqiNQJhXuyHP7ER8MdP6/iz/e2klhE1hfFfLi/MFrjW9+iNzulLY0SqQLQvtwWGZav3aJnEblo17OLiIxsKH/tkIro/ty04Fa1aVRku0PvBXYuUcIEU3KBdzuM2oh6zNBpzC9hLKtBjqeAcL4QpCcp77ldd2NWG2WoyOuWntcB09UKNeJ1YwnB6nl3KFGxuFLK04CiTN0N1MX1YvTbYcklkviBFq+qVuYYnQTKHTkhFC8pnfl9B31xZYFCER50hhpRQIUohAohtiA4jFsLR8JZGhQOWWxH8KLwDeI0QklABGe0Sd8DoHIDjxSR9P4hiXYDX6sr9rGj5mKA4uhsDaKMQk42iWqV771",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDEtMjFUMDM6MzI6MzJaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci1maWxlLXVwbG9hZC1idWNrZXQifSwgeyJrZXkiOiAiNEVFS0RsZnZLNWVYRHhKUmd6UXdVWXhzSlNIMi8wZGE2ZTY2Yi0zODBjLTRjMDItYTk4Ny01NWEzNjY0ZGU0NTgubXA0In0sIHsieC1hbXotYWxnb3JpdGhtIjogIkFXUzQtSE1BQy1TSEEyNTYifSwgeyJ4LWFtei1jcmVkZW50aWFsIjogIkFTSUE2R0JNRENLS01IUE5GRldDLzIwMjQwMTIxL3VzLWVhc3QtMi9zMy9hd3M0X3JlcXVlc3QifSwgeyJ4LWFtei1kYXRlIjogIjIwMjQwMTIxVDAyMzIzMloifSwgeyJ4LWFtei1zZWN1cml0eS10b2tlbiI6ICJJUW9KYjNKcFoybHVYMlZqRUdzYUNYVnpMV1ZoYzNRdE1pSkhNRVVDSVFDYXgxMnFkWnY5MDBOcm5XSU9JNGFLWm4zQ1YzQjc5UFdMRENNWHR2RE1CZ0lnR3BIQjVHT2RaeEorcE91WlVjKy84Ym9tdWFhYnNGK0o3VTg2dVByQnNLY3E5Z0lJSkJBQUdndzVOelV3TlRBd05USXlORFFpRENFT0t1U2k4Uk14MitESldpclRBZ0VQeGxBZXh5TzltYk9aeERvR3hvSzhzYm1WWmRLTllVU0JzemRNQlFDbmlPeGlubDZWbUVVZitOVUwxVWJHdmQzQmN0eDc1M0dlaURxM2w3OFo3Vi9zdFNSR3JOK09aN0dyeExJUDlpYURaZXZOUnR6cHlHN1VDN3ExMmtuemRwQWd5dnFyNThYZmsrZllib0VxU1R1SU0rTCtwUU9Ha09XOWU4OHM3QlpIMkUxZWxNTTdzMmFEQnNRRFVrbjlBaFpEaHV6S1Z1akVPS25ISzhrQnJBQ2wyOUJOR3JFK3Q1SXFPQ2tKd2NyK0VpMTZDeC8wb3krRDdpaEphaklVdHB5Wm5BT2xBbktIOXB4RjQyTSt1UjAydFBUQVNnR3FVTE5LbzFmWVVWQW9YYzdBaURVb3BqdXFQRkQ5TDRXZ1RZTlZxaU5RSmhYdXlIUDdFUjhNZFA2L2l6L2Uya2xoRTFoZkZmTGkvTUZyalc5K2lOenVsTFkwU3FRTFF2dHdXR1phdjNhSm5FYmxvMTdPTGlJeHNLSC90a0lyby90eTA0RmExYVZSa3UwUHZCWFl1VWNJRVUzS0JkenVNMm9oNnpOQnB6QzloTEt0QmpxZUFjTDRRcENjcDc3bGRkMk5XRzJXb3lPdVdudGNCMDlVS05lSjFZd25CNm5sM0tGR3h1RkxLMDRDaVROME4xTVgxWXZUYllja2xrdmlCRnErcVZ1WVluUVRLSFRraEZDOHBuZmw5QjMxeFpZRkNFUjUwaGhwUlFJVW9oQW9odGlBNGpGc0xSOEpaR2hRT1dXeEg4S0x3RGVJMFFrbEFCR2UwU2Q4RG9ISURqeFNSOVA0aGlYWURYNnNyOXJHajVtS0E0dWhzRGFLTVFrNDJpV3FWNzcxIn1dfQ==",
            "x-amz-signature": "a40bdd43c7e0d7534f4d91c20b82b57674075beef42f8289e5d7bb154d00bbff"
        }
    }
}

url = response['presigned_url']['url']
fields = response['presigned_url']['fields']

# Open the file in binary mode for upload
with open(object_name, 'rb') as f:
    data = fields.copy()
    files = {'file': (object_name, f)}

    # Send the POST request to S3
    http_response = requests.post(url, data=data, files=files)

    print(f'HTTP Status Code: {http_response.status_code}')