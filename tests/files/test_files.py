from http import HTTPStatus

import pytest

from clients.error_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.file_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from clients.files.files_client import FilesClient
from fixtures.files import FileFixture
from httpx_create_file import response_create_file
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_file_is_accessible, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.sсhema import validate_json_schema


@pytest.mark.regression
@pytest.mark.files
class TestFiles:
    def test_create_file(self, files_client:FilesClient):
        request = CreateFileRequestSchema(upload_file="C:/courses/autotest-api/testdata/files/image.png")
        response = files_client.create_file_api(request)
        expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_file_is_accessible(expected_url)

    def test_get_file(self, files_client:FilesClient, function_file:FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_file_with_empty_filename(self, files_client:FilesClient):
         request_create_file = CreateFileRequestSchema(filename="", upload_file="C:/courses/autotest-api/testdata/files/image.png")
         response_create_file= files_client.create_file_api(request=request_create_file)
         response_create_file_data = ValidationErrorResponseSchema.model_validate_json(response_create_file.text)

         #Проверка, что статус код 422 и валидация json схемы
         assert_status_code(response_create_file.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
         #Проверка что ответ соотвесвует ожидаемой валидационной ошибке
         assert_create_file_with_empty_filename_response(response_create_file_data)

         #Проверка струкутры JSON
         validate_json_schema(response_create_file.json(), response_create_file_data.model_json_schema())

    def test_create_file_with_empty_directory(self, files_client:FilesClient):
         request_create_file = CreateFileRequestSchema(directory="", upload_file="C:/courses/autotest-api/testdata/files/image.png")
         response_create_file= files_client.create_file_api(request=request_create_file)
         response_create_file_data = ValidationErrorResponseSchema.model_validate_json(response_create_file.text)

         #Проверка, что статус код 422 и валидация json схемы
         assert_status_code(response_create_file.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
         #Проверка что ответ соотвесвует ожидаемой валидационной ошибке
         assert_create_file_with_empty_directory_response(response_create_file_data)

         #Проверка струкутры JSON
         validate_json_schema(response_create_file.json(), response_create_file_data.model_json_schema())

    def test_delete_files(self, files_client : FilesClient , function_file: FileFixture):
        file_id = function_file.response.file.id
        delete_response = files_client.delete_file_api(file_id=file_id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(file_id=file_id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        """
        Тест проверяет обработку некорректного file_id при запросе файла.

        Проверяет, что API возвращает статус 422 и корректное сообщение валидационной ошибки,
        когда передается некорректный идентификатор файла (не UUID).
        """
        file_id = "incorrect-file-id"
        response = files_client.get_file_api(file_id=file_id)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_get_file_with_incorrect_file_id_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())