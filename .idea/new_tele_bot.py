from openai import OpenAI
import telebot
from telebot.types import Message

# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key="sk-ocZsDK2UM23MfVob1ncrgijjrEytVdeU",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация телеграмм бота с вашим токеном
bot = telebot.TeleBot("6766129487:AAEZ3WRPmlFxVvw2uiZtaYoL8pzFr4I6-ZM")

# Список для хранения истории разговора
conversation_history = []

@bot.message_handler(func=lambda message: True)
def handle_message(message: Message):
    # Получение сообщения от пользователя
    user_input = message.text
    conversation_history.append({"role": "user", "content": user_input})

    # Отправка запроса в нейронную сеть
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation_history
    )

    # Извлечение и отправка ответа нейронной сети
    ai_response_content = chat_completion.choices[0].message.content
    bot.send_message(message.chat.id, f" {ai_response_content}")

    conversation_history.append({"role": "system", "content": ai_response_content})

    if user_input.lower() == 'exit':
        # Выход из цикла, если пользователь ввел 'exit'
        bot.send_message(message.chat.id, "Выход из чата")
        bot.stop_polling()

bot.polling()