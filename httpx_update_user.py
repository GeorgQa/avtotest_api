import httpx
from tools import faker_data

create_user_payload = {
    "email": faker_data.get_random_email(),
    "password": faker_data.get_data()["password"],
    "lastName": faker_data.get_data()["last_name"],
    "firstName": faker_data.get_data()["first"],
    "middleName": faker_data.get_data()["middle"],
}

print("Data_from_create_user", create_user_payload)

create_user_response = httpx.post(
    "http://localhost:8000/api/v1/users", json=create_user_payload
)
create_user_response_data = create_user_response.json()

print("Create user:", create_user_response_data)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"],
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_payload
)
response_login_data = login_response.json()
print("Login:", response_login_data)
print(login_response.status_code)

update_user_payload = {
    "Authorization": f"Bearer {response_login_data['token']['accessToken']}"
}
print("Payload:", update_user_payload)

body_update_user = {
    "email": faker_data.get_random_email(),
    "lastName": faker_data.get_data()["last_name"],
    "firstName": faker_data.get_data()["first"],
    "middleName": faker_data.get_data()["middle"],
}

update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    json=body_update_user,
    headers=update_user_payload,
)
update_user_response_data = update_user_response.json()

print("New body user:", update_user_response_data)
print("Final response status code", update_user_response.status_code)
