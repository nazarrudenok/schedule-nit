import telebot
import json
import datetime
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    cht = message.chat.id

    bot.send_message(cht, f'/schedule - розклад дзвінків\n/timetable_1 - розклад уроків для 1 групи\n/timetable_2 - розклад уроків для 2 групи')


@bot.message_handler(commands=['schedule'])
def get_schedule(message):
    cht = message.chat.id

    with open('_jsons/schedule.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        result_list = [data[f'{i}'] for i in data]

        result_string = ''

        for i, item in enumerate(result_list, start=1):
            result_string += f"{i}. {item}\n"

        bot.send_message(cht, result_string)

@bot.message_handler(commands=['timetable_2'])
def get_timetable_1(message):
    cht = message.chat.id

    current_date = datetime.datetime.now()
    day = current_date.strftime("%A")

    with open('_jsons/timetable group 2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        num = 1
        result_string = ''
        for i in data:
            if i == day:
                for subject in data[i]:
                    result_string += f"{num}. {subject}\n"
                    num += 1

        bot.send_message(cht, result_string)


@bot.message_handler(commands=['timetable_1'])
def get_timetable_1(message):
    cht = message.chat.id

    current_date = datetime.datetime.now()
    day = current_date.strftime("%A")

    with open('_jsons/timetable group 1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        num = 1
        result_string = ''
        for i in data:
            if i == day:
                for subject in data[i]:
                    result_string += f"{num}. {subject}\n"
                    num += 1

        bot.send_message(cht, result_string)

bot.polling()