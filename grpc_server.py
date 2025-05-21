import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc


class UserServiceServiser(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f"Получен запрос к методу GetUser от пользователя {request.username}")
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username} ")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServiser(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Grpc сервер запущен на порту 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
