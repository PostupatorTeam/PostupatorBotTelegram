import telebot
import Bot.data

users = {}

def generate_markup():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    markup.add('Ye')
    markup.add('No')
    return markup

def registration(message,id):
    if not id in users:
        users[id] = Bot.data.User()

    if users[id].firstName == None:
        users[id].firstName = message
        return

    if users[id].lastName == None:
        users[id].lastName = message





