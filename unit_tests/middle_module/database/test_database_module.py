from typing import List
from psycopg2._psycopg import InternalError
from models.ConcreteUniversityStudent.implementations.EtuStudent import EtuStudent
from models.ConcreteUniversityStudent.implementations.RanepaStudent import RanepaStudent
from models.ConcreteUniversityStudent.implementations.SpbuStudent import SpbuStudent
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from models.Program.implementations.EtuProgram import EtuProgram
from models.Program.implementations.RanepaProgram import RanepaProgram
from models.Program.implementations.SpbuProgram import SpbuProgram


quantity_with_notifications = 0


def generate_spbu_student(userid: str, name: str, surname: str, lastname: str, quantity: int) -> SpbuStudent:
    programs = list()

    for i in range(0, quantity):
        programs.append((SpbuProgram(f"Example{i}", f"Example{i}", f"Example{i}"), i + 10))

    return SpbuStudent(userid, name, surname, lastname, programs)


def generate_ranepa_student(userid: str, name: str, surname: str, lastname: str, quantity: int) -> RanepaStudent:
    programs = list()

    for i in range(0, quantity):
        programs.append((RanepaProgram(f"Example{i}", f"Example{i}", f"Example{i}", f"Example{i}"), i + 5))

    return RanepaStudent(userid, name, surname, lastname, programs)


def generate_etu_student(userid: str, name: str, surname: str, lastname: str, quantity: int) -> EtuStudent:
    programs = list()

    for i in range(0, quantity):
        programs.append((EtuProgram(f"Example{i}", f"Example{i}"), i + 1))

    return EtuStudent(userid, name, surname, lastname, programs)


def create_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    return concrete_students[0].userid != "ExistingId"


def edit_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    return concrete_students[0].userid != "NotExistingId"


def get_info(userid: str) -> List[ConcreteUniversityStudent]:
    if userid == "NotExistingId":
        raise InternalError()

    if userid == "StudentWithNotExistingData":
        return [generate_ranepa_student(userid, "Notexistingname", "Notexistingsurname", "Notexistinglastname", 5)]

    if userid == "badrequest":
        return [EtuStudent(userid, "Name", "Surname", "Lastname", [(EtuProgram("Bad request", "Bad request"), 10)])]

    result = list()

    result.append(generate_spbu_student(userid, "Name", "Surname", "Lastname", 1))
    result.append(generate_etu_student(userid, "Name", "Surname", "Lastname", 2))
    result.append(generate_ranepa_student(userid, "Name", "Surname", "Lastname", 3))

    return result


def add_notifications(userid: str) -> bool:
    if userid == "NotExistingId":
        raise InternalError()

    return userid == "UserIdWithoutNotifications"


def remove_notifications(userid: str) -> bool:
    if userid == "NotExistingId":
        raise InternalError()

    return userid == "UserIdWithNotifications"


def get_all_with_notifications() -> List[ConcreteUniversityStudent]:
    result = list()

    for i in range(0, quantity_with_notifications):
        result.append(generate_spbu_student(f"userid{i}", f"Name{i}", f"Surname{i}", f"Lastname{i}", i + 1))
        if i % 2 == 0:
            result.append(generate_etu_student(f"userid{i}", f"Name{i}", f"Surname{i}", f"Lastname{i}", i + 1))
        if i % 3 == 0:
            result.append(generate_ranepa_student(f"userid{i}", f"Name{i}", f"Surname{i}", f"Lastname{i}", i + 1))

    return result


def update(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    return concrete_students[0].userid != "NotExistingId"


def check_if_user_is_exists(userid: str) -> bool:
    return userid == "existingUser"
