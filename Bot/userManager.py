from Bot.validator import *
from dataclasses import dataclass
from Bot.universityManager import University
from Bot.universityManager import add_university_info,get_first_message
from enum import Enum
users = {}

@dataclass
class User:
    firstName: str
    surname: str
    patronymic: str
    universities: list
    isRegistered: bool
    isAddUniversity: bool

class RegistrationData(Enum):
    Empty = 0
    FirstName = 1
    Surname = 2
    Patronymic = 3
    UniversityName = 4
    UniversityInfo = 5
    End = 6



def add_user(id):
    users[id] = User(firstName=None,surname=None,patronymic=None,universities=[],isRegistered=False,isAddUniversity=True)

def add_firstName_user(id,name):
    users[id].firstName = name

def add_surname_user(id,name):
    users[id].surname = name

def add_patronymic_user(id,name):
    users[id].patronymic = name

def add_points_user(id,points):
    users[id].points = points

def add_university_user(id,university):
    users[id].universities.append(University(name=university,paymentForm=None,studyForm=None,directionStudy=None,studyProgram=None,universityBranch=None))

def get_firstName_user(id):
    return users[id].firstName

def get_surname_user(id):
    return users[id].lastName

def get_patronymic_user(id):
    return users[id].patronymic

def get_points_user(id):
    return users[id].points

def get_universities_user(id):
    return users[id].universities

def end_registration(id):
    users[id].isRegistered = True

def add_data_user(id, message, data_type):
    if data_type == RegistrationData.Empty:
        add_user(id)
        return 'Введите имя'
    if data_type == RegistrationData.FirstName:
        add_firstName_user(id,message)
        return 'Введите фамилию'
    if data_type == RegistrationData.Surname:
        add_surname_user(id,message)
        return 'Введите отчество'
    if data_type == RegistrationData.Patronymic:
        add_patronymic_user(id, message)
        return 'Укажите университет'
    if data_type == RegistrationData.UniversityName:
        if is_validate_university(users[id],message):
            add_university_user(id,message)
            users[id].isAddUniversity = False
            return get_first_message(message)
        else:
            return 'Введите университет из списка или закончите регистрацию'
    if data_type == RegistrationData.UniversityInfo:
        response = add_university_info(message,users[id])
        if response == None:
            users[id].isAddUniversity = True
            return 'Укажите университет'
        else:
            return response
    if data_type == RegistrationData.End:
        end_registration(id)
        return 'Вы успешно зарегестрировались'



def get_registration_message(message):
    id = message.chat.id
    if not id in users:
        return add_data_user(id,message.text,RegistrationData.Empty)
    if users[id].firstName == None:
        return add_data_user(id, message.text, RegistrationData.FirstName)
    if users[id].surname == None:
        return add_data_user(id, message.text, RegistrationData.Surname)
    if users[id].patronymic == None:
        return add_data_user(id, message.text, RegistrationData.Patronymic)
    if not users[id].isAddUniversity:
        return add_data_user(id, message.text, RegistrationData.UniversityInfo)
    if message.text == 'Завершить регистрацию':
        return add_data_user(id, message.text, RegistrationData.End)
    return add_data_user(id, message.text, RegistrationData.UniversityName)