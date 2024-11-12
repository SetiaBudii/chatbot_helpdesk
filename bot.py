from dotenv import load_dotenv
import os
import telebot
from telebot.types import Message

load_dotenv()

# Ganti dengan token API bot yang diberikan oleh BotFather
token = os.getenv('API_TOKEN')

# Inisialisasi bot
bot = telebot.TeleBot(token)

# Fungsi untuk menangani pesan yang mengandung kata "Halo bot"
@bot.message_handler(func=lambda message: "Halo bot" in message.text)
def greet(message: Message):
    # Membalas dengan pesan ke grup
    bot.reply_to(message, "Halo! Ada yang bisa dibantu?")

# Fungsi untuk menangani perintah /start dalam grup
@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message, "Bot sudah siap di grup ini!")

# Memulai bot untuk terus memonitor pesan
bot.polling()
