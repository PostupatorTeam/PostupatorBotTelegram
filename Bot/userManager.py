from Bot.validator import *
from dataclasses import dataclass
users = {}

@dataclass
class User:
    firstName: str
    surname: str
    patronymic: str
    points: str
    universities: list
    isRegistered: bool

def add_data(id,answer):
    if users[id].firstName == None:
        add_firstName_user(id,answer)
        return 0
    if users[id].surname == None:
        add_surname_user(id,answer)
        return 1
    if users[id].patronymic == None:
        add_patronymic_user(id,answer)
        return 2
    if users[id].points == None:
        add_points_user(id,answer)
        return 3
    add_university_user(id,answer)
    return 3


def add_user(id):
    users[id] = User(firstName=None,surname=None,patronymic=None,points=None,universities=[],isRegistered=False)

def add_firstName_user(id,name):
    users[id].firstName = name

def add_surname_user(id,name):
    users[id].surname = name

def add_patronymic_user(id,name):
    users[id].patronymic = name

def add_points_user(id,points):
    users[id].points = points

def add_university_user(id,university):
    users[id].universities.append(university)

def get_firstName_user(id):
    return users[id].firstName

def get_last_Name_user(id):
    return users[id].lastName

def get_patronymic_user(id):
    return users[id].patronymic

def get_points_user(id):
    return users[id].points

def get_universities_user(id):
    return users[id].universities

def end_registration(id):
    users[id].isRegistered = True

def user_registration(message):
    id = message.chat.id
    if users[id].firstName == None:
        add_firstName_user(id,message.text)
        return 'Введите фамилию'
    if users[id].surname == None:
        add_surname_user(id,message.text)
        return 'Введите отчество'
    if users[id].patronymic == None:
        add_patronymic_user(id,message.text)
        return 'Введите баллы'
    if users[id].points == None:
        add_points_user(id,message.text)
        return 'Укажите университет'
    if message.text == 'Завершить регистрацию':
        end_registration(id)
        return 'Вы успешно зарегестрировались'
    if validate_university(id,message.text):
        add_university_user(id,message.text)
        return 'Укажите университет'
    else:
        return 'Введите университет из списка или закончите регистрацию'