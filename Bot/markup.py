from telebot import types
import Bot.config


def get_markup(user,message):
    if user.points == None or message == 'Вы успешно зарегестрировались' or not user.isAddUniversity:
        return types.ReplyKeyboardRemove()
    markup = create_markup(user)
    return markup

def create_markup(user):
    universities = get_universities_markup(user)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    for university in universities:
        markup.add(university)
    markup.add('Завершить регистрацию')
    return markup

def get_universities_markup(user):
    result = []
    for university in Bot.config.universities:
        is_selected = False
        for user_university in user.universities:
            if university == user_university.name:
                is_selected = True
                break
        if not is_selected:
            result.append(university)
    return result
