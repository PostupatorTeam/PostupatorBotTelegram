from typing import List
from src.main.models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from src.main.models.Student import Student
from src.main.models.ConcreteUniversityStudent.implementations.EtuStudent import EtuStudent
from src.main.models.ConcreteUniversityStudent.implementations.RanepaStudent import RanepaStudent
from src.main.models.ConcreteUniversityStudent.implementations.SpbuStudent import SpbuStudent
from src.main.models.University.implementations.EtuUniversity import EtuUniversity
from src.main.models.University.implementations.RanepaUniversity import RanepaUniversity
from src.main.models.University.implementations.SpbuUniversity import SpbuUniversity


def map_to_concrete_university_students(student: Student) -> List[ConcreteUniversityStudent]:
    result = list()

    for university in student.universities:
        programs = university.get_position(student.name, student.surname, student.lastname)

        if type(university) is SpbuUniversity:
            result.append(SpbuStudent(student.userid, student.name, student.surname, student.lastname, programs))
        elif type(university) is EtuUniversity:
            result.append(EtuStudent(student.userid, student.name, student.surname, student.lastname, programs))
        elif type(university) is RanepaUniversity:
            result.append(RanepaStudent(student.userid, student.name, student.surname, student.lastname, programs))

    return result


def map_to_student(students: List[ConcreteUniversityStudent]) -> Student:
    universities = list()

    for student in students:
        programs = list()
        for program in student.programs:
            programs.append(program[0])

        if type(student) is SpbuStudent:
            universities.append(SpbuUniversity(programs))
        elif type(student) is EtuStudent:
            universities.append(EtuUniversity(programs))
        elif type(student) is RanepaStudent:
            universities.append(RanepaUniversity(programs))

    return Student(students[0].userid, students[0].name, students[0].surname, students[0].lastname, universities)
