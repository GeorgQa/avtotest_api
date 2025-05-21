
import grpc
import course_service_pb2
import course_service_pb2_grpc



channel_courses = grpc.insecure_channel("localhost:50051")
stub = course_service_pb2_grpc.CourseServiceStub(channel_courses)

response = stub.GetCourse(course_service_pb2.GetCoursesRequest(course_id="api-course"))
print(response)