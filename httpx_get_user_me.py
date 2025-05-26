import json

import httpx

params_for_login = {
    "email": "test_test@yandex.ru",
    "password": "qwerty12345"
}
response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=params_for_login)

json_response_login = response_login.json()

access_token = json_response_login['token']['accessToken']

print(access_token)
print(response_login.status_code)

headers_for_requests = {"Authorization": f"Bearer {access_token}", "content-type":"application/json" }

response_user_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_for_requests)


print(response_user_me.headers)
print(response_user_me.status_code)

