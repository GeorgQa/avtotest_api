import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl, computed_field
from pydantic.alias_generators import to_camel
from pydantic_core.core_schema import UrlSchema

"""
{
      "id": "string",
      "title": "string",
      "maxScore": 0,
      "minScore": 0,
      "description": "string",
      "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
      },
      "estimatedTime": "string",
      "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
      }
    }
"""


# Добавили модель FileSchema
class FaileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")
    first_name: str = Field(alias="firstName")

    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


try:
    file = FaileSchema(
        id="file_id", url="lesson", directory="dile.png", filename="couses"
    )
except ValueError as error:
    print(error)
    print(error.errors())


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(default="Playwright")
    max_score: int = Field(alias="maxScore", default=10000)
    min_score: int = Field(alias="minScore", default=10)
    description: str = Field(default="Playwright course")
    preview_file: FaileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")
    estimated_time: str = Field(default="estimatedTime")


course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    previewFile=FaileSchema(
        id="file_id",
        url="http://localhost:8000/docs#/courses/get_courses_view_api_v1_courses_get",
        directory="dile.png",
        filename="couses",
    ),
    minScore=10,
    createdByUser=UserSchema(
        id="2323",
        email="2323@gmail.com",
        lastName="Бонд",
        middleName="Иванович",
        firstName="Иван",
    ),
    description="Playwright",
    estimatedTime="1 week",
)

print("Course defalt model1", course_default_model)
print("Course defalt model2", course_default_model.model_dump(by_alias=True))


course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "createdByUser": {
        "id": "2323",
        "email": "2323@gmail.com",
        "lastName": "Бонд",
        "middleName": " Иванович",
        "firstName": "Сильвия",
    },
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
        "id": "file_id",
        "url": "https://stepik.org/lesson",
        "directory": "dile.png",
        "filename": "courses",
    },
    "description": "Playwright",
    "estimatedTime": "1 week",
}
course_dict = CourseSchema(**course_dict)
print("Course dict model", course_dict)


course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "createdByUser": {
       "id": "2323",
       "email":"2323@gmail.com",
       "lastName": "Бонд",
       "middleName": " Иванович",
       "firstName": "Сильвия"
        },
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
       "id":"file_id",
       "url":"https://stepik.org/lesson",
       "directory":"dile.png",
       "filename": "courses"
        },
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("Course JSON model:", course_json_model)
print(course_json_model.model_dump())
print(course_json_model.model_dump_json(by_alias=True))
