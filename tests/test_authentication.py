from http import HTTPStatus

from clients.authentication.authentication import assert_login_response
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from tools.assertions.base import assert_status_code


def test_login_authentication():
    """
    Тест успешной авторизации пользователя в системе.
     Описание шагов:
    1. Создаётся новый пользователь.
    2. Выполняется запрос на авторизацию.
    3. Проверяется статус-код ответа.
    4. Проверяется структура и содержание токена в ответе.
    """

    public_client = get_public_users_client()
    create_user_request = CreateUserRequestSchema()

    public_client.create_user(create_user_request)

    auth_client = get_authentication_client()
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )

    login_response = auth_client.login_api(login_request)

    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

