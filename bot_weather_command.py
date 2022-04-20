from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext,  CallbackQueryHandler

from datetime import datetime,date
from parse_weather import *

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi, {update.effective_user.first_name}! Я погодный бот.')

def echo(update: Update, context: CallbackContext):
    if update.message.text[-1] == '?':
        update.message.reply_text('Конечно можно спросить! Только я культурно промолчу...')
    else:
        update.message.reply_text('Я плохой собеседник, вот погоду - пожалуйста, жми /weather')

def time_command(update: Update, context: CallbackContext):
    current_time = datetime.now().time()
    update.message.reply_text(f'today {date.today()}, current time is {current_time.hour}:{current_time.minute}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help\n/weather\n')

def weather_command(update: Update, context: CallbackContext):
    update.message.reply_text('Погода в каком городе тебя интересует?')
    keyboard = [[InlineKeyboardButton("Москва", callback_data='Москва'), InlineKeyboardButton("Питер", callback_data='Питер')]]
    reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text('Пожалуйста, выбери город:', reply_markup=reply_markup)
    

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    query.answer()
    if variant == "Москва":
        arg=1
    elif variant == "Питер":
        arg=2
    
    query.edit_message_text(text=f"{variant}:\n температура воздуха:\n {parse_date_temp(arg)}")

    
    
