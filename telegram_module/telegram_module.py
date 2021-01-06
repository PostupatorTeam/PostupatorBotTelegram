from typing import Tuple, List, Dict
from models.Program.interface.Program import Program
from middle_module import middle_module
from telegram_module.models.models_storage import Student
from telegram_module import bot_handler


def create_user(studentData: Student) -> Dict[str, List[Tuple[Program, int]]]:
    return middle_module.create_user(studentData)
    # С помощью опроса получаем информацию и создаем класс Student
    # Обрабатывая исключения, отправляем запрос на middle модуль
    # Ответ просто распарсиваем и выводим инфу пользователю
    # Здесь же пишем логи


def edit_user():
    # С помощью опроса получаем информацию и создаем класс Student
    # Обрабатывая исключения, отправляем запрос на middle модуль
    # Ответ просто распарсиваем и выводим инфу пользователю
    # Здесь же пишем логи
    pass


def get_info(userid: str) -> Dict[str, List[Tuple[Program, int]]]:
    return middle_module.get_info(userid)
    # Обрабатывая исключения, отправляем id на middle модуль
    # Распарсиваем полученную инфу
    # Здесь же пишем логи


def add_notifications(userid: str):
    middle_module.add_notifications(userid)
    # Обрабатывая исключения, отправляем id на middle модуль
    # Здесь же пишем логи
    pass


def remove_notifications(userid: str):
    middle_module.remove_notifications(userid)
    # Обрабатывая исключения, отправляем id на middle модуль
    # Здесь же пишем логи
    pass


def notify(userid: str, positions: Dict[str, List[Tuple[Program, int]]]):
    bot_handler.notify(userid, positions)
    # В чат с соответствующим id отправляем нужную инфу
    # Здесь же пишем логи
