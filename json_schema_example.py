import jsonschema

data = {
    "name": "Ivan",
    "age": 30,
    "numbers": [1, 2, 3],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "numbers": {"type": "array", "items": {"type": "number"}},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"}
            }
        }
    },
    "required": ["name"]
}
try:
    jsonschema.validate(instance=data, schema=schema)
    print("схема соответствует данным")
except ValueError as e:
    print(f"схема не соответствует данным: {e.message}")



schema_work = {
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "age": {"type": "number"}
  },
  "required": ["name"]
}

data_work = {
  "name": "John Doe",
  "age": 30
}


try:
    jsonschema.validate(instance=data_work, schema=schema_work)
    print("схема соответствует данным")
except ValueError as e:
    print(f"схема не соответствует данным: {e.message}")
