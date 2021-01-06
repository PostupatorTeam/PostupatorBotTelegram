from dataclasses import dataclass
from enum import Enum
from telegram_module.student_data import students, add_data_user


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


@dataclass
class Program:
    paymentForm: str
    studyForm: str
    directionStudy: str
    studyProgram: str
    universityBranch: str
    universityName: str
