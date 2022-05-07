import telebot
from common_data import *
import telebot
from telebot import types  # для указание типов
import config


bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("👨‍💻 Выбрать направление")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот, который поможет тебе развить навыки IT-специалиста и начать карьеру.\n\n ".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет, солнышко!)")
        bot.send_message(message.chat.id, text="😘😘😘")
        bot.send_message(message.chat.id, text="Скорее выбирай интересующее тебя направление!!")
    elif (message.text == "👨‍💻 Выбрать направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Mobile App Developer")
        btn2 = types.KeyboardButton("WEB Developer")
        btn3 = types.KeyboardButton("Database Administrator")
        btn4 = types.KeyboardButton("Machine learning")
        btn5 = types.KeyboardButton("Information Security")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,btn3,btn4,btn5, back)
        bot.send_message(message.chat.id, text="Смотри сколько всего интересного", reply_markup=markup)




    elif (message.text == "Mobile App Developer"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mad1 = types.KeyboardButton("Давай!")
        mad2 = types.KeyboardButton("Нет!")
        markup.add(mad1, mad2)
        bot.send_message(message.chat.id, text="Давай покажу тебе список навыков, которые нужны этому специалисту?", reply_markup=markup)


    elif message.text == "WEB Developer":
        bot.send_message(message.chat.id, text="Добавить навыки")

    elif message.text == "Database Administrator":
        bot.send_message(message.chat.id, text="Добавить навыки")

    elif message.text == "Machine learning":
        bot.send_message(message.chat.id, text="Добавить навыки")

    elif message.text == "Information Security":
        bot.send_message(message.chat.id, text="Добавить навыки")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("👨‍💻 Выбрать направление")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Попробуй что-то ещё, вдруг понравиться!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован...")


bot.polling(none_stop=True)






#bot = telebot.TeleBot(token=token)

#@bot.message_handler(commands=['start','help'])
#def start_message(message):
    #reply = 'Привет, дорогой студент!\n\n' \
    #        'Это бот, который поможет тебе развить навыки IT-специалиста и начать карьеру.\n\n'
    #bot.send_message(message.chat.id, reply)




