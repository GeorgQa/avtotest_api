import socket


def server_for_user():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(10)
    messages_history = []
    print("Сервер запущен и ждет подключения...")

    while True:
        client_socket_from_user, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        message_data = client_socket_from_user.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {message_data}")

        client_socket_from_user.send("\n".join(messages_history).encode())
        messages_history.append(message_data)

        client_socket_from_user.close()
        print(f"История сообщений {messages_history}")

if __name__ == '__main__':
    server_for_user()