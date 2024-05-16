import requests
import json

url = "https://api.devrev.ai/api/gateway/internal/works.create"

headers = {
    "Authorization": f"Bearer eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtaW4tMTpkZXZvLzJjZmRXdzdISEg6ZGV2dS8xIiwiZXhwIjoxODEwNDIwMTE5LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2xpbmtlZGlufFdBSHhaaFBwanMiLCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VzZXJfaWQiOiJsaW5rZWRpbnxXQUh4WmhQcGpzIiwiaHR0cDovL2RldnJldi5haS9kZXZvX2RvbiI6ImRvbjppZGVudGl0eTpkdnJ2LWluLTE6ZGV2by8yY2ZkV3c3SEhIIiwiaHR0cDovL2RldnJldi5haS9kZXZvaWQiOiJERVYtMmNmZFd3N0hISCIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2dWlkIjoiREVWVS0xIiwiaHR0cDovL2RldnJldi5haS9kaXNwbGF5bmFtZSI6ImFudWRzYXVkMDciLCJodHRwOi8vZGV2cmV2LmFpL2VtYWlsIjoiYW51ZHNhdWQwN0BnbWFpbC5jb20iLCJodHRwOi8vZGV2cmV2LmFpL2Z1bGxuYW1lIjoiQW51ZCBTYXVkIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxNTgxMjExOSwiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi1pbi0xOmRldm8vMmNmZFd3N0hISDp0b2tlbi81TFVEQzlyNyIsIm9yZ19pZCI6Im9yZ19uQXZUd3BVVXRBR1pqZURNIiwic3ViIjoiZG9uOmlkZW50aXR5OmR2cnYtaW4tMTpkZXZvLzJjZmRXdzdISEg6ZGV2dS8xIn0.ghBTOhOrrSThmesKQ6h5Ay9Mz5Qi5HcKEBzlsEmVvOSNwSMmahNVInl8I_TCPbEkf1jiBpeHJuzxmAyE01lbDmpKOGhGsqn70yReHwkwxsiN3kcdKjPYpgqbUD_NaUOV5J2NUGumNk542xDGd2BTLIX-bsnvgCQy9pQe3HyALILsaTMUp6Nyt1dub7GXNx_0KigsrkVcAhKTEWZCwYNQqH4Z5aQQmuJ1rBgxH0bklM1ViDNuRXE2FY7Dkiq26kg4QYi81E_z4-Yt-CtakX0zZO5sNSrNgL_gj-J3QERoVx-XboMKmM-Ec5aE7xguGXKKi6QR2iKtJqv1ldGHuKn0Gg",
    "Content-Type": "application/json"
}

payload = {
    "type": "issue",
    "applies_to_part": "Default Product 1",
    "owned_by": ["anudsaud07"],
    "title": "Create your Parts",
    "priority": "P1" 
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Work item created successfully.")
    print("Work item ID:", response.json()["work"]["id"])
else:
    print("Failed to create work item. Status code:", response.status_code)
    print("Error message:", response.text)
