import Bot.config
import telebot

bot = telebot.TeleBot(Bot.config.token)

@bot.message_handler(commands=['game'])
def hello(message):
    markup = generate_markup()
    bot.send_message(message.chat.id,'q',reply_markup=markup)


def generate_markup():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    markup.add('Ye')
    markup.add('No')
    return markup

if __name__ == '__main__':
    bot.polling(none_stop=True)
