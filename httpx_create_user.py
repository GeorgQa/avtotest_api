import httpx
from tools import faker_data

payload = {
    "email": faker_data.get_random_email(),
    "password": faker_data.get_data()["password"],
    "lastName": faker_data.get_data()["last_name"],
    "firstName": faker_data.get_data()["first"],
    "middleName": faker_data.get_data()["middle"],
}

print(payload)

response_create_user = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response_create_user.status_code)
print(response_create_user.json())
