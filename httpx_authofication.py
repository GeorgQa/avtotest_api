import httpx

payload = {
    "email": "test.1748955254.5540535@example.com",
    "password": "ac921213-fa64-4921-bff7-211c7c9447ec",
}

response_login = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=payload
)
login_response_data = response_login.json()

print("Login resposne:", login_response_data)
print("Status code:", response_login.status_code)

refresh_payload = {"refreshToken": login_response_data["token"]["refreshToken"]}

refresh_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload
)
refresh_response_data = refresh_response.json()

print("Refresh resposne:", refresh_response_data)
print("Status code:", refresh_response.status_code)
