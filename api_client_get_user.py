from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools import faker_data

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=faker_data.get_random_email(),
    password=faker_data.get_data()['password'],
    lastName=faker_data.get_data()['last_name'],
    firstName=faker_data.get_data()['first'],
    middleName= faker_data.get_data()['middle']
)

create_user_response = public_users_client.create_user(create_user_request)
print("Create user data:", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=f"{create_user_request['email']}",
    password=f"{create_user_request['password']}"
)

print("auth_user:", authentication_user)

private_users_client = get_private_users_client(authentication_user)
print("private", private_users_client)

get_user_response =  private_users_client.get_user(create_user_response['user']['id'])
print("Get user data:", get_user_response)