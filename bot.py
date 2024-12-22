
import telebot
from gtts import gTTS
import os

TOKEN = '7473518120:AAEymiYOm7bUhwjOwGibZ6AGsaNldbVPZMs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"سلام {message.chat.first_name}! من آماده‌ام که بهت کمک کنم. هر سوالی داری بپرس.")

bot.polling()
