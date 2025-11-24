import httpx

#
# headers ={"Authorization": "Bearer my_secret_token"}
# response_get = httpx.get("https://jsonplaceholder.typicode.com/todos/", headers=headers)
#
#
# print(response_get.status_code)
# print(response_get.request.headers)
# print(response_get.json())
#
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
#
# response_post= httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
# print(response_post.status_code)
# print(response_post.json())
#
# params={"userID":1}
# response_user_1 = httpx.get("https://jsonplaceholder.typicode.com/todos/", params=params)
#
# print(response_user_1.url)
# print(response_user_1.json())
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response_file = httpx.post("https://jsonplaceholder.typicode.com/todos/", files=files)
#
# print(response_file.json())
#

#
# with httpx.Client() as client:
#     response_1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response_2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response_1.json())
# print(response_2.json())
#
# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})

# #timeopth 503
# try:
#     response_client= client.get("https://jsonplaceholder.typicode.com/todos/invalide")
#     response_client.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса: {e}")


try:
    response_client = httpx.get("https://httpbin.org/delay/5", timeout=None)
    print(f"Запрос от клиента пришел успешно {response_client.json()}")
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
