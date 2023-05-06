# import os
# import telebot
# import texts
#
# BOT_TOKEN = os.environ.get('BOT_TOKEN')
# print(BOT_TOKEN)
#
# bot = telebot.TeleBot(BOT_TOKEN)
#
#
# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, texts.welcome_message)
#
# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, texts.welcome_message)
#
# bot.infinity_polling()


def handler(event, context):
    print('Lambda works')


