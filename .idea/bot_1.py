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
    "/p_dele - Удалить все пробелы из текста",
    "sticker - получите в ответ стикер",
    "/check_number - проверяет число на четность"
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

# Обработчик команды sticker
@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == 'sticker':
        bot.send_sticker(message.chat.id, 'CAADAgADsQADWQMDAAEJK1niI56hlhYE')

# Обработчик команды /check_number
@bot.message_handler(commands=['check_number'])
def handle_check_number(message):
    bot.send_message(message.chat.id, "Введите целое число:")
    bot.register_next_step_handler(message, process_number_step)

# Функция обработки введенного числа
def process_number_step(message):
    try:
        num = int(message.text)  # Преобразуем введенный текст в целое число
        if num % 2 == 0:
            response = f"{num} - четное число"
        else:
            response = f"{num} - нечетное число"
        bot.send_message(message.chat.id, response)  # Отправляем ответ пользователю
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите целое число.")


# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Извините, я не понимаю ваш запрос. Попробуйте использовать команды /help или /p_dele.")

# Обработчик команды /photo
@bot.message_handler(commands=['photo'])
def handle_photo(message):
    photo = open('z1.png', 'rb')  # Открываем фотографию для чтения в двоичном режиме
    bot.send_photo(message.chat.id, photo)  # Отправляем фотографию пользователю
    photo.close()  # Закрываем файл фотографии


# Запускаем бота
bot.polling()
