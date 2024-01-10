import requests

object_name = './rick_roll.mp4'


response = {
    "message": "Presigned URL generated successfully",
    "expires": 3600,
    "video_uuid": "11ff52a4-0438-4cb1-82a3-de6f0238420d",
    "presigned_url": {
        "url": "https://user-videos-bucket.s3.amazonaws.com/",
        "fields": {
            "key": "ginorey/11ff52a4-0438-4cb1-82a3-de6f0238420d.mp4",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-credential": "ASIAQMZWSSNHXRAXT4XU/20231223/us-east-2/s3/aws4_request",
            "x-amz-date": "20231223T041133Z",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjELT//////////wEaCXVzLWVhc3QtMiJGMEQCIHf1sVrTAdvPm0hkcLLfuTFm9td9DWfr450NNL0Umd6cAiBeRajXoExVVfDxM5+uf24QFPMpwuroZZ4hKXPJIN3EMiqlAwg9EAAaDDAyNzQ5NDg4MDA3OSIMSDnt4TMwgKAbK3FdKoIDiQSH1Jc9SaGlWBG5/NL9L2xkpjdW2GqdqF118e8crzZHUNPxso3h+uBXw7b3pRGiqN7trEIvwhusDwGe16rTA+BOqOhuPMmkQmoKobxyF+cevOt+qW0vSGfPZC9NOmHfuC8LH38qhTs6FQ8gIba+zTp+in2QCXo//xZeUA/fU6vy/EoCKv5lxdc7ZiqdxgXNMH05qkhMQ2bBZV1HbmZPxaaHXnNGiqv72wDIGwsKXYNjKrj7ybIwkGdRWbOnZwZPx5DCbh/tu5q/TLI3miNWHwnBCgDeiz8GeuOIktw8AyO+McF+qCpCo9CNBK7mzwmeY72R4++ayzJ4VAuMmqA2uCmE+b8rugVlOjn9tT5XrVlEC49nqxUmIZSyPOaZUbZFgpH0L1FJEz/dTES/Bu/fO9Qmx9Tl82ueK2OqTQBuJdOJLQA2hTUf1WJh5iBLdJLepohlYmuXiguuvwWMsG/nE8ioS61Zo78Dvb8UalAKpVujQ0NMnPh1Fgve/Bhoxirn6zsw9LSZrAY6ngFjf4hvpo7/INaByCHRDovTDYXPDNPgigN9g4x/1olM47Un3bXRRKpgkGb8kurIcNhLsFocLM4Q64MXt6pujWnJb8GPJddmdoitPAvJJS8T/ChwyYyFNmKzU0sDwHw1yHE1Nfeljb6+Poxa9hOHJzmCfvZy2vtuc3X2GwTPxql8VnsY68ipGq76+WvFaoS39/6APVM+dFs4IjPTzcV0nA==",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjQtMDQtMTZUMjE6NTg6MTNaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAidXNlci12aWRlb3MtYnVja2V0In0sIHsia2V5IjogImdpbm9yZXkvMTFmZjUyYTQtMDQzOC00Y2IxLTgyYTMtZGU2ZjAyMzg0MjBkLm1wNCJ9LCB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sIHsieC1hbXotY3JlZGVudGlhbCI6ICJBU0lBUU1aV1NTTkhYUkFYVDRYVS8yMDIzMTIyMy91cy1lYXN0LTIvczMvYXdzNF9yZXF1ZXN0In0sIHsieC1hbXotZGF0ZSI6ICIyMDIzMTIyM1QwNDExMzNaIn0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiSVFvSmIzSnBaMmx1WDJWakVMVC8vLy8vLy8vLy93RWFDWFZ6TFdWaGMzUXRNaUpHTUVRQ0lIZjFzVnJUQWR2UG0waGtjTExmdVRGbTl0ZDlEV2ZyNDUwTk5MMFVtZDZjQWlCZVJhalhvRXhWVmZEeE01K3VmMjRRRlBNcHd1cm9aWjRoS1hQSklOM0VNaXFsQXdnOUVBQWFEREF5TnpRNU5EZzRNREEzT1NJTVNEbnQ0VE13Z0tBYkszRmRLb0lEaVFTSDFKYzlTYUdsV0JHNS9OTDlMMnhrcGpkVzJHcWRxRjExOGU4Y3J6WkhVTlB4c28zaCt1Qlh3N2IzcFJHaXFON3RyRUl2d2h1c0R3R2UxNnJUQStCT3FPaHVQTW1rUW1vS29ieHlGK2Nldk90K3FXMHZTR2ZQWkM5Tk9tSGZ1QzhMSDM4cWhUczZGUThnSWJhK3pUcCtpbjJRQ1hvLy94WmVVQS9mVTZ2eS9Fb0NLdjVseGRjN1ppcWR4Z1hOTUgwNXFraE1RMmJCWlYxSGJtWlB4YWFIWG5OR2lxdjcyd0RJR3dzS1hZTmpLcmo3eWJJd2tHZFJXYk9uWndaUHg1RENiaC90dTVxL1RMSTNtaU5XSHduQkNnRGVpejhHZXVPSWt0dzhBeU8rTWNGK3FDcENvOUNOQks3bXp3bWVZNzJSNCsrYXl6SjRWQXVNbXFBMnVDbUUrYjhydWdWbE9qbjl0VDVYclZsRUM0OW5xeFVtSVpTeVBPYVpVYlpGZ3BIMEwxRkpFei9kVEVTL0J1L2ZPOVFteDlUbDgydWVLMk9xVFFCdUpkT0pMUUEyaFRVZjFXSmg1aUJMZEpMZXBvaGxZbXVYaWd1dXZ3V01zRy9uRThpb1M2MVpvNzhEdmI4VWFsQUtwVnVqUTBOTW5QaDFGZ3ZlL0Job3hpcm42enN3OUxTWnJBWTZuZ0ZqZjRodnBvNy9JTmFCeUNIUkRvdlREWVhQRE5QZ2lnTjlnNHgvMW9sTTQ3VW4zYlhSUktwZ2tHYjhrdXJJY05oTHNGb2NMTTRRNjRNWHQ2cHVqV25KYjhHUEpkZG1kb2l0UEF2SkpTOFQvQ2h3eVl5Rk5tS3pVMHNEd0h3MXlIRTFOZmVsamI2K1BveGE5aE9ISnptQ2Z2WnkydnR1YzNYMkd3VFB4cWw4Vm5zWTY4aXBHcTc2K1d2RmFvUzM5LzZBUFZNK2RGczRJalBUemNWMG5BPT0ifV19",
            "x-amz-signature": "a1652b0c60fc1e84d7a2b6e04251a9445a050074220636665fd79722b1c28d3f"
        }
    }
}

with open(object_name, 'rb') as f:
    files = {'file': (object_name, f)}
    http_response = requests.post(
        response['presigned_url']['url'], data=response['presigned_url']['fields'], files=files)
    
print(f'File upload HTTP status response: {http_response}')
print(f'File upload HTTP status code: {http_response.status_code}')
