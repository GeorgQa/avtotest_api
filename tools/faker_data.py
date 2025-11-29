from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерируем случайный текст

        :return: Случайный текст
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерируем случайный uuid

        :return: Случайный uuid4
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерируем случайный email

        :return: Генерируем случайный email
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генерируем случайное предложение

        :return: Случайное предложение
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерируем случайный пароль

        :return: Случайный пароль
        """
        return self.faker.password()

    def first_name(self) -> str:
        """
        Генерируем случайное имя

        :return: Случайное имя
        """
        return self.faker.first_name()

    def last_name(self) -> str:
        """
        Генерируем случайную фамилию

        :return: Случайная фамилия
        """
        return self.faker.last_name()

    def middle_name(self) -> str:
        """
        Генерируем случайное отчество

        :return: случайное отчество
        """
        return self.faker.first_name()  # ← возможно, ошибка: должно быть отчество?

    def estimated_time(self) -> str:
        """
        Генерируем случайное время

        :return: Случайное время
        """
        return f"{self.integer(start=1, end=10)}"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерируем случайное число

        :param start: Начало диапазона
        :param end: Конец диапазона
        :return: Генерируем случайное число
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерируем максимальный балл

        :return: Случайный балл от 50 до 100
        """
        return self.integer(start=50, end=100)

    def min_score(self) -> int:
        """
        Генерируем минимальный балл

        :return: Случайный балл от 10 до 30
        """
        return self.integer(start=10, end=30)


fake_en = Fake("en_US")
fake_ru = Fake("ru_RU")

fake = Fake("en_US")