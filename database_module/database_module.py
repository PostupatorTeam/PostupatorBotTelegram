from typing import List
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent


def create_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    # Проверяем существование такого юзера(с таким фио в общ таблице)
    # Существует - возвращаем false
    # Нет - бежим по списку, определяем тип и если вуз еще не добавлен добавляем в общ таблицу
    # Добавляем в таблицу конкретного вуза
    pass


def edit_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    # Проверяем существование такого юзера(с таким фио в общ таблице)
    # Существует - удаляем старого из всех(проверяем, какие нужгы)
    # Бежим по списку, определяем тип и если вуз еще не добавлен добавляем
    # Возвращаем true
    # Если не существует - возвращаем false
    pass


def get_info(userid: str) -> List[ConcreteUniversityStudent]:
    # Проверяем существование такого юзера(с таким фио в общ таблице)
    # Не существует - бросаем исключение InternalError
    # Существует - по каждому вузу обращаемся в нужную таблицу и берем нужную инфу
    # Возвращаем полученные значения
    pass


def add_notifications(userid: str) -> bool:
    # Проверяем существование такого юзера(с таким фио в общ таблице)
    # Существовует - если есть оповещение - возвр false
    # Если нет - true и добавляем
    # Если не сущ - бросаем исключение InternalError
    pass


def remove_notifications(userid: str) -> bool:
    # Проверяем существование такого юзера(с таким фио в общ таблице)
    # Существовует - если есть оповещение - возвр true и удаляем
    # Если нет - false
    # Если не сущ - бросаем исключение InternalError
    pass


def get_all_with_notifications() -> List[ConcreteUniversityStudent]:
    # Бежим по общ таблице
    # Создаем лист пар фио вуз
    # Бежим по списку, получаем всю нужную инфу
    pass


def update(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    # Если какая то штука не найдена - возвращаем false
    # Иначе - бежим по студентам, определяем нужную таблицу и обноваляем нужную запись
    # Возвращаем true
    pass
