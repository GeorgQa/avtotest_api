from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from tools.loger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")

@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Функция проверяет валидность JSON-объекта по указанному схеме.
    :param instance: JSON-объект для проверки
    :param schema: JSON-схема для проверки
    :raise jsonschema.exceptions.ValidationError: Если JSON-объект не соответствует схеме
    """
    logger.info("Validating JSON schema")
    validate(
        instance=instance,
        schema=schema,
        cls=Draft202012Validator,  # ← Правильный параметр
    )
