from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import (LoginRequestSchema,
                                                          LoginResponseSchema)
from clients.users.public_users_client import PublicUsersClient
from clients.users.user_schema import CreateUserRequestSchema
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.sсhema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
def test_login(
    public_users_client: PublicUsersClient,
    authentication_client: AuthenticationClient,
    function_user: UserFixture,
):
    """
    Тест успешной авторизации пользователя в системе.
     Описание шагов:
    1. Создаётся новый пользователь.
    2. Выполняется запрос на авторизацию.
    3. Проверяется статус-код ответа.
    4. Проверяется структура и содержание токена в ответе.
    """
    request = LoginRequestSchema(
        email=function_user.email, password=function_user.password
    )

    response = authentication_client.login_api(request)

    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())
