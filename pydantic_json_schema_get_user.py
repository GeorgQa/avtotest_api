import jsonschema

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools import faker_data

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=faker_data.get_random_email(),
    password=faker_data.get_data()["password"],
    last_name=faker_data.get_data()["last_name"],
    first_name=faker_data.get_data()["first"],
    middle_name=faker_data.get_data()["middle"],
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=f"{create_user_request.email}", password=f"{create_user_request.password}"
)

private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()

jsonschema.validate(instance=get_user_response.json(), schema=get_user_response_schema)
