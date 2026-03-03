from http import HTTPStatus

import pytest

from clients.files.file_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from clients.files.files_client import FilesClient
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_file_is_accessible, assert_get_file_response
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
