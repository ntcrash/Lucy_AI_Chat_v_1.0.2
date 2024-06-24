##################################################
# Main Application for Launching Lucy AI ChatBot #
# Version 1.0.2.1 - Released 2024-06-08          #
# Author - Lawrence Lutton                       #
##################################################

from Default_Functions import *

write_log(Message='Starting Main Application', FuncName='Main', ErrorType='Info')

telegram_ai_chatbot()

write_log(Message='Closing Main Application', FuncName='Main', ErrorType='Info')
