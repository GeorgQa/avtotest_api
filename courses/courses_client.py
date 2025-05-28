from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

class GetCoursesQueryDict(TypedDict):
    """
    Описание стурктуры запроса на получение списка курсов
    """
    userId: str

class RequestCreateCoures(TypedDict):
    """
    Описание структуры для создания курсов
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCoursesRequest(TypedDict):
    """
    Описнаие структуры для обновления курса
    """
    title: str | None
    maxScore:int | None
    minScore:int | None
    description:str | None
    estimatedTime:str | None

class CorsesClient(APIClient):
    """
    Клиент  для работы с api
    """
    def get_all_courses_for_user(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params= query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по course_id

        :param course_id: Уникальное значение для курса
        :return: Ответ от севера в виде оъекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request:UpdateCoursesRequest) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса

        :param course_id: Индефикатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request:RequestCreateCoures) -> Response:
        """
        Метод для создания курса

        :param request: Словарь в котором передается body для создания курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses" , json= request)