import config

import telebot

bot = telebot.TeleBot(config.id)

@bot.message_handler(commands=['start','старт'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я храню информацию о том, что лежит в твоем холодильнике')

@bot.message_handler(commands=['add','добавить'])
def send_add(message):
    msg = bot.send_message(message.chat.id, 'Введите продукт')
    @bot.message_handler(content_types=['text'])
    def add_food(message):
        food = message.text
        user = message.chat.id
        #print(food)
        msg = bot.send_message(message.chat.id,user)

bot.polling()