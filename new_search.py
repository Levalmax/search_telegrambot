import os
import telebot
from config import BOT_TOKEN, dirOfSearch

catalog = dirOfSearch
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет. Введи заводской номер трансформатора. Для справки отправь команду '/help'. ")

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,"Раздел в настоящее время не доступен.")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    searchNumber = message.text
    i = 0
    j = 0
    dictionary = {}
    newDictionary = {}
    for root, dirs, files in os.walk(catalog):
        dictionary[root] = files

    for key in dictionary:
        for names in dictionary[key]:
            all = names.split('_')
            zKey = str(i) + '_' + all[0]
            newDictionary[zKey] = key + '\\' + names
            i += 1

    for number in newDictionary:
        zNumber = number.split('_')
        if zNumber[1] == searchNumber:
            docm = newDictionary[number]
            bot.send_document(message.chat.id, open(docm, 'rb'))
            j += 1
    if j == 0:
        bot.send_message(message.chat.id, 'Файл с таким заводским номером не найден 😔')

bot.polling(none_stop=True, interval=0)

