import telebot
from config import TOKEN
from telebot import types
from random import *


bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('Инфо', "Рандомное число", "Чем занят?", "Как дела?","Где вы проживаете" )


@bot.message_handler(commands = ['start'])
def welcome(message):
    sti = open("stiker/sticker.webp", 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                    'Добро пожаловать {0.first_name}! \n Я ' ' <b>{1.first_name}</b> Ваш бот '.format(
                        message.from_user, bot.get_me()),
                        parse_mode='html', reply_markup=markup
                        )


@bot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Инфо':
            msg = 'Бот служит для общения и обучения. И ты тоже обучайся!'
            bot.send_message(message.chat.id, msg)

        elif message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(randint(1, 1000)))
        elif message.text == 'Чем занят?':
            spisok_del = ['Учу программирование', "Смотрю Netflix", "Готовлю ужин"]

            bot.send_message(message.chat.id, choice(spisok_del))
        
        elif message.text == 'Как дела?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Отлично!', callback_data='good')
            item2 = types.InlineKeyboardButton('Фигово!', callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Офигенно! Как у тебя?', reply_markup=markup)

        elif message.text =="Где вы проживаете":
            marku =types.InlineKeyboardMarkup(row_width=3)
            country1 =types.InlineKeyboardButton("Кызгызстан",callback_data='kg')
            country2 =types.InlineKeyboardButton("Казахстан",callback_data='kz')
            country3 =types.InlineKeyboardButton("Узбекистан",callback_data='uz')
            marku.add(country1,country2,country3)
            bot.send_message(message.chat.id, 'Выберите:', reply_markup=marku)



markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Офигенно! Как у тебя?', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Я рад!')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Фигня случается. Не растраивайся!')
                bot.edit_message_text(chat_id=call.message.message_id, text='Как дела?', reply_markup=None)
            
            elif call.data =='kg':
                bot.send_message(call.message.chat.id, "996")
            elif call.data =='kz':
                bot.send_message(call.message.chat.id, "995")
            elif call.data =='uz':
                bot.send_message(call.message.chat.id, "994")
    except Exception as e:
        print(repr(e))

bot.polling(non_stop=True)
