from typing import Dict, List, Tuple
from src.main.models.Program.implementations.EtuProgram import EtuProgram
from src.main.models.Program.implementations.RanepaProgram import RanepaProgram
from src.main.models.Program.implementations.SpbuProgram import SpbuProgram
from src.main.models.Program.interface.Program import Program
from src.main.models.Student import Student
from src.main.models.University.implementations.EtuUniversity import EtuUniversity
from src.main.models.University.implementations.RanepaUniversity import RanepaUniversity
from src.main.models.University.implementations.SpbuUniversity import SpbuUniversity
from src.main.telegram_module.models import models_storage


def add_etu_university_to_student(student: models_storage.Student, student_db: Student):
    student_db.universities.append(EtuUniversity([]))

    for program in student.programs:
        if program.university_name == 'ЛЭТИ':
            student_db.universities[-1].programs.append(EtuProgram(program.pay_form, program.program))


def add_spbu_university_to_student(student: models_storage.Student, student_db: Student):
    student_db.universities.append(SpbuUniversity([]))

    for program in student.programs:
        if program.university_name == 'СПБГУ':
            student_db.universities[-1].programs.append(SpbuProgram(program.educational_form, program.pay_form,
                                                                    program.approval))


def add_ranepa_university_to_student(student: models_storage.Student, student_db: Student):
    student_db.universities.append(RanepaUniversity([]))

    for program in student.programs:
        if program.university_name == 'РАНХИГС':
            student_db.universities[-1].programs.append(RanepaProgram(program.university_branch, program.approval,
                                                                      program.educational_form, program.program))


def is_exist_etu(programs: List[models_storage.Program]) -> bool:
    for program in programs:
        if program.university_name == 'ЛЭТИ':
            return True

    return False


def is_exist_spbu(programs: List[models_storage.Program]) -> bool:
    for program in programs:
        if program.university_name == 'СПБГУ':
            return True

    return False


def is_exist_ranepa(programs: List[models_storage.Program]) -> bool:
    for program in programs:
        if program.university_name == 'РАНХИГС':
            return True

    return False


def convert_to_student_database(student: models_storage.Student, userid: str) -> Student:
    student_database = Student(userid, student.name, student.surname, student.lastname, [])

    if is_exist_etu(student.programs):
        add_etu_university_to_student(student, student_database)

    if is_exist_spbu(student.programs):
        add_spbu_university_to_student(student, student_database)

    if is_exist_ranepa(student.programs):
        add_ranepa_university_to_student(student, student_database)

    return student_database


def convert_to_message(universities: Dict[str, List[Tuple[Program, int]]]) -> str:
    message = ''

    for key in universities:
        message += '{0}:\n'.format(key)

        for pair in universities[key]:
            message += 'На {0} позиция {1}\n'.format(str(pair[0]), pair[1])

    return message
