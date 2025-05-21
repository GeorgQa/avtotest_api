# import grpc
#
# from faker import Faker
# import course_service_pb2
# import course_service_pb2_grpc
#
# fake = Faker()
#
# # Генерируем UUID
# fake_uuid = fake.uuid4()
# print(f"Сгенерированный UUID: {fake_uuid}")
#
# channel_courses = grpc.insecure_channel("localhost:50051")
# stub = course_service_pb2_grpc.CourseServiceStub(channel_courses)
#
# response = stub.GetCourse(course_service_pb2.GetCoursesRequest(course_id= f"{fake_uuid}"))


import grpc
import course_service_pb2
import course_service_pb2_grpc



channel_courses = grpc.insecure_channel("localhost:50051")
stub = course_service_pb2_grpc.CourseServiceStub(channel_courses)

response = stub.GetCourse(course_service_pb2.GetCoursesRequest(course_id="api-course"))
print(response)