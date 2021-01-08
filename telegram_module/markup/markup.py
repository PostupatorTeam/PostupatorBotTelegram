from typing import Union, List
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from config.config import universities_list
from models.University.interface.University import University
from telegram_module.models.models_storage import Student


def get_markup(user: Student, message: str) -> Union[ReplyKeyboardMarkup, ReplyKeyboardRemove]:
    if user.lastname is None or message == 'Вы успешно зарегистрировались' or not user.is_added_program:
        return ReplyKeyboardRemove()

    return create_markup(user)


def create_markup(user: Student) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    for university in get_universities_markup(user):
        markup.add(university)
    markup.add('Завершить регистрацию')

    return markup


def get_universities_markup(user: Student) -> List[University]:
    result = []

    for university in universities_list:
        count = 0

        for user_university in user.programs:
            if university == user_university.university_name:
                count += 1

        if count < 3:
            result.append(university)

    return result
