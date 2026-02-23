from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import (
    PrivateUsersClient,
    get_private_users_client,
)
from clients.users.public_users_client import PublicUsersClient
from clients.users.user_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
)
from fixtures.users import UserFixture
from tools.assertions.base import assert_equal, assert_status_code
from tools.assertions.sсhema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.faker_data import fake


@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        """
        Тест создания нового юзера с разными параметрами доменов
        :param public_users_client - клиент для создания пользователей
        :param email - параметр домена для генерации почты
        """
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        response = public_users_client.create_user_api(request)

        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Проверка данных
        assert_create_user_response(request=request, response=response_data)

        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_user_and_get_it(
        self,
        public_users_client: PublicUsersClient,
        authentication_client: AuthenticationClient,
        function_user: UserFixture,
    ):
        """
        Тест проверки авторизации и получения данных пользователя.

        :param public_users_client: Клиент для взаимодействия с публичным API пользователей.
        :param authentication_client: Клиент для выполнения операций аутентификации.
        :param function_user: Фикстура, возвращающая данные созданного и авторизованного пользователя.

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

        get_response_data = CreateUserResponseSchema.model_validate_json(
            get_response.text
        )

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

    def test_get_user_me(
        self, private_users_client: PrivateUsersClient, function_user: UserFixture
    ):
        """
        Тест на получение данных авторизованного пользователя через /api/v1/users/me.

        Использует фикстуру private_users_client для автоматической аутентификации.
        Проверяет, что возвращённые данные совпадают с данными созданного пользователя.

        :param private_users_client: Авторизованный клиент для доступа к приватным эндпоинтам.
        :param function_user: Фикстура с данными созданного пользователя.
        """
        # Выполняем запрос к /api/v1/users/me
        response = private_users_client.get_user_me_api()

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

        # Парсим ответ
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        # Проверяем, что данные совпадают с ожидаемыми
        assert_get_user_response(response_data, function_user.response)

        # Валидация по json схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
