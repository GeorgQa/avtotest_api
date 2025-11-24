import httpx

params_for_login = {"email": "test_test@yandex.ru", "password": "qwerty12345"}

response_login = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=params_for_login
)
json_response_login = response_login.json()

print(json_response_login)

client_for_tets = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"authorization": f"Bearer {json_response_login['token']['accessToken']}"},
)
response_for_test = client_for_tets.get("/api/v1/users/me")
response_for_test_data = response_for_test.json()

print("Get user me data", response_for_test.text)
