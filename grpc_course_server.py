from concurrent import futures

import grpc

import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        print("Получен запрос")
        return course_service_pb2.GetCousesResponse(
            course_id="api-course",
            title="Автотесты API",
            descriptions="Будем изучать написание API автотестов",
        )


def course_serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=11))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Grpc сервер запущен на порту 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    course_serve()
