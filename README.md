# Lucy AI ChatBot 1.0.2.3 - 2024-06-23

## Change Log info
- x.x.z.y Y is the current active build, Z is the current active release build.
### ChangeLog started in ver. 1.0.1.x

### Current Build 1.0.2.3

- Cleaning up old functions moved them to testing.py
- Reminder Functions, working on cleaning up and fixing this section
- Fixed log file rotation
- Added Like and Love reactions to TelegramBot
- Added Reflex website for gpt4all
- Added GPT4All for the AI backend
- Changed Telegram Bot to use GPT4ALL API and append messages for better response
- Changed Telegram Bot to use GPT4ALL API and append messages for better response


#### Current Dev build 1.0.1.14
- Fixed AI training
- Added Text to Speech
- Added Speech to Text
- Added Get_Weather
- Added Emotional Marker Bot (beta)
- Cleaned up Default Functions and MainApp scripts
- Cleaning up function names and var names to meet standards
- Added Telegram Chat bot
- Reminder Function (beta partially working)
- Added write_reminder_file
- Added check_create_reminder_file
- Added Search_Web.py
- Added Image Reorganization
 
# How to run the app
## Running the app
- Once you install all the requirements launch MainApplication.py

## Setup Guide in progress
- You will need to create a creds.py file with these two variables
- openai.api_key = f"{creds.api_key}"
- BOT_TOKEN = f"{creds.BOT_TOKEN}"
- Use project requirements file for all packages.
- for psutil to work you will need to install it first
- pip3 install psutil
- Need to install chattbot lib - pip3 install chatterbot
- pip3 install chatterbot==1.0.4 pytz ---> This is the one that worked...
- Need to install pandas lib - pip install pandas
- pip3 install pandas
- need to install pip3 install gTTS
- install speech pip3 install PyAudio
- brew install portaudio
- pip3 install --upgrade pip setuptools wheel
- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
- pip3 install SpeechRecognition
- pip3 install requests
- pip3 install beautifulsoup4
- brew install flac

## This file contains main functions as well as test functions
### Includes
- write_log
- CSV File operations
- System info
- ChatPot AI 
- Text to Speech
- Speech to Text
- Weather
- Telegram bot
- ChatGPT AI integration
- Image Recognition with OpenCV and ChatGPT
- and more to come...

## Issue List
01 - Need to fix reminder function
    * working with telegram Bot now (still needs fine tuning)
02 - Need to fix Web Search crawler
03 - Image Training needs to be fixed

## Project Road Map
- Reminder and Notifier Apps (work in progress)
- Consolidated web searches
- Web / Mobile app frontend
- Add image recognition (work in progress) [1.0.1.14]


# Reflex Chat App

A user-friendly, highly customizable Python web app designed to demonstrate LLMs in a ChatGPT format.

<div align="center">
<img src="./docs/demo.gif" alt="icon"/>
</div>

# Getting Started

You'll need a valid OpenAI subscription - save your API key under the environment variable `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" # replace me!
```

### 🧬 1. Clone the Repo

```bash
git clone https://github.com/reflex-dev/reflex-chat.git
```

### 📦 2. Install Reflex

To get started with Reflex, you'll need:

- Python 3.7+
- Node.js 12.22.0+ \(No JavaScript knowledge required!\)
- Pip dependencies: `reflex`, `openai`

Install `pip` dependencies with the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 🚀 3. Run the application

Initialize and run the app:

```
reflex init
reflex run
```

# Features

- 100% Python-based, including the UI, using Reflex
- Create and delete chat sessions
- The application is fully customizable and no knowledge of web dev is required to use it.
    - See https://reflex.dev/docs/styling/overview for more details 
- Easily swap out any LLM
- Responsive design for various devices

# Contributing

We welcome contributions to improve and extend the LLM Web UI. 
If you'd like to contribute, please do the following:
- Fork the repository and make your changes. 
- Once you're ready, submit a pull request for review.

# License

The following repo is licensed under the MIT License.
