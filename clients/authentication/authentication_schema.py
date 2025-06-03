from pydantic import BaseModel, Field, HttpUrl


class LoginRequestSchema(BaseModel):
    email: str
    password: str

class TokenSchema(BaseModel):
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginResponseSchema(BaseModel):
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias="refreshToken")
