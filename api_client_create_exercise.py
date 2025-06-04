from clients.courses.course_schema import CreateCourseRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.file_schema import CreateFileRequestSchema
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from pydantic_create_user import CreateUserRequestSchema
from tools import faker_data

pyblic_users_client_for_exercise = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=faker_data.get_random_email(),
    password=faker_data.get_data()['password'],
    lastName=faker_data.get_data()['last_name'],
    firstName=faker_data.get_data()['first'],
    middleName= faker_data.get_data()['middle']
)
print("User data request:", create_user_request)
create_user_response = pyblic_users_client_for_exercise.create_user(create_user_request)
print("Create user data:", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

create_file_request =  CreateFileRequestSchema(
    filename='image.png',
    directory='courses',
    upload_file='testdata/files/file_2.png'
)
create_file_response= files_client.create_file(create_file_request)
print("Create File Data", create_file_response)

create_course_request = CreateCourseRequestSchema(
    title="Python",
    maxScore= 100,
    minScore= 10,
    description= "Python API course",
    estimatedTime="2 weeks",
    previewFileId= create_file_response.file.id,
    createdByUserId= create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print("Create Course Data:", create_course_response)

create_exercises_request = CreateExerciseRequestSchema(
    title="Тестовое задание",
    courseId= create_course_response.course.id,
    maxScore= 150,
    minScore= 1,
    orderIndex = 232323,
    description="Тест_тест",
    estimatedTime="2 days"
)

create_exercises_response = exercises_client.create_exercise(create_exercises_request)
print("Create Exercises Data:", create_exercises_response)

