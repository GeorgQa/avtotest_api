from pydantic import BaseModel, Field


class LoginRequestSchema(BaseModel):
    """
    Модель запроса на авторизацию
    """

    email: str
    password: str


class TokenSchema(BaseModel):
    """
    Модель сущности токена
    """

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """
    Модель ответа запрсоса на авторизацию
    """

    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Модель запроса на получение refresh токена
    """

    refresh_token: str = Field(alias="refreshToken")
