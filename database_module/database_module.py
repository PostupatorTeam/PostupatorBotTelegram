import logging
from typing import List
import psycopg2
from psycopg2._psycopg import InternalError
from models.ConcreteUniversityStudent.implementations.EtuStudent import EtuStudent
from models.ConcreteUniversityStudent.implementations.RanepaStudent import RanepaStudent
from models.ConcreteUniversityStudent.implementations.SpbuStudent import SpbuStudent
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from models.Program.implementations.EtuProgram import EtuProgram
from models.Program.implementations.RanepaProgram import RanepaProgram
from models.Program.implementations.SpbuProgram import SpbuProgram


def create_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                  host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT userid FROM main_table WHERE userid='{concrete_students[0].userid}'""")
    connection.commit()
    if len(cursor.fetchall()) != 0:
        connection.close()
        return False

    for student in concrete_students:
        if type(student) is SpbuStudent:
            # Здесь возможно строка неправильно перенесется
            cursor.execute(f"""INSERT INTO main_table(userid, name, surname, lastname, university_name, notifications) 
                            VALUES ('{student.userid}', 
                                    '{student.name}', 
                                    '{student.surname}', 
                                    '{student.lastname}', 
                                    'СПБГУ',
                                    false)""")
            connection.commit()

            for program in student.programs:
                # Здесь возможно строка неправильно перенесется
                cursor.execute(f"""INSERT INTO spbu_table(userid, educational_form, pay_form, program, place) 
                                VALUES ('{student.userid}', 
                                    '{program[0].educational_form}', 
                                    '{program[0].pay_form}', 
                                    '{program[0].program}', 
                                    {program[1]})""")
                connection.commit()
        elif type(student) is RanepaStudent:
            cursor.execute(f"""INSERT INTO main_table(userid, name, surname, lastname, university_name, notifications) 
                            VALUES ('{student.userid}', 
                                    '{student.name}', 
                                    '{student.surname}', 
                                    '{student.lastname}', 
                                    'РАНХИГС',
                                    false)""")
            connection.commit()

            for program in student.programs:
                cursor.execute(f"""INSERT INTO ranepa_table(userid, departament, approval, form, program, place) 
                                VALUES ('{student.userid}', 
                                        '{program[0].departament}', 
                                        '{program[0].approval}', 
                                        '{program[0].form}', 
                                        '{program[0].program}',
                                        {program[1]})""")
                connection.commit()
        else:
            cursor.execute(f"""INSERT INTO main_table(userid, name, surname, lastname, university_name, notifications) 
                                        VALUES ('{student.userid}', 
                                                '{student.name}', 
                                                '{student.surname}', 
                                                '{student.lastname}', 
                                                'ЛЭТИ',
                                                false)""")
            connection.commit()

            for program in student.programs:
                cursor.execute(f"""INSERT INTO ranepa_table(userid, form, program, place) 
                                                VALUES ('{student.userid}', 
                                                        '{program[0].form}', 
                                                        '{program[0].program}',
                                                        {program[1]})""")
                connection.commit()

    connection.close()
    return True


def edit_user(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                 host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT university_name FROM main_table WHERE userid='{concrete_students[0].userid}'""")
    connection.commit()

    universities = cursor.fetchall()
    if universities is None:  # Возможно пустой список
        connection.close()
        return False

    cursor.execute(f"""DELETE FROM main_table WHERE userid='{concrete_students[0].userid}'""")
    connection.commit()

    for university in universities:
        if university == "РАНХИГС":
            cursor.execute(f"""DELETE FROM ranepa_table WHERE userid='{concrete_students[0].userid}'""")
            connection.commit()
        elif university == "СПБГУ":
            cursor.execute(f"""DELETE FROM spbu_table WHERE userid='{concrete_students[0].userid}'""")
            connection.commit()
        else:
            cursor.execute(f"""DELETE FROM etu_table WHERE userid='{concrete_students[0].userid}'""")
            connection.commit()

    for student in concrete_students:
        if type(student) is SpbuStudent:
            # Здесь возможно строка неправильно перенесется
            cursor.execute(f"""INSERT INTO main_table(userid, name, surname, lastname, university_name, notifications) 
                            VALUES ('{student.userid}', 
                                    '{student.name}', 
                                    '{student.surname}', 
                                    '{student.lastname}', 
                                    'СПБГУ',
                                    false)""")
            connection.commit()

            for program in student.programs:
                # Здесь возможно строка неправильно перенесется
                cursor.execute(f"""INSERT INTO spbu_table(userid, educational_form, pay_form, program, place) 
                                VALUES ('{student.userid}', 
                                    '{program[0].educational_form}', 
                                    '{program[0].pay_form}', 
                                    '{program[0].program}', 
                                    {program[1]})""")
                connection.commit()
        elif type(student) is RanepaStudent:
            cursor.execute(f"""INSERT INTO main_table(userid, name, surname, lastname, university_name, notifications) 
                            VALUES ('{student.userid}', 
                                    '{student.name}', 
                                    '{student.surname}', 
                                    '{student.lastname}', 
                                    'РАНХИГС',
                                    false)""")
            connection.commit()

            for program in student.programs:
                cursor.execute(f"""INSERT INTO ranepa_table(userid, departament, approval, form, program, place) 
                                VALUES ('{student.userid}', 
                                        '{program[0].departament}', 
                                        '{program[0].approval}', 
                                        '{program[0].form}', 
                                        '{program[0].program}',
                                        {program[1]})""")
                connection.commit()
        else:
            cursor.execute(f"""INSERT INTO main_table(userid, name, surname, lastname, university_name, notifications) 
                                        VALUES ('{student.userid}', 
                                                '{student.name}', 
                                                '{student.surname}', 
                                                '{student.lastname}', 
                                                'ЛЭТИ',
                                                false)""")
            connection.commit()

            for program in student.programs:
                cursor.execute(f"""INSERT INTO ranepa_table(userid, form, program, place) 
                                                VALUES ('{student.userid}', 
                                                        '{program[0].form}', 
                                                        '{program[0].program}',
                                                        {program[1]})""")
                connection.commit()

    connection.close()
    return True


def get_info(userid: str) -> List[ConcreteUniversityStudent]:
    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                  host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM main_table WHERE userid='{userid}'""")
    connection.commit()

    result = list()
    for student_data in cursor.fetchall():
        if student_data[4] == "РАНХИГС":
            cursor.execute(f"""SELECT * FROM ranepa_table WHERE userid='{userid}'""")
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append(
                    (RanepaProgram(program_data[1], program_data[2], program_data[3], program_data[4]), program_data[5])
                )

            result.append(RanepaStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        elif student_data[4] == "СПБГУ":
            cursor.execute(f"""SELECT * FROM spbu_table WHERE userid='{userid}'""")
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((SpbuProgram(program_data[1], program_data[2], program_data[3]), program_data[4]))

            result.append(SpbuStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        else:
            cursor.execute(f"""SELECT * FROM etu_table WHERE userid='{userid}'""")
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
    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                  host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM main_table WHERE userid='{userid}'""")
    connection.commit()

    if len(cursor.fetchall()) == 0:
        connection.close()
        message = \
            f"Failure to find student with this userid in database was detecting in database_module/add_notifications."
        logging.warning(message)
        message = \
            f"Не удалось найти абитуриента с такими данными (Возможно, Вы еще не зарегистрированы)."
        raise InternalError(message)

    cursor.execute(f"""SELECT * FROM main_table WHERE userid='{userid}' and notifications=false""")
    connection.commit()
    result = len(cursor.fetchall()) != 0

    cursor.execute(f"""UPDATE main_table SET notifications = true WHERE userid='{userid}'""")
    connection.commit()
    connection.close()

    return result


def remove_notifications(userid: str) -> bool:
    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                  host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM main_table WHERE userid='{userid}'""")
    connection.commit()

    if len(cursor.fetchall()) == 0:
        connection.close()
        message = \
            f"Failure to find student with this userid in database was detecting in " \
            f"database_module/remove_notifications. "
        logging.warning(message)
        message = \
            f"Не удалось найти абитуриента с такими данными (Возможно, Вы еще не зарегистрированы)."
        raise InternalError(message)

    cursor.execute(f"""SELECT * FROM main_table WHERE userid='{userid}' and notifications=true""")
    connection.commit()
    result = len(cursor.fetchall()) != 0

    cursor.execute(f"""UPDATE main_table SET notifications = false WHERE userid='{userid}'""")
    connection.commit()
    connection.close()

    return result


def get_all_with_notifications() -> List[ConcreteUniversityStudent]:
    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                  host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM main_table WHERE notifications=true""")
    connection.commit()

    result = list()
    for student_data in cursor.fetchall():
        if student_data[4] == "РАНХИГС":
            cursor.execute(f"""SELECT * FROM ranepa_table WHERE notifications=true""")
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append(
                    (RanepaProgram(program_data[1], program_data[2], program_data[3], program_data[4]), program_data[5])
                )

            result.append(RanepaStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        elif student_data[4] == "СПБГУ":
            cursor.execute(f"""SELECT * FROM spbu_table WHERE notifications=true""")
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((SpbuProgram(program_data[1], program_data[2], program_data[3]), program_data[4]))

            result.append(SpbuStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))
        else:
            cursor.execute(f"""SELECT * FROM etu_table WHERE notifications=true""")
            connection.commit()

            programs = list()
            for program_data in cursor.fetchall():
                programs.append((EtuProgram(program_data[1], program_data[2]), program_data[3]))

            result.append(EtuStudent(student_data[0], student_data[1], student_data[2], student_data[3], programs))

    connection.close()
    return result


def update(concrete_students: List[ConcreteUniversityStudent]) -> bool:
    result = True

    for student in concrete_students:
        if type(student) is RanepaStudent:
            for program in student.programs:
                connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                              host='127.0.0.1', port='5432')
                cursor = connection.cursor()
                cursor.execute(f"""EXISTS(SELECT * FROM ranepa_table WHERE 
                                userid='{student.userid}' and departament='{program[0].departament}' and 
                                approval='{program[0].approval}' and form='{program[0].form}' and 
                                program='{program[0].program}')""")
                connection.commit()

                if not cursor.fetchone():
                    result = False

                cursor.execute(f"""UPDATE ranepa_table SET place = {program[1]} WHERE 
                                                userid='{student.userid}' and departament='{program[0].departament}' and 
                                                approval='{program[0].approval}' and form='{program[0].form}' and 
                                                program='{program[0].program}'""")
                connection.commit()
        elif type(student) is SpbuStudent:
            for program in student.programs:
                connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                              host='127.0.0.1', port='5432')
                cursor = connection.cursor()
                cursor.execute(f"""EXISTS(SELECT * FROM spbu_table WHERE 
                                userid='{student.userid}' and educational_form='{program[0].educational_form}' and 
                                pay_form='{program[0].pay_form}' and program='{program[0].program}')""")
                connection.commit()

                if not cursor.fetchone():
                    result = False

                cursor.execute(f"""UPDATE spbu_table SET place = {program[1]} WHERE 
                                userid='{student.userid}' and educational_form='{program[0].educational_form}' and 
                                pay_form='{program[0].pay_form}' and program='{program[0].program}'""")
                connection.commit()
        else:
            for program in student.programs:
                connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                              host='127.0.0.1', port='5432')
                cursor = connection.cursor()
                cursor.execute(f"""EXISTS(SELECT * FROM etu_table WHERE 
                                userid='{student.userid}' and form='{program[0].form}' 
                                and program='{program[0].program}')""")
                connection.commit()

                if not cursor.fetchone():
                    result = False

                cursor.execute(f"""UPDATE etu_table SET place = {program[1]} WHERE 
                                userid='{student.userid}' and form='{program[0].form}' 
                                and program='{program[0].program}'""")
                connection.commit()

    return result


def check_if_user_is_exists(userid: str) -> bool:
    connection = psycopg2.connect(database="postupatordb", user='postgres', password='adhog',
                                  host='127.0.0.1', port='5432')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT userid FROM main_table WHERE userid='{userid}'""")
    connection.commit()
    result = cursor.fetchall()
    connection.close()
    return len(result) != 0
