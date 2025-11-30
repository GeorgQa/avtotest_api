from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from tools import faker_data

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=faker_data.fake_en.email(),
    password=faker_data.fake_en.password(),
    last_name=faker_data.fake_en.last_name(),
    first_name=faker_data.fake_en.first_name(),
    middle_name=faker_data.fake_en.middle_name(),
)


create_user_response = public_users_client.create_user(create_user_request)
print("Create user data:", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=f"{create_user_request.email}", password=f"{create_user_request.password}"
)

print("auth_user:", authentication_user)

private_users_client = get_private_users_client(authentication_user)
print("private", private_users_client)

get_user_response = private_users_client.get_user(create_user_response.user.id)
print("Get user data:", get_user_response)
