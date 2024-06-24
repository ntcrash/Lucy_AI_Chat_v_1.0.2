##################################################
# Reminder and calendar feature Lucy AI ChatBot  #
# Version 1.0.2.2 - Released 2024-06-11          #
# Author - Lawrence Lutton                       #
##################################################

from appscript import app, k
from datetime import datetime, timedelta
# rom Default_Functions import write_log

# write_log(Message='Starting macos Functions', FuncName='macos_Functions', ErrorType='Info')


def add_to_calendar(title, location, event_start):
    # Get the Calendar app
    calendar = app('Calendar')

    # Select the calendar to add events to
    calendars = calendar.calendars()
    calendar_name = "Work"  # Change this to your desired calendar name
    selected_calendar = None

    for cal in calendars:
        if cal.name.get() == calendar_name:
            selected_calendar = cal
            break

    if not selected_calendar:
        print(f"Calendar '{calendar_name}' not found.")
        exit(1)

    # Create the event details
    event_title = f"{title}"
    event_location = f"{location}"
    # event_start = datetime(2024, 6, 11, 10, 0)  # Event start date and time
    event_end = event_start + timedelta(hours=1)  # Event duration

    # Add the event to the calendar
    event = selected_calendar.make(
        new=k.event,
        with_properties={
            k.summary: event_title,
            k.location: event_location,
            k.start_date: event_start,
            k.end_date: event_end,
        }
    )

    print(f"Event '{event_title}' added to the calendar '{calendar_name}'.")


def add_to_reminder(title, body):
    # write_log(Message='Adding Reminder', FuncName='macos_Functions', ErrorType='Info')
    # Get the Calendar app
    reminder = app('Reminders')

    # Select the calendar to add events to
    reminders = reminder.reminders()
    # reminder_name = 'My Inbox'  # Change this to your desired calendar name
    # selected_reminder = None

    # Create the event details
    event_title = f"{title}"
    event_body = f"{body}"
    # event_start = datetime(2024, 6, 6, 10, 0)  # Event start date and time
    # event_end = event_start + timedelta(hours=1)  # Event duration

    # Add the event to the calendar
    event = reminder.make(
        new=k.reminder,
        with_properties={
            k.name: event_title,
            k.body: event_body,
        }
    )

    # print(f"Event '{event_title}' added to the calendar '{reminder_name}'.")
    print(f"Event '{event_title}' added to the calendar.")
    # write_log(Message=f'Added Reminder - {event_title}', FuncName='macos_Functions', ErrorType='Info')
