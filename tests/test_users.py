from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import (PublicUsersClient,
                                               get_public_users_client)
from clients.users.user_schema import (CreateUserRequestSchema,
                                       CreateUserResponseSchema)
from tests.conftest import UserFixture
from tools.assertions.base import assert_equal, assert_status_code
from tools.assertions.sсhema import validate_json_schema
from tools.assertions.users import assert_create_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    """
    Тест создания нового юзера
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)

    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверка данных
    assert_create_user_response(request=request, response=response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_create_user_and_get_it(
    public_users_client: PublicUsersClient,
    authentication_client: AuthenticationClient,
    function_user: UserFixture,
):
    """
    Тест для проверки авторизации и получения информации о новом пользовательтеле
    """

    assert_create_user_response(
        request=function_user.request, response=function_user.response
    )
    user_id = function_user.response.user.id

    authentication_client = AuthenticationUserSchema(
        email=function_user.request.email, password=function_user.request.password
    )

    private_client = get_private_users_client(authentication_client)

    get_response = private_client.get_user_api(user_id)
    assert_status_code(get_response.status_code, HTTPStatus.OK)

    get_response_data = CreateUserResponseSchema.model_validate_json(get_response.text)

    assert_equal(get_response_data.user.id, user_id, "id")
    assert_equal(
        get_response_data.user.email, function_user.response.user.email, "email"
    )
    assert_equal(
        get_response_data.user.first_name,
        function_user.response.user.first_name,
        "first name",
    )
    assert_equal(
        get_response_data.user.last_name,
        function_user.response.user.last_name,
        "last name",
    )
    assert_equal(
        get_response_data.user.middle_name,
        function_user.response.user.middle_name,
        "middle name",
    )
