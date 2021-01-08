import logging
from typing import List
from psycopg2._psycopg import InternalError

from src.main.database_module.database.get_connection import get_connection
from src.main.database_module.database.sql_scripts import insert_main_table, insert_spbu_table, insert_ranepa_table, \
    insert_etu_table, get_info_by_id, get_universities, delete_by_id, get_info_by_id_and_notifications, \
    set_notifications, get_all_users_with_notifications, get_user_from_ranepa_table, \
    get_user_from_spbu_table, get_user_from_etu_table, set_place_in_ranepa_table, set_place_in_spbu_table, \
    set_place_in_etu_table
from src.main.models.ConcreteUniversityStudent.implementations.EtuStudent import EtuStudent
from src.main.models.ConcreteUniversityStudent.implementations.RanepaStudent import RanepaStudent
from src.main.models.ConcreteUniversityStudent.implementations.SpbuStudent import SpbuStudent
from src.main.models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from src.main.models.Program.implementations.EtuProgram import EtuProgram
from src.main.models.Program.implementations.RanepaProgram import RanepaProgram
from src.main.models.Program.implementations.SpbuProgram import SpbuProgram


def create(concrete_students: List[ConcreteUniversityStudent]):
    connection = get_connection()
    cursor = connection.cursor()

    for student in concrete_students:
        if type(student) is SpbuStudent:
            cursor.execute(insert_main_table(student.userid, student.name, student.surname, student.lastname, "СПБГУ"))
            connection.commit()

            for program in student.programs:
                cursor.execute(insert_spbu_table(student.userid, program[0].educational_form, program[0].pay_form,
                                                 program[0].program, program[1]))
                connection.commit()
        elif type(student) is RanepaStudent:
            cursor.execute(insert_main_table(student.userid, student.name, student.surname, student.lastname,
                                             "РАНХИГС"))
            connection.commit()

            for program in student.programs:
                cursor.execute(insert_ranepa_table(student.userid, program[0].departament, program[0].approval,
                                                   program[0].form, program[0].program, program[1]))
                connection.commit()
        elif type(student) is EtuStudent:
            cursor.execute(insert_main_table(student.userid, student.name, student.surname, student.lastname, "ЛЭТИ"))
            connection.commit()

            for program in student.programs:
                cursor.execute(insert_etu_table(student.userid, program[0].form, program[0].program, program[1]))
                connection.commit()

    connection.close()


def create_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    if check_if_user_is_exists(concrete_students[0].userid):
        return False

    create(concrete_students)
    return True


def edit_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(get_universities(concrete_students[0].userid))
    connection.commit()

    universities = cursor.fetchall()

    if len(universities) == 0:
        connection.close()
        return False

    cursor.execute(delete_by_id("main_table", concrete_students[0].userid))
    connection.commit()

    for university in universities:
        if university[0] == "РАНХИГС":
            cursor.execute(delete_by_id("ranepa_table", concrete_students[0].userid))
        elif university[0] == "СПБГУ":
            cursor.execute(delete_by_id("spbu_table", concrete_students[0].userid))
        elif university[0] == "ЛЭТИ":
            cursor.execute(delete_by_id("etu_table", concrete_students[0].userid))

        connection.commit()

    connection.close()

    create(concrete_students)

    return True


def get_info(userid: str) -> List[ConcreteUniversityStudent]:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(get_info_by_id("main_table", userid))
    connection.commit()

    result = list()
    for student_data in cursor.fetchall():
        if student_data[4] == "РАНХИГС":
            cursor.execute(get_info_by_id("ranepa_table", userid))
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((RanepaProgram(program_data[1], program_data[2], program_data[3], program_data[4]),
                                 program_data[5]))

            result.append(RanepaStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        elif student_data[4] == "СПБГУ":
            cursor.execute(get_info_by_id("spbu_table", userid))
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((SpbuProgram(program_data[1], program_data[2], program_data[3]), program_data[4]))

            result.append(SpbuStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        elif student_data[4] == "ЛЭТИ":
            cursor.execute(get_info_by_id("etu_table", userid))
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((EtuProgram(program_data[1], program_data[2]), program_data[3]))

            result.append(EtuStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))

    connection.close()

    if len(result) == 0:
        message = \
            f"Failure to find student with this userid in database was detecting in database_module/get_info."
        logging.warning(message)
        message = \
            f"Не удалось найти абитуриента с такими данными (Возможно, Вы еще не зарегистрированы)."
        raise InternalError(message)

    return result


def add_notifications(userid: str) -> bool:
    if not check_if_user_is_exists(userid):
        message = \
            f"Failure to find student with this userid in database was detecting in database_module/add_notifications."
        logging.warning(message)
        message = \
            f"Не удалось найти абитуриента с такими данными (Возможно, Вы еще не зарегистрированы)."
        raise InternalError(message)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(get_info_by_id_and_notifications(userid, "false"))
    connection.commit()
    result = len(cursor.fetchall()) != 0

    cursor.execute(set_notifications(userid, "true"))
    connection.commit()
    connection.close()

    return result


def remove_notifications(userid: str) -> bool:
    if not check_if_user_is_exists(userid):
        message = \
            f"Failure to find student with this userid in database was detecting in " \
            f"database_module/remove_notifications. "
        logging.warning(message)
        message = \
            f"Не удалось найти абитуриента с такими данными (Возможно, Вы еще не зарегистрированы)."
        raise InternalError(message)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(get_info_by_id_and_notifications(userid, "true"))
    connection.commit()
    result = len(cursor.fetchall()) != 0

    cursor.execute(set_notifications(userid, "false"))
    connection.commit()
    connection.close()

    return result


def get_all_with_notifications() -> List[ConcreteUniversityStudent]:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(get_all_users_with_notifications())
    connection.commit()

    result = list()
    for student_data in cursor.fetchall():
        if student_data[4] == "РАНХИГС":
            cursor.execute(get_info_by_id("ranepa_table", student_data.userid))
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((RanepaProgram(program_data[1], program_data[2], program_data[3], program_data[4]),
                                 program_data[5]))

            result.append(RanepaStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        elif student_data[4] == "СПБГУ":
            cursor.execute(get_info_by_id("spbu_table", student_data.userid))
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((SpbuProgram(program_data[1], program_data[2], program_data[3]), program_data[4]))

            result.append(SpbuStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        elif student_data[4] == "ЛЭТИ":
            cursor.execute(get_info_by_id("etu_table", student_data.userid))
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((EtuProgram(program_data[1], program_data[2]), program_data[3]))

            result.append(EtuStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))

    connection.close()

    return result


def update(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    connection = get_connection()
    cursor = connection.cursor()

    result = True

    for student in concrete_students:
        if type(student) is RanepaStudent:
            for program in student.programs:
                cursor.execute(get_user_from_ranepa_table(student.userid, program[0].departament, program[0].approval,
                                                          program[0].form, program[0].program))
                connection.commit()

                if len(cursor.fetchall()) == 0:
                    result = False

                cursor.execute(set_place_in_ranepa_table(student.userid, program[0].departament, program[0].approval,
                                                         program[0].form, program[0].program, program[1]))
                connection.commit()
        elif type(student) is SpbuStudent:
            for program in student.programs:
                cursor.execute(get_user_from_spbu_table(student.userid, program[0].educational_form,
                                                        program[0].pay_form, program[0].program))
                connection.commit()

                if len(cursor.fetchall()) == 0:
                    result = False

                cursor.execute(set_place_in_spbu_table(student.userid, program[0].educational_form, program[0].pay_form,
                                                       program[0].program, program[1]))
                connection.commit()
        elif type(student) is EtuStudent:
            for program in student.programs:
                cursor.execute(get_user_from_etu_table(student.userid, program[0].form, program[0].program))
                connection.commit()

                if len(cursor.fetchall()) == 0:
                    result = False

                cursor.execute(set_place_in_etu_table(student.userid, program[0].form, program[0].program, program[1]))
                connection.commit()

    return result


def check_if_user_is_exists(userid: str) -> bool:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(get_info_by_id("main_table", userid))
    connection.commit()

    result = cursor.fetchall()

    connection.close()

    return len(result) != 0
