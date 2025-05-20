import json

escaped_json = "{\\\"pet\\\": {\\\"name\\\": \\\"Барсик\\\", \\\"type\\\": \\\"кот\\\", \\\"age\\\": 3, \\\"toys\\\": [\\\"мяч\\\", \\\"мышка\\\"]}}"

# Убираем лишние экранирования (заменяем \" на ")
unescaped_json = escaped_json.replace('\\"', '"')

# Парсим JSON
parsed_data = json.loads(unescaped_json)

# Достаем объект pet
pet = parsed_data["pet"]["toys"]

print(pet)