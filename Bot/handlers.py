import telebot
from Bot.config import token
from Bot.userManager import add_user, users,get_registration_message
from Bot.markup import get_markup

bot = telebot.TeleBot(token)

def start():
    bot.polling(none_stop=True)

@bot.message_handler(commands=['register'])
def send_register(message):
    bot.send_message(message.chat.id,get_registration_message(message))


@bot.message_handler(content_types=['text'])
def send_message(message):
    id = message.chat.id
    if id in users and not users[id].isRegistered:
        bot_message = get_registration_message(message)
        bot.send_message(id, bot_message, reply_markup=get_markup(users[id],bot_message))
    elif id in users:
        bot.send_message(id,'Вы зарегистрированы',reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(id,'Вы не зарегистрированы',reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['position'])
def send_position(message):
    id = message.chat.id

