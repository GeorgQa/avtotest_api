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

print("Create_user", create_user_response_data)


login_payload = {
    "email": create_user_payload['email'],
    "password":create_user_payload['password']
}


login_response =httpx.post("http://localhost:8000/api/v1/authentication/login", json= login_payload)
response_login_data = login_response.json()

print("Login_data", response_login_data)


create_file_headers = {
    "authorization": f"Bearer {response_login_data['token']['accessToken']}"
}

response_create_file = httpx.post("http://localhost:8000/api/v1/files",
                                    data={"filename":"test.png",
                                          "directory": "directoria"},
                                    files={"upload_file": open('./testdata/files/file_2.png', 'rb')},
                                    headers=create_file_headers )
response_create_file_data = response_create_file.json()
print("Create file data:",response_create_file_data)
print(response_create_file.status_code)
print(response_create_file.headers)
