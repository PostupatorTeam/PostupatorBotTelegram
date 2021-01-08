from typing import Dict, List, Tuple
import telebot
from config.config import token
from middle_module import middle_module
from models.Program.interface.Program import Program
from telegram_module.converters.converters import convert_to_message
from telegram_module.markup.markup import get_markup
from telegram_module.users_manager.users_manager import get_registration_message, students
from telegram_module.validators.validator import is_validate_message


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['createUser'])
def create_user(message):
    bot.send_message(message.chat.id, get_registration_message(message))


@bot.message_handler(commands=['addNotifications'])
def add_notifications(message):
    middle_module.add_notifications(str(message.chat.id))


@bot.message_handler(commands=['removeNotifications'])
def remove_notifications(message):
    middle_module.remove_notifications(str(message.chat.id))


@bot.message_handler(commands=['getInfo'])
def get_info(message):
    chat_id = message.chat.id

    info = middle_module.get_info(str(chat_id))

    bot.send_message(chat_id, convert_to_message(info))


@bot.message_handler(commands=['editUser'])
def edit_user(message):
    bot.send_message(message.chat.id, get_registration_message(message))


# Строки для взаимодействия с пользователем
@bot.message_handler(content_types=['text'])
def send_message(message):
    chat_id = message.chat.id

    if not is_validate_message(message.text):
        bot.send_message(chat_id, 'Вы отправили некорректное сообщение')
    elif chat_id in students and not students[chat_id].is_registered:
        bot_message = get_registration_message(message)

        markup = None
        if chat_id in students:
            markup = get_markup(students[chat_id], bot_message)

        bot.send_message(chat_id, bot_message, reply_markup=markup)
    elif middle_module.check_if_user_is_exists(str(chat_id)):
        bot.send_message(chat_id, 'Вы успешно зарегистрированы')
    else:
        bot.send_message(chat_id, 'Вы не зарегистрированы', reply_markup=telebot.types.ReplyKeyboardRemove())


def notify(userid: str, positions: Dict[str, List[Tuple[Program, int]]]):
    bot.send_message(userid, convert_to_message(positions))


def start():
    bot.polling(none_stop=True)
