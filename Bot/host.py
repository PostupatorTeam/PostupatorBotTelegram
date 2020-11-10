import telebot
from Bot.config import token
from Bot.userData import add_data,add_user,users
from Bot.markup import generate_markup

bot = telebot.TeleBot(token)

def host():
    bot.polling(none_stop=True)

@bot.message_handler(commands=['register'])
def send_register(message):
    add_user(message.chat.id)
    bot.send_message(message.chat.id,'Введите Имя')

@bot.message_handler(content_types=['text'])
def send_message(message):
    id = message.chat.id
    if(id in users and not users[id].isRegistered):
        if message.text == 'Завершить регистрацию':
            users[id].isRegistered = True
            bot.send_message(id,'Вы зареганы')
            return
        result = add_data(id,message.text)
        if result == 0:
            bot.send_message(id,'Введите фамилию')
        elif result == 1:
            bot.send_message(id, 'Введите Отчество')
        elif result == 2:
            bot.send_message(id,'Введите баллы')
        elif result == 3:
            bot.send_message(id, 'Выберите вуз',reply_markup=generate_markup(users[id]))
