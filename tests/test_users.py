from http import HTTPStatus

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code, assert_equal
from tools.assertions.sсhema import validate_json_schema
from tools.assertions.users import assert_create_user_response


def test_create_user():
    public_users_client = get_public_users_client()
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    #Валидация схемы body ответа
    response_data =CreateUserResponseSchema.model_validate_json(response.text)
    #Проверка статус кода
    assert_status_code(response.status_code, HTTPStatus.OK)
    #Проверка данных
    assert_create_user_response(request= request, response=response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())


def test_get_user():
    # Шаг 1: Создаём пользователя
    public_client = get_public_users_client()
    create_request = CreateUserRequestSchema()

    create_response = public_client.create_user_api(create_request)
    # Проверка статус-кода
    assert_status_code(create_response.status_code, HTTPStatus.OK)
    # Парсим ответ
    create_response_data = CreateUserResponseSchema.model_validate_json(create_response.text)
    # Проверяем данные пользователя
    assert_create_user_response(request=create_request, response=create_response_data)

    #проверка статус-кода
    assert_status_code(create_response.status_code, HTTPStatus.OK)

    # Парсим ответ с помощью jsonschema
    create_response_data = CreateUserResponseSchema.model_validate_json(create_response.text)
    user_id = create_response_data.user.id

    # Шаг 2: Авторизуемся под созданным пользователем
    auth_user = AuthenticationUserSchema(
        email=create_request.email,
        password=create_request.password
    )

    private_client = get_private_users_client(auth_user)

    # Шаг 3: Получаем пользователя по ID
    get_response = private_client.get_user_api(user_id)
    #Проверяем статусу код при запросе на получение пользователя
    assert_status_code(get_response.status_code, HTTPStatus.OK)

    # Парсим ответ получения
    get_response_data = CreateUserResponseSchema.model_validate_json(get_response.text)

    # Шаг 4: Проверяем данные

    assert_equal(get_response_data.user.id,  user_id, 'id')
    assert_equal(get_response_data.user.email , create_request.email,'email')
    assert_equal(get_response_data.user.first_name, create_request.first_name,"first name")
    assert_equal(get_response_data.user.last_name, create_request.last_name,"last name")
    assert_equal(get_response_data.user.middle_name, create_request.middle_name,"middle name")