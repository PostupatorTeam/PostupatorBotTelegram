from typing import List
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from models.Student import Student
from models.ConcreteUniversityStudent.implementations.EtuStudent import EtuStudent
from models.ConcreteUniversityStudent.implementations.RanepaStudent import RanepaStudent
from models.ConcreteUniversityStudent.implementations.SpbuStudent import SpbuStudent
from models.University.implementations.EtuUniversity import EtuUniversity
from models.University.implementations.RanepaUniversity import RanepaUniversity
from models.University.implementations.SpbuUniversity import SpbuUniversity


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
    programs = list()
    universities = list()

    for student in students:
        for program in student.programs:
            programs.append(program[0])

        if type(student) is SpbuStudent:
            universities.append(SpbuUniversity(programs))
        elif type(student) is EtuStudent:
            universities.append(EtuUniversity(programs))
        elif type(student) is RanepaStudent:
            universities.append(RanepaUniversity(programs))

        programs = list()

    return Student(students[0].userid, students[0].name, students[0].surname, students[0].lastname, universities)
