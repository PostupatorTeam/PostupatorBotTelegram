from telegram_module.validator import *
from dataclasses import dataclass
from telegram_module.program import Program
from telegram_module.program import add_program_info, get_first_message
from enum import Enum

students = {}


@dataclass
class Student:
    firstName: str
    surname: str
    patronymic: str
    programs: list
    isRegistered: bool
    isAddProgram: bool


class RegistrationData(Enum):
    Empty = 0
    FirstName = 1
    Surname = 2
    Patronymic = 3
    UniversityName = 4
    ProgramInfo = 5
    End = 6


def add_user(id):
    students[id] = Student(firstName=None, surname=None, patronymic=None, programs=[], isRegistered=False,
                           isAddProgram=True)


def add_firstName_user(id, name):
    students[id].firstName = name


def add_surname_user(id, name):
    students[id].surname = name


def add_patronymic_user(id, name):
    students[id].patronymic = name


def add_points_user(id, points):
    students[id].points = points


def add_program_user(id, university):
    students[id].programs.append(
        Program(paymentForm=None, studyForm=None, directionStudy=None, studyProgram=None,
                universityBranch=None,universityName=university))


def end_registration(id):
    students[id].isRegistered = True


def add_data_user(id, message, data_type):
    if data_type == RegistrationData.Empty:
        add_user(id)
        return 'Введите имя'
    if data_type == RegistrationData.FirstName:
        add_firstName_user(id, message)
        return 'Введите фамилию'
    if data_type == RegistrationData.Surname:
        add_surname_user(id, message)
        return 'Введите отчество'
    if data_type == RegistrationData.Patronymic:
        add_patronymic_user(id, message)
        return 'Укажите университет'
    if data_type == RegistrationData.UniversityName:
        if is_validate_university(students[id], message):
            add_program_user(id, message)
            students[id].isAddProgram = False
            return get_first_message(message)
        else:
            return 'Введите университет из списка или закончите регистрацию'
    if data_type == RegistrationData.ProgramInfo:
        response = add_program_info(message, students[id])
        if response is None:
            students[id].isAddProgram = True
            return 'Укажите университет'
        else:
            return response
    if data_type == RegistrationData.End:
        end_registration(id)
        return 'Вы успешно зарегестрировались'


def get_registration_message(message):
    id = message.chat.id
    if not id in students:
        return add_data_user(id, message.text, RegistrationData.Empty)
    if students[id].firstName is None:
        return add_data_user(id, message.text, RegistrationData.FirstName)
    if students[id].surname is None:
        return add_data_user(id, message.text, RegistrationData.Surname)
    if students[id].patronymic is None:
        return add_data_user(id, message.text, RegistrationData.Patronymic)
    if not students[id].isAddProgram:
        return add_data_user(id, message.text, RegistrationData.ProgramInfo)
    if message.text == 'Завершить регистрацию':
        return add_data_user(id, message.text, RegistrationData.End)
    return add_data_user(id, message.text, RegistrationData.UniversityName)
