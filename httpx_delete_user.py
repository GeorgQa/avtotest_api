import httpx

from tools import faker_data

create_user_payload = {
    "email": faker_data.fake_en.email(),
    "password": faker_data.fake_en.password(),
    "lastName": faker_data.fake_ru.last_name(),
    "firstName": faker_data.fake_ru.first_name(),
    "middleName": faker_data.fake_ru.middle_name(),
}

print(create_user_payload["email"])
print(create_user_payload["lastName"])
print(create_user_payload["firstName"])
print(create_user_payload["middleName"])


create_user_response = httpx.post(
    "http://localhost:8000/api/v1/users", json=create_user_payload
)
create_user_response_data = create_user_response.json()

print("Create_user", create_user_response_data)


login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"],
}


login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_payload
)
response_login_data = login_response.json()

print(response_login_data)

delete_user_headers = {
    "Authorization": f"Bearer {response_login_data['token']['accessToken']}"
}

delete_user_response = httpx.delete(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=delete_user_headers,
)

print("Create user data check", create_user_response_data["user"]["id"])
print("Create user  deletk", delete_user_response.json())
print("Status_code", delete_user_response.status_code)
