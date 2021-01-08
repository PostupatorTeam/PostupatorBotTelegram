import logging
from typing import Dict, List, Tuple
import telebot
from psycopg2._psycopg import InternalError
from werkzeug.exceptions import NotFound, BadRequest
from config.config import token
from middle_module import middle_module
from models.Program.interface.Program import Program
from telegram_module.converters.converters import convert_to_message
from telegram_module.markup.markup import get_markup
from telegram_module.users_manager import users_manager
from telegram_module.users_manager.users_manager import get_registration_message, students
from telegram_module.validators.validator import is_validate_message


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['createUser'])
def create_user(message):
    chat_id = message.chat.id
    users_manager.is_create = True

    try:
        bot.send_message(chat_id, get_registration_message(message))
    except NotFound as e:
        logging.warning(f"NotFound was detecting in telegram_module/create_user (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except BadRequest as e:
        logging.warning(f"BadRequest was detecting in telegram_module/create_user (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except InternalError as e:
        logging.warning(f"InternalError was detecting in telegram_module/create_user (userid: {chat_id})")
        bot.send_message(chat_id, str(e))
    except Exception:
        logging.warning(f"Exception was detecting in telegram_module/create_user (userid: {chat_id})")
        bot.send_message(chat_id, "Что-то пошло не так, попробуйте еще раз")


@bot.message_handler(commands=['addNotifications'])
def add_notifications(message):
    chat_id = message.chat.id

    try:
        if middle_module.add_notifications(str(chat_id)):
            bot.send_message(chat_id, "Оповещения были успешно добавлены")
        else:
            bot.send_message(chat_id, "У Вас уже есть оповещения")
    except InternalError as e:
        logging.warning(f"InternalError was detecting in telegram_module/add_notifications (userid: {chat_id})")
        bot.send_message(chat_id, str(e))
    except Exception:
        logging.warning(f"Exception was detecting in telegram_module/add_notifications (userid: {chat_id})")
        bot.send_message(chat_id, "Что-то пошло не так, попробуйте еще раз")


@bot.message_handler(commands=['removeNotifications'])
def remove_notifications(message):
    chat_id = message.chat.id

    try:
        if middle_module.remove_notifications(str(message.chat.id)):
            bot.send_message(chat_id, "Оповещения были успешно удалены")
        else:
            bot.send_message(chat_id, "Оповещения уже были отключены")
    except InternalError as e:
        logging.warning(f"InternalError was detecting in telegram_module/remove_notifications (userid: {chat_id})")
        bot.send_message(chat_id, str(e))
    except Exception:
        logging.warning(f"Exception was detecting in telegram_module/remove_notifications (userid: {chat_id})")
        bot.send_message(chat_id, "Что-то пошло не так, попробуйте еще раз")


@bot.message_handler(commands=['getInfo'])
def get_info(message):
    chat_id = message.chat.id

    try:
        info = middle_module.get_info(str(chat_id))

        bot.send_message(chat_id, convert_to_message(info))
    except NotFound as e:
        logging.warning(f"NotFound was detecting in telegram_module/get_info (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except BadRequest as e:
        logging.warning(f"BadRequest was detecting in telegram_module/get_info (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except InternalError as e:
        logging.warning(f"InternalError was detecting in telegram_module/get_info (userid: {chat_id})")
        bot.send_message(chat_id, str(e))
    except Exception:
        logging.warning(f"Exception was detecting in telegram_module/get_info (userid: {chat_id})")
        bot.send_message(chat_id, "Что-то пошло не так, попробуйте еще раз")


@bot.message_handler(commands=['editUser'])
def edit_user(message):
    chat_id = message.chat.id

    users_manager.is_create = False

    try:
        bot.send_message(message.chat.id, get_registration_message(message))
    except NotFound as e:
        logging.warning(f"NotFound was detecting in telegram_module/edit_user (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except BadRequest as e:
        logging.warning(f"BadRequest was detecting in telegram_module/edit_user (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except InternalError as e:
        logging.warning(f"InternalError was detecting in telegram_module/edit_user (userid: {chat_id})")
        bot.send_message(chat_id, str(e))
    except Exception:
        logging.warning(f"Exception was detecting in telegram_module/edit_user (userid: {chat_id})")
        bot.send_message(chat_id, "Что-то пошло не так, попробуйте еще раз")


@bot.message_handler(content_types=['text'])
def send_message(message):
    chat_id = message.chat.id

    try:
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
    except NotFound as e:
        logging.warning(f"NotFound was detecting in telegram_module/send_message (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except BadRequest as e:
        logging.warning(f"BadRequest was detecting in telegram_module/send_message (userid: {chat_id})")
        bot.send_message(chat_id, e.description)
    except InternalError as e:
        logging.warning(f"InternalError was detecting in telegram_module/send_message (userid: {chat_id})")
        bot.send_message(chat_id, str(e))
    except Exception:
        logging.warning(f"Exception was detecting in telegram_module/send_message (userid: {chat_id})")
        bot.send_message(chat_id, "Что-то пошло не так, попробуйте еще раз")


def notify(userid: str, positions: Dict[str, List[Tuple[Program, int]]]):
    try:
        bot.send_message(int(userid), convert_to_message(positions))
    except Exception:
        logging.warning(f"Exception was detecting in telegram_module/notify (userid: {int(userid)})")
        bot.send_message(int(userid), "Что-то пошло не так, попробуйте еще раз")


def start():
    bot.polling(none_stop=True)
