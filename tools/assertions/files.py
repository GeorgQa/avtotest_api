import httpx

from clients.files.file_schema import FileSchema, CreateFileRequestSchema, CreateFileResponseSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal


def assert_files(actual: FileSchema, expected: FileSchema):
    """
      Проверяет, что фактиечские данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла (полученные из API).
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")


def assert_create_file_response(request:CreateFileRequestSchema,response:CreateFileResponseSchema):
    """
    Проверяем, что ответ на создание файла соответсвует запросу.

    :param request: Исходный запрос на создание файла
    :param response: Ответ API с данными созданного фалйа
    :raise: Asserton Error: Если хотя бы одно поле не совпадает
    """
    #Формируем ожидаемую ссылка на файл
    expected_url = str(response.file.url)

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory,  "directory")


def assert_file_is_accessible(url: str):
    """
    Проверяет, что файл доступен по указанному URL.

    :param url: Ссылка на файл.
    :raises AssertionError: Если файл не доступен.
    """
    response = httpx.get(url)
    assert response.status_code == 200, f"Файл недоступен по URL: {url}"

def assert_file(actual:FileSchema, expected:FileSchema):
    """
    Проверяем, что фактические данные файла соответствют ожидаемых

    :param actual: Фактические данные файла
    :param expected: Ожидаемые данные файла
    :raise: AssertinonError: Если хотя бы одно поле не совпало
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")


def assert_get_file_response(get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    """
    Прооверяем получнный ответ на получение файла соотвестиует ответу на его создание

    :param get_file_response: Ответ API при созданеиданных файла
    :param create_file_response: Ответ API на создание файла
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_file(get_file_response.file, create_file_response.file)