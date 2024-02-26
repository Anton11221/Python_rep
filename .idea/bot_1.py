import telebot
from telebot import types

# Укажите токен вашего бота
TOKEN = '6766129487:AAEZ3WRPmlFxVvw2uiZtaYoL8pzFr4I6-ZM'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Перечень доступных функций
available_functions = [
    "/start - Начать работу с ботом",
    "/help - Показать список доступных функций",
    "/p_dele - Удалить все пробелы из текста"
]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я бот. Чем могу помочь?")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    functions_list = "\n".join(available_functions)
    bot.reply_to(message, f"Список доступных функций:\n{functions_list}")

# Обработчик команды /p_dele
@bot.message_handler(commands=['p_dele'])
def handle_p_dele(message):
    original_text = message.text[len("/p_dele "):]
    result = original_text.replace(" ", "")
    bot.reply_to(message, f"Результат: {result}")

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Извините, я не понимаю ваш запрос. Попробуйте использовать команды /help или /p_dele.")

# Запускаем бота
bot.polling()
