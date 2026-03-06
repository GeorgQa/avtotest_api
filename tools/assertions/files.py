import allure
import httpx

from clients.error_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema

from clients.files.file_schema import FileSchema, CreateFileRequestSchema, CreateFileResponseSchema, \
    GetFileResponseSchema
from config import settings
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from tools.loger import get_logger

logger= get_logger("FILES_ASSERTIONS")

@allure.step("Check files")
def assert_files(actual: FileSchema, expected: FileSchema):
    """
      Проверяет, что фактиечские данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла (полученные из API).
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Files check")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")

@allure.step("Check create file response")
def assert_create_file_response(request:CreateFileRequestSchema,response:CreateFileResponseSchema):
    """
    Проверяем, что ответ на создание файла соответсвует запросу.

    :param request: Исходный запрос на создание файла
    :param response: Ответ API с данными созданного фалйа
    :raise: Asserton Error: Если хотя бы одно поле не совпадает
    """
    logger.info("Check create file response")

    expected_url = f"{settings.http_client.client_url}/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory,  "directory")

@allure.step("Check file with correct Url")
def assert_file_is_accessible(url: str):
    """
    Проверяет, что файл доступен по указанному URL.

    :param url: Ссылка на файл.
    :raises AssertionError: Если файл не доступен.
    """
    logger.info("Check file is accessible")
    response = httpx.get(url)
    assert response.status_code == 200, f"Файл недоступен по URL: {url}"

@allure.step("Check file ")
def assert_file(actual:FileSchema, expected:FileSchema):
    """
    Проверяем, что фактические данные файла соответствют ожидаемых

    :param actual: Фактические данные файла
    :param expected: Ожидаемые данные файла
    :raise: AssertinonError: Если хотя бы одно поле не совпало
    """
    logger.info("Check file")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")

@allure.step("Check get file response")
def assert_get_file_response(get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    """
    Прооверяем получнный ответ на получение файла соотвестиует ответу на его создание

    :param get_file_response: Ответ API при созданеиданных файла
    :param create_file_response: Ответ API на создание файла
    :raises AssertionError: Если данные файла не совпадают.
    """
    logger.info("Check get  file response")
    assert_file(get_file_response.file, create_file_response.file)

@allure.step("Check create file response with empty filename")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty filename response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "filename"]  # Ошибка возникает в теле запроса, поле "filename".
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check create file response with empty directory")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty direstory response")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустая директория.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "directory"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check create file response with not found file")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    logger.info("Check create file with  with not found file")

    # Ожидаемое сообщение об ошибке, если файл не найден
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get file response with empty incorrect file id")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на получение файла с некорректным file_id соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check get file with incorrect file id  response")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                location=["path", "file_id"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)