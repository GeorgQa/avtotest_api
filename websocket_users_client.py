import asyncio

import websockets


async def client():
    url_user = "ws://localhost:8765"
    async with websockets.connect(url_user) as websocket:
        messages = "Привет, сервер!"
        await websocket.send(messages)
        print(f"Отправка: {messages}")

        for j in range(5):
            response = await websocket.recv()
            print(response)


asyncio.run(client())
