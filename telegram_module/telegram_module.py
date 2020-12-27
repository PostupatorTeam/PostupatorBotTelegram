from typing import Tuple, List
from models.Program.interface.Program import Program


def create_user():
    # С помощью опроса получаем информацию и создаем класс Student
    # Обрабатывая исключения, отправляем запрос на middle модуль
    # Ответ просто распарсиваем и выводим инфу пользователю
    # Здесь же пишем логи
    pass


def edit_user():
    # С помощью опроса получаем информацию и создаем класс Student
    # Обрабатывая исключения, отправляем запрос на middle модуль
    # Ответ просто распарсиваем и выводим инфу пользователю
    # Здесь же пишем логи
    pass


def get_info():
    # Обрабатывая исключения, отправляем id на middle модуль
    # Распарсиваем полученную инфу
    # Здесь же пишем логи
    pass


def add_notifications():
    # Обрабатывая исключения, отправляем id на middle модуль
    # Здесь же пишем логи
    pass


def remove_notifications():
    # Обрабатывая исключения, отправляем id на middle модуль
    # Здесь же пишем логи
    pass


def notify(userid: str, positions: List[Tuple[Program, int]]):
    # В чат с соответствующим id отправляем нужную инфу
    # Здесь же пишем логи
    pass
