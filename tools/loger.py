import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    #Устанавиливаем уровень логирования Debug
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик, который будет выводить логи в консоль
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Устанавливае формат вывода сообщений
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)  # Применяем форматтер к обработчику

    logger.addHandler(handler)

    return logger