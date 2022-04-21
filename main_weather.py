# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from bot_weather_command import *

updater = Updater('Token')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('weather', weather_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

print ('server start')

updater.start_polling()
updater.idle()
