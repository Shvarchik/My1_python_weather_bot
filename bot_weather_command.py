from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext 
from datetime import datetime,date
from parse_weather import *

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

def time_command(update: Update, context: CallbackContext):
    current_time = datetime.now().time()
    update.message.reply_text(f'today {date.today()}, current time is {current_time.hour}:{current_time.minute}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help\n/weather\n')

def weather_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'температура воздуха:\n{parse_date_temp()}')   
    
    