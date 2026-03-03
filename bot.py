import os
print("TOKEN:", os.environ.get("TOKEN"))
print("ADMIN_ID:", os.environ.get("ADMIN_ID"))
import telebot
import os

TOKEN = os.environ.get("TOKEN")
ADMIN_ID = int(os.environ.get("ADMIN_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    username = message.from_user.username
    text = message.text

    bot.send_message(
        ADMIN_ID,
        f"Новое сообщение от @{username} (ID: {user_id}):\n\n{text}"
    )

@bot.message_handler(commands=['reply'])
def reply_to_user(message):
    if message.from_user.id == ADMIN_ID:
        try:
            parts = message.text.split(" ", 2)
            user_id = int(parts[1])
            reply_text = parts[2]
            bot.send_message(user_id, reply_text)
            bot.send_message(ADMIN_ID, "Ответ отправлен.")
        except:
            bot.send_message(ADMIN_ID, "Ошибка формата. Используй: /reply user_id текст")

bot.infinity_polling()
