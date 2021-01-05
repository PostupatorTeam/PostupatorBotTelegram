import telebot
from config.config import token
from telegram_module.student import add_user, students,get_registration_message
from telegram_module.bot_markup import get_markup

bot = telebot.TeleBot(token)

def start():
    bot.polling(none_stop=True)

@bot.message_handler(commands=['register'])
def send_register(message):
    bot.send_message(message.chat.id,get_registration_message(message))


@bot.message_handler(content_types=['text'])
def send_message(message):
    id = message.chat.id
    if id in students and not students[id].isRegistered:
        bot_message = get_registration_message(message)
        bot.send_message(id, bot_message, reply_markup=get_markup(students[id], bot_message))
    if not id in students:
        bot.send_message(id,'Вы не зарегистрированы',reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['position'])
def send_position(message):
    id = message.chat.id