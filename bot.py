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
TRON_SCAN_URL="https://apilist.tronscanapi.com/api/token_trc20?contract="+os.getenv('DGTRON_ADDRESS')

bot = telebot.TeleBot(BOT_TOKEN)
PRICE_VALUE = 0.0
HOLDERS_VALUE = "200"

ssl._create_default_https_context = ssl._create_unverified_context

buy_messages = ["/add", "/ca", "/buy", "/how","/hodl","/howtobuy","/where","/dgtron","/purchase"]
roadmap_message = ["/where", "/roadmap", "/rp", "/whitepapers","/whitepaper","/wp","/utility"]


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Become a Holder", url="https://sun.io/#/sun_swap/v2?t0=T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb&t1=TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e&type=swap"))
    return markup

def get_latest_Price():
    try:
        response = urllib.request.urlopen(TRON_SCAN_URL)
        contents = response.read()
        json_object = json.loads(contents)
        # print(json_object)
        price_query = jp.parse("$.trc20_tokens[0].market_info.priceInUsd")
        holder_query = jp.parse("$.trc20_tokens[0].holders_count")
        PRICE_VALUE = price_query.find(json_object)[0].value
        HOLDERS_VALUE = holder_query.find(json_object)[0].value 
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    finally:return [PRICE_VALUE,HOLDERS_VALUE]

def manageMessages(message):
    actualValue = message.text.lower()
    chatID = message.chat.id
    if actualValue in ["/start","/hello"]:
        bot.send_message(chatID,"Howdy, how are you doing? Welcome To Dragon On Tron $DGTRON")
    elif actualValue in buy_messages:
        PRICE_VALUE = get_latest_Price()[0]
        HOLDERS_VALUE = str(get_latest_Price()[1])
        bot.send_message(chatID,'''
	<a href="https://dexscreener.com/tron/TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e">$DGTRON</a> | DRAGON on TRON ❤️
                         
	<b>Contract Address</b> :
	TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e
				  
	✅ Listed on <a href="https://sun.io/#/sun_swap/v2?t0=T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb&t1=TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e&type=swap">SUN SWAP</a> 🌞 
				  			  
	<b>Price</b> : ${:.9f}'''.format(PRICE_VALUE)+
    
    '''
	<b>Holders</b> : '''+HOLDERS_VALUE+'''

 	📊 <a href="https://dexscreener.com/tron/TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e">DEX S</a> | 💰 <a href="https://sun.io/#/sun_swap/v2?t0=T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb&t1=TPBEsjyW8gZ72wpkyBF7gQNszKpGnSQT8e&type=swap">BUY</a> | 🐤 <a href="https://x.com/OfficialDGTRON">Twitter</a> | 🕸 <a href="https://thedragontron.meme/">WEBSITE</a>

    ''', 
    parse_mode='html'
    ,reply_markup=gen_markup()
    )
        
    elif actualValue == "/when":
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
    elif actualValue in ["/admin","/contact"]:
         bot.reply_to(message, "Offical admins of $DGTRON \n" +
    "@dragontron_admin \n" +
    "@Prabhafeb16 \n" +
    "@jaysampat \n" +
    "@MVarma \n" +
    "## NOTE: WE DO NOT SEND ANY DIRECT MESSAGES ##")
    elif actualValue in roadmap_message:     
        bot.send_photo(chatID,'https://thedragontron.meme/wp-content/uploads/2024/10/RoadMap.png',
                       '''<a href="https://dgtron.gitbook.io/DGTRON-docs/roadmap/our-roadmap">Click Here for the Road Map</a>'''
                       ,parse_mode='html')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	manageMessages(message)

bot.infinity_polling()
