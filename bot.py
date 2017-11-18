# импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# !!! обязательно прописать чтобы был лог файл для поиска ошибок
import logging
logging.basicConfig(format = '%(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log',
                    )

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    updater = Updater('436444787:AAGatvt8WUVE_gnxzX_8RLtaApTz7k-CCZQ')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    
    # print(update)
    # print('Вызван /start')

    text = 'Вызван /start'
    print(text)
    # print(1/0) тестировали ошибку
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)

# Вызываем функцию - эта строчка собственно запускает бота
main()
