from telebot import types
from config.config import universities_list


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
