
from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")


user = User(
    id= 678,
    name="Alice",
    email="test@test.com",
    isActive=False,
)
print(user.model_dump())
print(user.model_dump_json())


