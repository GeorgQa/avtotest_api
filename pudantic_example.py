
from pydantic import BaseModel, Field



class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel, strict=True):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = Field(validation_alias='isActive')

user_data = {
    "id": 1,
    "email": "test_test@example.com",
    "address": {
    "city":"World",
    "zip_code": "232323"
    },
    "name": "Alice",
    "isActive": True
}

user = User.model_validate(user_data)
print(user)



{
  "type": "object",
  "properties": {
    "username": { "type": "string", "minLength": 5, "maxLength": 15}
    },
    "required": ["username"]
}