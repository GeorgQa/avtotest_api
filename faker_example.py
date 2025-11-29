from  faker import Faker

fake = Faker("ru_RU")
#
# print(fake.name())
# print(fake.address())
# print(fake.email())

data = {
    "name": fake.first_name(),
    "email": fake.email(),
    "age": fake.random_int(min= 19, max=30)
}
print(data)