import Bot.config
import telebot
import Bot.bot
import Bot.data

bot = telebot.TeleBot(Bot.config.token)

@bot.message_handler(commands=['new'])
def registration(message):
    Bot.bot.users[message.chat.id] = Bot.data.User()
    bot.send_message(message.chat.id,'Введите Имя')

@bot.message_handler()
def reg(message):
    if Bot.bot.users[message.chat.id].firstName == None:
        Bot.bot.users[message.chat.id].firstName = message.text
        bot.send_message(message.chat.id,'Введите фамилию')
        return

    if Bot.bot.users[message.chat.id].lastName == None:
        Bot.bot.users[message.chat.id].lastName = message.text
        markup = Bot.bot.generate_markup()
        bot.send_message(message.chat.id,'Выберите вуз',reply_markup=markup)
        return

    if Bot.bot.users[message.chat.id].university == None:
        Bot.bot.users[message.chat.id].university = message.text
    bot.send_message(message.chat.id,'{0} {1} {2}'.format(Bot.bot.users[message.chat.id].firstName,Bot.bot.users[message.chat.id].lastName,Bot.bot.users[message.chat.id].university))





if __name__ == '__main__':
    bot.polling(none_stop=True)
