import telebot
from typing import Tuple, List, Dict
from config.config import token
from telegram_module.bot_markup import get_markup
from telegram_module.student_data import students, get_registration_message
from telegram_module.validator import is_validate_message
from middle_module.middle_module import check_if_user_is_exists
from telegram_module import telegram_module
from telegram_module.converter import convert_to_message
from models.Program.interface.Program import Program

bot = telebot.TeleBot(token)


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
    telegram_module.add_notifications(str(id))


@bot.message_handler(commands=['removeNotifications'])
def remove_notifications(message):
    id = message.chat.id
    telegram_module.remove_notifications(str(id))


@bot.message_handler(commands=['getInfo'])
def get_info(message):
    id = message.chat.id
    info = telegram_module.get_info(str(id))
    bot_message = convert_to_message(info)
    bot.send_message(id, bot_message)


@bot.message_handler(commands=['editUser'])
def edit_user(message):
    bot.send_message(message.chat.id, get_registration_message(message))


def notify(userid: str, positions: Dict[str, List[Tuple[Program, int]]]):
    bot_message = convert_to_message(positions)
    bot.send_message(userid, bot_message)
