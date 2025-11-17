 from typing import Any

 from jsonschema import validate
 from jsonschema.validators import Draft202012Validator


 def vaildate_json_schema(instanse: Any, schema: dict) -> None:
     """
     Функция проверяет валидность JSON-объекта по указанному схеме.
     :param instanse: JSON-объект для проверки
     :param schema: JSON-схема для проверки
     :raise jsonschema.exceptions.ValidationError: Если JSON-объект не соответствует схеме
     """
     validate(
         schema=schema,
         instance=instanse,
         cls=Draft202012Validator.FORMAT_CHECKER
     )