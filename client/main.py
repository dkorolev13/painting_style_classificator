import telebot

token = "5057381153:AAHPgJ3HpqDKkjrBq4CH1Me0dgClypbqYQk"


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start', 'help'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello Admin!")


    @bot.message_handler(content_types=['photo'])
    def get_photo(message):
        bot.send_message(message.chat.id, "This is photo!")


    bot.polling()
if __name__ == '__main__':
    telegram_bot(token)