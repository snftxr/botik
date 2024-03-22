import telebot # подключение библиотек
import os
import random
from telebot import types
# универсальный токен 
token='7100074310:AAFD0mOeodQ4yiWy_dlROoee0_Q_aqIeTMg'

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn4 = types.InlineKeyboardButton(text='Меню', callback_data='menuu')
    markup.add(btn4)
    bot.send_message(message.chat.id, text='Привет! Ты попал в gm бот. Я умею отправлять открытки и считать дни до твоей смерти', reply_markup=markup)

def menu(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='help', callback_data='helpp')
    btn2 = types.InlineKeyboardButton(text='Получить открытку', callback_data='dobroeytro')
    btn3 = types.InlineKeyboardButton(text='Получить дату смерти', callback_data='ymer')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0}! Выбери, что ты хочешь сделать".format(message.chat.first_name), reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    
    if callback.data == 'helpp':
        bot.send_message(callback.message.chat.id, text='Привет! ты попал в gm бот. Я умею отправлять рандомные открытки и определять твою дату смерти.')
    if callback.data == 'dobroeytro':
        photo = open('lox/' + random.choice(os.listdir('lox')), 'rb')
        bot.send_photo(callback.message.chat.id, photo)
        menu(callback.message)
    if callback.data == 'ymer':
        random_year = random.randint(2000, 3000)
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)  
        random_date = "{0}.{1}.{2}".format(random_day, random_month, random_year)
        bot.send_message(callback.message.chat.id, text='Твоя дата смерти ' + random_date)
        menu(callback.message)
    if callback.data == 'menuu':
        menu(callback.message)
   
bot.infinity_polling()