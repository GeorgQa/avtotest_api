from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import (CreateUserRequestSchema,
                                       GetUserResponseSchema)
from tools import faker_data
from tools.assertions.sсhema import validate_json_schema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=faker_data.fake_en.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=f"{create_user_request.email}", password=f"{create_user_request.password}"
)

private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
