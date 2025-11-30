import httpx

from tools import faker_data

payload = {
    "email": faker_data.fake_en.email(),
    "password": faker_data.fake_en.password(),
    "lastName": faker_data.fake_ru.last_name(),
    "firstName": faker_data.fake_ru.first_name(),
    "middleName": faker_data.fake_ru.middle_name(),
}

print(payload)

response_create_user = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response_create_user.status_code)
print(response_create_user.json())
