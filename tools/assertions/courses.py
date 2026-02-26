from clients.courses.course_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetIDCoursesRequestSchema, GetIDCoursesResponseSchema
from tools.assertions.base import assert_equal


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Проверяем, что обьект на нобновление курса соответсвует данным из запроса.

    :param request: Исходный запрос на обновление круса
    :param response: Ответ API с обноленными данными курса
    :raise AssertionError: Если хоть одно поле не совпало
    """
    if request.title is not None:
        assert_equal(response.course.title, request.title, "title")

    if request.max_score is not None:
        assert_equal(response.course.max_score, request.max_score, "max_score")

    if request.min_score is not None:
        assert_equal(response.course.min_score, request.min_score, "min_score")

    if request.description is not None:
        assert_equal(response.course.description, request.description, "description")

    if request.estimated_time is not None:
        assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")



def assert_get_id_course_response(request: UpdateCourseResponseSchema, response:GetIDCoursesResponseSchema):
    """
    Проверка ответа запроса на получение данных о курсе по его ID.

    :param request: Принимает ответ запроса на изменение данных курса
    :param response: Ответ запроса на получение данных по ID
    :return: Если хоть одно поле не совпало
    """
    assert_equal(response.course.title, request.course.title , "title" )
    assert_equal(response.course.max_score, request.course.max_score , "max_score" )
    assert_equal(response.course.min_score, request.course.min_score , "min_score" )
    assert_equal(response.course.description, request.course.description , "description" )
    assert_equal(response.course.estimated_time, request.course.estimated_time , "min_score" )



