import telebot

universities = ['СПБГУ','ЛЭТИ','ИТМО','МФТИ','ВШЭ']

def generate_markup(user):
    universities = get_universities(user)
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    for university in universities:
        markup.add(university)
    markup.add('Завершить регистрацию')
    return markup

def get_universities(user):
    result = []
    for university in universities:
        is_selected = False
        for user_university in user.universities:
            if university == user_university:
                is_selected = True
                break
        if not is_selected:
            result.append(university)
    return result
