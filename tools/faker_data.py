import time

from faker import Faker

fake = Faker("ru")


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


def get_data() -> dict:
    return {
        "last_name": fake.last_name(),
        "first": fake.first_name(),
        "middle": fake.middle_name(),
        "password": fake.uuid4(),
    }
