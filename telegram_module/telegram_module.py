import types
from typing import Tuple, List, Dict

import telebot

from config.config import universities_list, token
from database_module.database_module import check_if_user_is_exists
from models.Program.implementations.EtuProgram import EtuProgram
from models.Program.implementations.RanepaProgram import RanepaProgram
from models.Program.implementations.SpbuProgram import SpbuProgram
from models.Program.interface.Program import Program
from middle_module import middle_module
from models.University.implementations.EtuUniversity import EtuUniversity
from models.University.implementations.RanepaUniversity import RanepaUniversity
from models.University.implementations.SpbuUniversity import SpbuUniversity
from telegram_module.models.models_storage import Student, RegistrationData
# from telegram_module import bot_handler, student_data

students = {}

bot = telebot.TeleBot(token)

def create_user(studentData: Student) -> Dict[str, List[Tuple[Program, int]]]:
    return middle_module.create_user(studentData)
    # С помощью опроса получаем информацию и создаем класс Student
    # Обрабатывая исключения, отправляем запрос на middle модуль
    # Ответ просто распарсиваем и выводим инфу пользователю
    # Здесь же пишем логи


def edit_user():
    # С помощью опроса получаем информацию и создаем класс Student
    # Обрабатывая исключения, отправляем запрос на middle модуль
    # Ответ просто распарсиваем и выводим инфу пользователю
    # Здесь же пишем логи
    pass


def get_info(userid: str) -> Dict[str, List[Tuple[Program, int]]]:
    return middle_module.get_info(userid)
    # Обрабатывая исключения, отправляем id на middle модуль
    # Распарсиваем полученную инфу
    # Здесь же пишем логи


def add_notifications(userid: str):
    middle_module.add_notifications(userid)
    # Обрабатывая исключения, отправляем id на middle модуль
    # Здесь же пишем логи
    pass


def remove_notifications(userid: str):
    middle_module.remove_notifications(userid)
    # Обрабатывая исключения, отправляем id на middle модуль
    # Здесь же пишем логи
    pass


def notify(userid: str, positions: Dict[str, List[Tuple[Program, int]]]):
    bot_handler.notify_handler(userid, positions)
    # В чат с соответствующим id отправляем нужную инфу
    # Здесь же пишем логи



def start():
    bot.polling(none_stop=True)


@bot.message_handler(commands=['createUser'])
def send_register(message):
    bot.send_message(message.chat.id, get_registration_message(message))


@bot.message_handler(content_types=['text'])
def send_message(message):
    id = message.chat.id
    if not is_validate_message(message.text):
        bot.send_message(id, 'Вы отправили не корректное сообщение')
    elif id in students and not students[id].isRegistered:
        bot_message = get_registration_message(message)
        bot.send_message(id, bot_message, reply_markup=get_markup(students[id], bot_message))
    elif check_if_user_is_exists(str(id)):
        bot.send_message(id, 'Вы зарегестрированы')
    else:
        bot.send_message(id, 'Вы не зарегистрированы', reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(commands=['addNotifications'])
def add_notifications(message):
    id = message.chat.id
    add_notifications(str(id))


@bot.message_handler(commands=['removeNotifications'])
def remove_notifications(message):
    id = message.chat.id
    remove_notifications(str(id))


@bot.message_handler(commands=['getInfo'])
def get_info(message):
    id = message.chat.id
    info = get_info(str(id))
    bot_message = convert_to_message(info)
    bot.send_message(id, bot_message)


@bot.message_handler(commands=['editUser'])
def edit_user(message):
    bot.send_message(message.chat.id, get_registration_message(message))


def notify_handler(userid: str, positions: Dict[str, List[Tuple[Program, int]]]):
    bot_message = convert_to_message(positions)
    bot.send_message(userid, bot_message)


def get_markup(user, message):
    if user.patronymic is None or message == 'Вы успешно зарегестрировались' or not user.isAddProgram:
        return types.ReplyKeyboardRemove()
    markup = create_markup(user)
    return markup


def create_markup(user):
    universities = get_universities_markup(user)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for university in universities:
        markup.add(university)
    markup.add('Завершить регистрацию')
    return markup


def get_universities_markup(user):
    result = []
    for university in universities_list:
        count = 0
        for user_university in user.programs:
            if university == user_university.universityName:
                count += 1
        if count < 3:
            result.append(university)
    return result

def convert_to_message(universities: Dict[str, List[Tuple[Program, int]]]) -> str:
    message = ''
    for key in universities:
        message += '{0}:\n'.format(key)
        for pair in universities[key]:
            message += 'На {0} позиция {1}\n'.format(str(pair[0]), pair[1])
    return message


def convert_to_student_database(student: Student, userid: str) -> Student:
    student_database = Student(userid=userid, name=student.firstName, surname=student.surname,
                               lastname=student.patronymic, universities=[])

    if is_exist_etu(student.programs):
        add_etu_university_to_student(student, student_database)

    if is_exist_spbu(student.programs):
        add_spbu_university_to_student(student, student_database)

    if is_exist_ranepa(student.programs):
        add_ranepa_university_to_student(student, student_database)

    return student_database


def add_etu_university_to_student(student: Student, student_db: Student):
    student_db.universities.append(EtuUniversity(programs=[]))
    for program in student.programs:
        if program.universityName == 'ЛЭТИ':
            student_db.universities[-1].programs.append(EtuProgram(form=program.paymentForm
                                                                   , program=program.studyProgram))


def add_spbu_university_to_student(student: Student, student_db: Student):
    student_db.universities.append(SpbuUniversity(programs=[]))
    for program in student.programs:
        if program.universityName == 'СПБГУ':
            student_db.universities[-1].programs.append(SpbuProgram(pay_form=program.paymentForm
                                                                    , educational_form=program.directionStudy
                                                                    , program=program.studyForm))


def add_ranepa_university_to_student(student: Student, student_db: Student):
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

def add_program_info(info, student):
    if student.programs[-1].universityName == 'ЛЭТИ':
        if student.programs[-1].studyProgram is None:
            student.programs[-1].studyProgram = info
            return 'Введите форму обучения'
        if student.programs[-1].paymentForm is None:
            student.programs[-1].paymentForm = info
            return None
    if student.programs[-1].universityName == 'РАНХГИС':
        if student.programs[-1].universityBranch is None:
            student.programs[-1].universityBranch = info
            return 'Введите направление обучения'
        if student.programs[-1].directionStudy is None:
            student.programs[-1].directionStudy = info
            return 'Введите форму обучения'
        if student.programs[-1].studyForm is None:
            student.programs[-1].studyForm = info
            return 'Введите программу обучения'
        if student.programs[-1].studyProgram is None:
            student.programs[-1].studyProgram = info
            return None
    if student.programs[-1].universityName == 'СПБГУ':
        if student.programs[-1].directionStudy is None:
            student.programs[-1].directionStudy = info
            return 'Введите форму обучения'
        if student.programs[-1].studyForm is None:
            student.programs[-1].studyForm = info
            return 'Введите форму оплаты'
        if student.programs[-1].paymentForm is None:
            student.programs[-1].paymentForm = info
            return None


def get_first_message(university):
    if university == 'ЛЭТИ':
        return 'Введите программу обучения'
    if university == 'РАНХГИС':
        return 'Введите филиал вуза'
    if university == 'СПБГУ':
        return 'Введите направление обучения'



def add_user(id):
    students[id] = Student(firstName=None, surname=None, patronymic=None, programs=[], isRegistered=False,
                      isAddProgram=True)


def add_firstName_user(student, name):
    student.firstName = name


def add_surname_user(student, name):
    student.surname = name


def add_patronymic_user(student, name):
    student.patronymic = name


def add_points_user(student, points):
    student.points = points


def add_program_user(student, university):
    student.programs.append(
        Program(paymentForm=None, studyForm=None, directionStudy=None, studyProgram=None,
                universityBranch=None, universityName=university))


def end_registration(id) -> str:
    students[id].isRegistered = True
    student = convert_to_student_database(students[id], id)
    del students[id]
    univers_data = create_user(student)
    return convert_to_message(univers_data)


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
        return end_registration(id)
        # return 'Вы успешно зарегестрировались'

def is_validate_university(student, university):
    if not university in universities_list:
        return False
    count = 0
    for program in student.programs:
        if program.universityName == university:
            count += 1
    if count >= 3:
        return False
    return True


def is_validate_message(message):
    allowed_characters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ- '
    for i in message:
        if not i in allowed_characters:
            return False
    return True

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
