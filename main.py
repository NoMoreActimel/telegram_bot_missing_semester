import telebot
from os import environ

token_file = open("token.txt", 'r')

token = environ.get('API')
bot = telebot.TeleBot(token_file.readline())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "hello bastard!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
