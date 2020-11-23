import telebot
from Bot.config import token
from Bot.userManager import add_user, users,user_registration
from Bot.markup import get_markup

bot = telebot.TeleBot(token)

def start():
    bot.polling(none_stop=True)

@bot.message_handler(commands=['register'])
def send_register(message):
    id = message.chat.id
    add_user(id)
    bot.send_message(id, 'Введите имя')


@bot.message_handler(content_types=['text'])
def send_message(message):
    id = message.chat.id
    if id in users and not users[id].isRegistered:
        bot_message = user_registration(message)
        bot.send_message(id, bot_message, reply_markup=get_markup(users[id],bot_message))
    elif id in users:
        bot.send_message(id,'Вы зарегистрированы',reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(id,'Вы не зарегистрированы',reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['position'])
def send_position(message):
    id = message.chat.id

