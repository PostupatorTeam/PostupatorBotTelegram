import logging
from typing import Dict, Tuple, List
from psycopg2 import InternalError
from mapping_module.mapping_module import map_to_concrete_university_students, map_to_student
from models import Student
from database_module import database_module
from models.ConcreteUniversityStudent.implementations.EtuStudent import EtuStudent
from models.ConcreteUniversityStudent.implementations.RanepaStudent import RanepaStudent
from models.ConcreteUniversityStudent.implementations.SpbuStudent import SpbuStudent
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from models.Program.interface.Program import Program


database_module = database_module


def send_notifications() -> Dict[str, Dict[str, List[Tuple[Program, int]]]]:
    concrete_students = database_module.get_all_with_notifications()

    unique_students = dict()
    students = list()

    for concrete_student in concrete_students:
        if concrete_student.userid in unique_students.keys():
            unique_students[concrete_student.userid].append(concrete_student)
        else:
            unique_students[concrete_student.userid] = [concrete_student]

    for unique_student_info in unique_students.values():
        students.append(map_to_student(unique_student_info))

    current_info = dict()

    for student in students:
        cur = map_to_concrete_university_students(student)
        current_info[student.userid] = cur

        if not database_module.update(cur):
            logging.warning("Failure to update database was detected in middle_module/send_notifications.")

    result = dict()

    for info in current_info.items():
        info[1].sort(key=lambda item: item.userid)
        unique_students[info[0]].sort(key=lambda item: item.userid)

        current_result = list()

        for i in range(0, len(info[1])):
            if info[1][i] != unique_students[info[0]][i]:
                current_result.append(info[1][i])

        result[info[1][0].userid] = reformat_info(current_result)

    return result


def reformat_info(concrete_students: List[ConcreteUniversityStudent]) -> Dict[str, List[Tuple[Program, int]]]:
    result = dict()

    for concrete_student in concrete_students:
        university_name = ""
        programs = concrete_student.programs

        if type(concrete_student) is SpbuStudent:
            university_name = "СПБГУ"
        elif type(concrete_student) is EtuStudent:
            university_name = "ЛЭТИ"
        elif type(concrete_student) is RanepaStudent:
            university_name = "РАНХИГС"

        result[university_name] = programs

    return result


def create_user(student: Student) -> Dict[str, List[Tuple[Program, int]]]:
    concrete_students = map_to_concrete_university_students(student)

    if not database_module.create_user(concrete_students):
        logging.warning("Trying to create an existing user was detecting in middle module.")
        raise InternalError("Пользователь c такими данными уже существует.")

    return reformat_info(concrete_students)


def edit_user(student: Student) -> Dict[str, List[Tuple[Program, int]]]:
    concrete_students = map_to_concrete_university_students(student)

    if not database_module.edit_user(concrete_students):
        logging.warning("Trying to edit a non-existent user was detecting in middle module.")
        raise InternalError("Пользователь с такими данными не существует.")

    return reformat_info(concrete_students)


def get_info(userid: str) -> Dict[str, List[Tuple[Program, int]]]:
    student = map_to_student(database_module.get_info(userid))

    concrete_students = map_to_concrete_university_students(student)

    if not database_module.update(concrete_students):
        logging.warning("Failure to update database was detected in middle_module/get_info.")

    return reformat_info(concrete_students)


def add_notifications(userid: str) -> bool:
    return database_module.add_notifications(userid)


def remove_notifications(userid: str) -> bool:
    return database_module.remove_notifications(userid)


def notify():
    # Как-то по умному создаем отдельный поток и вызываем функцию notifications
    # Также не забываем вызвать метод telegram
    pass
