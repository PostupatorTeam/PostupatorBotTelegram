import telebot
from Bot.config import token
from Bot.userData import add_data,add_user,users

bot = telebot.TeleBot(token)

def host():
    bot.polling(none_stop=True)

@bot.message_handler(commands=['register'])
def send_register(message):
    add_user(message.chat.id)
    bot.send_message(message.chat.id,'Введите Имя')

@bot.message_handler(content_types=['text'])
def send_message(message):
    if(message.chat.id in users):
        result = add_data(message.chat.id,message.text)
        if result == 0:
            bot.send_message(message.chat.id,'Введите фамилию')
        elif result == 1:
            bot.send_message(message.chat.id, 'Введите Отчество')
        elif result == 2:
            bot.send_message(message.chat.id,'Введите баллы')
        elif result == 3:
            bot.send_message(message.chat.id, 'Вы зареганы')
