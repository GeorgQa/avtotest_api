from clients.files.file_schema import FileSchema
from tools.assertions.base import assert_equal


def assert_files(actual: FileSchema, expected: FileSchema):
    """
      Проверяет, что фактиечские данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла (полученные из API).
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")
