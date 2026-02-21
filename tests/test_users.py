from http import HTTPStatus

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal, assert_status_code
from tools.assertions.sсhema import validate_json_schema
from tools.assertions.users import assert_create_user_response


def test_create_user():
    """
    Тест создания нового юзера
    """
    public_users_client = get_public_users_client()
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    # Валидация схемы body ответа
    response_data = CreateUserResponseSchema.model_validate_json(response.text)
    # Проверка статус кода
    assert_status_code(response.status_code, HTTPStatus.OK)
    # Проверка данных
    assert_create_user_response(request=request, response=response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())


def test_create_user_and_get_it():
    """
    Тест для проверки авторизации и получения информации о новом пользовательтеле
    """

    public_client = get_public_users_client()
    create_request = CreateUserRequestSchema()
    create_response = public_client.create_user_api(create_request)
    assert_status_code(create_response.status_code, HTTPStatus.OK)
    create_response_data = CreateUserResponseSchema.model_validate_json(
        create_response.text
    )

    assert_create_user_response(request=create_request, response=create_response_data)
    create_response_data = CreateUserResponseSchema.model_validate_json(
        create_response.text
    )
    assert_status_code(create_response.status_code, HTTPStatus.OK)

    user_id = create_response_data.user.id

    auth_user = AuthenticationUserSchema(
        email=create_request.email, password=create_request.password
    )

    private_client = get_private_users_client(auth_user)

    get_response = private_client.get_user_api(user_id)
    assert_status_code(get_response.status_code, HTTPStatus.OK)

    get_response_data = CreateUserResponseSchema.model_validate_json(get_response.text)

    assert_equal(get_response_data.user.id, user_id, "id")
    assert_equal(get_response_data.user.email, create_request.email, "email")
    assert_equal(
        get_response_data.user.first_name, create_request.first_name, "first name"
    )
    assert_equal(
        get_response_data.user.last_name, create_request.last_name, "last name"
    )
    assert_equal(
        get_response_data.user.middle_name, create_request.middle_name, "middle name"
    )
