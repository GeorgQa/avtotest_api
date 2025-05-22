import asyncio

import websockets


async def client():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        messages = "Привет, сервер!"
        await websocket.send(messages)
        print(f"Отправка: {messages}")

        for j in range(5):
             response = await websocket.recv()
             print(f"Ответ от сервера:{response}")


asyncio.run(client())