import requests

object_name = './rick_roll.mp4'


response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "video_uuid": "2d6f3e21-edc8-48cf-b0a5-3214ac9c51cc",
    "presigned_url": {
        "url": "https://user-videos-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "ginorey/2d6f3e21-edc8-48cf-b0a5-3214ac9c51cc.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIAQMZWSSNHW5QWEO5S/20231223/us-east-2/s3/aws4_request",
            "x-amz-date": "20231223T034736Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjELT//////////wEaCXVzLWVhc3QtMiJHMEUCICTKRhpJGpnRQNVo4Cz2Nbf7cpzNhXX1cDHi6LkgXBqCAiEAzI0PFTCJkKa0tTG+QIp/5RkYiujd9P3HwgfMt2g1kpcqpQMIPRAAGgwwMjc0OTQ4ODAwNzkiDNoDmaKwd0HVOhiUmCqCA75QqN7acjPdqvNgdRdbuA8rmua2litRegjE8J4BwZVsFWJI6Pv4asGCq48B/Pn+07fdSVjvE7Dd3Kc65xY654vraKr3yXBV1IyRkbsftr3povNqYcPsiYz9IhZPYicsPS7Yb7XPNGu1lOKSiuPJ0ZelJkTD4p4uYIPk3t581/g47dL02OFigoZqBTcOjAwR8mSzFOuR9PZnKdhsSCSbYwHNydoKB1P8o4Q3xOZ1SynBoEESbUHoxyl3z80uNpBhHJqlg9m0VWOMS8/8ZW7PEZ+jg8y5INGOyfttGvuhrRrOdhDk+8u645Bn4ZRRE5DGmHYDJen4VUzYKNN1ac+BRoR99FrEcrhA5NQ5f+urQaLiYjQiuf3iW8eUGvi63ogyua7R5ow/fHoIS7BnMd68/ZjxDxdrFHrswKVhwPa8BuZa40kdP/B1iFBjXS3qDPlUoqVO9rggnPveRR9+UNCaJ1FD19UsWjN9RRFalT0B3kiFznn++U3ioQS/uAJA2iQfSselMMWwmawGOp0BWk9hIEIcEl0HjwCAIgz3zvHdMOeEVwI7qjRtTeRqYRCiin9ZtzK+3zkfteMF5/SvIvH8NwTAWNbx+Ek3nXEbS5KPlTG6Wei/BrnOcuAnZBosqkVvzzrdoIqNYfm52xURT4U1y6N5ZNaVN2X0AL/maYe15CbqbcpB+0RhGPd9aVNykDNrZssNs7z5o66Ddm95AbWDN/wc01QjWoJjYg==",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDQtMTZUMjE6MzQ6MTZaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci12aWRlb3MtYnVja2V0In0sIHsia2V5IjogImdpbm9yZXkvMmQ2ZjNlMjEtZWRjOC00OGNmLWIwYTUtMzIxNGFjOWM1MWNjLm1wNCJ9LCB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sIHsieC1hbXotY3JlZGVudGlhbCI6ICJBU0lBUU1aV1NTTkhXNVFXRU81Uy8yMDIzMTIyMy91cy1lYXN0LTIvczMvYXdzNF9yZXF1ZXN0In0sIHsieC1hbXotZGF0ZSI6ICIyMDIzMTIyM1QwMzQ3MzZaIn0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiSVFvSmIzSnBaMmx1WDJWakVMVC8vLy8vLy8vLy93RWFDWFZ6TFdWaGMzUXRNaUpITUVVQ0lDVEtSaHBKR3BuUlFOVm80Q3oyTmJmN2Nwek5oWFgxY0RIaTZMa2dYQnFDQWlFQXpJMFBGVENKa0thMHRURytRSXAvNVJrWWl1amQ5UDNId2dmTXQyZzFrcGNxcFFNSVBSQUFHZ3d3TWpjME9UUTRPREF3TnpraUROb0RtYUt3ZDBIVk9oaVVtQ3FDQTc1UXFON2FjalBkcXZOZ2RSZGJ1QThybXVhMmxpdFJlZ2pFOEo0QndaVnNGV0pJNlB2NGFzR0NxNDhCL1BuKzA3ZmRTVmp2RTdEZDNLYzY1eFk2NTR2cmFLcjN5WEJWMUl5Umtic2Z0cjNwb3ZOcVljUHNpWXo5SWhaUFlpY3NQUzdZYjdYUE5HdTFsT0tTaXVQSjBaZWxKa1RENHA0dVlJUGszdDU4MS9nNDdkTDAyT0ZpZ29acUJUY09qQXdSOG1TekZPdVI5UFpuS2Roc1NDU2JZd0hOeWRvS0IxUDhvNFEzeE9aMVN5bkJvRUVTYlVIb3h5bDN6ODB1TnBCaEhKcWxnOW0wVldPTVM4LzhaVzdQRVoramc4eTVJTkdPeWZ0dEd2dWhyUnJPZGhEays4dTY0NUJuNFpSUkU1REdtSFlESmVuNFZVellLTk4xYWMrQlJvUjk5RnJFY3JoQTVOUTVmK3VyUWFMaVlqUWl1ZjNpVzhlVUd2aTYzb2d5dWE3UjVvdy9mSG9JUzdCbk1kNjgvWmp4RHhkckZIcnN3S1Zod1BhOEJ1WmE0MGtkUC9CMWlGQmpYUzNxRFBsVW9xVk85cmdnblB2ZVJSOStVTkNhSjFGRDE5VXNXak45UlJGYWxUMEIza2lGem5uKytVM2lvUVMvdUFKQTJpUWZTc2VsTU1Xd21hd0dPcDBCV2s5aElFSWNFbDBIandDQUlnejN6dkhkTU9lRVZ3STdxalJ0VGVScVlSQ2lpbjladHpLKzN6a2Z0ZU1GNS9Tdkl2SDhOd1RBV05ieCtFazNuWEViUzVLUGxURzZXZWkvQnJuT2N1QW5aQm9zcWtWdnp6cmRvSXFOWWZtNTJ4VVJUNFUxeTZONVpOYVZOMlgwQUwvbWFZZTE1Q2JxYmNwQiswUmhHUGQ5YVZOeWtETnJac3NOczd6NW82NkRkbTk1QWJXRE4vd2MwMVFqV29KallnPT0ifV19",
            "x-amz-signature": "808b5f0e16928ee9118170b9591ef16b5cb5ceeaa04e4f5e412bd3a7358d80cc"
        }
    }
}

with open(object_name, 'rb') as f:
    files = {'file': (object_name, f)}
    http_response = requests.post(
        response['presigned_url']['url'], data=response['presigned_url']['fields'], files=files)
    
print(f'File upload HTTP status response: {http_response}')
print(f'File upload HTTP status code: {http_response.status_code}')
