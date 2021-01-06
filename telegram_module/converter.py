from models.Student import Student
from telegram_module import student_data
from models.Program.interface.Program import Program
from models.Program.implementations.EtuProgram import EtuProgram
from models.Program.implementations.SpbuProgram import SpbuProgram
from models.Program.implementations.RanepaProgram import RanepaProgram
from models.University.implementations.EtuUniversity import EtuUniversity
from models.University.implementations.SpbuUniversity import SpbuUniversity
from models.University.implementations.RanepaUniversity import RanepaUniversity
from typing import Dict, Tuple, List


def convert_to_message(univers: Dict[str, List[Tuple[Program.Program, int]]]) -> str:
    message = ''
    for key in univers:
        message += '{0}:\n'.format(key)
        for pair in univers[key]:
            message += 'На {0} позиция {1}\n'.format(pair[0].program, pair[1])
    return message

def convert_to_student_database(student: student_data.Student, userid: str) -> Student:
    student_database = Student(userid=userid, name=student.firstName, surname=student.surname
                               , lastname=student.patronymic, universities=[])

    if is_exist_etu(student.programs):
        add_etu_university_to_student(student, student_database)

    if is_exist_spbu(student.programs):
        add_spbu_university_to_student(student, student_database)

    if is_exist_ranepa(student.programs):
        add_ranepa_university_to_student(student, student_database)

    return student_database


def add_etu_university_to_student(student: student_data.Student, student_db: Student):
    student_db.universities.append(EtuUniversity(programs=[]))
    for program in student.programs:
        if program.universityName == 'ЛЭТИ':
            student_db.universities[-1].programs.append(EtuProgram(form=program.paymentForm
                                                                   , program=program.studyProgram))


def add_spbu_university_to_student(student: student_data.Student, student_db: Student):
    student_db.universities.append(SpbuUniversity(programs=[]))
    for program in student.programs:
        if program.universityName == 'СПБГУ':
            student_db.universities[-1].programs.append(SpbuProgram(pay_form=program.paymentForm
                                                                    , educational_form=program.directionStudy
                                                                    , program=program.studyForm))


def add_ranepa_university_to_student(student: student_data.Student, student_db: Student):
    student_db.universities.append(RanepaUniversity(programs=[]))
    for program in student.programs:
        if program.universityName == 'СПБГУ':
            student_db.universities[-1].programs.append(RanepaProgram(program=program.studyProgram
                                                                      , form=program.studyForm
                                                                      , departament=program.universityBranch
                                                                      , approval=program.directionStudy))


def is_exist_etu(programs: list) -> bool:
    for program in programs:
        if program.universityName == 'ЛЭТИ':
            return True
    return False


def is_exist_spbu(programs: list) -> bool:
    for program in programs:
        if program.universityName == 'СПБГУ':
            return True
    return False


def is_exist_ranepa(programs: list) -> bool:
    for program in programs:
        if program.universityName == 'РАНХГИС':
            return True
    return False
