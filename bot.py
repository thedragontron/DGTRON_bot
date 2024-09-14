# This Bot is created to Serve Dragon On Tron - $DGTRON
import os

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? Welcome To Dragon On Tron $DGTRON")

@bot.message_handler(commands=['ca', 'contract_address', 'CA', 'Contract_Address', 'CONTRACT_ADDRESS'])
def send_welcome(message):
    bot.reply_to(message, "https://tronscan.org/#/token20/TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e")

@bot.message_handler(commands=['when', 'WHEN'])
def send_welcome(message):
    bot.reply_to(message, "patience is the key to success. \n" +
    "耐心是成功的关键 \n" +
    "la paciencia es la clave del éxito \n" +
    "धैर्य सफलता की कुंजी है \n" +
    "பொறுமையே வெற்றிக்கு முக்கியமாகும் \n" +
    "సహనం విజయానికి కీలకం \n" +
    "kannatlikkus on edu võti \n" +
    "терпение – ключ к успеху \n" +
    "paciência é a chave para o sucesso\n" +
    "HODL")

@bot.message_handler(commands=['admin', 'ADMIN'])
def send_welcome(message):
    bot.reply_to(message, "Offical admins of $DGTRON \n" +
    "@dragontron_admin \n" +
    "@Prabhafeb16 \n" +
    "@jaysampat \n" +
    "@MVarma \n" +
    "## NOTE: WE DO NOT SEND ANY DIRECT MESSAGES ##")

bot.infinity_polling()
