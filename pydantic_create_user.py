import uuid

from pydantic import BaseModel,  EmailStr, Field


"""
Модель данных пользователя

:return Готовая модель пользователя
"""
class UserSchema(BaseModel):
    id: str = Field(default_factory= lambda : str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

"""
Модель запроса на создание пользователя

:return Готовая модель для запроса на создание пользователя
"""
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

"""
Модель на получение ответа с данными созданного пользователя

:return Модель созданного пользователя
"""
class CreateUserResponseSchema(BaseModel):
    user: UserSchema


