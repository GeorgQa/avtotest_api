from faker import Faker

fake = Faker("ru_RU")


data = {
    "name": fake.first_name(),
    "email": fake.email(),
    "age": fake.random_int(min=19, max=30),
}
print(data)
