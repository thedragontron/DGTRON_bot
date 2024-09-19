# This Bot is created to Serve Dragon On Tron - $DGTRON
import os
import telebot
import urllib.error
from dotenv import load_dotenv
import urllib.request
import ssl
import json
import jsonpath_ng as jp
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
if(BOT_TOKEN is None):
	print("No BOT token")
	exit
TRON_SCAN_URL="https://apilist.tronscanapi.com/api/search/v2?term="+os.getenv('DGTRON_ADDRESS')

bot = telebot.TeleBot(BOT_TOKEN)
PRICE_VALUE = 0.0

ssl._create_default_https_context = ssl._create_unverified_context

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("SunSwap", url="https://sun.io/#/sun_swap/v2?t0=T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb&t1=TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e&type=swap"),
                               InlineKeyboardButton("SunPump", url="https://sunpump.meme/token/TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e"))
    return markup

def get_latest_Price():
    try:
        response = urllib.request.urlopen(TRON_SCAN_URL)
        contents = response.read()
        json_object = json.loads(contents)
        name_query = jp.parse("$.token[0].market_info.priceInUsd")
        result = name_query.find(json_object)
        PRICE_VALUE = result[0].value
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    finally:return PRICE_VALUE

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? Welcome To Dragon On Tron $DGTRON")

@bot.message_handler(commands=['ca','buy','hodl','purchase','how','where','howtobuy','dgtron','$dgtron','CA','BUY','HODL','PURCHASE','HOW','HOWTOBUY','WHERE','DGTRON','$DGTRON','contract_address', 'Contract_Address', 'CONTRACT_ADDRESS'])
def send_welcome(message):
    PRICE_VALUE = get_latest_Price()
    chatID = message.chat.id
    bot.send_message(chatID,'''
	DRAGON on TRON | DGTRON | TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e
				  
				  
	Listed on SunSwap ✅
				  
				  
	Price: ${:.9f}
				  
				  '''.format(PRICE_VALUE),reply_markup=gen_markup())

@bot.message_handler(commands=['when', 'WHEN','contact', 'CONTACT'])
def send_welcome(message):
    bot.reply_to(message, "patience is the key to success. \n" +
    "耐心是成功的关键 \n" +
    "la paciencia es la clave del éxito \n" +
    "धैर्य सफलता की कुंजी है \n" +
    "பொறுத்தார் பூமி ஆள்வார்... \n" +
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
