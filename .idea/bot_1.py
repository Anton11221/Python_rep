import telebot
from telebot import types

# Укажите токен вашего бота
TOKEN = '6766129487:AAEZ3WRPmlFxVvw2uiZtaYoL8pzFr4I6-ZM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()