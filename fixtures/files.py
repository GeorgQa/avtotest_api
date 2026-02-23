import pytest
from pydantic import BaseModel

from clients.files.file_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.files.files_client import get_files_client, FilesClient
from fixtures.users import UserFixture


# Модель для агрегации возвращаемых данных
class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

#Эта фикстура создает клиент FilesClient, который будет использоваться для работы с API загрузки файлов.
@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)

#Фикстура автоматически создает тестовый файл перед каждым тестом и возвращает информацию о нем
@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request=request)
    return FileFixture(request=request, response= response)