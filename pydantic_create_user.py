import uuid

from pydantic import BaseModel, EmailStr, Field, constr

"""
Модель данных пользователя

:return Готовая модель пользователя
"""


class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: constr(min_length=1, max_length=250) = EmailStr
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


"""
Модель запроса на создание пользователя

:return Готовая модель для запроса на создание пользователя
"""


class CreateUserRequestSchema(BaseModel):
    email: constr(min_length=1, max_length=250) = EmailStr
    password: constr(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


"""
Модель на получение ответа с данными созданного пользователя

:return Модель ответа созданного пользователя
"""


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
