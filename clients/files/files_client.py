from importlib.metadata import files
from typing import TypedDict

from httpx import URL, Response

from clients.api_client import APIClient


class CreateFilesRequestDict(TypedDict):
    """
    Описание тела запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """
    Климент для работы с api  /api/v1/files/
    """
    def create_files_api(self, request:CreateFilesRequestDict) -> Response:
        """
        метод для создания файла

        :param request: словарь содержаший названия файла, директорию жля сохранения, путь до файла
        :return: Отвтет от сервера в виде обьекта httpx.Resposne
        """
        return self.post(
            "/api/v1/files/",
            data=request,
            #Путь будет на уровне словаря определяться т.е. он не захардкожен
            files={"upload file": open(request['upload_file'], 'rb')}
        )

    def get_files_api(self, file_id:str) -> Response:
        """
        Метод для получения файла

        :param file_id: укникальный индификатор файла
        :return: Ответа от сервера в виде объекта httpx.Response
        """
        return self.client.get(f"/api/v1/files/{file_id}")

    def delete_files_api(self, file_id:str) -> Response:
        """
        Метод, который удаляет файл

        :param file_id: уникальный индификатор файла
        :return: Ответ от сервера в виде объекта httx.Response
        """
        return  self.client.delete(f"/api/v1/files/{file_id}")