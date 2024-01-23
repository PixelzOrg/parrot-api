import requests    # To install: pip install requests

# Generate a presigned S3 POST URL
object_name = 'rick_roll.mp4'
response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "file_uid": "ce2e8d01-78d1-40b4-a10f-e80c431ebf69",
    "presigned_url": {
        "url": "https://user-file-upload-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "irfoismfosmdv9020943234/ce2e8d01-78d1-40b4-a10f-e80c431ebf69.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIA6GBMDCKKKAHZLGGO/20240123/us-east-2/s3/aws4_request",
            "x-amz-date": "20240123T025815Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEJv//////////wEaCXVzLWVhc3QtMiJHMEUCIEe2eEeRPAVsBjectWLAj79YAvmVA5qTO74nwDA6lAa7AiEA97khwfHgZcvYYZtEKOq5JkgL6+b5YWtv9RvCpUClvf8q9gIIVBAAGgw5NzUwNTAwNTIyNDQiDL+Dn2aIRqamu01grSrTAjBhyOa8x7FPeCRArrRp6Xro29hYKxok+bmJWJdOERWATKcvefcLS7aIfXbn736Y/enwAmSGeavCOE3xXnRGS5L7jEejZwCN/kscto6q44a9ItoBCwAITtmqQwj3sICrGsPwE2IOLjIro0TGik1KPWTnU5IPxH8nCRcEK9CogNnb+TzdFL3bcrQkZYHTglHBbDVkn8WGFtk/GuK1HSX1hDbEx+sff/cNaqFOGSEV0i4UNhBLNWmbYhww5Vwc+DIpfkchtCTUImPlts7oLYbLyJC79J4H9pdKip+4yRpyfQPW8E2QDtnYBqHLo72ruM7ScV6MYWWtXoGipR5d1dLzQnHd+doBRyQjlpLLwPQdM0Aw565hn7IPAT9waVoF5Bzu9UU67cVf/QJ7lR9F3r/si6+l4fsBY/Bwt7LVir82T/LIkbc0xHXZCjxAdQXS0o84F8EwrTDE1rytBjqeAcC5cfLuoIk6szDNziPMS5X8miJkhhYOWuEw9YiYKh2vI9LuSr+PvhDQfuk2psxAowo4nXHtQAyLJKrSgohciQpb1UQ634tXNBCDaVPGQuVhm+NkO4hcs/YOzEdzA9LY+hUw3QQ+ILtaOSlKMW9JuCZ8vbamtDam8LM8Nl4ujolc7PXQbiXTq5n26NGOg9c2ULM3xuQ0AG2t5UM6CSDX",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDEtMjNUMDM6NTg6MTVaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci1maWxlLXVwbG9hZC1idWNrZXQifSwgeyJrZXkiOiAiaXJmb2lzbWZvc21kdjkwMjA5NDMyMzQvY2UyZThkMDEtNzhkMS00MGI0LWExMGYtZTgwYzQzMWViZjY5Lm1wNCJ9LCB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sIHsieC1hbXotY3JlZGVudGlhbCI6ICJBU0lBNkdCTURDS0tLQUhaTEdHTy8yMDI0MDEyMy91cy1lYXN0LTIvczMvYXdzNF9yZXF1ZXN0In0sIHsieC1hbXotZGF0ZSI6ICIyMDI0MDEyM1QwMjU4MTVaIn0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiSVFvSmIzSnBaMmx1WDJWakVKdi8vLy8vLy8vLy93RWFDWFZ6TFdWaGMzUXRNaUpITUVVQ0lFZTJlRWVSUEFWc0JqZWN0V0xBajc5WUF2bVZBNXFUTzc0bndEQTZsQWE3QWlFQTk3a2h3ZkhnWmN2WVladEVLT3E1SmtnTDYrYjVZV3R2OVJ2Q3BVQ2x2ZjhxOWdJSVZCQUFHZ3c1TnpVd05UQXdOVEl5TkRRaURMK0RuMmFJUnFhbXUwMWdyU3JUQWpCaHlPYTh4N0ZQZUNSQXJyUnA2WHJvMjloWUt4b2srYm1KV0pkT0VSV0FUS2N2ZWZjTFM3YUlmWGJuNzM2WS9lbndBbVNHZWF2Q09FM3hYblJHUzVMN2pFZWpad0NOL2tzY3RvNnE0NGE5SXRvQkN3QUlUdG1xUXdqM3NJQ3JHc1B3RTJJT0xqSXJvMFRHaWsxS1BXVG5VNUlQeEg4bkNSY0VLOUNvZ05uYitUemRGTDNiY3JRa1pZSFRnbEhCYkRWa244V0dGdGsvR3VLMUhTWDFoRGJFeCtzZmYvY05hcUZPR1NFVjBpNFVOaEJMTldtYllod3c1VndjK0RJcGZrY2h0Q1RVSW1QbHRzN29MWWJMeUpDNzlKNEg5cGRLaXArNHlScHlmUVBXOEUyUUR0bllCcUhMbzcycnVNN1NjVjZNWVdXdFhvR2lwUjVkMWRMelFuSGQrZG9CUnlRamxwTEx3UFFkTTBBdzU2NWhuN0lQQVQ5d2FWb0Y1Qnp1OVVVNjdjVmYvUUo3bFI5RjNyL3NpNitsNGZzQlkvQnd0N0xWaXI4MlQvTElrYmMweEhYWkNqeEFkUVhTMG84NEY4RXdyVERFMXJ5dEJqcWVBY0M1Y2ZMdW9JazZzekROemlQTVM1WDhtaUpraGhZT1d1RXc5WWlZS2gydkk5THVTcitQdmhEUWZ1azJwc3hBb3dvNG5YSHRRQXlMSktyU2dvaGNpUXBiMVVRNjM0dFhOQkNEYVZQR1F1VmhtK05rTzRoY3MvWU96RWR6QTlMWStoVXczUVErSUx0YU9TbEtNVzlKdUNaOHZiYW10RGFtOExNOE5sNHVqb2xjN1BYUWJpWFRxNW4yNk5HT2c5YzJVTE0zeHVRMEFHMnQ1VU02Q1NEWCJ9XX0=",
            "x-amz-signature": "107121ad513feea5997d69557536f3f54c1a4667eeb4c4a5bd028ff4e891eddd"
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