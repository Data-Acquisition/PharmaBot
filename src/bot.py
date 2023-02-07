from telebot import types
import telebot
import logging

#@PharmaBot_botbot 
# example
API_TOKEN = '5881308145:AAHQxw09ZrRSTzOchFA2-pM0WhiSHtmz4no'

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)


def web_app_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    web_app_test = types.WebAppInfo('https://17cf-176-52-19-144.eu.ngrok.io')
        # "https://yandex.ru/maps/org/238736570145")
    one_butt = types.KeyboardButton(
        text="Войти", web_app=web_app_test)
    keyboard.add(one_butt)
    return keyboard


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     """Привет! 👋🏻
Я бот сети аптек "Фарма"🔥
Запустить меня можно, нажав на кнопку "Войти".""",
                     reply_markup=web_app_keyboard())


@bot.message_handler(content_types=["text"])
def echo(message):
    start(message)
    
bot.polling()