import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for i in range(5):
            response = f"{i + 1 } Сообщение пользователя: {message}"
            await websocket.send(response)


async  def main():
    server = await websockets.serve(echo, host = "localhost", port= 8765)
    print("WebSocket сервер запущен ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())