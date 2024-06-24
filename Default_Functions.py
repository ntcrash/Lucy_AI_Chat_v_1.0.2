##################################################
# Main Functions for Lucy AI ChatBot             #


# Version 1.0.2.3 - Released 2024-06-xx          #

# Version 1.0.2.2 - Released 2024-06-17          #


# Version 1.0.2.3 - Released 2024-06-xx          #

# Author - Lawrence Lutton                       #
##################################################

# Importing libraries
import logging
import logging.handlers
import os
import os.path
import re
import sys
from datetime import datetime
import base64
import googlesearch
import psutil
from typing import Literal, get_args
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver  # to control browser operations
import assistant
import pync
import time
import creds
import telebot
import openai
from googlesearch import search
import search_web as google
from ImageReconition import *
import json
from telebot.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton, MenuButtonDefault, MenuButton, MenuButtonCommands, MessageReactionUpdated, ReactionType, ReactionTypeEmoji
from reminder import *
from macos import *
import python_weather
from datetime import datetime, timedelta
from pymeteosource.api import Meteosource
from pymeteosource.types import tiers
from pymeteosource.types import sections, langs, units
# import venice_openapi
import gpt4all

city_names = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim",
              "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville",
              "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore",
              "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings",
              "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton",
              "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington",
              "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign",
              "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista",
              "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station",
              "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi",
              "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach",
              "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte",
              "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield",
              "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith",
              "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton",
              "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie",
              "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi",
              "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet",
              "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston",
              "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood",
              "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet",
              "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee",
              "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing",
              "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln",
              "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon",
              "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis",
              "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile",
              "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon",
              "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London",
              "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal",
              "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala",
              "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange",
              "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City",
              "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh",
              "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie",
              "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine",
              "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County",
              "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw",
              "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio",
              "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana",
              "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota",
              "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley",
              "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale",
              "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton",
              "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton",
              "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler",
              "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco",
              "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster",
              "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York",
              "Youngstown"]

# Setting up a list for error logging levels.
LogLevel = Literal['Info', 'Error', 'Critical']

filename = 'events.log'

# Adding rollover for log file
should_roll_over = os.path.isfile(filename)
handler = logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=5*1024*1024, backupCount=5)

"""
if should_roll_over:  # log already exists, roll over!
    handler.doRollover()
"""

# Setting up openai api url to my local server gpt4all
openai.base_url = "http://lucyaichatbotapi.loclx.io/v1/"
os.environ["OPENAI_API_KEY"] = "notneeded"

# Checking if the API key is set properly
if not os.getenv("OPENAI_API_KEY"):
    raise Exception("Please set OPENAI_API_KEY environment variable.")


# Creating the Main Logging Function
# Creates a nice Date Stamp for use with Logging.
def date_time_log():
    # datetime object containing current date and time
    now = datetime.now()
    # mm/dd/YY H:M:S
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string
# End DateTime Function


#  Creates a nice Date Stamp for use with Logging.
def date_time_reminder():
    # datetime object containing current date and time
    now = datetime.now()
    # mm/dd/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return dt_string
# End DateTime Function


def write_log(Message, FuncName, ErrorType: LogLevel = "Info"):
    options = get_args(LogLevel)
    assert ErrorType in options, f"'{ErrorType}' is not in {options}"

    TimeStamp: str = date_time_log()
    logger = logging.getLogger(FuncName)
    if ErrorType == 'Info':
        logging.basicConfig(filename=f'{filename}', level=logging.INFO)
        logger.info(repr(TimeStamp) + ": " + repr(Message) + '')
    elif ErrorType == 'Error':
        logging.basicConfig(filename=f'{filename}', level=logging.ERROR)
        logger.error(repr(TimeStamp) + ": " + repr(Message) + '')
    elif ErrorType == 'Critical':
        logging.basicConfig(filename=f'{filename}', level=logging.CRITICAL)
        logger.critical(repr(TimeStamp) + ": " + repr(Message) + '')

    """
    TimeStamp = date_time_log()

    f = open("events.log", "a")
    f.write(repr(TimeStamp) + " " + repr( ErrorType ) + " " + repr( Message ) + '\n')
    f.close()

    #open and read the file after the appending:
    #f = open("events.log", "r")
    #print(f.read())
    """
# End write_log Function


# Had to wait for the correct functions to load before writing event log
write_log(Message='**************************************************', FuncName='Default_Functions', ErrorType='Info')
# write_log(Message=(f"{0:^30}".format("*")), FuncName='Default_Functions', ErrorType='Info')
write_log(Message='Starting Default Functions', FuncName='Default_Functions', ErrorType='Info')


class QA:

    question: str
    answer: str


"""
class QA(telebot):
    

    question: str
    answer: str
"""


# Creating the Telegram function to pass input and output to Lucy
def telegram_ai_chatbot():
    openai.api_key = f"{creds.api_key}"
    write_log(Message='Starting telegram_ai_chatbot Functions', FuncName='telegram_ai_chatbot', ErrorType='Info')

    BOT_TOKEN = f"{creds.BOT_TOKEN}"

    bot = telebot.TeleBot(BOT_TOKEN)

    # Setting api calls to gpt4all
    openai.api_base = "http://localhost:4891/v1/"
    # openai.base_url = "http://lucyaichatbotapi.loclx.io/v1/"
    model = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"

    path = './python1.jpeg'
    path2 = './python2.jpeg'

    # Cleaning up if old files are still there
    if os.path.isfile('./python1.jpeg') is True:
        print("Deleting Image file")
        os.remove("python1.jpeg")
    if os.path.isfile('./python2.jpeg') is True:
        print("Deleting Image file 2")
        os.remove("python2.jpeg")


    print("Telegram Bot Started")

    @bot.message_handler(commands=['start', 'hello', 'like', '👍', 'help', 'testing'])
    def send_welcome(message):
        write_log(Message='Welcome Message', FuncName='telegram_ai_chatbot', ErrorType='Info')
        """markup = InlineKeyboardMarkup()
        like_button = InlineKeyboardButton('👍', callback_data='like')
        markup.add(like_button)"""

        c1 = BotCommand(command='start', description='Start the Bot')
        c2 = BotCommand(command='help', description='Click for Help')
        c3 = BotCommand(command='testing', description='Testing')
        bot.set_my_commands([c1, c2, c3])
        bot.set_chat_menu_button(message.chat.id, MenuButtonCommands('commands'))

        # bot.send_message(message.chat.id, "Do you like this message?", reply_markup=markup)
        if message.text == "/start":
            bot.reply_to(message, "Welcome to Lucy AI Chat Bot")
        elif message.text == "/help":
            bot.reply_to(message, "You can ask this bot any question.\n"
                                  "/start for welcome message\n"
                                  "/help for list of commands (This list)\n"
                                  "You can send a photo to get analysed\n"
                                  "Examples of interactions: \n"
                                  "get weather 'city'\n"
                                  "search wiki 'mount everest'\n"
                                  "set reminder 'Your reminder'\n"
                                  "remind me 'Your reminder'\n"
                                  "mark my calendar 'Your Calendar Event'\n"
                                  "Any plain speech question\n")
        elif message.text == "/testing":
            bot.reply_to(message, "This is for testing purposes, more options to come...")
        elif message.text == '👍':
            bot.reply_to(message, "👍")

    # Main message handler for AI chat.
    @bot.message_handler(func=lambda msg: True)
    def echo_all(message):
        markup = InlineKeyboardMarkup()
        like_button = InlineKeyboardButton('👍', callback_data='like')
        love_button = InlineKeyboardButton('❤️', callback_data='love')
        wow_button = InlineKeyboardButton('😳', callback_data='wow')


        # Build the messages.
        messages = [
            {
                "role": "system",
                "content": "A chat between Lawrence and Lucy an artificial intelligence assistant.\n",
            }
        ]

        question = f"{message.text}\n"
        answer = "\n"
        messages.append({"role": "user", "content": question})
        messages.append({"role": "assistant", "content": answer})

        # Remove the last mock answer.
        messages = messages[:-1]

        # Make the API request
        session = openai.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            max_tokens=4000,
        )

        # bot.reply_to(message, message.text)
        lucy_question = message
        # lucy_question = bot.reply_to(message, message.text)
        print(f"{lucy_question.text.lower()}")


        print(f"{session.choices[0].message.content}")
        lucy_response = f"{session.choices[0].message.content}"

        # Enable this for local chatbot
        # lucy_response = lucy_gui(query=f"{lucy_question.text.lower()}")

        # Enable this for Local GPT4ALL Chatbot
        # lucy_response = lucy_gpt_local(query=f"{lucy_question.text.lower()}")

        # Enable this for ChatGPT chatbot
        # lucy_response = lucy_gpt_chat(query=f"{lucy_question.text.lower()}")

        # This adds the buttons to telegram message
        markup.add(like_button, love_button, wow_button)

        # Sending the message to telegram
        bot.send_message(message.chat.id, f"{lucy_response}", reply_markup=markup)

        # Getting message ID
        lastChatId = message.chat.id
        print(f"{lastChatId}")
        write_log(Message=f"{lastChatId} - {lucy_response}", FuncName='telegram_ai_chatbot', ErrorType='Info')

    # Getting and detecting images
    @bot.message_handler(func=lambda m: True, content_types=['photo'])
    def get_broadcast_picture(message):
        write_log(Message='downloading photo', FuncName='telegram_ai_chatbot', ErrorType='Info')
        file_path = bot.get_file(message.photo[-1].file_id).file_path
        file = bot.download_file(file_path)
        # lastMessageId = message[-1].message_id

        lastChatId = message.chat.id
        with open("python1.jpeg", "wb") as code:
            code.write(file)

        check_file = os.path.isfile(path)
        img = 0
        if check_file is True:
            base64_image = encode_image(image_path="python1.jpeg")

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai.api_key}"
            }

            payload = {
                "model": "gpt-4o",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "What’s in this image?"
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 300
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response_dict = json.loads(response.text)

            # Access the content section
            content = response_dict['choices'][0]['message']['content']

            bot.reply_to(message, f"{content}")

            print(f"{lastChatId}")
            img = stop_sign_recognition(image=f"python1.jpeg")
        if img != 1:
            print(f"{lastChatId}")
            img = face_detector(image=f"python1.jpeg")

        check_file2 = os.path.isfile(path2)
        if check_file2 is True:
            bot.send_photo(chat_id=lastChatId, photo=open("python2.jpeg", "rb"))
            write_log(Message=f"{lastChatId} - Sending photo", FuncName='telegram_ai_chatbot', ErrorType='Info')
        else:
            bot.reply_to(message, f"No match found")

        # Cleaning up if old files are still there
        if os.path.isfile('./python1.jpeg') is True:
            print("Deleting Image file")
            os.remove("python1.jpeg")
        if os.path.isfile('./python2.jpeg') is True:
            print("Deleting Image file 2")
            os.remove("python2.jpeg")

    @bot.message_handler(func=lambda m: True, content_types=['document'])
    def downloader(update, context):
        context.bot.get_file(update.message.document).download()

        # writing to a custom file
        with open("Resources/telegram_file.doc", 'wb') as f:
            context.bot.get_file(update.message.document).download(out=f)

    @bot.callback_query_handler(func=lambda call: call.data == 'like' or call.data == 'love')
    def callback_query(call):
        write_log(Message='callback_query', FuncName='telegram_ai_chatbot', ErrorType='Info')
        if call.data == 'like':
            bot.answer_callback_query(call.id, "You liked this message!")
            bot.send_message(call.message.chat.id, "Thanks for liking the message!")
        elif call.data == 'love':
            bot.answer_callback_query(call.id, "You loved this message!")
            bot.send_message(call.message.chat.id, "Thanks for loving the message!")
        elif call.data == 'wow':
            bot.answer_callback_query(call.id, "You wowed this message!")
            bot.send_message(call.message.chat.id, "Thanks for wowing the message!")

    bot.infinity_polling()
    write_log(Message='Closing Telegram_AI_Chatbot Function', FuncName='Telegram_AI_Chatbot', ErrorType='Info')


# Function to encode the image
def encode_image(image_path):
    write_log(Message='encoding photo for telegram', FuncName='encode_image', ErrorType='Info')
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def reminder(query):
    # TODO need to fix this function to make this work.
    now = datetime.now()
    # Getting time info from query
    if "morning" in query:
        task_time = '8:00:00'
    elif "afternoon" in query:
        task_time = '12:00:00'
    elif "evening" in query:
        task_time = '18:00:00'
    elif "tonight" in query:
        task_time = '21:20:00'
    else:
        task_time = '12:00:00'
    reminder_time = now.strftime(f"%Y-%m-%d {task_time}")
    day = datetime.now().strftime('%A')
    status = "Open"

    mystring = f"{query}"
    keyword = 'remind'
    before_keyword, keyword, after_keyword = mystring.partition(keyword)
    print(before_keyword)
    print(keyword)
    print(after_keyword)
    print(task_time)

    reminder_data = f"1, {after_keyword}, {task_time}, {day}, {status}"

    add_to_reminder(title=f"{query}", body=f"{after_keyword}")
    # set_reminder(reminder_time=f"{reminder_time}", message=f"{after_keyword}")
    # write_reminder_file(reminder_data)
    # return query


def set_calendar(query):
    # TODO need to fix this function to make this work.
    now = datetime.now()
    # Getting time info from query
    if "morning" in query:
        task_time = '8, 00'
    elif "afternoon" in query:
        task_time = '12, 00'
    elif "evening" in query:
        task_time = '18, 00'
    elif "tonight" in query:
        task_time = '21, 20'
    else:
        task_time = '12, 00'
    reminder_time = now.strftime(f"%Y, %m, %d, {task_time}")
    day = datetime.now().strftime('%A')
    status = "Open"

    mystring = f"{query}"
    keyword = 'mark my calendar'
    before_keyword, keyword, after_keyword = mystring.partition(keyword)
    print(before_keyword)
    print(keyword)
    print(after_keyword)
    print(task_time)

    reminder_data = f"1, {after_keyword}, {task_time}, {day}, {status}"

    add_to_calendar(title=f"{after_keyword}", location=f"Remote", event_start=f"{reminder_time}")


def get_weather_updated(city):
    # Change this to your actual API key
    YOUR_API_KEY = f"{creds.YOUR_API_KEY}"
    # Change this to your actual tier
    YOUR_TIER = tiers.FREE

    # Fixes formatting issue
    city = city.replace("'", "")

    # Initialize the main Meteosource object
    meteosource = Meteosource(YOUR_API_KEY, YOUR_TIER)

    # Get the forecast for a given point
    forecast = meteosource.get_point_forecast(
        # lat=None,  # Latitude of the point
        # lon=-None,  # Longitude of the point
        place_id=f"{city}",  # You can specify place_id instead of lat+lon
        sections=[sections.CURRENT, sections.HOURLY],  # Defaults to '("current", "hourly")'
        tz='US/Pacific',  # Defaults to 'UTC', regardless of the point location
        lang=langs.ENGLISH,  # Defaults to 'en'
        units=units.US  # Defaults to 'auto'

    )
    temp = (forecast.current['temperature'])
    sky = (forecast.current['summary'])
    wind = (forecast.current['wind']['speed'])
    wind_dir = (forecast.current['wind']['dir'])

    # print(forecast.hourly[0]['temperature'])
    # print(forecast.current['temperature'] + "F")
    # print(forecast.current['summary'])
    # print(forecast.current['cloud_cover'])
    # print(forecast.current['wind']['speed'] + "mph")
    print(f"Here is the current weather for {city}, "
          f"{temp}F, Skies are {sky}, wind is {wind}mph, coming in from the {wind_dir}")
    return (f"Here is the current weather for {city}, "
            f"{temp}F, Skies are {sky}, wind is {wind}mph, coming in from the {wind_dir}")


# get weather
def get_weather(city):
    write_log(Message='getting weather info', FuncName='get_weather', ErrorType='Info')
    print(city)
    city = city.replace("'", "")
    if city is None:
        # enter city name
        city = "Boise"

    # create url
    url = "https://www.google.com/search?q=" + "weather" + "+" + city
    print(url)
    # requests instance
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')

    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    weather = (f"{data}" + f" {temp}")
    return weather
# End get weather


def get_city_for_weather(query):
    write_log(Message='Starting get_city_for_weather Functions', FuncName='get_city_for_weather', ErrorType='Info')
    citynames: str = (
        'Aberdeen|Abilene|Akron|Albany|Albuquerque|Alexandria|Allentown|Amarillo|Anaheim|Anchorage|Ann '
        'Arbor|Antioch|Apple Valley|Appleton|Arlington|Arvada|Asheville|Athens|Atlanta|Atlantic '
        'City|Augusta|Aurora|Austin|Bakersfield|Baltimore|Barnstable|Baton Rouge|Beaumont|Bel '
        'Air|Bellevue|Berkeley|Bethlehem|Billings|Birmingham|Bloomington|Boise|Boise City|Bonita '
        'Springs|Boston|Boulder|Bradenton|Bremerton|Bridgeport|Brighton|Brownsville|Bryan|Buffalo|Burbank|Burlington'
        '|Cambridge|Canton|Cape Coral|Carrollton|Cary|Cathedral City|Cedar '
        'Rapids|Champaign|Chandler|Charleston|Charlotte|Chattanooga|Chesapeake|Chicago|Chula Vista|Cincinnati|Clarke '
        'County|Clarksville|Clearwater|Cleveland|College Station|Colorado Springs|Columbia|Columbus|Concord|Coral '
        'Springs|Corona|Corpus Christi|Costa Mesa|Dallas|Daly City|Danbury|Davenport|Davidson County|Dayton|Daytona '
        'Beach|Deltona|Denton|Denver|Des Moines|Detroit|Downey|Duluth|Durham|El Monte|El Paso|Elizabeth|Elk '
        'Grove|Elkhart|Erie|Escondido|Eugene|Evansville|Fairfield|Fargo|Fayetteville|Fitchburg|Flint|Fontana|Fort '
        'Collins|Fort Lauderdale|Fort Smith|Fort Walton Beach|Fort Wayne|Fort '
        'Worth|Frederick|Fremont|Fresno|Fullerton|Gainesville|Garden Grove|Garland|Gastonia|Gilbert|Glendale|Grand '
        'Prairie|Grand Rapids|Grayslake|Green Bay|GreenBay|Greensboro|Greenville|Gulfport-Biloxi|Hagerstown|Hampton'
        '|Harlingen|Harrisburg|Hartford|Havre de Grace|Hayward|Hemet|Henderson|Hesperia|Hialeah|Hickory|High '
        'Point|Hollywood|Honolulu|Houma|Houston|Howell|Huntington|Huntington '
        'Beach|Huntsville|Independence|Indianapolis|Inglewood|Irvine|Irving|Jackson|Jacksonville|Jefferson|Jersey '
        'City|Johnson City|Joliet|Kailua|Kalamazoo|Kaneohe|Kansas '
        'City|Kennewick|Kenosha|Killeen|Kissimmee|Knoxville|Lacey|Lafayette|Lake '
        'Charles|Lakeland|Lakewood|Lancaster|Lansing|Laredo|Las Cruces|Las '
        'Vegas|Layton|Leominster|Lewisville|Lexington|Lincoln|Little Rock|Long Beach|Lorain|Los '
        'Angeles|Louisville|Lowell|Lubbock|Macon|Madison|Manchester|Marina|Marysville|McAllen|McHenry|Medford'
        '|Melbourne|Memphis|Merced|Mesa|Mesquite|Miami|Milwaukee|Minneapolis|Miramar|Mission '
        'Viejo|Mobile|Modesto|Monroe|Monterey|Montgomery|Moreno Valley|Murfreesboro|Murrieta|Muskegon|Myrtle '
        'Beach|Naperville|Naples|Nashua|Nashville|New Bedford|New Haven|New London|New Orleans|New York|New York '
        'City|Newark|Newburgh|Newport News|Norfolk|Normal|Norman|North Charleston|North Las Vegas|North '
        'Port|Norwalk|Norwich|Oakland|Ocala|Oceanside|Odessa|Ogden|Oklahoma '
        'City|Olathe|Olympia|Omaha|Ontario|Orange|Orem|Orlando|Overland Park|Oxnard|Palm Bay|Palm '
        'Springs|Palmdale|Panama City|Pasadena|Paterson|Pembroke '
        'Pines|Pensacola|Peoria|Philadelphia|Phoenix|Pittsburgh|Plano|Pomona|Pompano Beach|Port Arthur|Port '
        'Orange|Port Saint Lucie|Port St. Lucie|Portland|Portsmouth|Poughkeepsie|Providence|Provo|Pueblo|Punta '
        'Gorda|Racine|Raleigh|Rancho Cucamonga|Reading|Redding|Reno|Richland|Richmond|Richmond '
        'County|Riverside|Roanoke|Rochester|Rockford|Roseville|Round Lake Beach|Sacramento|Saginaw|Saint Louis|Saint '
        'Paul|Saint Petersburg|Salem|Salinas|Salt Lake City|San Antonio|San Bernardino|San Buenaventura|San Diego|San '
        'Francisco|San Jose|Santa Ana|Santa Barbara|Santa Clara|Santa Clarita|Santa Cruz|Santa Maria|Santa '
        'Rosa|Sarasota|Savannah|Scottsdale|Scranton|Seaside|Seattle|Sebastian|Shreveport|Simi Valley|Sioux City|Sioux '
        'Falls|South Bend|South Lyon|Spartanburg|Spokane|Springdale|Springfield|St. Louis|St. Paul|St. '
        'Petersburg|Stamford|Sterling Heights|Stockton|Sunnyvale|Syracuse|Tacoma|Tallahassee|Tampa|Temecula|Tempe'
        '|Thornton|Thousand Oaks|Toledo|Topeka|Torrance|Trenton|Tucson|Tulsa|Tuscaloosa|Tyler|Utica|Vallejo|Vancouver'
        '|Vero Beach|Victorville|Virginia Beach|Visalia|Waco|Warren|Washington|Waterbury|Waterloo|West Covina|West '
        'Valley City|Westminster|Wichita|Wilmington|Winston|Winter Haven|Worcester|Yakima|Yonkers|York|Youngstown')
    checkCity = re.findall(citynames, query, flags=re.IGNORECASE)
    checkCityFixed = str(checkCity)[1:-1]
    write_log(Message='Closing get_city_for_weather Functions', FuncName='get_city_for_weather', ErrorType='Info')
    return checkCityFixed


def get_application_name(query):
    write_log(Message='Starting get_application_name Functions', FuncName='get_application_name', ErrorType='Info')
    application_names = 'Chrome|Notes|'
    checkapplication_names = re.findall(application_names, query, flags=re.IGNORECASE)
    checkapplication_namesFixed = str(application_names)[1:-1]
    write_log(Message='Closing get_application_name Functions', FuncName='get_application_name', ErrorType='Info')
    return checkapplication_namesFixed


def search_google(query):
    # set query to search for in Google
    # query = "long winter coat"
    # execute query and store search results
    # results = search(query, tld="com", lang="en", stop=3, pause=2)
    results = search(query, lang='en', num_results=5)
    # iterate over all search results and print them
    for result in results:
        print(result)
        return result


# gets web search results in a text file from Wiki
def get_wiki_search(search):
    import urllib.request
    from bs4 import BeautifulSoup

    mystring = f"{search}"
    keyword = 'search wiki '
    before_keyword, keyword, after_keyword = mystring.partition(keyword)
    print(before_keyword)
    print(keyword)
    print(after_keyword)

    fixed_search = after_keyword.replace(" ", "_")
    search_result = "search_text_file.txt"
    cleaned_search = "cleaned_search.txt"

    # here we have to pass url and path
    # (where you want to save your text file)
    print(f"https://en.wikipedia.org/wiki/{fixed_search}")
    urllib.request.urlretrieve(f"https://en.wikipedia.org/wiki/{fixed_search}",
                               f"{search_result}")

    file = open(f"{search_result}", "r")
    contents = file.read()
    soup = BeautifulSoup(contents, 'html.parser')

    f = open(f"{cleaned_search}", "w")

    # traverse paragraphs from soup
    for data in soup.find_all("p"):
        sum = data.get_text()
        f.writelines(sum)

    f.close()


# Lucy function
def lucy_gui(query):
    write_log(Message='Starting Lucy Functions', FuncName='Lucy', ErrorType='Info')
    from chatterbot import ChatBot
    chatbot = ChatBot(
        "Lucy",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri='sqlite:///site////lucy.sqlite3',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am not sure how to respond to that, I am still learning',
                'maximum_similarity_threshold': 0.40
            }
        ]
    )

    # Trainer
    """
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    trainer = ListTrainer(chatbot)
    trainer.train([
        "Hi",
        "Hello, I am Lucy!!! 🤗",
    ])
    trainer.train([
        "What is your name?",
        "I am Lucy!!! 🤗",
    ])
    data = pd.read_csv("dialogs.csv", index_col="Index")
    i = 0
    for row in data.index:
        # retrieving row by loc method
        first = (data['question'].values[i])
        second = (data['answer'].values[i])

        # Adding info from the csv file for training...
        question = f'{first}'
        answer = f'{second}'

        # print(f"{question}", f"{answer}")
        trainer.train([
            f"{question}",
            f"{answer}",
        ])
        i += 1
    """

    exit_conditions = (":q", "quit", "exit")

    if query in exit_conditions:
        speech = f"Goodbye"
        print(f"🤪 {speech}")
        write_log(Message='Closing Lucy Functions', FuncName='Lucy', ErrorType='Info')
        return f"🤪 {speech}"
    elif 'get weather' in query or 'what is the weather' in query:
        checkCityFixed = get_city_for_weather(query=query)

        if checkCityFixed is None:
            speech = f"What City would you like me to check for you?"
            print(f"🤪 {speech}")

            speech = f"Getting weather for {checkCityFixed}! Please wait a second..."
            print(f"🤪 {speech}")

        weather = get_weather_updated(city=f"{checkCityFixed}")
        # weather = get_weather(city=f"{checkCityFixed}")
        print(f"🤪 Here is your weather {weather}")
        speech = f"Here is your weather for {checkCityFixed} {weather}"
        write_log(Message='Closing Lucy Functions', FuncName='Lucy', ErrorType='Info')
        return f"🤪 {speech}"
    elif 'get wiki search' in query or 'search wiki' in query:
        print(f"Lucy search wiki: {query}")
        get_wiki_search(search=f"{query}")

        write_log(Message=f'getting results from wiki - {query}', FuncName='Lucy', ErrorType='Info')
        write_log(Message='closing Lucy', FuncName='Lucy', ErrorType='Info')
        cleaned_search = "cleaned_search.txt"
        search_results_wiki = open(f"{cleaned_search}", "r")
        # search_results_wiki.close()
        return f"{search_results_wiki}"
    elif 'search' in query or 'youtube' in query or 'wikipedia' in query:
        # search_google(query)
        # Download images example
        html = google.search(f"{query}")

        print(f"🤪 Here is your web search")
        speech = f"Here is your web search"
        # text_to_speech(text=speech)
        write_log(Message='Closing Lucy Functions', FuncName='Lucy', ErrorType='Info')
        return f"🤪 {html}"
    elif 'remind me' in query or 'set reminder' in query:
        write_log(Message='Adding reminder Lucy Functions', FuncName='Lucy', ErrorType='Info')
        print(f"This is the input - {query}")
        reminder(query=f"{query}")

        print(f"🤪 Setting Reminder")
        speech = f"Setting your reminder now"
        write_log(Message='Closing Lucy Functions', FuncName='Lucy', ErrorType='Info')
        return f"🤪 {speech}"
    elif 'mark my calendar' in query or 'set my calendar' in query:
        write_log(Message='setting a reminder', FuncName='Lucy_GUI', ErrorType='Info')
        print(f"This is the input - {query}")
        print(f"ChatGPT Calendar: {query}")

        set_calendar(query=f"{query}")

        write_log(Message=f'setting a calendar - {query}', FuncName='Lucy', ErrorType='Info')
        write_log(Message='closing Lucy_GUI', FuncName='Lucy_GUI', ErrorType='Info')
        return "Setting your calendar now"
    else:
        speech = f"{chatbot.get_response(query)}"
        print(f"🤪 {speech}")
        write_log(Message='Closing Lucy Functions', FuncName='Lucy', ErrorType='Info')
        return f"🤪 {speech}"
# End Lucy


def lucy_gpt_chat(query):
    write_log(Message='Starting lucy_GPT_chat', FuncName='lucy_gpt_chat', ErrorType='Info')
    openai.api_key = f"{creds.api_key}"
    messages = [{"role": "system", "content":
                "You are Lucy a intelligent assistant."}]
    while True:
        message = f"{query}"
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content

        if 'remind me' in query:
            write_log(Message='setting a reminder', FuncName='lucy_gpt_chat', ErrorType='Info')
            print(f"This is the input - {query}")
            print(f"ChatGPT Reminder: {query}")

            reminder(query=f"{query}")
            messages.append({"role": "assistant", "content": "Setting your reminder now"})
            # messages.append({"role": "assistant", "content": reply})
            write_log(Message=f'setting a reminder - {query}', FuncName='lucy_gpt_chat', ErrorType='Info')
            write_log(Message='closing lucy_GPT_chat', FuncName='lucy_gpt_chat', ErrorType='Info')
            return "Setting your reminder now"
        elif 'set a reminder' in query:
            print(f"This is the input - {query}")
            print(f"ChatGPT Reminder: {query}")
            reminder(query=f"{query}")
            messages.append({"role": "assistant", "content": "Setting your reminder now"})
            # messages.append({"role": "assistant", "content": reply})
            write_log(Message=f'setting a reminder - {query}', FuncName='lucy_gpt_chat', ErrorType='Info')
            write_log(Message='closing lucy_GPT_chat', FuncName='lucy_gpt_chat', ErrorType='Info')
            return "Setting your reminder now"
        elif 'get wiki search' in query or 'search wiki' in query:
            print(f"ChatGPT search wiki: {query}")
            get_wiki_search(search=f"{query}")
            # messages.append({"role": "assistant", "content": "getting results from wiki"})
            # messages.append({"role": "assistant", "content": reply})
            write_log(Message=f'getting results from wiki - {query}', FuncName='lucy_gpt_chat', ErrorType='Info')
            write_log(Message='closing lucy_GPT_chat', FuncName='lucy_gpt_chat', ErrorType='Info')
            cleaned_search = "cleaned_search.txt"
            search_results_wiki = open(f"{cleaned_search}", "r")
            # search_results_wiki.close()
            return f"{search_results_wiki}"
        elif 'mark my calendar' in query or 'set my calendar' in query:
            write_log(Message='setting a reminder', FuncName='lucy_gpt_chat', ErrorType='Info')
            print(f"This is the input - {query}")
            print(f"ChatGPT Calendar: {query}")

            set_calendar(query=f"{query}")
            # messages.append({"role": "assistant", "content": "Setting your calendar now"})
            # messages.append({"role": "assistant", "content": reply})
            write_log(Message=f'setting a calendar - {query}', FuncName='lucy_gpt_chat', ErrorType='Info')
            write_log(Message='closing lucy_GPT_chat', FuncName='lucy_gpt_chat', ErrorType='Info')
            return "Setting your calendar now"
        elif 'get weather' in query or 'what is the weather' in query:
            write_log(Message=f'getting weather - {query}', FuncName='lucy_gpt_chat', ErrorType='Info')
            checkCityFixed = get_city_for_weather(query=query)
            print(checkCityFixed)
            if checkCityFixed is None:
                # Setting Default City to Boise
                checkCityFixed = "Boise"

            weather = get_weather_updated(city=f"{checkCityFixed}")
            # weather = get_weather(city=f"{checkCityFixed}")
            print(f"🤪 Here is your weather {weather}")
            speech = f"Here is your weather for {checkCityFixed} {weather}"
            messages.append({"role": "assistant", "content": speech})
            write_log(Message=f'{speech}', FuncName='lucy_gpt_chat', ErrorType='Info')
            return speech
        else:
            print(f"ChatGPT: {reply}")
            messages.append({"role": "assistant", "content": reply})
            write_log(Message=f"ChatGPT: {reply}", FuncName='lucy_gpt_chat', ErrorType='Info')
            write_log(Message='closing lucy_GPT_chat', FuncName='lucy_gpt_chat', ErrorType='Info')
            return reply


def lucy_gpt_local(query):
    from pathlib import Path
    from gpt4all import GPT4All

    model_name = 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'
    # model_name = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
    model_path = Path.home() / 'Library/Application Support/nomic.ai/GPT4All/'
    model = GPT4All(model_name=model_name, model_path=model_path)
    system_template = 'A chat between Lawrence and Lucy an artificial intelligence assistant.\n'
    # prompt_template = f'USER: {query}\n\nASSISTANT: \n\n'
    # with model.chat_session(system_template, prompt_template):
    with model.chat_session(system_template):
        response1 = model.generate(f'{query}', max_tokens=1900)
        print(response1)
        print()
        # response2 = model.generate('why is the sky blue?')
        # print(response2)
        return f"{response1}"


def lucy_gpt_local_testing(query):
    from pathlib import Path
    from gpt4all import GPT4All

    model_name = 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'
    # model_name = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
    model_path = Path.home() / 'Library/Application Support/nomic.ai/GPT4All/'
    model = GPT4All(model_name=model_name, model_path=model_path)
    system_template = 'A chat between Lawrence and Lucy an artificial intelligence assistant.\n'
    tokens = []
    with model.chat_session():
        for token in model.generate(f"{query}", streaming=True):
            tokens.append(token)
    print(tokens)

def website():
    # reflex init
    # reflex run
    import reflex as rx

    def index() -> rx.Component:
        return rx.container(
            rx.box(
                "What is Reflex?",
                # The user's question is on the right.
                text_align="right",
            ),
            rx.box(
                "A way to build web apps in pure Python!",
                # The answer is on the left.
                text_align="left",
            ),
        )

    # Add state and page to the app.
    app = rx.App()
    app.add_page(index)
    app.compile()

write_log(Message='Finished loading all Default Functions Successfully', FuncName='Default_Functions', ErrorType='Info')
