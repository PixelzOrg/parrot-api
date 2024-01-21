import requests    # To install: pip install requests

# Generate a presigned S3 POST URL
object_name = 'rick_roll.mp4'
response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "file_uid": "fe3581a6-d32c-43e5-ba4c-61cccf6f52ea",
    "presigned_url": {
        "url": "https://user-file-upload-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "irfoismfosmdv9020943234/fe3581a6-d32c-43e5-ba4c-61cccf6f52ea.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIA6GBMDCKKFFBNDEGC/20240121/us-east-2/s3/aws4_request",
            "x-amz-date": "20240121T101545Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEHIaCXVzLWVhc3QtMiJIMEYCIQC2hSRwSX0U9NC2v/Fj1QRSEngOss8xit+khm/d9hqa5gIhALYtAbUkJT5tcdUfsClag9BJqvVu2ELtp9/WIYA75P4UKvYCCCsQABoMOTc1MDUwMDUyMjQ0IgybrkfWnOY8QobVUmIq0wL6cGeyDISkiJp1Kw5oIi5fSgm3f7lCGlCE9ggP8CJEKqkQAAVlhUo6Z8E31ZgCBKPWMU3ATyQNLQwYupUEvfsok+Kk1qMSu+la13H3I3tyAA9zskGmOBGdbi1rBS6fMIyT/bauRmaTqwRucjPLeVFN4GIsxASI/gi2bAg6/4h4384YRdh4LShUM99kSPzL0QY9RfySh73y8AkstwXT4ZTmZTbkGXHiWe5cjxmbTWXcWRyujkrcFSZ9ndr1eASbrWRdvQFDyThbYQ+tuHdfKU9R04sZseZWgls0psvQVGERJ6tR6mvnnLQh0U6bSu0UlIPr6f82G5rnH4b0n2fbecpBrt9O71HMDrt6YzZPwlH01X0e860EEbc9NRYyfe/sFV0jVqsxFhwPbEo90IiYSmL8UJSgyzilNFzbe60QbO2XNrEhmP4GQ2vzwX7ISJzbWuZGMqowvNizrQY6nQGhTg4Kz0oDGWDjFTlwrNc7+MQyxNlZ3Qb4rdMvEgsT0Tk40pjB2Ip4guj0NXmEAJGMOD/ehCErliGh5MCk1n+/hp1QUndB2N+BxFPAhyjpvJiHCJ9NGk7zcauvHs6ef8RACHgbhrwIIbe2JkTzMmu0UwOpecx7/r1pzmsw9fkP1B4uAtvKXDqvYAs+Pxsu3Qr0QjOqVgI1NwYhmVZU",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDEtMjFUMTE6MTU6NDVaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci1maWxlLXVwbG9hZC1idWNrZXQifSwgeyJrZXkiOiAiaXJmb2lzbWZvc21kdjkwMjA5NDMyMzQvZmUzNTgxYTYtZDMyYy00M2U1LWJhNGMtNjFjY2NmNmY1MmVhLm1wNCJ9LCB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sIHsieC1hbXotY3JlZGVudGlhbCI6ICJBU0lBNkdCTURDS0tGRkJOREVHQy8yMDI0MDEyMS91cy1lYXN0LTIvczMvYXdzNF9yZXF1ZXN0In0sIHsieC1hbXotZGF0ZSI6ICIyMDI0MDEyMVQxMDE1NDVaIn0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiSVFvSmIzSnBaMmx1WDJWakVISWFDWFZ6TFdWaGMzUXRNaUpJTUVZQ0lRQzJoU1J3U1gwVTlOQzJ2L0ZqMVFSU0VuZ09zczh4aXQra2htL2Q5aHFhNWdJaEFMWXRBYlVrSlQ1dGNkVWZzQ2xhZzlCSnF2VnUyRUx0cDkvV0lZQTc1UDRVS3ZZQ0NDc1FBQm9NT1RjMU1EVXdNRFV5TWpRMElneWJya2ZXbk9ZOFFvYlZVbUlxMHdMNmNHZXlESVNraUpwMUt3NW9JaTVmU2dtM2Y3bENHbENFOWdnUDhDSkVLcWtRQUFWbGhVbzZaOEUzMVpnQ0JLUFdNVTNBVHlRTkxRd1l1cFVFdmZzb2srS2sxcU1TdStsYTEzSDNJM3R5QUE5enNrR21PQkdkYmkxckJTNmZNSXlUL2JhdVJtYVRxd1J1Y2pQTGVWRk40R0lzeEFTSS9naTJiQWc2LzRoNDM4NFlSZGg0TFNoVU05OWtTUHpMMFFZOVJmeVNoNzN5OEFrc3R3WFQ0WlRtWlRia0dYSGlXZTVjanhtYlRXWGNXUnl1amtyY0ZTWjluZHIxZUFTYnJXUmR2UUZEeVRoYllRK3R1SGRmS1U5UjA0c1pzZVpXZ2xzMHBzdlFWR0VSSjZ0UjZtdm5uTFFoMFU2YlN1MFVsSVByNmY4Mkc1cm5INGIwbjJmYmVjcEJydDlPNzFITURydDZZelpQd2xIMDFYMGU4NjBFRWJjOU5SWXlmZS9zRlYwalZxc3hGaHdQYkVvOTBJaVlTbUw4VUpTZ3l6aWxORnpiZTYwUWJPMlhOckVobVA0R1Eydnp3WDdJU0p6Yld1WkdNcW93dk5penJRWTZuUUdoVGc0S3owb0RHV0RqRlRsd3JOYzcrTVF5eE5sWjNRYjRyZE12RWdzVDBUazQwcGpCMklwNGd1ajBOWG1FQUpHTU9EL2VoQ0VybGlHaDVNQ2sxbisvaHAxUVVuZEIyTitCeEZQQWh5anB2SmlIQ0o5TkdrN3pjYXV2SHM2ZWY4UkFDSGdiaHJ3SUliZTJKa1R6TW11MFV3T3BlY3g3L3IxcHptc3c5ZmtQMUI0dUF0dktYRHF2WUFzK1B4c3UzUXIwUWpPcVZnSTFOd1lobVZaVSJ9XX0=",
            "x-amz-signature": "6081b5f54b76145cc08a44d836975e2b5b6cf0282343370f264277730da4700e"
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