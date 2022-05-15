import telebot
from common_data import *
import telebot
from telebot import types  # для указание типов

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
        bot.send_message(message.chat.id, text="Смотри сколько всего интересного!", reply_markup=markup)


    elif (message.text == "Mobile App Developer"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Смотреть 👀', url='https://cerulean-nephew-71d.notion.site/Mobile-App-Developer-7b9d1d43c9934ed18cdb25f26e92e758')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Давай покажу тебе, что нужно этому специалисту? По ссылке ты найдёшь всю информацию, удачи!", reply_markup=markup)


    elif (message.text == "WEB Developer"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Смотреть 👀', url='https://cerulean-nephew-71d.notion.site/WEB-Developer-75fcd595a4724baa815431c9540da91f')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Давай покажу тебе, что нужно этому специалисту? По ссылке ты найдёшь всю информацию, удачи!", reply_markup=markup)


    elif (message.text == "Database Administrator"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Смотреть 👀', url='https://cerulean-nephew-71d.notion.site/Database-Administrator-1e311adc8e3f4f549f0127443892f3fa')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Давай покажу тебе, что нужно этому специалисту? По ссылке ты найдёшь всю информацию, удачи!", reply_markup=markup)


    elif (message.text == "Machine learning"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Смотреть 👀', url='https://cerulean-nephew-71d.notion.site/12c89284ae4f4dddb0d0ce007a1e87b6')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Давай покажу тебе, что нужно этому специалисту? По ссылке ты найдёшь всю информацию, удачи!", reply_markup=markup)


    elif message.text == "Information Security":
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Смотреть 👀', url='https://cerulean-nephew-71d.notion.site/7055119020a142a1ba66e76c1a30beb0')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Давай покажу тебе, что нужно этому специалисту? По ссылке ты найдёшь всю информацию, удачи!", reply_markup=markup)


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("👨‍💻 Выбрать направление")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Попробуй что-то ещё, вдруг понравиться!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован...")


bot.polling(none_stop=True)







