##################################################
# Reminder Function for Lucy AI chat             #
# Version 1.0.2.1 - Released 2024-06-08          #
# Author - Lawrence Lutton                       #
##################################################

import time
import threading
from datetime import datetime, timedelta
import creds
import telebot
import openai
# from Default_Functions import write_log

# write_log(Message='Starting Reminders Functions', FuncName='Reminders', ErrorType='Info')


def set_reminder(reminder_time, message):
    now = datetime.now()
    # reminder_time = datetime.strptime(reminder_time, '%Y-%m-%d %H:%M:%S')
    delay = (reminder_time - now).total_seconds()

    if delay <= 0:
        print("The reminder time has already passed.")
        return

    print(f"Reminder set for {reminder_time}")
    threading.Timer(delay, show_reminder, [message]).start()


def show_reminder(message):
    openai.api_key = f"{creds.api_key}"
    BOT_TOKEN = f"{creds.BOT_TOKEN}"
    bot = telebot.TeleBot(BOT_TOKEN)

    print(f"\nReminder: {message}")

    # Create bot
    bot = telebot.TeleBot(token=BOT_TOKEN)

    # Send message
    bot.send_message(5686752435, f"\nReminder: {message}")


"""
if __name__ == "__main__":
    while True:
        reminder_time = input("Enter the reminder time (YYYY-MM-DD HH:MM:SS): ")
        message = input("Enter the reminder message: ")
        set_reminder(reminder_time, message)

        another = input("Do you want to set another reminder? (yes/no): ").lower()
        if another != 'yes':
            break
"""