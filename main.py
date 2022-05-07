import telebot
from common_data import *

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start','help'])
def start_message(message):
    reply = 'Привет, дорогой студент!\n\n' \
            'Это бот, который поможет тебе развить навыки IT-специалиста и начать карьеру.\n\n'
    bot.send_message(message.chat.id, reply)



bot.polling()
