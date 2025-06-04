import httpx
from tools import faker_data

create_user_payload = {
    "email": faker_data.get_random_email(),
    "password": faker_data.get_data()['password'],
    "lastName": faker_data.get_data()['last_name'],
    "firstName": faker_data.get_data()['first'],
    "middleName": faker_data.get_data()['middle']
}

print(create_user_payload["email"])
print(create_user_payload["lastName"])
print(create_user_payload["firstName"])
print(create_user_payload["middleName"])


create_user_response = httpx.post("http://localhost:8000/api/v1/users", json= create_user_payload)
create_user_response_data = create_user_response.json()


login_payload = {
    "email": create_user_payload['email'],
    "password":create_user_payload['password']
}


login_response =httpx.post("http://localhost:8000/api/v1/authentication/login", json= login_payload)
response_login_data = login_response.json()

get_user_headers = {
    "Authorization": f"Bearer {response_login_data['token']['accessToken']}"
}

get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", headers= get_user_headers)

print(get_user_response.json())
print(get_user_response.status_code)
print(get_user_response.headers)
